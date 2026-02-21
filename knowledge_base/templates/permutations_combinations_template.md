# Permutations & Combinations - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Covers counting principles, arrangements, selections, and distribution. Formulas are in `permutations_combinations.json`.

---

## The Master Decision Tree

### Step 1: Arrangement or Selection?
- Does ORDER matter? -> **Permutation** (arrangement)
- Does ORDER not matter? -> **Combination** (selection)

### Step 2: Any Special Structure?
- **Circular arrangement?** -> Fix one element, arrange rest
  - Distinct clockwise/anticlockwise: (n-1)!
  - Identical (necklace/bracelet): (n-1)!/2
- **Repeated/identical objects?** -> Divide by factorial of repetitions: n!/(p!q!r!)
- **Repetition allowed?** -> n^r (for r positions, n choices each)
- **Stars and bars?** -> Distributing identical objects: use C(n+r-1, r)

### Step 3: Any Restrictions?
- **Together constraint** -> Group method: treat group as one unit, then arrange within group
- **Apart constraint** -> Gap method: arrange others first, place restricted objects in gaps
  - OR use complementary counting: Total - Together
- **At least / at most** -> Usually easiest with complementary counting

---

## Problem Type Approaches

### Type 1: Arrangement of Distinct Objects
- n objects in a row: n!
- r objects from n: nPr
- Circular: (n-1)!

### Type 2: Arrangement with Identical Objects
- n objects where p are alike, q are alike: n!/(p!q!)
- Example approach: MISSISSIPPI = 11!/(4!4!2!)

### Type 3: Numbers Formed from Digits
**Approach**:
1. Determine how many digits the number has
2. Handle leading-zero restriction separately (first digit has fewer choices)
3. Fill remaining positions
4. With repetition: multiply choices. Without: use permutation counting.

### Type 4: Selection Problems
- Basic: choose r from n = C(n,r)
- With constraints: fix required items, choose remaining
- At least one: Total - None
- Distribution of identical objects into distinct groups: Stars and bars C(n+k-1, k-1)
- Positive integer solutions of x1+x2+...+xk = n: C(n-1, k-1)

### Type 5: Distribution Problems
- Distinct objects into distinct groups (sizes r1, r2, ...): n!/(r1!r2!...rk!)
- Each object to one of k groups (unrestricted): k^n
- Identical objects into distinct groups: Stars and bars

### Type 6: Derangement
- No object in its original position
- Use derangement formula: !n = n! * sum((-1)^k / k!) from k=0 to n
- Small values: !1=0, !2=1, !3=2, !4=9, !5=44

### Type 7: Inclusion-Exclusion
- |A1 union A2 union ... union Ak| = sum|Ai| - sum|Ai intersect Aj| + ...
- Useful when counting elements NOT in any set, or in at least one set

---

## Common Mistakes
- Confusing permutation (order matters) with combination (order doesn't matter)
- Not handling leading zeros in digit problems
- Using wrong formula for circular permutations ((n-1)! not n!)
- Double-counting: not dividing by repetitions
- Applying nPr when n < r (impossible)
- Forgetting to consider identical arrangements when objects are similar

---

## JEE Problem-Solving Checklist
- FIRST decide: arrangement or selection?
- Check for restrictions: together, apart, at least, at most
- Use complementary counting when direct counting is hard
- For circular: fix one element first
- For digit problems: handle leading zero separately
- Verify: does your answer accidentally count identical arrangements?
