# Relational Geometry — Mathematical Notation

**Status:** Working notation  
**Last updated:** 2026-09-01

---

## Primitive Objects

| Symbol | Meaning |
|---|---|
| $R$ | Relational structure of Being |
| $r$ | A relation or relational subset |
| $A$ | An argument |
| $A_D$ | Arguments available to detector $D$ |
| $D$ | Detector |
| $D_n$ | Detector at succession index $n$ |
| $E$ | Candidate entity |
| $\Omega(D)$ | Potential state space of detector $D$ |
| $\mathcal{A}(D)$ | Admissible state space of detector $D$ |

---

## Detector Operations

### Detection

$$
\mathsf{Detect}_D:\Omega(D)\rightarrow\mathcal{A}(D)
$$

The detector maps a potential state to an admissible state.

### Detector Succession

$$
D_0\rightarrow D_1\rightarrow D_2\rightarrow\cdots
$$

Succession denotes repeated detector realization. The detector itself has no duration.

---

## Relational Constraint

A relation $r$ constraining an argument $A$:

$$
r\vdash A
$$

This notation is provisional and should not be confused with logical entailment unless that interpretation is explicitly intended.

---

## Argument Set of a Relation

$$
\operatorname{Args}(r)
$$

denotes the arguments constrained or instantiated by relation $r$.

---

## Self-Relation

A self-relation relates an argument to itself:

$$
A\leftrightarrow A
$$

Self-relation represents the minimal relational participation of an argument in detector realization.

---

## Inclusive Relation

An inclusive relation permits its arguments to be admissible in the same detector state:

$$
A\land B
$$

The use of $\land$ is provisional notation for relational inclusion and does not necessarily denote the logical conjunction operator.

---

## Exclusive Relation

An exclusive relation prevents its arguments from simultaneously being the case:

$$
A\mid B
$$

where $A$ and $B$ cannot both be the case within the same detector state.

Exclusive relation is distinct from non-simultaneous relation.

---

## Simultaneous Relation

A simultaneous relation asserts that its arguments are the case within the same detector instance:

$$
A\mathrel{S}B
$$

with:

$$
A,B\in D_n.
$$

A simultaneous relation implies inclusion.

---

## Non-Simultaneous Relation

A non-simultaneous relation connects arguments across detector succession while asserting that they are not simultaneously realized:

$$
A\mathrel{N}B
$$

For a detector state $D_n$:

$$
\neg(A,B\in D_n)
$$

while the relational connection between $A$ and $B$ remains admissible across succession.

Non-simultaneous relation is therefore **not** equivalent to exclusive relation:

$$
A\mathrel{N}B\neq A\mid B.
$$

---

## Projection

Projection denotes the realization of relational structure within the detector-visible dimensions:

$$
\pi:R\rightarrow D
$$

This notation is provisional. The precise mathematical type of $\pi$ remains to be determined.

---

## Shadow

Let $S$ denote detector-invisible relational degrees of freedom.

A shadow map is provisionally written:

$$
\sigma:R\rightarrow S
$$

A relation may therefore be represented schematically as:

$$
r=\pi(r)+\sigma(r).
$$

This expression is **not** yet asserted to be vector addition. It represents a conceptual decomposition into detector-visible and detector-invisible components.

---

## Partial Projection

A relation is partially projected when its detector-visible realization does not exhaust its relational structure.

Schematically:

$$
0<\|\pi(r)\|<\|r\|.
$$

The norm $\|\cdot\|$ and the underlying mathematical spaces have not yet been formally specified.

Thus this is currently a conceptual notation rather than an established definition.

---

## Full Projection

A relation is fully projected when its relevant relational content is completely represented within the detector:

$$
\sigma(r)=0.
$$

This notation is provisional and depends upon the eventual formal definition of shadow.

---

## Cancellation

A relation may have nonzero relational structure while its detector-visible projection cancels:

$$
\pi(r)=0,
\qquad
\sigma(r)\neq0.
$$

This represents a candidate state in which the relation remains present in the relational structure but is not realized within the detector-visible state.

Cancellation is a proposed mechanism for detector dynamics and is **not yet an axiom**.

---

## Existence

Existence is defined downstream of detection.

An entity $E$ exists in detector $D_n$ if detector succession does not destroy its admissible instantiation.

Schematically:

$$
E\in D_n
\quad\Longrightarrow\quad
E\in D_{n+1}.
$$

The precise identity criterion for $E$ remains to be formally defined.

Existence therefore denotes persistence under detector succession rather than mere participation in Being.

---

## Finite Existence

If $E$ remains admissibly instantiated through $N$ detector increments:

$$
E\in D_0,D_1,\ldots,D_N.
$$

Then $E$ has an existence of length $N$.

---

## Unbounded Existence

If $E$ remains admissibly instantiated for an arbitrary number of detector increments:

$$
\forall N\in\mathbb{N},\qquad
E\in D_0,D_1,\ldots,D_N.
$$

Then $E$ has unbounded existence in the detector.

---

## Projection and Detector Dynamics

The current hypothesis is that nontrivial detector dynamics may arise from incomplete projection.

A candidate relational cycle is:

$$
\text{full projection}
\rightarrow
\text{partial projection}
\rightarrow
\text{cancellation}
\rightarrow
\text{partial projection}
\rightarrow
\text{full projection}.
$$

The corresponding detector sequence is provisionally represented as:

$$
D_0\rightarrow D_1\rightarrow D_2\rightarrow D_3\rightarrow D_4.
$$

This is a **modeling hypothesis**, not a current axiom.

The intended purpose is to determine whether oscillatory behavior can emerge from relational structure and projection alone, without introducing a primitive transition relation.

---

## Important Notational Caution

The symbols above are placeholders for structures whose precise algebraic interpretation remains open.

In particular, the following have **not** yet been established:

- that relations form a vector space;
- that projection is linear;
- that shadow is a vector-space complement;
- that amplitudes are real or complex numbers;
- that detector states form a manifold;
- that detector succession possesses a metric;
- that $S$ is orthogonal to the detector space;
- that Euler's formula applies formally;
- that probability amplitudes are fundamental;
- that partial projection necessarily produces oscillation.

These are possible mathematical realizations or research hypotheses, **not current axioms**.