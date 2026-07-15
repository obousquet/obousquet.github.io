# Cross-support and extenture-purity history router

This is a router for the closed cross-support part of the VC-radius/extenture-purity campaign. Load it when auditing historical reductions, extracting reusable local mechanisms, or checking that a proposed bridge-realization route is not reusing an already-closed VC-radius branch.

## Current status

- `thm:minimal_nonample_vcr_purity` proves `VC_r(H)=VC(H)` and pure global extenture support `VC(H)+1` for minimal non-ample classes.
- Cross-realized fibre supports have size `VC(H)` in the final theorem; earlier low-support branches are proof history, not active conjectures.
- `cor:minimal_nonample_sphere_law` and `thm:maximum_fiber` are closed downstream outputs.
- Do not reopen Claim-X as an open lemma; it is a proved projection-minor criterion/tool.

## Child packets

- `minimal-nonample-cross-support-fiber-purity.md`: extenture conditioning, cross-realized fibre supports, co-pair/circuit reductions, exchange uniformity, and the equivalence between cross-support purity and global extenture-support purity.
- `minimal-nonample-low-degree-star-normalization.md`: minimum low-degree extenture normalization against a shattered set, replacement-star/cylinder reductions, overlap-deletion bookkeeping, and the historical graded-tower obstruction.
- `minimal-nonample-top-skeleton-copair.md`: calibrated homology handoff, one-coordinate top-skeleton trichotomy, antipodal co-pair calibration, and partial-cube/minor guardrails.
- `minimal-nonample-calibrated-homology-history.md`: dedicated calibrated-homology closure packet; load this instead of the cross-support packets when the question is specifically homological.

## Guardrails

- Do not infer extenture size `= VC(fiber)+1` from fibre ampleness alone; ample classes can have small extentures on constant-coordinate blocks and larger VC elsewhere.
- Do not treat co-pair endpoints as Claim-X by one coordinate deletion: `lem:copair_one_step_behavior` says deleting any coordinate from an antipodal co-pair gives the full cube, while conditioning gives a punctured ample cube.
- Treat historical residuals in these packets as route diagnostics unless the active ledger explicitly reactivates them for prescribed-dual bridge realization.
