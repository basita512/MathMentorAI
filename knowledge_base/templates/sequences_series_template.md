# Sequences & Series - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Covers AP, GP, HP, special series, and advanced series techniques. Formulas are in `sequences_series.json`.

---

## Problem Type Identification & Approach

### Type 1: Identify the Sequence Type
**Decision**:
- Constant difference between consecutive terms -> AP
- Constant ratio between consecutive terms -> GP
- Reciprocals form an AP -> HP
- Terms are product of AP and GP terms -> AGP

### Type 2: Find nth Term or Sum

**For AP**: Use a_n = a + (n-1)d and S_n = n/2 * (first + last). Key: identify a and d first.

**For GP**: Use a_n = a*r^(n-1) and S_n = a(r^n - 1)/(r - 1). Key: identify a and r first.

**For HP**: Convert to AP of reciprocals, solve, then take reciprocal back.

**Choosing terms** (for problems where sum/product is given):
- 3 terms AP: (a-d), a, (a+d) -> sum = 3a
- 4 terms AP: (a-3d), (a-d), (a+d), (a+3d) -> common diff is 2d
- 3 terms GP: a/r, a, ar -> product = a^3
- 5 terms GP: a/r^2, a/r, a, ar, ar^2

### Type 3: Summation of Series

**Method selection**:
1. **Recognize standard series**: Sum of n, n^2, n^3 formulas
2. **Telescoping**: If terms cancel pairwise. Look for f(k) - f(k+1) pattern.
   - 1/(k*(k+1)) = 1/k - 1/(k+1) -> telescopes
   - Use partial fractions to reveal telescoping structure
3. **Method of differences**: When consecutive term differences form AP or GP
   - Find T_n = S_n - S_(n-1), identify pattern
4. **Vn method**: For series like 1/(a_n * a_(n+1)) where a_n is AP
   - 1/(a_n * a_(n+1)) = (1/d) * [1/a_n - 1/a_(n+1)]
5. **Multiply and subtract (S - rS)**: For AGP series
   - Write S, multiply by r, subtract to collapse most terms

### Type 4: Inequalities (AM-GM-HM)

**For positive real numbers**: AM >= GM >= HM. Equality when all numbers are equal.

**How to use for optimization**:
- To find minimum of (x + 1/x): Apply AM-GM. Min = 2 when x = 1/|x|, i.e., x = 1.
- To find minimum of sum given product constraint: Use AM >= GM
- To find maximum of product given sum constraint: Use AM >= GM (equality gives max product)

### Type 5: Infinite GP

**Before summing**: ALWAYS check |r| < 1. If not, infinite sum doesn't exist.
- Sum = a/(1-r) only when |r| < 1
- Common in problems involving recurring decimals

---

## Common Mistakes
- Confusing a_n (nth term) with S_n (sum of n terms). Remember: a_n = S_n - S_(n-1)
- Using infinite GP formula when |r| >= 1
- Applying AM-GM to negative numbers (only valid for positive reals)
- Wrong common difference when choosing symmetric AP terms (d vs 2d)
- Not converting HP to AP before solving
- For telescoping: missing the surviving terms at beginning and end

---

## JEE Problem-Solving Checklist
- Identify sequence type FIRST (AP, GP, HP, AGP, special)
- Write general term before attempting sum
- Check |r| < 1 for infinite GP
- Look for telescoping pattern in summation problems
- Use symmetric term selection to simplify sum/product conditions
- AM-GM is powerful for optimization - always check if applicable
