Relational Geometry — Current Theory

Status: Working axiomatic formulation
Last updated: 2026-09-01

⸻

0. Scope and Status

Relational Geometry (RG) is a proposed formal framework in which relational structure is primitive and detector-level existence is derived from admissibility and persistence under detection.

The theory distinguishes:

1. Being — the total relational structure.
2. is-ness — participation in Being through relational structure.
3. arguments — detector-level entities instantiated through relations.
4. detectors — infinitesimally thin structures that determine what is and is not the case.
5. admissibility — the constraint imposed by relational structure on possible detector states.
6. detection — selection of an admissible state and pruning of unsupported relations.
7. existence — persistence of an entity under detector succession.

The current formulation contains two layers:

* a core relational/detector axiomatization, stated below;
* a provisional projection/shadow extension, motivated by the failure of the core Boolean formulation to generate nontrivial dynamics.

The projection/shadow extension is currently a research hypothesis rather than an established axiom.

⸻

I. Primitive Ontology

Axiom 1 — Relational Primacy

Relations precede arguments in Being.

Let

$$
R
$$

denote the relational structure of Being.

Being contains relations but contains no arguments as primitive entities.

Arguments are instantiated only through relational structure within a detector.

⸻

Axiom 2 — Relational Constraint

Arguments are constrained by relations.

An argument has no independent determination apart from the relations that constrain it.

Arguments therefore do not self-exist as primitive entities.

In schematic form:

$$
A \not\Rightarrow \text{primitive Being}.
$$

Rather:

$$
R \rightarrow A
$$

where the arrow denotes relational instantiation rather than temporal causation.

⸻

Axiom 3 — Relational Is-ness

Relations possess primitive is-ness within Being.

Arguments possess secondary is-ness through participation in relations.

Thus:

$$
\text{Being} \supset R
$$

while detector realization contains instantiated arguments:

$$
D \supset A_D.
$$

The predicate of formal existence is intentionally not introduced at this level.

Relations and arguments are therefore pre-existent to the formal definition of existence.

⸻

II. Detector Bounds

Axiom 4 — Argument-Boundedness

The arguments represented by a detector constrain which relations may be admissible within that detector.

Let

$$
A_D
$$

denote the arguments available to detector $`D`$.

A relation is not admissible merely because it belongs to the relational structure $`R`$.

Its arguments must either:

1. already be available to the detector; or
2. be instantiable by an admissible relation.

For example, if

$$
A,B\in A_D
$$

but

$$
C,D\notin A_D,
$$

then a relation whose constrained arguments are $`C,D`$ is not directly admissible to $`D`$.

⸻

Axiom 5 — Invertibility of Constraint

Constraint must be defined so that it is invertible.

If a relation is admitted because it constrains an argument, then absence of the required argument provides grounds for pruning that relation.

Thus:

$$
r\text{ constrains }A
$$

together with

$$
A\notin A_D
$$

implies that $`r`$ cannot remain active in $`D`$, unless $`r`$ itself admits the instantiation of $`A`$.

Schematically:

$$
\boxed{
\text{no admissible argument for }r
\Rightarrow
\text{prune }r
}
$$

This establishes a reciprocal relationship between relational constraint and relational pruning.

⸻

III. Admissibility

Axiom 6 — Admissibility

Admissibility limits the states that arguments may occupy.

Let

$$
\Omega(D)
$$

denote the potential state space of the arguments represented by detector $`D`$.

Let

$$
\mathcal{A}(D)\subseteq\Omega(D)
$$

denote the subset satisfying the relations admissible to $`D`$.

Then:

$$
\boxed{
\mathcal{A}(D)

\{s\in\Omega(D)\mid s
\text{ satisfies the active relational constraints of }D\}
}
$$

The exact mathematical structure of $`\Omega(D)`$, the relations acting upon it, and the resulting closure/admissibility operator remain to be formally specified.

⸻

Axiom 7 — Relational Subset

Let

$$
r\subseteq R.
$$

A relational subset $`r`$ is the case in detector $`D`$ if:

1. $`r`$ is compatible with all relations already admitted to $`D`$; and
2. $`r`$ either instantiates an argument constrained by the existing relational structure, or constrains an argument already instantiated by $`D`$.

Thus admission is not unrestricted permeability to relations in Being.

It is permeability conditioned by available or relationally instantiable arguments.

⸻

IV. Detection

Axiom 8 — Detection

Detection selects admissible states of arguments from their potential state space.

Schematically:

$$
D:\Omega(D)\rightarrow\mathcal{A}(D).
$$

Detection is not itself a temporal event.

The detector is infinitesimally thin and possesses no duration.

It relates:

$$
\text{what is the case}
$$

to:

$$
\text{what may be the case given what is the case}.
$$

It therefore also determines what is not the case relative to the currently admitted state.

⸻

Axiom 9 — Detector Succession

The result of detection may constitute the relationally constrained input to a subsequent detector.

Thus a succession may be represented as:

$$
D_0\rightarrow D_1\rightarrow D_2\rightarrow\cdots
$$

where each detector state is constrained by the relational structure available to it.

Succession is not assumed to be primitive causation.

⸻

Axiom 10 — Pruning

Detection prunes relations for which no admissible arguments remain.

Let

$$
\operatorname{Args}(r)
$$

denote the arguments constrained by relation $`r`$.

Then:

$$
\boxed{
\operatorname{Args}(r)\cap A_D=\varnothing
\Rightarrow
r\notin D
}
$$

unless $`r`$ is itself capable of instantiating the missing arguments through admissible relational structure.

Pruning is therefore the inverse operation to relational constraint.

⸻

V. Primitive Relational Forms

Axiom 11 — Self-Relation

A self-relation relates an argument to itself under detection.

$$
A\leftrightarrow A.
$$

Self-relation is infinitely self-admissible.

It provides the minimal relational condition for an argument to participate in detector realization.

Self-relation alone does not determine the complete state of an argument once other-relations are admitted.

Other-relations supersede self-relation in determining relational configuration.

⸻

Axiom 12 — Exclusive Relation

An exclusive relation places its arguments in mutually incompatible states of a detector.

For arguments $`A`$ and $`B`$:

$$
A\mid B
$$

means that $`A`$ and $`B`$ cannot both be admitted as the case within the same detector state.

⸻

Axiom 13 — Inclusive Relation

An inclusive relation permits its arguments to be admitted within the same detector state.

Schematically:

$$
A\land B.
$$

Inclusion therefore does not require separation of its arguments.

⸻

Axiom 14 — Implicit Relation

For an argument to be the case, it must possess:

1. self-relation; and
2. relation to what else is the case.

The latter is called the implicit relation.

Thus:

$$
\text{self-relation}
+
\text{other-relation}
$$

constitutes the minimal relational condition for detector-level determination.

⸻

VI. Simultaneity

Axiom 15 — Simultaneous Relation

A simultaneous relation is an inclusive relation whose arguments are asserted to be the case within the same infinitesimal detector instance.

Schematically:

$$
A\mathrel{S}B
\Rightarrow
A,B\in D_n.
$$

Simultaneity therefore implies inclusion.

⸻

Axiom 16 — Non-Simultaneous Relation

A non-simultaneous relation is an inclusive relation whose arguments are related across detector instances rather than being simultaneously admitted in the same detector state.

Schematically:

$$
A\mathrel{N}B
$$

indicates that $`A`$ and $`B`$ are related, while their realization is separated across detector succession.

Critically:

$$
\boxed{
\text{non-simultaneous}\neq\text{exclusive}
}
$$

Exclusive relation describes incompatibility within a detector state.

Non-simultaneous relation describes relational separation across detector instances.

⸻

VII. Detector Classes

Axiom 17 — Implied Detectors

For every self-relation there is an implied detector.

For every set of things that are the case, there is an explicit detector.

The explicit detector must be compatible with the set of implied detectors generated by the self-relations of its arguments.

⸻

Axiom 18 — Relationally Undifferentiated Detector

In the absence of simultaneous and non-simultaneous relations, every relation whose arguments are available to the detector is admissible.

Since relations in Being are self-related, no sequential distinction is thereby generated.

Such a detector represents undifferentiated relational Being rather than sequential dynamics.

⸻

Axiom 19 — Generative Detector

A detector containing simultaneous or non-simultaneous relations has a relational structure capable of distinguishing successive detector realizations.

Such a detector may therefore generate a succession:

$$
D_0,D_1,D_2,\ldots
$$

through repeated application of admissibility and detection.

Transition is not primitive.

Any apparent transition must arise from changing relational admissibility.

⸻

VIII. Existence

Existence is formally downstream of relations, arguments, admissibility, and detection.

Neither relations nor arguments are required to satisfy a primitive predicate of existence.

They are pre-existent to the definition.

⸻

Axiom 20 — Existence

An entity $`E`$ exists in detector $`D`$ iff incrementing the detector does not destroy $`E`$.

Schematically:

$$
E\in D_n
$$

and

$$
E\in D_{n+1}
$$

under the relevant identity criterion implies persistence of $`E`$.

The exact identity criterion remains to be formalized.

⸻

Axiom 21 — Finite Existence

If $`E`$ remains admissibly instantiated for $`N`$ detector increments, then $`E`$ has an existence of length $`N`$.

$$
E\in D_0,D_1,\ldots,D_N.
$$

Existence does not entail invariant form.

An existent entity may undergo relational change while remaining the same entity under the relevant persistence criterion.

⸻

Axiom 22 — Unbounded Existence

If $`E`$ remains admissibly instantiated for an arbitrary number of detector increments, then $`E`$ has unbounded existence.

$$
\forall N\in\mathbb{N},
\quad
E\in D_0,\ldots,D_N.
$$

Thus:

$$
\boxed{
\text{existence}\neq\text{state invariance}
}
$$

and:

$$
\boxed{
\text{existence}=\text{persistence under detection}
}
$$

subject to the yet-to-be-formalized identity criterion.

⸻

IX. Provisional Projection / Shadow Extension

The original Boolean formulation produces admissibility but does not naturally generate nontrivial oscillatory dynamics.

A subsequent hypothesis therefore introduces multidimensional relations and partial projection.

This is not yet part of the proven core axioms.

⸻

Hypothesis P1 — Multidimensional Relations

Relations may possess more dimensions than are represented by a detector.

In the minimal toy model:

$$
\dim(R)=2
$$

while:

$$
\dim(D)=1.
$$

Arguments therefore possess a detector-visible component and an unrepresented component.

⸻

Hypothesis P2 — Projection

Detection realizes only the component of a relational configuration representable by the detector.

Let:

$$
\pi:R\rightarrow D
$$

denote projection onto the detector-visible relational dimension.

The remainder is not necessarily nonexistent.

It is unrepresented within the detector.

⸻

Hypothesis P3 — Shadow

For a relational state $`r`$, define:

$$
r=\pi(r)+\sigma(r)
$$

where:

$$
\pi(r)
$$

is the detector-visible projection and:

$$
\sigma(r)
$$

is the detector-invisible shadow component.

The shadow is relational structure constrained by the detector but not represented within its visible state.

⸻

Hypothesis P4 — Partial Projection

An argument need not be either completely represented or completely absent.

A relational configuration may therefore occupy an intermediate state:

$$
0<|\pi(r)|<|r|.
$$

This creates a third possibility between:

$$
\text{full projection}
$$

and:

$$
\text{cancellation}.
$$

⸻

Hypothesis P5 — Projection Dynamics

A candidate oscillator may arise from a cyclic redistribution between projected and shadow components:

$$
\text{full projection}
\rightarrow
\text{partial projection}
\rightarrow
\text{shadow-dominant state}
\rightarrow
\text{partial projection}
\rightarrow
\text{full projection}.
$$

No primitive transition relation is introduced.

The apparent transition is instead produced by changing projection under successive admissibility conditions.

⸻

Hypothesis P6 — Dimensional Mismatch

The apparent indeterminacy of a detector may arise from the detector representing fewer relational degrees of freedom than are present in the constraining relation.

Thus randomness may be modeled as:

$$
\boxed{
\text{randomness}
\sim
\text{dimensional mismatch}
}
$$

This is a conjecture about the eventual relation between projection and probability, not a current theorem.

⸻

X. Current Research Direction

The immediate objective is to determine whether a minimal finite relational system can satisfy the core axioms and exhibit:

1. persistent entities;
2. multidimensional relations;
3. partial projection;
4. shadow states;
5. sequential detector succession;
6. nontrivial oscillation;
7. no primitive transition relation;
8. no primitive causality;
9. potentially emergent probability.

The smallest useful target is a system containing at least two relational objects that persist and share state under detector succession.

The ultimate objective is to determine whether an algebraic structure can be constructed in which these phenomena emerge from relational constraints rather than being inserted as primitives.
