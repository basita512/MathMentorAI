# Permutations & Combinations – Comprehensive Worked Examples (JEE Level)

## Example 1: Basic Permutation

**Problem:** In how many ways can 5 books be arranged on a shelf?

**Key Concepts:**
- Linear arrangement of n distinct objects = n!
- Order matters in permutation

**Detailed Solution:**
```
Number of arrangements = 5! = 5 × 4 × 3 × 2 × 1 = 120
```

**Final Answer:** 120

---

## Example 2: Permutations with Repetition

**Problem:** How many 4-digit numbers can be formed using digits {1, 2, 3, 4, 5} with repetition allowed?

**Key Concepts:** Each position has all choices available when repetition allowed.

**Detailed Solution:**
```
Each of 4 positions can be filled by any of 5 digits
Total = 5 × 5 × 5 × 5 = 5⁴ = 625
```

**Final Answer:** 625

---

## Example 3: Circular Permutation

**Problem:** In how many ways can 6 people sit around a circular table?

**Key Concepts:**
- Circular permutations = (n-1)!
- One position is fixed to avoid counting rotations

**Detailed Solution:**
```
Fix one person's position, arrange remaining 5
Arrangements = (6-1)! = 5! = 120
```

**Final Answer:** 120

**Note:** If the table has a distinct front (like necklace), divide by 2: 120/2 = 60

---

## Example 4: Permutations with Identical Objects

**Problem:** How many distinct arrangements of the word MISSISSIPPI are possible?

**Key Concepts:**
- n!/(p!·q!·r!) where p, q, r are frequencies of repeated letters

**Detailed Solution:**

**Step 1:** Count letters
```
M = 1, I = 4, S = 4, P = 2
Total letters = 11
```

**Step 2:** Apply formula
```
Arrangements = 11!/(4!·4!·2!) 
             = 39916800/(24 × 24 × 2)
             = 39916800/1152
             = 34650
```

**Final Answer:** 34,650

**Common Mistakes:**
- Missing repeated letters
- Not counting all occurrences correctly

---

## Example 5: Restricted Permutation (Group Constraint)

**Problem:** In how many ways can 4 boys and 3 girls sit in a row if all girls must sit together?

**Key Concepts:**
- Treat the group as a single unit
- Arrange units, then arrange within the group

**Detailed Solution:**

**Step 1:** Treat 3 girls as one block → 5 units (4 boys + 1 block)
```
Arrangements of 5 units = 5! = 120
```

**Step 2:** Girls can arrange within their block
```
Internal arrangements = 3! = 6
```

**Step 3:** Total
```
Total = 5! × 3! = 120 × 6 = 720
```

**Final Answer:** 720

---

## Example 6: Combination (Selection)

**Problem:** In how many ways can a committee of 3 be selected from 8 people?

**Key Concepts:**
- nCr = n!/(r!(n-r)!)
- Order does NOT matter in combination

**Detailed Solution:**
```
8C3 = 8!/(3!·5!) = (8 × 7 × 6)/(3 × 2 × 1) = 56
```

**Final Answer:** 56

---

## Example 7: Combinations with Constraints

**Problem:** From 5 men and 4 women, form a committee of 4 with at least 2 women.

**Key Concepts:** "At least 2 women" = exactly 2W + exactly 3W + exactly 4W

**Detailed Solution:**

**Case 1:** 2 women + 2 men
```
4C2 × 5C2 = 6 × 10 = 60
```

**Case 2:** 3 women + 1 man
```
4C3 × 5C1 = 4 × 5 = 20
```

**Case 3:** 4 women + 0 men
```
4C4 × 5C0 = 1 × 1 = 1
```

**Total:**
```
60 + 20 + 1 = 81
```

**Final Answer:** 81

---

## Example 8: Derangement

**Problem:** Find the number of derangements of {1, 2, 3, 4} (no element in its original position).

**Key Concepts:**
- Derangement formula: !n = n! × Σ(-1)^k/k! for k = 0 to n
- !n = n!(1 - 1/1! + 1/2! - 1/3! + ... + (-1)^n/n!)

**Detailed Solution:**
```
!4 = 4!(1 - 1 + 1/2 - 1/6 + 1/24)
   = 24(1/2 - 1/6 + 1/24)
   = 24(12/24 - 4/24 + 1/24)
   = 24(9/24)
   = 9
```

**Final Answer:** 9 derangements

---

## Example 9: Complementary Counting

**Problem:** How many 3-digit numbers contain at least one digit 5?

**Key Concepts:**
- "At least one" → Total - None
- Complementary counting is often easier

**Detailed Solution:**

**Step 1:** Count all 3-digit numbers
```
100 to 999 → Total = 900
```

**Step 2:** Count 3-digit numbers with NO 5
```
Hundreds place: 8 choices (1-9 except 5)
Tens place: 9 choices (0-9 except 5)
Units place: 9 choices (0-9 except 5)
Without 5 = 8 × 9 × 9 = 648
```

**Step 3:** Answer
```
At least one 5 = 900 - 648 = 252
```

**Final Answer:** 252

---

## Example 10: Distribution Problems

**Problem:** Distribute 5 identical balls into 3 distinct boxes.

**Key Concepts:**
- Stars and bars: C(n+r-1, r-1) ways
- n = balls, r = boxes

**Detailed Solution:**
```
Ways = C(5+3-1, 3-1) = C(7, 2) = 21
```

**Final Answer:** 21

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Permutation | nPr = n!/(n-r)! |
| Combination | nCr = n!/(r!(n-r)!) |
| Circular Perm. | (n-1)! |
| With repetition | n!/(p!q!r!) |
| Derangement | !n = n!Σ(-1)^k/k! |
| Stars and bars | C(n+r-1, r-1) |
| At least one | Total - None |
