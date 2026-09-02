"""
L1 RELATIONAL LABORATORY
========================

Minimal finite environment for testing the L1 closure-load hypothesis.

Relational substrate:

    x1 -> x2 -> x3
    y1 -> y2 -> y3

Detector quotient:

    x2 ~ y2 = M

Therefore:

    x1 -> M -> x3
    y1 -> M -> y3

At the path-1 prompt:

    sigma_n = {x1, x2}

the detector observes:

    q(sigma_n) = {x1, M}

The detector knows the prefix relation r1, but the relation required
to uniquely determine the continuation, r2, is not available.

L1:

    Delta_n = R_req - C_n
    rho_C(n) = |Delta_n|

We then vary the emission policy WITHOUT changing rho_C.

This is intentionally:
    - no neural network
    - no embeddings
    - no temperature
    - no external packages
    - no hidden stochastic mechanism

The goal is to establish the structural separation:

    relational deficit != emission stochasticity
    relational deficit != empirical error

"""

from dataclasses import dataclass
from typing import FrozenSet, Optional
import random


# ============================================================
# 1. RELATIONAL SUBSTRATE
# ============================================================

NODES = {
    "x1", "x2", "x3",
    "y1", "y2", "y3",
}

RELATIONS = {
    "r1": ("x1", "x2"),
    "r2": ("x2", "x3"),
    "r3": ("y1", "y2"),
    "r4": ("y2", "y3"),
}


# ============================================================
# 2. DETECTOR QUOTIENT
# ============================================================

# x2 and y2 are observationally indistinguishable.
QUOTIENT = {
    "x1": "x1",
    "x2": "M",
    "x3": "x3",

    "y1": "y1",
    "y2": "M",
    "y3": "y3",
}


def q(node: str) -> str:
    """Detector quotient map q : X -> X/~."""
    return QUOTIENT[node]


def quotient_relation(relation):
    """Apply q to both endpoints of a relation."""
    source, target = relation
    return q(source), q(target)


# ============================================================
# 3. DETECTOR STATE
# ============================================================

@dataclass(frozen=True)
class L1State:
    sigma: FrozenSet[str]

    # Relations currently accessible to the detector.
    C_n: FrozenSet[str]

    # Relations required to completely determine the continuation.
    R_req: FrozenSet[str]

    # Missing required relations.
    Delta_n: FrozenSet[str]

    # L1 closure load.
    rho_C: int

    # Continuations compatible with the quotient.
    admissible_continuations: FrozenSet[str]

    # Actual emitted continuation, if any.
    emitted: Optional[str] = None

    # Whether emission agrees with the original path.
    correct: Optional[bool] = None


def build_state(
    sigma,
    C_n,
    R_req,
    admissible_continuations,
    emitted=None,
):
    """
    Construct an L1 detector state.

    L1 is purely combinatorial:

        Delta_n = R_req - C_n

        rho_C(n) = |Delta_n|
    """

    Delta_n = frozenset(R_req - C_n)

    rho_C = len(Delta_n)

    correct = None

    if emitted is not None:
        # For this experiment, x3 is the continuation of the
        # original x-path.
        correct = (emitted == "x3")

    return L1State(
        sigma=frozenset(sigma),
        C_n=frozenset(C_n),
        R_req=frozenset(R_req),
        Delta_n=Delta_n,
        rho_C=rho_C,
        admissible_continuations=frozenset(
            admissible_continuations
        ),
        emitted=emitted,
        correct=correct,
    )


# ============================================================
# 4. INITIAL DETECTOR STATE
# ============================================================

def initial_state():
    """
    Construct the path-1 prompt.

        sigma_n = {x1, x2}

    The observed prefix is:

        r1 : x1 -> x2

    The required continuation is:

        r2 : x2 -> x3

    But because:

        q(x2) = q(y2) = M

    the detector cannot distinguish:

        M -> x3

    from:

        M -> y3
    """

    sigma = {
        "x1",
        "x2",
    }

    C_n = {
        "r1",
    }

    R_req = {
        "r1",
        "r2",
    }

    admissible_continuations = {
        "x3",
        "y3",
    }

    state = build_state(
        sigma=sigma,
        C_n=C_n,
        R_req=R_req,
        admissible_continuations=admissible_continuations,
    )

    return state


# ============================================================
# 5. EMISSION
# ============================================================

def emit(state, probability_x3, rng=None):
    """
    Emit either x3 or y3.

    probability_x3:
        probability of selecting x3.

    IMPORTANT:

        This function does NOT modify the relational substrate.
        It does NOT modify C_n.
        It does NOT modify Delta_n.
        It does NOT modify rho_C.

    It only specifies the emission policy.
    """

    if not 0.0 <= probability_x3 <= 1.0:
        raise ValueError(
            "probability_x3 must lie between 0 and 1"
        )

    if rng is None:
        rng = random

    if rng.random() < probability_x3:
        emitted = "x3"
    else:
        emitted = "y3"

    return build_state(
        sigma=state.sigma,
        C_n=state.C_n,
        R_req=state.R_req,
        admissible_continuations=state.admissible_continuations,
        emitted=emitted,
    )


# ============================================================
# 6. STRUCTURAL TESTS
# ============================================================

def test_quotient():
    """
    Verify the detector actually collapses x2 and y2.
    """

    assert q("x2") == "M"
    assert q("y2") == "M"

    assert q("x2") == q("y2")

    assert quotient_relation(
        RELATIONS["r2"]
    ) == ("M", "x3")

    assert quotient_relation(
        RELATIONS["r4"]
    ) == ("M", "y3")


def test_initial_state():
    """
    Verify the exact L1 deficit.
    """

    state = initial_state()

    assert state.Delta_n == {"r2"}

    assert state.rho_C == 1

    assert state.admissible_continuations == {
        "x3",
        "y3",
    }


def test_load_independent_of_emission():
    """
    Verify that changing emission policy does not change
    relational closure load.
    """

    state = initial_state()

    # Always emit x3.
    result = emit(
        state,
        probability_x3=1.0,
    )

    assert result.rho_C == 1
    assert result.correct is True

    # Always emit y3.
    result = emit(
        state,
        probability_x3=0.0,
    )

    assert result.rho_C == 1
    assert result.correct is False


# ============================================================
# 7. MONTE CARLO TEST
# ============================================================

def empirical_error(
    probability_x3,
    trials=10_000,
    seed=7,
):
    """
    Estimate empirical emission error.

    Since x3 is the correct continuation:

        expected error = 1 - P(x3)
    """

    rng = random.Random(seed)

    state = initial_state()

    errors = 0

    for _ in range(trials):

        result = emit(
            state,
            probability_x3=probability_x3,
            rng=rng,
        )

        if not result.correct:
            errors += 1

    return errors / trials


# ============================================================
# 8. REPORT
# ============================================================

def print_report():

    # Run structural tests first.
    test_quotient()
    test_initial_state()
    test_load_independent_of_emission()

    state = initial_state()

    print()
    print("=" * 72)
    print("L1 RELATIONAL LABORATORY")
    print("=" * 72)

    print()
    print("RELATIONAL SUBSTRATE")
    print("--------------------")

    print("    x1 -> x2 -> x3")
    print("    y1 -> y2 -> y3")

    print()
    print("DETECTOR QUOTIENT")
    print("------------------")

    print("    q(x2) = M")
    print("    q(y2) = M")

    print()
    print("Therefore:")
    print("    x2 ~ y2")

    print()
    print("PROMPT STATE")
    print("------------")

    print("    sigma_n =", sorted(state.sigma))

    quotient_sigma = {
        q(x)
        for x in state.sigma
    }

    print(
        "    q(sigma_n) =",
        sorted(quotient_sigma)
    )

    print(
        "    C_n =",
        sorted(state.C_n)
    )

    print(
        "    R_req =",
        sorted(state.R_req)
    )

    print(
        "    Delta_n =",
        sorted(state.Delta_n)
    )

    print(
        "    rho_C(n) =",
        state.rho_C
    )

    print(
        "    admissible continuations =",
        sorted(state.admissible_continuations)
    )

    print()
    print("EMISSION EXPERIMENT")
    print("-------------------")

    print(
        "  P(x3)      rho_C       empirical error"
    )

    print(
        "  ----------------------------------------"
    )

    for probability in [
        0.00,
        0.25,
        0.50,
        0.75,
        1.00,
    ]:

        error = empirical_error(
            probability
        )

        print(
            f"  {probability:5.2f}"
            f"        {state.rho_C:3d}"
            f"           {error:7.3f}"
        )

    print()
    print("STRUCTURAL RESULT")
    print("-----------------")

    print("    rho_C(n) = 1")
    print()
    print(
        "The quotient does not uniquely determine the"
    )
    print(
        "continuation."
    )

    print()
    print(
        "Changing emission policy changes empirical error,"
    )
    print(
        "but does not change rho_C."
    )

    print()
    print("Therefore:")
    print()
    print(
        "    structural underdetermination"
    )
    print(
        "                 !="
    )
    print(
        "    stochastic emission"
    )

    print()
    print(
        "and:"
    )

    print()
    print(
        "    closure load != empirical error"
    )

    print()
    print(
        "A nonzero closure load permits an unanchored"
    )
    print(
        "continuation, but does not force an incorrect"
    )
    print(
        "emission."
    )

    print()
    print("=" * 72)
    print("ALL STRUCTURAL TESTS PASSED")
    print("=" * 72)
    print()


# ============================================================
# 9. MAIN
# ============================================================

if __name__ == "__main__":
    print_report()
