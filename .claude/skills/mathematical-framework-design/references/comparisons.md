# Comparison Obligations

These are design prompts, not a requirement to prove every possible property.
Select the properties that the intended use actually needs.

## Enlargement And Completion

Specify the original objects C, the proposed objects D, and the map or functor
J between them. State a universal property only with its class of test objects
and morphisms. A construction may enlarge the objects while changing the
available morphisms or identifying some original distinctions.

For example, a metric space embeds isometrically and densely in its metric
completion. Every uniformly continuous map from the space into a complete metric
space extends uniquely and uniformly continuously to the completion. Here the
purpose, retained data, and extension theorem can all be stated before invoking
any elaborate machinery. Removing the target's completeness or the map's uniform
continuity needs a different statement. The completion does not prove unrelated
estimates about all maps from the original space.

For an embedding into a category of sheaves, specify the test category, coverings,
and the assignment of a sheaf to an original object. Prove that it is a sheaf
and determine faithfulness, fullness, and recoverability when needed. A presheaf
representation, sheafification, and an embedding preserving the desired operations
are different claims. State which limits, colimits, or exactness properties survive.
For added module or completion structures, prove the additional properties there.

## Correspondence And Duality

For a proposed F:C→D and G:D→C, first verify the categories, functors, and
variance. An equivalence needs the appropriate natural isomorphisms relating GF
and FG to identities. An adjunction has different obligations and does not imply
an equivalence. A correspondence between isomorphism classes is weaker still.

To transport a theorem, write the full statement in both settings, including
quantifiers and side conditions. Identify which operations the comparison
preserves and which conclusions it reflects. If only a restricted image has an
inverse, state the image condition. Richer morphisms or auxiliary data may be
needed even when numerical invariants match perfectly.

Use a proposed dictionary to generate questions in both directions. A missing
counterpart to a useful construction can motivate a new definition, but its
existence and properties require proof. Record partial comparisons as partial;
do not discard useful one-way mathematics because full duality fails.

## Internal Languages And Quantitative Recovery

A sound interpretation sends derivations to valid statements in specified
models. Conservativity asserts that specified old-language conclusions gain no
new provability from the extension. Neither follows merely from a successful
type-check or a proposed semantic diagram. Identify assumptions about universes,
choice, classical logic, and the trusted proof system when they affect the claim.

If an internal proof is supposed to imply an ordinary analytic or combinatorial
statement, write that implication explicitly. For limits or quotients, check
whether information about rates, exceptional sets, norms, or representatives has
been lost. Qualitative existence, an algorithm to find a witness, and a usable
quantitative bound are distinct outputs. A theorem for one cannot silently serve
as the other.
