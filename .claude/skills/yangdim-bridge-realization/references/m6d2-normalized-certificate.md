# Normalized (6,2) finite certificate route

This file was split out of the former monolithic `m6d2-finite-signatures.md`. Load it only when the task specifically touches this finite-signature route.

The sampled
next-layer diagnostic `scripts/explore_antipodal_signature_m6d2.py` probes
`(m,d)=(6,2)` bridge pairs by taking VC-two primal bridges from
antipodal prefix `12`-cycles in `Q_6` and VC-three dual bridges from
antipodal suspensions of known `(5,2)` sides; it reports equality rank,
equality components, accepted signatures, and dual-NAE rejections.  This is
diagnostic evidence only, not an exhaustive classification.  Initial bounded
evidence (`--samples 20 --trials 1000 --base-dual-limit 24 --seed 2`) found
rank `19` on `20` variables, connected equality graph, two affine solutions,
and zero dual-NAE rejections in every sampled disjoint bridge pair.  The
exact normalized orbit-base mode (`--exact-normalized --orbit-base-duals
--seed 0`) fixes one prefix `12`-cycle, regenerates the six first-middle
cube-orbit representatives from the `11904` compatible sides, and exhausts
cube transforms of their suspended dual bridges; after deduplication it found
`454` disjoint dual bridges, all again with rank `19`, connected equality
graph, two affine solutions, and zero dual-NAE rejections.  A solution-key
diagnostic found `454` distinct accepted solution pairs up to global
complement, so the proof should not look for a fixed universal sign vector;
the sign pair varies with the dual bridge.  The stabilizer quotient diagnostic
gives the current finite certificate target: the normalized prefix bridge has
cube-stabilizer size `24`, and the `454` disjoint transformed dual bridges
split into `43` stabilizer orbits with orbit-size profile
`((2,1),(4,2),(6,6),(12,34))`.  Every orbit representative still has rank
`19`, connected equality graph, exactly two accepted signatures, and zero
dual-NAE rejections.  The certificate-summary mode shows that every one of
these `43` representatives admits a compact finite certificate: a `19`-edge
equality spanning tree, zero equality failures for the canonical accepted
solution, `16` dual-NAE constraints, and `16` explicit two-triple
nonconstancy witnesses.  The signed-Levi-graph diagnostic isolates the next
proof lemma: for every one of the `43` representatives, the graph on the
`20` triple vertices and `10` outside-pair vertices is connected with
component profile `(30,)`, signed-balanced, and has zero bad outside-pair
overlaps; the coherent overlap graph on the `10` outside pairs is connected
with component profile `(10,)`.  Thus the remaining structural part should be
proved as an outside-pair overlap/rank lemma for suspended first-middle dual
bridges disjoint from the prefix bridge.  The dual-NAE branch is no longer a
separate final check: once the ten outside rows are oriented, the Sauer
nonaddability lemma `lem:m6d2_sauer_nonaddability` forbids any additional
oriented dual row.  The adjacent-triple and row-local NAE diagnostics remain
regression/calibration for explicit witnesses.  The provenance/hidden-axis diagnostic compresses the
`43` stabilizer orbits into four first-middle source types: `2` orbits from
first-middle orbit `1`, `18` from the paired source set `(2,6)`, `10` from
orbit `3`, and `13` from the paired source set `(4,5)`.  The hidden-axis
profiles match this split exactly: type `1` has all six coordinate fibres in
first-middle orbit `1`; type `(2,6)` has two axes of orbit `2` and four axes
of orbit `6`; type `3` has all six axes in orbit `3`; and type `(4,5)` has
three axes of orbit `4` and three axes of orbit `5`.  Every hidden split is
antipodal.  Thus the next proof attempt should be organized by these four
provenance types, not by `43` unrelated stabilizer cases.  The
type-representative diagnostic prints one canonical proof-table record for
each of the four provenance types, including hidden axes, signed-Levi
invariants, `D` pair reps, outside-pair rows, a `19`-edge equality spanning
tree, and all `16` dual-NAE witnesses.  The four canonical solution keys are
`20cb7`, `10000`, `24437`, and `22cb7` for types `1`, `(2,6)`, `3`, and
`(4,5)`, respectively.  The `--verify-displayed-records` mode reconstructs
the four displayed certificate records and checks their outside-pair
partition, rank-`19` equality tree, solution key, all `16` NAE witnesses,
signed-Levi connectivity/balancedness, and coherent-overlap connectedness.
The `--verify-normalized-orbit-accounting` mode reruns the exact normalized
orbit-base census and checks the remaining finite accounting: `11904`
first-middle sides with orbit sizes `(384,1920,1920,1920,1920,3840)`, `454`
disjoint transformed dual bridges, stabilizer order `24`, `43` stabilizer
orbits with profile `((2,1),(4,2),(6,6),(12,34))`, and source-union profile
`((1,),2), ((2,6),18), ((3,),10), ((4,5),13)`.  The canonical
representative solution keys are `20cb7`, `10000`, `24437`, and `22cb7`, but
solution keys are not constant across all orbits within a provenance type.
This is small enough for a finite proof table if the structural
outside-overlap proof remains elusive.  The normalized finite-audit status is
now summarized in `main.tex` as `rem:m6d2_normalized_certificate_audit`,
explicitly not as a full intrinsic classification theorem.
