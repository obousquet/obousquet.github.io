---
name: ledger-to-journal-writeup
description: >-
  Convert proof ledgers, route notes, exploratory drafts, or campaign archives
  into journal-style self-contained LaTeX writeups. Use to remove chronology
  and campaign jargon, rebuild definitions in logical order, audit proof
  contracts, consolidate one-use lemma chains, subsume superseded modules, and
  align drafts with published-paper structure.
---

# Ledger to Journal Writeup

Transform working notes into a logical, self-contained mathematical paper—never
a polished chronological diary. Keep historical routes and old labels out of
main prose unless a short remark clarifies why a hypothesis or obstruction is
needed.

## Conversion Workflow

Work in short passes (freeze source -> theorem graph -> definitions -> proof
contracts & subsumption -> orientation & examples -> build sync) rather than
smoothing prose before contracts stabilize:

1. **Freeze one source of truth.** Pick one authoritative `.tex` file (prefer a
   proof-only companion note if proofs overwhelm the main paper) and classify
   inherited claims (`proved`, `conditional`, `computational`, `false route`) so
   old ledger phrasing never leaks upward as established theorem status.
2. **Extract the theorem graph & unify/subsume.** Build the true dependency DAG:
   - *Promote* statements with clean standalone hypotheses and independent value
     to Theorems/Propositions; *demote* local plumbing or linear chains of
     one-use lemmas into named proof steps inside one proof (`proof-simplification`
     handles deeper structural/constant compression once chronology is gone).
   - *Subsume and reduce module count:* whenever a general theorem or shared
     principle absorbs older special cases, delete or archive the superseded
     lemmas and merge overlapping proof modules instead of leaving parallel
     versions around. Strip chronological per-iteration tallies.
3. **Rebuild definitions before first use.** Give formal data, domain,
   normalization, degenerate cases, and validity/failure criteria near first use
   instead of campaign nicknames (`packet`, `gate`, `row`, `holonomy`). Apply
   the *deletion test*: if a coined name just shortens a short formula or
   condition list, inline the condition instead. Keep one global name per object.
4. **Audit proof contracts.** For every nontrivial step make explicit what the
   reduction transfers, which finite universe or support is fixed, what certifies
   any quotient, how every failure/minimal-counterexample exit closes, and where
   auxiliary constructions return to the original theorem. Never hide gaps under
   "by transport" or "after repair."
5. **Build the reader path & targeted examples.** Add a concise abstract/status
   opening, reading guide or dependency map for long proofs, notation table when
   symbol-dense, and small concrete examples immediately where conventions or
   counterexample barriers are subtle.
6. **Clean history & synchronize outputs.** Archive false-route archaeology;
   ensure no two active files claim to prove the same result differently; compile
   PDFs with SyncTeX (`latexmk -pdf -synctex=1 main.tex`), update dashboards or
   inventories if tracked, and commit source plus generated outputs together when
   repo policy tracks PDFs.

## Gap-Audit Checklist

Before calling a writeup journal-ready, confirm:

- Every theorem states exact hypotheses, quantifiers, and conclusions; all
  central terms and degenerate cases are defined before first use.
- Every proof branch handles all cases, names the exact closed result or order
  invoked, and transfers back to the original object cleanly.
- One-use chains are collapsed, superseded modules removed/archived, examples
  match formal definitions, and SyncTeX PDFs rebuild without stale warnings.
