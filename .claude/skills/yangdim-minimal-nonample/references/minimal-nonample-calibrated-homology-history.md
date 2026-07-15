# Calibrated homology and VC-radius closure history

This file was split out of the former monolithic `minimal-nonample-vcr-history.md`. Load it only when the task specifically touches this historical route.

The calibrated cubical route has an exact terminal full-slice normal form
(`lem:terminal_full_slice_core_normal_form`): a terminal residual core over a shattered `S` is
`2^{S union R}` with all missing labels confined to one opposite `R`-corner, i.e.
`H_R=2^{S union R}\\(M x {bar b_R})`; opposite slices have the same form with one fewer residual
coordinate.  The packaged alternative (`cor:calibrated_homology_terminal_alternatives`) says that
for every shattered `VC(H)`-set `S`, either `X_{H^c}` has the calibrated homology class and hence
`VC_r(H)=VC(H)`, or `H` has a low-degree extenture, or `H` enters the Claim-X top-circuit branch.
Positive exclusion form (`cor:calibrated_homology_exclusion_criterion`): for a fixed shattered
`VC(H)`-set `S`, if there is no low-degree extenture and no punctured one-coordinate projection
on `S union {y}`, then `X_{H^c}` has calibrated homology in degree `n-VC(H)-1`; this is stronger
than bare VC-radius purity.  Contrapositive localization
(`cor:calibrated_failure_forces_claimx`): once low-degree extentures are excluded, any failure of
calibrated homology for that fixed `S` forces a punctured projection on `S union {y}` and hence the
already-proved Claim-X projection-minor branch.  Since Claim X is itself now a theorem, the terminal
alternatives collapse further (`cor:calibrated_homology_low_extenture_reduction`): for every
minimal non-ample class and every shattered `VC(H)`-set, either calibrated complement homology holds
in degree `n-VC(H)-1`, or `H` has an extenture of support at most `VC(H)`.  The consolidated form is
`cor:calibrated_homology_vcr_equiv`: for every minimal non-ample class, calibrated complement
homology in degree `n-VC(H)-1`, nonzero calibrated complement homology in that degree,
`VC_r(H)=VC(H)`, and absence of extentures of support at most `VC(H)` are equivalent.  The
low-degree extenture / VC-radius-purity branch is now closed by
`thm:minimal_nonample_vcr_purity`: every cross-realized support has size `VC(H)`, every global
extenture has support size `VC(H)+1`, and `VC_r(H)=VC(H)`.  Consequently
`cor:minimal_nonample_sphere_law` proves the complement-normalized homology sphere law for every
minimal non-ample class, with homology concentrated in degree `n-VC(H)-1`.  This does NOT yet prove
maximum fibers.
