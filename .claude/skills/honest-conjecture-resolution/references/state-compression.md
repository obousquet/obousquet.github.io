# State Compression, Plateaus, Side Routes, And Subagents

Load this when a campaign is growing many leaves/pages/terms, has repeated zero-delta rounds, needs a
side quest, or needs subagents.

## Progress Accounting

Progress means the proof contract shrinks:

- a row is proved or refuted;
- an equivalent reformulation is found;
- a smallest falsifier profile is sharpened;
- a proxy is killed or demoted;
- leaves are merged;
- a route is parked with a blocker;
- an imported theorem or native invariant changes a proof-debt row.

New vocabulary, more examples, more dashboards, or a cleaner long note are not progress unless they
change this contract.

## Compression Audit

Use before another exploration round when the campaign feels busy but not closer:

```text
Top theorem:
Last exact/equivalent reduction:
Current active crux:
Rows that are genuinely independent:
Rows that are inherited consequences:
Rows that are only sufficient proxies:
Rows to delete/merge/park now:
One next decisive move:
Success/failure effect on the live state:
```

## Gates

- **One-screen state gate:** target, exact reduction, active rows, parked routes, falsifier, and next
  move must fit in one ledger opening and one dashboard screen.
- **Deletion-before-expansion gate:** a new route must say what it can delete, merge, demote, or
  refute.
- **Two zero-delta rounds gate:** after two rounds without proof-debt movement, walk back, search for
  a falsifier, import a theorem, or switch proof geometry.
- **Proof-spine growth gate:** add TeX pages only for durable definitions, examples, theorem
  statements, proofs, or compact warnings.
- **Invariant-before-taxonomy gate:** when labels/cases proliferate, seek the invariant, exact
  sequence, obstruction class, potential, boundary map, or dual certificate.
- **Side-route ROI gate:** side routes must export a native theorem, lemma, counterexample, exact
  reformulation, diagnostic, theorem citation, proxy kill, or blindness statement.

## Conditional-Lemma Wall

If a route has more than three unproved conditional rows, stop adding lemmas and make a table:

```text
Claim:
Direction relative to target:
Why needed:
Smallest falsifier:
Evidence:
What closes/kills it:
```

Exactly one row may remain active; the rest must be proved, merged, parked, or converted into
counterexample searches. Hidden “regularity,” “compatibility,” or “genericity” assumptions count as
debt unless already proved.

## Branch Walkback

When the same obstruction reappears under new names, write:

```text
original target -> reduced target -> current crux -> smallest falsifier profile
```

Mark every arrow as `equivalent`, `necessary`, `sufficient`, `special-case`, or `heuristic`. Record
what structure is preserved or lost at each arrow: signs, endpoint data, support, rank, topology,
boundary orientation, admissibility, cycle compatibility, cancellation. Restart from the last exact
or equivalent layer unless the current proxy has a decisive kill/promote test.

## Plateau Response

After two zero-delta rounds or a third non-closing split, choose exactly one:

- walk back to the last exact reduction;
- search for a counterexample satisfying the current falsifier profile;
- import one located theorem or bounded side route with required native export;
- compress the branch into a proof-debt table and park it;
- change proof geometry via invariant, dual certificate, topological obstruction, algebraic
  encoding, or exactness statement.

## Side Quests

Use side quests when the route becomes a reduction treadmill. They must be bounded and genuinely
different: external method, dual reformulation, structural analogue, geometric/algebraic/topological
translation, or located literature.

Before:

```text
Active crux:
Falsifier profile:
Side method:
Deliverable:
Time/size bound:
Success/failure criterion:
```

After:

```text
Native export:
Proof-contract row changed:
Promoted / parked / retired:
```

If the side quest gives only vocabulary or analogy, park it as background.

## Subagent Discipline

Subagents are for independent evidence, not momentum.

- Spawn only from a written packet.
- Split by evidence type: proof, counterexample search, finite diagnostic, exact reformulation,
  literature match, abstraction descent.
- Do not ask several agents to elaborate the same taxonomy.
- Require outputs calibrated as `proved`, `reduced`, `verified computationally`, `plausible`,
  `refuted`, or `stalled`.
- Merge by proof-contract delta: prove, refute, merge, park, relabel, or sharpen active debt.
- A low-yield batch means the decomposition failed; consolidate before spawning again.

Packet:

```text
Round:
Target:
Definitions/hypotheses:
Allowed proved tools:
Known false shortcuts:
Routes and route IDs:
Deliverable format:
Success / failure / stall criteria:
Merge destination:
```

## Retrospective Packet

After repeated cleanup or false starts:

```text
Observed symptoms:
Last rounds classified by output:
State-model failure:
Rules/gates to install:
Artifacts to compress or separate:
One next mathematical move:
One state item to delete/merge/park:
```

The packet is useful only if it installs a future constraint or shrinks active state.
