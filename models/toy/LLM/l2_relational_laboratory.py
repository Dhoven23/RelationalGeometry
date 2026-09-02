#!/usr/bin/env python3

"""
L2 RELATIONAL LABORATORY

L1:
    rho_L1 = |Delta|

L2:
    rho_L2 = sum(w(r) for r in Delta)

The experiment keeps structural closure load separate from
emission probability and empirical error.
"""

from dataclasses import dataclass
import random


# ============================================================
# RELATIONAL SUBSTRATE
# ============================================================

RELATIONS = {
    "r1": ("x1", "x2"),
    "r2": ("x2", "x3"),
    "r3": ("y1", "y2"),
    "r4": ("y2", "y3"),
}

# In this toy model:
#
#     w(r) = number of downstream distinctions depending on r
#
# Hence r2 and r4 carry more closure load than r1 and r3.

WEIGHTS = {
    "r1": 1.0,
    "r2": 5.0,
    "r3": 1.0,
    "r4": 5.0,
}


# ============================================================
# DETECTOR QUOTIENT
# ============================================================

QUOTIENT = {
    "x1": "x1",
    "x2": "M",
    "x3": "x3",
    "y1": "y1",
    "y2": "M",
    "y3": "y3",
}


# ============================================================
# STATE
# ============================================================

@dataclass(frozen=True)
class L2State:

    sigma: frozenset
    C_n: frozenset
    R_req: frozenset
    Delta_n: frozenset

    rho_L1: int
    rho_L2: float


# ============================================================
# CLOSURE LOAD
# ============================================================

def closure_load_l1(deficit):
    """
    L1 = cardinality of relational deficit.
    """

    return len(deficit)


def closure_load_l2(deficit, weights):
    """
    L2 = weighted relational deficit.
    """

    return sum(
        weights[r]
        for r in deficit
    )


def build_state(sigma, C_n, R_req, weights):

    Delta_n = frozenset(
        R_req - C_n
    )

    return L2State(

        sigma=frozenset(sigma),

        C_n=frozenset(C_n),

        R_req=frozenset(R_req),

        Delta_n=Delta_n,

        rho_L1=closure_load_l1(
            Delta_n
        ),

        rho_L2=closure_load_l2(
            Delta_n,
            weights
        ),
    )


# ============================================================
# ADMISSIBLE CONTINUATIONS
# ============================================================

def admissible_continuations():

    """
    Because x2 and y2 are identified by the detector,

        q(x2) = q(y2) = M

    the quotient cannot distinguish the two downstream
    continuations.
    """

    return frozenset({
        "x3",
        "y3"
    })


# ============================================================
# EMISSION MODEL
# ============================================================

def emit(p_x3):

    """
    Explicit emission policy.

    p_x3 = probability of emitting x3.
    """

    if random.random() < p_x3:
        return "x3"

    return "y3"


def empirical_error(
    p_x3,
    trials=10000,
    seed=12345
):

    """
    The reference continuation is x3.

    This measures empirical emission error while leaving
    the relational structure completely unchanged.
    """

    random.seed(seed)

    errors = 0

    for _ in range(trials):

        prediction = emit(p_x3)

        if prediction != "x3":
            errors += 1

    return errors / trials


# ============================================================
# L1 vs L2 COMPARISON
# ============================================================

def compare_deficits():

    """
    Construct different deficits and compare:

        L1 = number of missing relations

        L2 = weighted relational load

    """

    examples = {

        # One high-weight relation
        "A": frozenset({
            "r2"
        }),

        # Two low-weight relations
        "B": frozenset({
            "r1",
            "r3"
        }),

        # One high-weight relation
        "C": frozenset({
            "r4"
        }),

        # One low + one high
        "D": frozenset({
            "r1",
            "r2"
        }),

        # One low + one high
        "E": frozenset({
            "r3",
            "r4"
        }),
    }

    print("L1 vs L2 DEFICIT COMPARISON")
    print("---------------------------")

    print(
        "  case   missing relations      "
        "L1       L2"
    )

    print(
        "  -------------------------------------------"
    )

    for name, deficit in examples.items():

        l1 = closure_load_l1(
            deficit
        )

        l2 = closure_load_l2(
            deficit,
            WEIGHTS
        )

        relations = ", ".join(
            sorted(deficit)
        )

        print(
            f"   {name:<4}   "
            f"{relations:<20} "
            f"{l1:>3}    "
            f"{l2:>6.1f}"
        )

    print()


# ============================================================
# STRUCTURAL TESTS
# ============================================================

def run_assertions(state):

    # Detector quotient

    assert (
        QUOTIENT["x2"]
        ==
        QUOTIENT["y2"]
        ==
        "M"
    )

    # The deficit is exactly r2.

    assert state.Delta_n == frozenset({
        "r2"
    })

    # L1 sees one missing relation.

    assert state.rho_L1 == 1

    # L2 sees a relational load of five.

    assert state.rho_L2 == 5.0

    # Quotient does not uniquely determine continuation.

    assert (
        admissible_continuations()
        ==
        frozenset({
            "x3",
            "y3"
        })
    )

    # Emission policy cannot change structural load.

    for p in (
        0.0,
        0.25,
        0.5,
        0.75,
        1.0
    ):

        state_again = build_state(

            sigma={
                "x1",
                "x2"
            },

            C_n={
                "r1"
            },

            R_req={
                "r1",
                "r2"
            },

            weights=WEIGHTS
        )

        assert (
            state_again.rho_L1
            ==
            state.rho_L1
        )

        assert (
            state_again.rho_L2
            ==
            state.rho_L2
        )


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 72)
    print("L2 RELATIONAL LABORATORY")
    print("=" * 72)

    print()

    # --------------------------------------------------------
    # SUBSTRATE
    # --------------------------------------------------------

    print("RELATIONAL SUBSTRATE")
    print("--------------------")

    print("    x1 -> x2 -> x3")
    print("    y1 -> y2 -> y3")

    print()

    # --------------------------------------------------------
    # WEIGHTS
    # --------------------------------------------------------

    print("RELATIONAL WEIGHTS")
    print("------------------")

    for r in sorted(WEIGHTS):

        source, target = RELATIONS[r]

        print(
            f"    {r}: "
            f"{source} -> {target}    "
            f"weight = {WEIGHTS[r]:.1f}"
        )

    print()

    # --------------------------------------------------------
    # QUOTIENT
    # --------------------------------------------------------

    print("DETECTOR QUOTIENT")
    print("-----------------")

    print("    q(x2) = M")
    print("    q(y2) = M")

    print()

    print("Therefore:")
    print("    x2 ~ y2")

    print()

    # --------------------------------------------------------
    # PROMPT STATE
    # --------------------------------------------------------

    sigma_n = {
        "x1",
        "x2"
    }

    C_n = {
        "r1"
    }

    R_req = {
        "r1",
        "r2"
    }

    state = build_state(

        sigma=sigma_n,

        C_n=C_n,

        R_req=R_req,

        weights=WEIGHTS
    )

    print("PROMPT STATE")
    print("------------")

    print(
        f"    sigma_n = "
        f"{sorted(state.sigma)}"
    )

    print(
        f"    q(sigma_n) = "
        f"{[QUOTIENT[x] for x in sorted(state.sigma)]}"
    )

    print(
        f"    C_n = "
        f"{sorted(state.C_n)}"
    )

    print(
        f"    R_req = "
        f"{sorted(state.R_req)}"
    )

    print(
        f"    Delta_n = "
        f"{sorted(state.Delta_n)}"
    )

    print(
        f"    rho_L1(n) = "
        f"{state.rho_L1}"
    )

    print(
        f"    rho_L2(n) = "
        f"{state.rho_L2:.1f}"
    )

    print(
        "    admissible continuations = "
        f"{sorted(admissible_continuations())}"
    )

    print()

    # --------------------------------------------------------
    # EMISSION EXPERIMENT
    # --------------------------------------------------------

    print("EMISSION EXPERIMENT")
    print("-------------------")

    print(
        "  P(x3)      rho_L1     "
        "rho_L2       empirical error"
    )

    print(
        "  ----------------------------------------------------"
    )

    for p in (
        0.00,
        0.25,
        0.50,
        0.75,
        1.00
    ):

        error = empirical_error(
            p
        )

        print(
            f"   {p:>4.2f}         "
            f"{state.rho_L1:>1}         "
            f"{state.rho_L2:>4.1f}            "
            f"{error:>7.3f}"
        )

    print()

    # --------------------------------------------------------
    # DEFICIT COMPARISON
    # --------------------------------------------------------

    compare_deficits()

    # --------------------------------------------------------
    # INTERPRETATION
    # --------------------------------------------------------

    print("STRUCTURAL RESULT")
    print("-----------------")

    print(
        f"    rho_L1(n) = "
        f"{state.rho_L1}"
    )

    print(
        f"    rho_L2(n) = "
        f"{state.rho_L2:.1f}"
    )

    print()

    print(
        "The quotient does not uniquely determine the"
    )

    print(
        "continuation."
    )

    print()

    print(
        "L1 counts the missing relation."
    )

    print(
        "L2 measures the weighted relational load of"
    )

    print(
        "that deficit."
    )

    print()

    print(
        "Changing emission policy changes empirical error,"
    )

    print(
        "but does not change rho_L1 or rho_L2."
    )

    print()

    print("Therefore:")

    print()

    print(
        "    relational deficit"
    )

    print(
        "             !="
    )

    print(
        "    weighted closure load"
    )

    print(
        "             !="
    )

    print(
        "    emission probability"
    )

    print(
        "             !="
    )

    print(
        "    empirical error"
    )

    print()

    print(
        "The key L2 question is:"
    )

    print()

    print(
        "    Does weighted relational load predict"
    )

    print(
        "    detector failure better than raw"
    )

    print(
        "    deficit cardinality?"
    )

    print()

    # --------------------------------------------------------
    # TESTS
    # --------------------------------------------------------

    run_assertions(
        state
    )

    print("=" * 72)
    print("ALL L2 STRUCTURAL TESTS PASSED")
    print("=" * 72)


if __name__ == "__main__":
    main()
