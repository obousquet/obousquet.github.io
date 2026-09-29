# Find Existing Results Before Repeating Work

Use this procedure before substantial investment in a proposed claim or route, and before
crediting a result as new. Recover the previous search and result map when resuming a campaign.
Extend that check when the target, terminology, related work, or available evidence changes;
do not rerun an exhaustive workspace search for every implementation step.

## Search The Mathematical Claim

1. Write the proposed statement with its hypotheses, quantifiers, conclusion, and intended role.
   Identify equivalent formulations, renamed objects, dual descriptions, and the mechanism of a
   proposed proof or counterexample. Search those, not just the current theorem label.
2. Read the current ledger and result inventory, then search earlier rounds, archived notes,
   manuscripts, proof modules, and relevant experiment descriptions. Include proved inputs,
   conditional reductions, counterexamples, failed imports, and parked mechanisms. The latest
   summary can omit a result that remains valid and useful.
3. Identify related repositories from project guides, workspace inventories, handoffs, and source
   cross-references. Search their result maps and mathematical artifacts as well. If no links are
   available, inspect sibling project summaries to find likely overlap. Choose repos by shared
   objects or techniques, not only similar project names; record the scope actually checked.
4. Search the common extracted literature with `shared-literature` as well. Its catalog and project
   notes complement campaign searches; they do not necessarily contain locally proved results or
   failed routes. Keep external literature novelty separate from novelty within the workspace.

Use a project's existing campaign map and search helper when available, checking which files and
repos it actually covers; supplement missing proof modules or sibling repos with direct searches.
Start with `rg --files` to locate authored `.md`, `.tex`, and dashboard `.json` files, then use
targeted `rg -n -i` searches over the relevant roots. For example, replacing the placeholders:

```bash
rg -n -i -g '*.md' -g '*.tex' -g '*dashboard*.json' \
  -g '!**/.claude/**' -g '!**/.agents/**' -g '!**/.git/**' \
  -e 'mathematical phrase' -e 'older terminology' . ../related-project
python3 scripts/research_library.py search 'mathematical phrase'
```

Use `rg -l` to narrow a large hit list before reading the matches. Include existing uncommitted
research files; `git grep` alone misses them. Follow explicit archive and compatibility links when
needed rather than traversing every symlink indiscriminately. If a cited source was moved or deleted,
inspect its history with `git log --all -- path/to/file` and `git show REV:path/to/file`.
A missing checkout, inaccessible history, or incomplete search leaves a stated coverage limit;
zero keyword matches is not evidence of novelty.

## Compare Before Reusing Or Claiming Novelty

Read the actual theorem and proof or witness, not just a dashboard status. Translate notation and
compare assumptions, quantifiers, parameter ranges, constants, conclusions, and dependence on
unproved inputs. Check later corrections or superseding statements; a historical `proved` label
does not settle current validity. Record the relationship:

- **Same result or a special case:** cite and reuse it. Rechecking can be useful verification,
  but does not create a new theorem or change its original discovery date.
- **Extension, different proof, or new application:** state the exact difference and why it matters.
  Removing a hypothesis or connecting established results can be substantive; new notation alone
  does not establish an advance.
- **Previously failed mechanism:** identify the old witness or missing implication and explain
  what new ingredient avoids it before reopening. Failure of a stronger auxiliary claim need not
  refute the target or rule out a different route; compare the scope in both directions.
- **Conflicting or incomplete records:** audit the discrepancy and correct the authoritative record
  before relying on it. Distinguish a source proof gap from a gap in importing it into this setting.
- **No located match:** state the search scope and uncertainty. Continue promising mathematics
  within the user's scope without claiming that the search proves global novelty.

An independent reproof is appropriate when requested or when auditing a disputed argument. Name
that purpose in advance instead of inadvertently treating repeated work as a discovery.

## Make The Check Survive The Next Session

Use a compact section in the existing result inventory or ledger, rather than another round log.
For reusable results and failures, preserve:

- a succinct mathematical statement, assumptions, and useful aliases;
- current evidence status and the originating repo/path plus theorem label or section;
- the earliest known round/date and a revision when needed to identify the evidence;
- links to corrections, proof dependencies, counterexamples, and superseding results;
- relevant related-repo sources, the search scope/date, and any actual addition still sought.

Do not invent an original discovery date when only a later source can be located. Link to one
authoritative proof and index its aliases rather than creating competing copies. Keep concrete
project mappings and results in the consuming workspace, not in reusable skills.

Include these source links and known failures in handoffs and, when delegation is authorized,
task packets. A deliberately independent perspective may omit the detailed route narrative, but
its output must be reconciled with existing results before further investment or progress claims.
When rediscovery happens, add the missing alias or cross-reference that would have found the
earlier result, then continue from the actual unresolved difference.
