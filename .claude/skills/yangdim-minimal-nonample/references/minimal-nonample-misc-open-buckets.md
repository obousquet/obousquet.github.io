# Residual algebraic and teaching buckets

This file was split out of the former monolithic `minimal-nonample-vcr-history.md`. Load it only when the task specifically touches this historical route.

- **PROVED (`cor:minimal_nonample_low_homology`, old label `conj:crux_negative_h`)**: minimal non-ample classes have subtop Yang homology.  Proof: `prop:minimal_buchsbaum` gives Buchsbaum and reduces Cohen--Macaulayness to subtop homology vanishing; if all subtop homology vanished, then `thm:cm_iff_ample` would force the class to be ample, contradicting minimal non-ampleness.  The stronger complement-normalized sphere-law target is now also proved by `cor:minimal_nonample_sphere_law`.
- `conj:algebraic_fw` — `mfw(H) ≤ hd(H)`. `q:trace_level_ocn` — does a trace-level OCS of complexity
k give `hd ≤ k`? `conj:teaching_pd_lower` — `hd ≤ max_h pd(T_h) + 1`.
- Dead ends worth remembering: monotone compression maps are only the identity (Quillen route
vacuous); h≥0 and M-vector do NOT characterize ample; RTD is not an h-vector invariant.
