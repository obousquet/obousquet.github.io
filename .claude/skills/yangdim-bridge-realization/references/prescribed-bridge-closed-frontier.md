# Closed frontiers feeding prescribed-dual bridge realization

- **Current remaining topological-dictionary priorities.**  The raw `Delta_H` hierarchy is mostly
  closed and summarized formally in `cor:raw_yang_topological_dictionary`; do not keep adding global
  topological adjectives there unless the statement is precise.
  The local-CM sharpness route is also closed.  The radius inequality `hd-VC <= t^*(H)` is proved,
  and equality off the ample stratum is impossible: every Buchsbaum Yang complex has `hd=VC`
  (`thm:buchsbaum_hd_equals_vc`), so every non-ample class satisfies
  `hd(H)-VC(H) <= t^*(H)-1` (`cor:strict_local_cm_gap_bound`).  The decisive mechanism is
  `lem:buchsbaum_split_no_phantom_faces`: in any Buchsbaum coordinate split, every non-empty trace
  seen separately in both split fibers is realized by a common projected concept.  For a singleton
  phantom trace, a one-literal conditioning would shatter the split coordinate without strongly
  shattering it; for a larger phantom trace, conditioning on one literal gives an ample link, and
  `lem:ample_clean_coordinate_intersections` forces the remaining trace into the common reduction.
  The sphere-law/VC-radius and maximum-fiber frontiers are now closed in all VC dimensions:
  `thm:minimal_nonample_vcr_purity` proves `VC_r=VC` and pure global extenture support `VC+1`,
  `cor:minimal_nonample_sphere_law` gives the complement-normalized homology sphere law, and
  `thm:maximum_fiber` proves every one-coordinate fiber is a maximum VC `VC(H)-1` class.  The
  maximum-fiber proof assembles existing ingredients: cross-support purity plus
  `cor:vc_drop_failure_top_circuit` turns any VC-preserving fiber into a punctured top projection,
  and `cor:top_circuit_claimx_minor` turns that into a forbidden Claim-X projection minor.  The old
  `VC=4` full-cylinder, one-exchange, and endpoint-frontier analyses are now proof history and
  diagnostic support rather than active radius or maximum-fiber obstructions.  The live higher-VC
  target is structural: classify the graph/cubical gluings of the two maximum fibers in
  connected-middle cases.
  The old one-exchange and unit-defect frontier is now proof history.  Its key
  outputs were `cor:one_exchange_cross_support_purity_failure`,
  `cor:extendable_min_cross_unit_defect`,
  `cor:extendable_small_cross_support_impossible`, and finally
  `lem:min_cross_no_one_step_extension`, which closes the cross-support purity
  branch.  Some side-fibre diagnostics such as
  `cor:one_exchange_nonmaximum_side_fiber` and
  `cor:one_exchange_maximum_fiber_failure` are now proof-history diagnostics:
  together with `thm:maximum_fiber` they rule out the one-exchange residuals
  that earlier drafts treated as possible maximum-fiber failures.
