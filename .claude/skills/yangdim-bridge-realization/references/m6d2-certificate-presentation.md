# Certificate presentation and coherent-overlap diagnostics

This file was split out of the former monolithic `m6d2-finite-signatures.md`. Load it only when the task specifically touches this finite-signature route.

The synthesis draft
`drafts/m6d2_antipodal_signature_certificate.tex` records the signed-Levi
graph criterion, the NAE witness criterion, the finite normalized certificate
with computational status, and the remaining outside-pair overlap lemma as a
proof route.  It now also displays the four canonical proof records: for
each provenance type, the `16` dual-pair representatives, the `10`
outside-pair representatives, a `19`-edge spanning equality tree, and `16`
NAE witnesses.  The finite table route now has a direct verifier command,
`uv run python scripts/explore_antipodal_signature_m6d2.py --verify-displayed-records`;
the orbit accounting has a second direct verifier command,
`uv run python scripts/explore_antipodal_signature_m6d2.py --verify-normalized-orbit-accounting`.
The grouped profile mode
`--exact-normalized --orbit-base-duals --type-profile-summary` adds the
current structural calibration: provenance types are not single rigid coarse
signed-Levi profiles.  Orbit sizes, solution keys, distance profiles,
outside-row size profiles, triple-degree profiles, overlap-size profiles, and
NAE active-size profiles can vary inside a provenance type.  The stable
invariant is the crux status: rank `19`, two accepted signatures, zero
NAE rejections, connected balanced signed-Levi graph, no bad outside-pair
overlap, connected signed-balanced coherent overlap graph, full triple
coverage, a `19`-edge equality tree, and `16` NAE witnesses.  The synthesis
draft now proves the coherent-overlap reduction: no bad overlaps, connected
signed-balanced coherent row-overlap graph, and full triple coverage imply
the connected balanced signed-Levi criterion and hence rank `19`.  The
current coarse-fingerprint counts by type
`1`, `(2,6)`, `3`, `(4,5)` are `2`, `15`, `8`, and `12`.  The
`--coherent-certificate-summary` mode verifies the smaller row-overlap proof
object: every stabilizer orbit has a `9`-edge coherent row spanning tree,
zero bad overlaps, zero signed-balance failures, and all `20` triples
covered; coherent-edge count profile
`30^13,31^2,32^6,33^10,34^6,35^2,36^2,38^1,39^1`.  The
`--dual-nae-certificate-summary` mode checks the NAE part using the coherent
row potentials instead of an arbitrary solution-key table: all `43` orbit
representatives have zero construction failures, `16` coherent-potential
NAE witnesses, zero NAE failures, and a coherent-derived solution key
matching the full affine solver.  The `--dual-nae-adjacency-summary` mode
sharpens this: in every orbit representative, each of the `16` dual rows has
opposite coherent-potential values on a pair of active triples sharing two
coordinates, so the minimum Johnson-distance profile is `1^16`.  The same
audit now records the mechanism: every dual active row induces a connected
`3`-regular subgraph of `J(6,3)` with `6,9,12` edges for active sizes
`4,6,8`, and the coherent-potential colouring cuts each row graph in at
least `3` Johnson edges.  The active-row graphs fall into exactly four
invariant types across the `43*16=688` audited rows: `K4^106`,
`triangular-prism^319`, `cube-Q3^64`, and `eight-triangle^199`.  The
distribution varies by orbit/source, so the structural NAE crux is not
rigidity of a single row graph.  A general connected-row sharpening now
removes adjacency as an independent obstruction: on a connected active-row
graph, ordinary shifted nonconstancy of the coherent colouring implies a
bichromatic Johnson edge by a path argument.  The script tracks zero
`connected-row-sharpening-failure-count`.  The stronger prefix-row verifier
`--verify-prefix-active-rows` checks all `26` antipodal pairs outside the
normalized prefix bridge and finds connected active rows with type profile
`K4^6`, `triangular-prism^12`, `cube-Q3^2`, and `eight-triangle^6`, so any
disjoint dual bridge inherits active-row connectedness.  The earlier NAE
obligation was shifted nonconstancy of the coherent colouring.  It was
reduced to a row-level dichotomy by `--verify-dual-nae-potential-dichotomy`:
a dual row is certified either by a direct bad outside overlap, or by two
coherent outside rows implying opposite dual-row potentials.  Across the
`688` audited rows the aggregate mode profile is
`direct-bad-overlap^181` and `potential-contrast^507`, with zero failures.
This structural NAE target is now closed conceptually by
`lem:m6d2_sauer_nonaddability`: after an affine sign vector orients the ten
outside rows, any additional oriented dual row would give `23` concepts on
six coordinates shattering no triple, contradicting Sauer's bound
`sum_{i<=2} binom(6,i)=22`.  The formal reformulation remains useful for
diagnostics: if the coherent
outside rows induce triple values `beta_T`, then a dual row `d` fails NAE
exactly when `beta_T+h_d(T)` is constant on `A_K(d)`, and this constant is
precisely a coherent potential for adding `d` as another equality row.  The
refinement verifier `--verify-dual-nae-potential-refinement` shows that the
row-local active graph type, not provenance type, is the sharp visible
discriminator: active sizes `4` and `6` are all potential-contrast; `K4` and
`triangular-prism` rows are all potential-contrast; `cube-Q3` rows are all
direct-bad-overlap; only `eight-triangle` rows mix the mechanisms, with
`direct-bad-overlap^117` and `potential-contrast^82`.  These local profiles
now explain witness structure rather than define a remaining proof
obligation.  The new
`--verify-dual-nae-bad-partner-absorption` verifier sharpens this further:
for the normalized prefix bridge, a bad partner of a row is another
prefix-outside row with nonconstant parity on the active overlap.  `K4` and
`triangular-prism` rows have no bad partners, `eight-triangle` rows have two,
and `cube-Q3` rows have four; every bad overlap has two common triples.
Across all `688` audited rows, direct-bad-overlap occurs exactly when at
least one bad partner remains outside `D`, and the direct-bad count equals
the number of outside bad partners.  If all bad partners are absorbed into
`D` or there are none, the row is potential-contrast.  The exact profile is
`(0,0)->pc^425`, `(2,0)->pc^82`, `(2,1)->bad^109`,
`(2,2)->bad^8`, `(4,1)->bad^47`, `(4,2)->bad^17`, with zero
failures.  The verifier now also checks identity-level absorption: for each
audited row, the outside rows appearing in direct bad overlaps are exactly
`Bad_K(r) cap outside(D)`, with the same complementary-pair labels as in the
prefix table; the exact normalized audit has zero count failures and zero
identity failures.  The `--verify-prefix-bad-partner-template` verifier gives the
prefix-local template: bad partners are exactly complementary triple-pair
incidences `T|T^c` inside active rows.  Eighteen prefix-outside rows have no
complementary pairs, six eight-triangle rows have two, and two cube-Q3 rows
have four; the bad-partner graph has ten such labelled edges.  The new
strengthened check records the bijective edge form: each complementary pair
`012|345`, `013|245`, `014|235`, `015|234`, `023|145`, `024|135`, `025|134`,
`034|125`, `035|124`, `045|123` occurs in exactly two prefix rows, and those
two rows are exactly the endpoints of the corresponding bad edge.  The
finite absorption statement is therefore: a direct bad outside overlap can
only use one of these ten labelled edges, and absorption means the other
endpoint has been placed in `D`.
