/-
Portable Lean 4 meta-level theorem and statement-isolation verifier template.

Run from a Lake project root (after building the target module):
  lake env lean --run CheckTheorem.lean <proof_module> <theorem_name> <statement_file> <defs_modules_csv>

What it checks:
1. Statement isolation: parses and elaborates <statement_file> strictly in an
   environment containing only `Mathlib` (when available) and the comma-separated
   <defs_modules_csv> definitions modules — never importing <proof_module>. Local
   notations, instances, or macros in the proof module cannot alter statement meaning.
2. Kernel theorem check: locates <theorem_name> in <proof_module> as a `.thmInfo`
   and checks structural equality (`thm.type == recorded`) against the isolated
   statement expression.
3. Transitive axiom walk: walks `ConstantInfo.getUsedConstantsAsSet` across all
   constants reachable from <theorem_name> and rejects any axiom outside
   `[propext, Classical.choice, Quot.sound]` (including `sorryAx` and custom axioms).

Exit 0: ACCEPTED (with `AXIOMS: [...]`).
Exit 1: REJECTED (<reason>): <message>.
Exit 3: Checker setup/CLI error.
-/
import Lean

open Lean

namespace ResearchToolsChecker

def standardAxioms : List Name := [``propext, ``Classical.choice, ``Quot.sound]

structure WalkState where
  seen : NameSet := {}
  axioms : Array Name := #[]
  missing : Array Name := #[]

partial def walkConstants (env : Environment) (name : Name) : StateM WalkState Unit := do
  if (← get).seen.contains name then
    return
  modify fun s => { s with seen := s.seen.insert name }
  match env.find? name with
  | none =>
    modify fun s => { s with missing := s.missing.push name }
  | some ci =>
    if ci matches .axiomInfo _ then
      modify fun s => { s with axioms := s.axioms.push name }
    for dep in ci.getUsedConstantsAsSet do
      walkConstants env dep

def reject (cls msg : String) : IO UInt32 := do
  IO.println s!"REJECTED ({cls}): {msg.replace "\n" " "}"
  return 1

def parseCsvModules (csv : String) : Array Import :=
  csv.splitOn ","
    |>.map String.trim
    |>.filter (!·.isEmpty)
    |>.map (fun s => { module := s.toName })
    |>.toArray

def elaborateStatement (env : Environment) (stmtText : String) : IO (Except String Expr) := do
  match Parser.runParserCategory env `term stmtText "<statement>" with
  | .error err => return .error s!"parse error: {err}"
  | .ok stx =>
    let ctx : Core.Context := { fileName := "<statement>", fileMap := FileMap.ofString stmtText }
    let coreAction : CoreM (Except String Expr) := do
      let (e, _) ← (Elab.Term.elabTerm stx none).run {} {}
      let e ← instantiateMVars e
      return .ok e
    match ← (coreAction.run' {}).toBaseIO ctx { env } with
    | .ok res => return res
    | .error err => return .error s!"elaboration error: {← err.toMessageData.toString}"

end ResearchToolsChecker

open ResearchToolsChecker in
def main (args : List String) : IO UInt32 := do
  let [proofModStr, thmStr, stmtPath, defsCsv] := args
    | do
        IO.eprintln "usage: CheckTheorem.lean <proof_module> <theorem_name> <statement_file> <defs_modules_csv>"
        return 3
  initSearchPath (← findSysroot)
  let stmtText ← IO.FS.readFile stmtPath
  let defsImports := #[{ module := `Mathlib : Import }] ++ parseCsvModules defsCsv
  let stmtEnv ← importModules defsImports {}
  let recorded ← match ← elaborateStatement stmtEnv stmtText with
    | .ok e => pure e
    | .error msg => return ← reject "statement" msg

  let proofMod := proofModStr.toName
  let fullImports := defsImports ++ #[{ module := proofMod : Import }]
  let fullEnv ← importModules fullImports {}
  let thmName := thmStr.toName
  let some ci := fullEnv.find? thmName
    | return ← reject "missing-theorem" s!"theorem {thmStr} not found in {proofModStr}"
  let .thmInfo thm := ci
    | return ← reject "not-a-theorem" s!"declaration {thmStr} is not a theorem"
  unless thm.type == recorded do
    return ← reject "statement-mismatch" s!"{thmStr} type does not structurally match frozen statement"

  let (_, walk) := (walkConstants fullEnv thmName).run {}
  unless walk.missing.isEmpty do
    return ← reject "missing-constant" s!"unresolved constants: {walk.missing.toList}"
  let disallowed := walk.axioms.toList.filter (!standardAxioms.contains ·)
  unless disallowed.isEmpty do
    return ← reject "axioms" s!"disallowed axioms: {disallowed}"

  let axiomNames := walk.axioms.toList.map toString
  IO.println s!"AXIOMS: [{", ".intercalate axiomNames}]"
  IO.println s!"ACCEPTED ({thmStr})"
  return 0
