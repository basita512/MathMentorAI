# Matrices & Determinants – Comprehensive Worked Examples (JEE Level)

## Example 1: Matrix Multiplication

**Problem:** If A = [[1,2],[3,4]] and B = [[2,0],[1,2]], find AB.

**Key Concepts:**
- (AB)ᵢⱼ = Σ Aᵢₖ · Bₖⱼ (row of A × column of B)
- Matrix multiplication is NOT commutative: AB ≠ BA generally

**Detailed Solution:**

**Step 1:** Verify dimensions (2×2 · 2×2 = 2×2 ✓)

**Step 2:** Compute each element
```
AB₁₁ = 1×2 + 2×1 = 4
AB₁₂ = 1×0 + 2×2 = 4
AB₂₁ = 3×2 + 4×1 = 10
AB₂₂ = 3×0 + 4×2 = 8
```

**Final Answer:** AB = [[4,4],[10,8]]

---

## Example 2: Determinant (2×2)

**Problem:** Find |A| where A = [[3,5],[1,2]]

**Key Concepts:** |A| = ad - bc for [[a,b],[c,d]]

**Detailed Solution:**
```
|A| = 3×2 - 5×1 = 6 - 5 = 1
```

**Final Answer:** |A| = 1

---

## Example 3: Determinant (3×3) Using Row Operations

**Problem:** Evaluate |1 2 3; 4 5 6; 7 8 9|

**Key Concepts:**
- Row operations: Rᵢ → Rᵢ + kRⱼ don't change determinant
- If two rows are proportional, determinant = 0

**Detailed Solution:**

**Step 1:** Apply R₂ → R₂ - R₁, R₃ → R₃ - R₁
```
|1 2 3|    |1 2 3|
|4 5 6| → |3 3 3|
|7 8 9|    |6 6 6|
```

**Step 2:** R₃ = 2R₂, so rows are proportional
```
Determinant = 0
```

**Final Answer:** 0

---

## Example 4: Inverse of a 2×2 Matrix

**Problem:** Find inverse of A = [[2,1],[5,3]]

**Key Concepts:**
- A⁻¹ = (1/|A|) · adj(A)
- For 2×2: adj([[a,b],[c,d]]) = [[d,-b],[-c,a]]
- A⁻¹ exists only if |A| ≠ 0

**Detailed Solution:**

**Step 1:** Find determinant
```
|A| = 2×3 - 1×5 = 6 - 5 = 1 ≠ 0 ✓
```

**Step 2:** Find adjugate
```
adj(A) = [[3,-1],[-5,2]]
```

**Step 3:** Find inverse
```
A⁻¹ = (1/1)[[3,-1],[-5,2]] = [[3,-1],[-5,2]]
```

**Final Answer:** A⁻¹ = [[3,-1],[-5,2]]

**Verification:** AA⁻¹ = [[2,1],[5,3]]·[[3,-1],[-5,2]] = [[1,0],[0,1]] = I ✓

---

## Example 5: Solving System of Linear Equations (Cramer's Rule)

**Problem:** Solve: 2x + y = 5, x - y = 1

**Key Concepts:**
- Cramer's Rule: x = Dₓ/D, y = Dᵧ/D
- D = determinant of coefficient matrix

**Detailed Solution:**

**Step 1:** Find D
```
D = |2  1| = 2(-1) - 1(1) = -3
    |1 -1|
```

**Step 2:** Find Dₓ (replace x-coefficients with constants)
```
Dₓ = |5  1| = 5(-1) - 1(1) = -6
     |1 -1|
```

**Step 3:** Find Dᵧ
```
Dᵧ = |2 5| = 2(1) - 5(1) = -3
     |1 1|
```

**Step 4:** Solve
```
x = Dₓ/D = -6/-3 = 2
y = Dᵧ/D = -3/-3 = 1
```

**Final Answer:** x = 2, y = 1

**Verification:** 2(2)+1 = 5 ✓, 2-1 = 1 ✓

---

## Example 6: Area of Triangle Using Determinant

**Problem:** Find area of triangle with vertices (1,2), (4,6), (7,2).

**Key Concepts:**
- Area = (1/2)|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|
- Using determinant: Area = (1/2)|det of coordinate matrix|

**Detailed Solution:**
```
Area = (1/2)|1(6-2) + 4(2-2) + 7(2-6)|
     = (1/2)|4 + 0 - 28|
     = (1/2)|-24|
     = 12
```

**Final Answer:** Area = 12 square units

---

## Example 7: Properties of Determinants

**Problem:** If |A| = 5 for a 3×3 matrix A, find |3A|.

**Key Concepts:**
- |kA| = k^n · |A| for n×n matrix
- |AB| = |A|·|B|
- |A⁻¹| = 1/|A|
- |Aᵀ| = |A|

**Detailed Solution:**
```
|3A| = 3³ · |A| = 27 × 5 = 135
```

**Final Answer:** |3A| = 135

**Common Mistake:** Writing |3A| = 3|A| = 15 (WRONG! Must be 3^n · |A|)

---

## Example 8: Cayley-Hamilton Theorem

**Problem:** Verify Cayley-Hamilton theorem for A = [[1,2],[3,4]]

**Key Concepts:**
- Every matrix satisfies its own characteristic equation
- If det(A - λI) = 0 gives λ² - 5λ - 2 = 0, then A² - 5A - 2I = 0

**Detailed Solution:**

**Step 1:** Find characteristic equation
```
|A - λI| = |1-λ  2  | = (1-λ)(4-λ) - 6 = λ² - 5λ - 2 = 0
           |3    4-λ|
```

**Step 2:** Compute A² - 5A - 2I
```
A² = [[7,10],[15,22]]
5A = [[5,10],[15,20]]
2I = [[2,0],[0,2]]

A² - 5A - 2I = [[7-5-2, 10-10-0],[15-15-0, 22-20-2]] = [[0,0],[0,0]] ✓
```

**Final Answer:** Cayley-Hamilton verified: A² - 5A - 2I = 0

## Key Properties Reference

- |AB| = |A|·|B|
- |A⁻¹| = 1/|A|
- |kA| = k^n·|A| (n×n matrix)
- (AB)⁻¹ = B⁻¹A⁻¹
- (Aᵀ)⁻¹ = (A⁻¹)ᵀ
- Rank + Nullity = n
