# Finite Sufficient Representations And Candidate Algebras

Use only with supplied finite objects, effective operations, and computable
observations. This is a classical finite-state construction, not a universal
algorithm for discovering mathematical abstractions.

## Coarsest Stable Partition

Let X be finite nonempty, U a finite set of total maps X->X, and Q:X->Y a supplied
observable with decidable equality on its finite image. Multiple observations can
be combined into a tuple. Start with the partition by Q. Repeatedly assign to x
its signature

    (current_block(x), tuple(current_block(u(x)) for u in U))

and split blocks according to signatures, until no block splits. Use a fixed
ordering of U. Compare partitions by their equivalence relations, or canonicalize
block names; arbitrary numeric labels need not stabilize.

Every strict step increases the number of blocks. Starting from b0 blocks, there
are at most |X|-b0 strict steps. Stability ensures every u and Q descends to the
quotient. Its equivalence is exactly

    x ~ y iff Q(w(x)) = Q(w(y)) for every finite composition w of U,

including the empty composition. To prove this, equal future observations imply
equality in every refinement by induction on the stage. Conversely stability
preserves equivalence under each operation; induction on word length gives equal
future observations. Any equivalence preserving Q and every u is contained in
this one, proving it is the coarsest such equivalence (the smallest quotient in
number of classes). These are relative claims for the supplied U and Q.

For partial operations add a distinct absorbing failure state, with an observable
value different from every ordinary value. This preserves definedness as well as
ordinary observations. For a finite finitary signature, form all unary contexts
obtained by fixing the other arguments, then refine under these; stability in
each argument gives well-defined operations on the quotient by successive
replacement. This context set can be large.

Save a distinguishing word when a block splits: an initial split is witnessed by
Q; a successor split prepends the relevant operation to the previously recorded
future observation. The witness explains which operation exposes the missing data.

## From Observations To A Linear Operator Algebra

For real-valued Q on finite X, regard functions as vectors in R^X. Start with
W0=span{1,Q} and iterate

    W_(r+1) = W_r + span{ f composed with u : f in W_r, u in U }.

A basis suffices to compute the next stage because pullback is linear. There are
at most |X|-dim(W0) strict increases, and equality at a stage implies invariance
and stabilization. Use exact arithmetic when the inputs allow it; a floating-point
rank tolerance provides numerical evidence, not a certified quotient.

The stable space W contains every Q composed with a finite word, and is spanned
by these functions together with 1, by induction on the construction. Two objects
agree on W exactly when they have identical future observations. A basis of W
therefore gives feature coordinates determining the same stable partition.

Each u induces a linear map u*:W->W, f |-> f composed with u. Composition obeys
(u composed with v)* = v* u*. These operators generate an associative algebra of
linear operators on W; matrices, relations, and commutators can be computed.
This is an algebra of operators on an invariant vector space. W is not claimed
to be closed under pointwise multiplication.

For increasing instance sizes, compare the distinguishing features and operator
relations. Seek a uniform description and prove invariance, relations, model
estimates, and the needed comparison on the intended infinite class. Finite
patterns do not prove these claims. W can grow to the full function space and
provide no simplification, just as the quotient can keep every concrete state.

## A Small Witness

Take X={-2,-1,0,1,2} plus an absorbing failure state. Observe x^2 (with a distinct
failure value), and apply x |-> x+1, sending overflow to failure. Initially 1
and -1 agree. After one operation their observed values are 4 and 0, so the
stable representation must distinguish them. The failure identifies a role for
sign, rather than merely saying that the square is a poor invariant.

## Provenance And Limits

Partition refinement is standard in automata minimization; see Hopcroft,
*An n log n algorithm for minimizing states in a finite automaton* (1971),
https://www.cs.cmu.edu/~cdm/resources/Hopcroft1971.pdf. The elementary iteration
here does not claim that algorithm's running time. For the related verification
pattern see Clarke et al., *Counterexample-Guided Abstraction Refinement* (2000),
https://doi.org/10.1007/10722167_15. The observable-space construction is standard
linear pullback closure; its value here is an explicit bridge from distinguishing
observations to candidate operators, not a novelty claim.

The mechanical guarantees concern supplied finite systems. They do not choose a
fruitful initial language, compute an unknown mathematical answer, or guarantee
termination of an open-ended search for a useful infinite theory.
