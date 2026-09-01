# Relational Geometry — Agent Instructions

## Purpose

This repository contains the development of Relational Geometry (RG),
a proposed formal framework in which relational structure precedes
argument instantiation, detector states arise through admissibility,
and existence is defined downstream as persistence under detector
succession.

This is a mathematical research project, not a software product.

## Core principle

Do not silently convert conjectures, interpretations, analogies,
or experimentally observed behavior into axioms or theorems.

Always distinguish:

- Definition
- Axiom
- Lemma
- Theorem
- Conjecture
- Model result
- Experimental result
- Interpretation
- Open problem

## Current theory

The authoritative statement of the current theory is:

    theory/current.md

Do not infer the current axioms from historical research notes when
current.md disagrees with them.

## Research history

Historical reasoning, abandoned formulations, failed approaches,
and conceptual decisions are stored in:

    research/

These files are important because previous failures often constrain
the current theory.

## Formal mathematics

The Lean formalization lives in:

    formal/

Lean is the authority for formally proven mathematical claims.

Do not describe a proposition as proven unless it is actually
verified by Lean or another explicitly identified formal system.

## Computational models

Finite and computational experiments live in:

    models/
    experiments/

Computational evidence does not constitute a proof.

## AI behavior

Before modifying the repository:

1. Read AGENTS.md.
2. Read theory/current.md.
3. Read the relevant research files.
4. Inspect the relevant formal or experimental implementation.
5. State the proposed change before making substantial modifications.

Do not rewrite axioms merely to make a proof succeed.

If a theorem fails because the axioms are insufficient, report that
as a mathematical result rather than weakening the theorem or adding
an unrequested axiom.

## Terminology

Use RG terminology exactly as defined in theory/definitions.md.

Do not silently substitute conventional physics terminology for RG
terminology.

In particular, distinguish:

- Being
- is-ness
- existence
- relation
- argument
- detector
- admissibility
- projection
- shadow
- simultaneity
- non-simultaneity
- exclusion
- persistence

## Research philosophy

Prefer the smallest structure capable of demonstrating a phenomenon.

When possible:

1. construct the smallest finite model;
2. search it computationally;
3. identify the mathematical structure;
4. formulate the general theorem;
5. formalize and prove it.

Counterexamples are valuable results.

A failure to produce an oscillator is not evidence that the theory
is wrong until the relevant assumptions have been isolated.

## Current research priority

The immediate mathematical objective is to determine whether
multidimensional relations, partial projection, and shadow structure
can produce a nontrivial detector succession containing an oscillator
without introducing primitive transition or causality.
