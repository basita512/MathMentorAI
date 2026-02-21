# Sets, Relations & Functions – Comprehensive Worked Examples (JEE Level)

## Example 1: Power Set

**Problem:** Find the power set of A = {1, 2, 3}.

**Key Concepts:**
- Power set P(A) = set of all subsets of A
- |P(A)| = 2^n where n = |A|

**Detailed Solution:**

**Step 1:** Count: |P(A)| = 2³ = 8

**Step 2:** List all subsets
```
P(A) = {∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
```

**Final Answer:** 8 elements; P(A) = {∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}

---

## Example 2: Set Operations and De Morgan's Laws

**Problem:** If U = {1,2,3,4,5,6,7,8,9,10}, A = {1,2,3,4,5}, B = {3,4,5,6,7}, verify (A ∪ B)' = A' ∩ B'.

**Key Concepts:**
- A' = complement = U - A
- De Morgan's: (A ∪ B)' = A' ∩ B', (A ∩ B)' = A' ∪ B'

**Detailed Solution:**

**Step 1:** LHS
```
A ∪ B = {1,2,3,4,5,6,7}
(A ∪ B)' = {8,9,10}
```

**Step 2:** RHS
```
A' = {6,7,8,9,10}
B' = {1,2,8,9,10}
A' ∩ B' = {8,9,10}
```

**Step 3:** Compare
```
LHS = RHS = {8,9,10} ✓
```

**Final Answer:** Verified: (A ∪ B)' = A' ∩ B' = {8,9,10}

---

## Example 3: Types of Relations

**Problem:** Let A = {1, 2, 3}. Determine if R = {(1,1), (2,2), (3,3), (1,2), (2,1)} is an equivalence relation.

**Key Concepts:**
- Reflexive: (a,a) ∈ R for all a ∈ A
- Symmetric: (a,b) ∈ R ⟹ (b,a) ∈ R
- Transitive: (a,b) ∈ R and (b,c) ∈ R ⟹ (a,c) ∈ R
- Equivalence = Reflexive + Symmetric + Transitive

**Detailed Solution:**

**Step 1:** Reflexive check
```
(1,1) ∈ R ✓, (2,2) ∈ R ✓, (3,3) ∈ R ✓
Reflexive ✓
```

**Step 2:** Symmetric check
```
(1,2) ∈ R → (2,1) ∈ R ✓
All others are reflexive pairs
Symmetric ✓
```

**Step 3:** Transitive check
```
(1,2) ∈ R and (2,1) ∈ R → need (1,1) ∈ R ✓
(2,1) ∈ R and (1,2) ∈ R → need (2,2) ∈ R ✓
Transitive ✓
```

**Final Answer:** R IS an equivalence relation

---

## Example 4: Number of Relations and Functions

**Problem:** If |A| = 2 and |B| = 3, find: (a) number of relations from A to B, (b) number of functions from A to B.

**Key Concepts:**
- Relations from A to B: subsets of A × B → 2^(|A|×|B|)
- Functions from A to B: each element of A maps to exactly one in B → |B|^|A|

**Detailed Solution:**
```
(a) Relations = 2^(2×3) = 2⁶ = 64
(b) Functions = 3² = 9
```

**Final Answer:** 64 relations, 9 functions

---

## Example 5: One-One and Onto Functions

**Problem:** Check if f: ℝ → ℝ defined by f(x) = 2x + 3 is one-one and onto.

**Key Concepts:**
- One-one (injective): f(a) = f(b) ⟹ a = b
- Onto (surjective): every element in codomain has a preimage
- Bijective = one-one + onto → invertible

**Detailed Solution:**

**Step 1:** One-one test
```
f(a) = f(b) → 2a + 3 = 2b + 3 → a = b ✓
```

**Step 2:** Onto test
```
For any y ∈ ℝ, we need x such that 2x + 3 = y
x = (y-3)/2 ∈ ℝ ✓
```

**Final Answer:** f is one-one AND onto (bijective)

**Inverse:** f⁻¹(x) = (x - 3)/2

---

## Example 6: Composition of Functions

**Problem:** If f(x) = x² and g(x) = x + 1, find (f ∘ g)(x) and (g ∘ f)(x). Are they equal?

**Key Concepts:**
- (f ∘ g)(x) = f(g(x)): apply g first, then f
- Composition is NOT commutative in general

**Detailed Solution:**

**Step 1:** f ∘ g
```
(f ∘ g)(x) = f(g(x)) = f(x+1) = (x+1)² = x² + 2x + 1
```

**Step 2:** g ∘ f
```
(g ∘ f)(x) = g(f(x)) = g(x²) = x² + 1
```

**Step 3:** Compare
```
(f ∘ g)(x) = x² + 2x + 1
(g ∘ f)(x) = x² + 1
They are NOT equal!
```

**Final Answer:** f ∘ g ≠ g ∘ f (composition is not commutative)

---

## Example 7: Domain and Range

**Problem:** Find domain and range of f(x) = √(4 - x²).

**Key Concepts:**
- Domain: values of x for which f(x) is defined
- For √(expression): expression ≥ 0

**Detailed Solution:**

**Step 1:** Domain - need 4 - x² ≥ 0
```
x² ≤ 4
-2 ≤ x ≤ 2
Domain = [-2, 2]
```

**Step 2:** Range - find min and max of √(4-x²)
```
Minimum: when x² = 4 → f = 0
Maximum: when x = 0 → f = √4 = 2
Range = [0, 2]
```

**Final Answer:** Domain = [-2, 2], Range = [0, 2]

---

## Example 8: Inverse Function

**Problem:** Find inverse of f(x) = (2x + 3)/(x - 1), x ≠ 1.

**Key Concepts:**
- Replace f(x) with y, solve for x in terms of y
- Then swap x and y

**Detailed Solution:**

**Step 1:** Set y = (2x+3)/(x-1)
```
y(x-1) = 2x + 3
xy - y = 2x + 3
xy - 2x = y + 3
x(y - 2) = y + 3
x = (y + 3)/(y - 2)
```

**Step 2:** Swap x and y
```
f⁻¹(x) = (x + 3)/(x - 2), x ≠ 2
```

**Final Answer:** f⁻¹(x) = (x + 3)/(x - 2)

**Verification:** f(f⁻¹(x)) = f((x+3)/(x-2)) = ... = x ✓

## Key Concepts Summary

| Concept | Condition |
|---------|-----------|
| Reflexive | (a,a) ∈ R ∀a |
| Symmetric | (a,b) ∈ R ⟹ (b,a) ∈ R |
| Transitive | (a,b),(b,c) ∈ R ⟹ (a,c) ∈ R |
| One-one | f(a) = f(b) ⟹ a = b |
| Onto | Range = Codomain |
| Bijective | One-one + Onto |
| \|P(A)\| | 2^n |
| Functions A→B | \|B\|^{\|A\|} |
