# Vector Algebra – Comprehensive Worked Examples (JEE Level)

## Example 1: Magnitude of a Vector

**Problem:** Find magnitude of vector a = 3i - 4j + 12k

**Key Concepts:**
- |a| = √(a₁² + a₂² + a₃²)

**Detailed Solution:**
```
|a| = √(3² + (-4)² + 12²)
    = √(9 + 16 + 144)
    = √169 = 13
```

**Final Answer:** |a| = 13

---

## Example 2: Unit Vector

**Problem:** Find unit vector in direction of a = 2i + 2j + k

**Key Concepts:**
- Unit vector â = a/|a|
- |â| = 1 always

**Detailed Solution:**

**Step 1:** Find magnitude
```
|a| = √(4 + 4 + 1) = √9 = 3
```

**Step 2:** Divide by magnitude
```
â = (2i + 2j + k)/3 = (2/3)i + (2/3)j + (1/3)k
```

**Final Answer:** â = (2/3)i + (2/3)j + (1/3)k

**Verification:** |(2/3)² + (2/3)² + (1/3)²| = |4/9 + 4/9 + 1/9| = 1 ✓

---

## Example 3: Dot Product and Angle Between Vectors

**Problem:** Find angle between a = i + j + k and b = 2i - j + k

**Key Concepts:**
- a · b = |a||b|cos θ
- cos θ = (a · b)/(|a||b|)

**Detailed Solution:**

**Step 1:** Compute dot product
```
a · b = (1)(2) + (1)(-1) + (1)(1) = 2 - 1 + 1 = 2
```

**Step 2:** Find magnitudes
```
|a| = √(1+1+1) = √3
|b| = √(4+1+1) = √6
```

**Step 3:** Find angle
```
cos θ = 2/(√3 × √6) = 2/√18 = 2/(3√2) = √2/3
θ = cos⁻¹(√2/3)
```

**Final Answer:** θ = cos⁻¹(√2/3)

---

## Example 4: Projection of Vector

**Problem:** Find projection of a = 3i + 4j - 5k on b = 2i - 3j + 6k

**Key Concepts:**
- Scalar projection = (a · b)/|b|
- Vector projection = [(a · b)/|b|²]b

**Detailed Solution:**

**Step 1:** Dot product
```
a · b = 3(2) + 4(-3) + (-5)(6) = 6 - 12 - 30 = -36
```

**Step 2:** |b|
```
|b| = √(4 + 9 + 36) = √49 = 7
```

**Step 3:** Scalar projection
```
Projection = -36/7
```

**Final Answer:** Scalar projection = -36/7 (negative means opposite direction)

---

## Example 5: Cross Product

**Problem:** Find a × b where a = i + 2j + 3k and b = 2i + j - k

**Key Concepts:**
- a × b = |i  j  k |
            |a₁ a₂ a₃|
            |b₁ b₂ b₃|
- a × b is perpendicular to both a and b

**Detailed Solution:**

**Step 1:** Set up determinant
```
a × b = | i    j    k  |
        | 1    2    3  |
        | 2    1   -1  |
```

**Step 2:** Expand
```
= i(2(-1) - 3(1)) - j(1(-1) - 3(2)) + k(1(1) - 2(2))
= i(-2 - 3) - j(-1 - 6) + k(1 - 4)
= -5i + 7j - 3k
```

**Final Answer:** a × b = -5i + 7j - 3k

**Verification:** Check perpendicularity:
a · (a × b) = 1(-5) + 2(7) + 3(-3) = -5 + 14 - 9 = 0 ✓

---

## Example 6: Area of Triangle Using Cross Product

**Problem:** Find area of triangle with vertices A(1,1,1), B(2,3,1), C(1,2,3)

**Key Concepts:**
- Area = (1/2)|AB × AC|

**Detailed Solution:**

**Step 1:** Find vectors
```
AB = B - A = (1, 2, 0)
AC = C - A = (0, 1, 2)
```

**Step 2:** Cross product
```
AB × AC = | i  j  k |
          | 1  2  0 |
          | 0  1  2 |
= i(4-0) - j(2-0) + k(1-0) = 4i - 2j + k
```

**Step 3:** Find area
```
|AB × AC| = √(16 + 4 + 1) = √21
Area = (1/2)√21
```

**Final Answer:** Area = √21/2 square units

---

## Example 7: Scalar Triple Product and Volume

**Problem:** Find volume of parallelepiped formed by a = i + j, b = j + k, c = k + i

**Key Concepts:**
- Volume = |a · (b × c)| = |[a b c]|
- If [a b c] = 0 → vectors are coplanar

**Detailed Solution:**

**Step 1:** Compute using determinant
```
[a b c] = |1 1 0|
          |0 1 1|
          |1 0 1|
```

**Step 2:** Expand along first row
```
= 1(1-0) - 1(0-1) + 0(0-1)
= 1 + 1 + 0 = 2
```

**Final Answer:** Volume = 2 cubic units

---

## Example 8: Coplanarity Test

**Problem:** Check if vectors a = (1,2,3), b = (2,4,6), c = (1,1,1) are coplanar.

**Key Concepts:** Coplanar if and only if [a b c] = 0

**Detailed Solution:**
```
[a b c] = |1 2 3|
          |2 4 6|
          |1 1 1|
```

Note: R₂ = 2R₁, so det = 0

**Final Answer:** Vectors ARE coplanar (b = 2a, so they're linearly dependent)

## Key Formulas Reference

| Operation | Formula | Result |
|-----------|---------|--------|
| Dot product | a · b = Σaᵢbᵢ | Scalar |
| Cross product | a × b = det | Vector ⊥ both |
| Scalar triple | [a b c] = a·(b×c) | Scalar (volume) |
| Projection | (a·b)/\|b\| | Scalar |
| Area of triangle | (1/2)\|a × b\| | Scalar |
| Volume | \|[a b c]\| | Scalar |
| a × b = 0 | a ∥ b | Parallel test |
| a · b = 0 | a ⊥ b | Perpendicular test |
