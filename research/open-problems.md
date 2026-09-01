# Relational Geometry — Open Problems

**Priority:** Research frontier  
**Last updated:** 2026-09-01

---

# I. Foundational Problems

## 1. What exactly is a relation?

The current theory treats relations as primitive but does not yet provide their algebraic definition.

Questions:

- What is the underlying set of relations?
- Can relations have arity?
- Can relations compose?
- Can relations be ordered?
- Can relations possess dimension?
- What is relational identity?

---

## 2. What exactly is an argument?

Arguments are currently defined negatively: they are not primitive and arise through relations.

We need a positive mathematical definition.

Questions:

- Is an argument an element of a set?
- Is it a tuple?
- Is it a projection of a relation?
- Is it a state-dependent realization?
- What determines argument identity across detector succession?

---

## 3. What is is-ness mathematically?

The theory distinguishes is-ness from existence, but no mathematical object currently represents is-ness.

Candidate structures:

- membership;
- realization;
- incidence;
- support;
- relational participation.

---

# II. Detector Problems

## 4. What is a detector mathematically?

The detector is currently described operationally.

We need to determine whether it is best represented as:

- an algebra;
- a closure system;
- a lattice;
- a relational substructure;
- a projection;
- a state-transition operator;
- a manifold;
- or a combination of these.

---

## 5. What determines admissibility?

This is currently the largest foundational ambiguity.

Possible candidates:

### A. Prior-state admissibility

\[
\mathcal A_{n+1}=F(D_n).
\]

### B. Joint admissibility

\[
\mathcal A_{n+1}=F(D_n,D_{n+1}^{\mathrm{potential}}).
\]

### C. Global relational admissibility

\[
\mathcal A_{n+1}=F(R,D_n).
\]

### D. Partial-projection admissibility

\[
\mathcal A_{n+1}
=
F(\pi(R),\sigma(R),D_n).
\]

Determine which formulation is mathematically consistent with the intended theory.

---

## 6. What makes admissibility generative?

A detector must be able to produce nontrivial succession without primitive transition.

Determine the minimal relational conditions under which:

\[
D_n\rightarrow D_{n+1}
\]

is not static.

---

# III. Projection and Shadow

## 7. What is the shadow space?

We need a formal definition of the detector-invisible component.

Questions:

- Is it a quotient?
- A complement?
- A fiber?
- A kernel?
- A higher-dimensional ambient space?
- A second relational algebra?

---

## 8. What is projection?

Determine whether projection is:

\[
\pi:R\rightarrow D
\]

or whether the detector itself defines the projection.

The latter would be substantially more interesting because projection would then emerge from detector architecture rather than being externally imposed.

---

## 9. What is partial projection?

Find the smallest formal structure allowing:

\[
0<\pi(r)<r
\]

in an appropriate mathematical sense.

---

## 10. Does cancellation mean destruction?

Determine whether:

\[
\pi(r)=0
\]

means:

1. the relation is destroyed;
2. the argument ceases to exist;
3. the argument remains in shadow;
4. the relation becomes undetectable but persists in Being.

---

# IV. Dynamics

## 11. Minimal Oscillator

Construct the smallest finite relational structure satisfying the current axioms and exhibiting a recurrent detector sequence.

Target:

\[
D_0\rightarrow D_1\rightarrow\cdots\rightarrow D_k=D_0.
\]

---

## 12. Oscillator Without Primitive Transition

Determine whether recurrence can arise solely from:

- simultaneous relations;
- non-simultaneous relations;
- admissibility;
- projection;
- shadow;
- pruning.

---

## 13. Minimum Relational Dimension

Determine the minimum relational dimension required for an oscillator.

Candidate hypothesis:

\[
\dim(R)\geq 2
\]

while:

\[
\dim(D)=1.
\]

---

## 14. Closure Rate

Determine whether the rate at which relational closure occurs is related to the number of undetected degrees of freedom.

Candidate relationship:

\[
\text{rate}
\sim
f(\text{undetected relational degrees of freedom}).
\]

---

# V. Probability

## 15. Emergence of Probability

Determine whether apparent randomness can arise from partial projection.

Candidate hypothesis:

\[
\boxed{
\text{randomness}
=
\text{dimensional mismatch}
}
\]

rather than fundamental stochasticity.

---

## 16. Emergence of Amplitude

Determine whether a continuous or complex amplitude arises naturally from the geometry of projection.

Potential candidate:

\[
r
=
\pi(r)+\sigma(r)
\]

followed by a rotational parameterization of the projection/shadow decomposition.

---

## 17. Recovery of Wave Functions

Determine whether conventional wave-function mathematics can emerge as a low-dimensional representation of relational projection.

This must be derived rather than assumed.

---

# VI. Causality and Time

## 18. Emergent Causality

Determine whether apparent causal direction can emerge from detector succession without primitive causality.

---

## 19. Retrocausality

Investigate whether apparent retrocausality can arise from joint admissibility.

Candidate interpretation:

A prior state does not get altered by a future state.

Rather, both belong to a joint relational class whose admissible members are constrained by the final detected state.

---

# VII. High-Dimensional State Space

## 20. Dimensional Blowup

Determine whether increasing relational dimension produces:

\[
|\text{possible histories}|\rightarrow\infty
\]

or, counterintuitively,

\[
|\text{admissible histories}|\downarrow.
\]

This is one of the central scalability questions.

---

## 21. History Compression

Determine whether relational constraints become sufficiently restrictive at higher dimension to reduce admissible histories.

If so, identify the mathematical mechanism.

---

# VIII. Formalization

## 22. Algebra of Relations

Identify the appropriate algebraic framework.

Candidates include:

- universal algebra;
- lattice theory;
- closure algebras;
- relation algebras;
- category theory;
- ordered structures;
- topological/algebraic structures;
- dynamical systems.

---

## 23. Formal Detector

Construct the first rigorous detector object.

---

## 24. Formal Existence

Formalize:

\[
E\text{ exists in }D
\iff
E\text{ persists under detector increment}.
\]

The critical unresolved issue is the identity relation required to determine whether \(E\) at \(D_n\) and \(E\) at \(D_{n+1}\) are the same entity.

---

## 25. Formal Oscillator

Prove or disprove the existence of a minimal oscillator satisfying the axioms without adding primitive transition or causality.
