"""
L3 MATROID RELATIONAL LABORATORY
================================

Demonstrates that L1 counts raw missing relations, whereas L3 counts 
independent relational degrees of freedom via pure matroid rank r_M(Delta).

No vector spaces, no matrices, no floating-point arithmetic.
"""

from dataclasses import dataclass
from typing import FrozenSet, Set, Callable

# ============================================================
# 1. MATROID DEFINITION (PURE COMBINATORICS)
# ============================================================

@dataclass
class Matroid:
    ground_set: FrozenSet[str]
    # Independence oracle: returns True if subset S in I
    _independent_oracle: Callable[[FrozenSet[str]], bool]

    def is_independent(self, subset: FrozenSet[str]) -> bool:
        assert subset.issubset(self.ground_set), "Subset must be in ground set."
        return self._independent_oracle(subset)

    def rank(self, subset: FrozenSet[str]) -> int:
        """
        r_M(A) = max { |I| : I <= A, I in Calligraphic_I }
        Calculated by greedy evaluation over power set of the subset.
        """
        subset_list = list(subset)
        max_rank = 0
        
        # Power set search for maximal independent subset
        n = len(subset_list)
        for i in range(1 << n):
            candidate = frozenset([subset_list[j] for j in range(n) if (i & (1 << j))])
            if self.is_independent(candidate):
                max_rank = max(max_rank, len(candidate))
                
        return max_rank

    def closure(self, subset: FrozenSet[str]) -> FrozenSet[str]:
        """
        cl_M(A) = { e in R : r_M(A U {e}) = r_M(A) }
        """
        r_A = self.rank(subset)
        cl = set(subset)
        for e in self.ground_set:
            if self.rank(subset | {e}) == r_A:
                cl.add(e)
        return frozenset(cl)


# ============================================================
# 2. EXPERIMENTAL SETUP
# ============================================================

def build_relational_matroid() -> Matroid:
    """
    Constructs a matroid where:
      - {r1, r2, r3} forms a dependent circuit (e.g., r3 is transitively implied by r1 and r2).
      - {r4, r5} are mutually independent relations.
    """
    ground_set = frozenset({"r1", "r2", "r3", "r4", "r5"})

    def oracle(S: FrozenSet[str]) -> bool:
        # {r1, r2, r3} is a dependent set; any subset containing all 3 is dependent
        if {"r1", "r2", "r3"}.issubset(S):
            return False
        return True

    return Matroid(ground_set=ground_set, _independent_oracle=oracle)


# ============================================================
# 3. EXPERIMENT RUNNER
# ============================================================

def run_l3_laboratory():
    M = build_relational_matroid()

    # Deficit A: 3 missing relations, but r3 is in cl_M({r1, r2})
    Delta_A = frozenset({"r1", "r2", "r3"})
    
    # Deficit B: 2 missing relations, both structurally independent
    Delta_B = frozenset({"r4", "r5"})

    # Evaluate Metrics
    L1_A = len(Delta_A)
    L3_A = M.rank(Delta_A)

    L1_B = len(Delta_B)
    L3_B = M.rank(Delta_B)

    print("========================================================================")
    print("L3 MATROID RELATIONAL LABORATORY RESULT")
    print("========================================================================")
    print(f"Deficit A (Redundant):   Delta_A = {sorted(Delta_A)}")
    print(f"  L1 Load: |Delta_A|            = {L1_A}")
    print(f"  L3 Load: r_M(Delta_A)          = {L3_A}")
    print(f"  Closure: cl_M({{r1, r2}})       = {sorted(M.closure(frozenset({'r1', 'r2'})))}")
    print()
    print(f"Deficit B (Independent): Delta_B = {sorted(Delta_B)}")
    print(f"  L1 Load: |Delta_B|            = {L1_B}")
    print(f"  L3 Load: r_M(Delta_B)          = {L3_B}")
    print("------------------------------------------------------------------------")
    print("STRUCTURAL DIVERGENCE:")
    print(f"  L1 Order: L1(Delta_A) > L1(Delta_B)  -->  ({L1_A} > {L1_B}) [MISLEADING]")
    print(f"  L3 Order: L3(Delta_A) == L3(Delta_B) -->  ({L3_A} == {L3_B}) [STRUCTURALLY EXACT]")
    print("========================================================================")


if __name__ == "__main__":
    run_l3_laboratory()
