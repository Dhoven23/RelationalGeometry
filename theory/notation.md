# Relational Geometry — Mathematical Notation

**Status:** Working notation  
**Last updated:** 2026-09-01

---

## Primitive Objects

| Symbol | Meaning |
|---|---|
| \(R\) | Relational structure of Being |
| \(r\) | A relation or relational subset |
| \(A\) | An argument |
| \(A_D\) | Arguments available to detector \(D\) |
| \(D\) | Detector |
| \(D_n\) | Detector at succession index \(n\) |
| \(E\) | Candidate entity |
| \(\Omega(D)\) | Potential state space of detector \(D\) |
| \(\mathcal A(D)\) | Admissible state space of detector \(D\) |

---

## Detector Operations

Detection:

\[
D:\Omega(D)\rightarrow\mathcal A(D)
\]

Detector succession:

\[
D_0\rightarrow D_1\rightarrow D_2\rightarrow\cdots
\]

---

## Relational Constraint

A relation \(r\) constraining argument \(A\):

\[
r\vdash A
\]

This notation is provisional and should not be confused with logical entailment unless that interpretation is explicitly intended.

---

## Argument Set of a Relation

\[
\operatorname{Args}(r)
\]

denotes the arguments constrained or instantiated by relation \(r\).

---

## Self-Relation

\[
A\leftrightarrow A
\]

---

## Inclusive Relation

\[
A\land B
\]

---

## Exclusive Relation

\[
A\mid B
\]

where \(A\) and \(B\) cannot both be the case within the same detector state.

---

## Simultaneous Relation

\[
A\mathrel{S}B
\]

with:

\[
A,B\in D_n.
\]

---

## Non-Simultaneous Relation

\[
A\mathrel{N}B
\]

indicating relational connection across detector succession rather than simultaneous realization.

---

## Projection

\[
\pi:R\rightarrow D
\]

denotes the projection of relational structure into detector-visible dimensions.

---

## Shadow

\[
\sigma:R\rightarrow S
\]

where \(S\) denotes the detector-invisible relational space.

A provisional decomposition is:

\[
r=\pi(r)+\sigma(r).
\]

This is not yet asserted to be vector addition in the mathematical sense.

---

## Partial Projection

\[
0<\|\pi(r)\|<\|r\|.
\]

The norm and underlying space have not yet been formally specified.

---

## Existence

Persistence of \(E\) under detector succession:

\[
E\in D_n
\Rightarrow
E\in D_{n+1}.
\]

The implication is subject to the eventual formal identity criterion for \(E\).

---

## Finite Existence

\[
E\in D_0,D_1,\ldots,D_N.
\]

---

## Unbounded Existence

\[
\forall N\in\mathbb N,\quad
E\in D_0,\ldots,D_N.
\]

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
- that \(S\) is orthogonal to the detector space;
- that Euler's formula applies formally.

Those are possible mathematical realizations, not current axioms.
