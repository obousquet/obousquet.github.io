# Row-local NAE and bad-partner diagnostics

This file was split out of the former monolithic `m6d2-finite-signatures.md`. Load it only when the task specifically touches this finite-signature route.

The new
proof-shaped normal form is: with normalized prefix pair representatives
`111100,111110,011110,001110,000110,000010`, the triple holes are `010/101`
on triples avoiding coordinate `5`, `100/011` on triples `{i<j<5}` with
`i,j<=3`, and `000/111` on triples `{i,4,5}`; for a row with `x_5=0`,
activity is respectively `x_a=x_c!=x_b`, `x_i=1,x_j=0`, or `x_i=0,x_4=0`.
The verifier `--verify-prefix-hole-normal-form` checks this normal form
directly.  A hand proof of the prefix bad-partner template should start from
this three-line rule.  The new
`--verify-dual-nae-no-bad-nonaddability` verifier sharpens the complementary
branch directly: all `507` no-outside-bad potential-contrast rows have
shifted values covering the active row, with zero conflicts, zero uncovered
active triples, and zero constant shifted colourings.  The companion
`--verify-dual-nae-no-bad-potential-witnesses` verifier checks that all
`4991` opposite-potential outside-row pairs are disjoint on the dual row and
that the candidate `0`- and `1`-overlap unions partition `A_K(d)`.  The row
profile is `K4^106`, `triangular-prism^319`, `eight-triangle^82`; by
bad-partner count it is `0^425,2^82`.  Disjointness is now understood as
formal from coherence, so the stable audited invariant is
nonaddability/nonconstancy; witness choice and common-size profile are
artifacts.  The combined verifier `--verify-dual-nae-row-local-dichotomy`
packages the full row-local certificate: `181` rows are certified by direct
bad-partner absorption and `507` by no-outside-bad shifted nonaddability,
covering all `43*16=688` normalized dual rows with zero branch failures.  The
wrapper `--verify-m6d2-finite-normalized-certificate` now runs the complete
normalized finite certificate suite in one command: orbit accounting,
displayed provenance records, prefix hole normal form, prefix bad-partner
template, and row-local NAE dichotomy.  The NAE route is closed by the Sauer
nonaddability lemma; the prefix bad-partner and no-outside-bad verifiers
remain regression tests for witness structure.  The finite promotion work beyond the main-paper summary
`rem:m6d2_normalized_certificate_audit` is therefore presentation plus this
calibrated profile audit, while a structural proof must target the crux
rank/existence properties rather than representative-profile rigidity.
