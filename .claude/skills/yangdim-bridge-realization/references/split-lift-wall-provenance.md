# Split-lift wall and provenance descent

Use this packet for boundary handoffs, singleton collars, dual-clean projection, anchored swallowing, and wall-collar descent.

## Boundary and singleton-collar guardrails

- Do not sharpen singleton-collar descent to "the puncture-coordinate edge descends". A two-coordinate collar can have the puncture edge entirely inside `Omega`, with the actual `F/Omega` boundary edge in another outside coordinate.
- The primal collar target is arbitrary boundary-edge provenance descent.
- Every backed `F/Omega` boundary edge forces a primal top-puncture handoff by conditioning on the `Omega`-side value of the changing coordinate and using maximumity of `F`.
- The forced top-puncture support over an off-path label cannot lie entirely inside the path support `S`; every backed incidence yields a cross-realized punctured cube and enters singleton-collar machinery.

## Current singleton-collar split

Normalized singleton collars split into three alternatives:

- direct terminal singleton boundary in the puncture coordinate; terminal
  dimension bookkeeping is now closed by the maximum deletion-reduction lemma:
  primal terminal conditioning targets ranks `(d-2, |Y|-d-1)`, dual terminal
  conditioning targets `(d-1, |Y|-d-2)`, and any failure of those rank
  conditions is a vertical boundary or projected-overlap handoff.  The
  dimension-correct terminal slice is the common-reduction/projection recursive
  prescribed pair, so terminal side-conditioning survival is closed;
- dual-clean projected local collar; in the naive clean-witness applications,
  projected survival is closed because clean projected witnesses force
  projected `F/D` overlap and all named `t`-visible failures are strict
  handoffs.  Reopen only for an explicitly non-naive or rank-changed projected
  formulation;
- anchored swallowing, where the projected point is swallowed by a `D`-lift
  and all hit dual top-hole supports contain the projected coordinate.  This
  receiver is closed for the canonical existential endpoint route: follow the
  fixed-path canonical successor, whose path-remaining measure strictly
  decreases, rather than the overstrong all-handoff suffix-stationarity target.

This is local progress only. Do not claim it solves bridge realization.

## Dual-clean and anchored branches

- Dual-clean projection is local. It must be upgraded to projected prescribed-minor survival: projected `F,D` remain an admissible prescribed bridge pair and the endpoint obstruction survives, or the admissibility failure descends.
- Local dual-clean models can have `pi_t(F) cap pi_t(D) != empty`.
- Every projected `F/D` overlap is `t`-anchored on the `F` side, because each hit dual top-hole support contains `t`.
- In the current `prescribed_dual_bridge_realization.tex` formulation, clean projected movable witnesses force projected `F/D` overlap by Sauer projection counting. Therefore the naive handoff-free disjoint projected-survival branch is closed.
- Projected-overlap handoffs are strict conditioned collars: the trace-backed boundary edge lies in the proper dual top-hole cylinder `B=theta_B`, where the dual side is empty and only `d` coordinates remain free.
- In the disjoint-projection branch, pointwise vertex loss is controlled: projected movable points are swallowed either by an actual `F/Omega` boundary edge in coordinate `t` or by a `D`-lift whose hit dual supports all contain `t`.
- Controlled point-swallowing is also strict: using the full projected trace fibre `Y\\{t}` turns `F-SWALLOW_t` or `D-SWALLOW_t` into a terminal one-edge singleton collar with puncture support `{t}`.
- One-sided wall handoffs are strict as well: fixed-side outcomes are terminal one-edge collars, and internal wall-crossings preserve the full wall support `R` or `B`, giving a proper conditioned singleton collar in that support.

## Wall/provenance debt

- Support-avoiding repair incidences project correctly; support-containing-`t` incidences are one-sided projection walls.
- A point on such a wall has only three opposite-lift outcomes: fixed-side boundary, internal movable `t`-edge, or anchored swallowing.
- The projected `t`-visible branch has no remaining local or strictness debt in the naive projection formulation. Do not list naive disjoint projected-minor survival as live unless a future rank-changed or non-naive projected-minor formulation is explicitly introduced.
- Full wall-collar separator subcases are locally handed off to boundary provenance. Top clauses cannot obstruct a repair in a boundary-free residual once primal/dual repair all-or-none cross tests hold.
- The remaining endpoint-separation branch after the collar receivers close is
  boundary selected support transfer across the dual-spine `tau`-gap, not
  another local singleton-collar subcase.
