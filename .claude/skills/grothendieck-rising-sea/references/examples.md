# Grothendieck-Style Rising Sea: Examples

Use these examples to identify abstraction patterns. The lesson is not to imitate terminology, but
to notice what kind of hidden structure was made primitive.

## Schemes

Schemes enlarge algebraic varieties so that nilpotents, arithmetic base rings, gluing, and generic
behavior live in one category. Many statements about varieties become functorial after passing to
schemes.

Transfer lesson: if examples force boundary, infinitesimal, or arithmetic phenomena that the native
objects cannot represent, enlarge the object class until those phenomena are first-class.

Source: https://stacks.math.columbia.edu/tag/01I1

## Sheaves and cohomology

Sheaves encode local-to-global data, and sheaf cohomology measures the obstruction to assembling
local information globally.

Transfer lesson: if every local proof works but global assembly fails, stop treating assembly as
bookkeeping. Define the object whose cohomology or obstruction class measures the failure.

Source: https://stacks.math.columbia.edu/tag/006U

## Etale cohomology and Weil conjectures

Grothendieck's development of etale cohomology supplied a cohomology theory for algebraic varieties
over finite fields with the formal properties needed to approach the Weil conjectures.

Transfer lesson: when the desired proof requires a tool that does not exist in the current category,
build the theory whose formal properties would make the proof natural, then prove comparison and
finiteness theorems.

Source: https://stacks.math.columbia.edu/tag/03YQ

## Toposes

Topos theory abstracts sheaf categories and treats spaces through the logic and sheaves they support.
It unifies geometric and logical viewpoints.

Transfer lesson: if two domains repeatedly produce the same descent, forcing, or local-truth
phenomena, search for a common ambient category where both are instances.

Source: https://ncatlab.org/nlab/show/topos

## Motives

The theory of motives seeks a universal cohomology theory underlying many cohomology theories.

Transfer lesson: if several invariants prove parallel theorems with the same formal properties,
define the universal object that explains why those invariants are shadows of one structure.

Source: https://ncatlab.org/nlab/show/motive

## "Rising sea" strategy

The rising-sea metaphor is associated with Grothendieck's preference for immersing a hard problem in
a sufficiently general theory until direct resistance disappears.

Transfer lesson: when a problem is not yielding to force, ask what theory would make the desired
statement tautological or functorial. Then build the smallest useful fragment of that theory, not the
maximal possible abstraction.

Source: https://mathoverflow.net/questions/408811/grothendiecks-rising-sea-approach

## How to use these examples

For a live problem, make an abstraction audit:

```text
What operations keep appearing?
Which operations are currently ad hoc?
What data is invisible in the native objects?
What local-to-global failure keeps recurring?
What invariant has the same formal behavior across examples?
What enlarged category would make these maps natural?
```

The next target should be the first structural theorem in the new setting, not the full original
conjecture.
