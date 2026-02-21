# Complex Numbers & Quadratic Equations – Comprehensive Worked Examples (JEE Level)

## Example 1: Modulus and Argument

**Problem:** If z = 3 + 4i, find |z| and arg(z).

**Key Concepts:**
- |z| = √(a² + b²) for z = a + bi
- arg(z) = tan⁻¹(b/a), adjusted for quadrant

**Detailed Solution:**

**Step 1:** Find modulus
```
|z| = √(3² + 4²) = √(9 + 16) = √25 = 5
```

**Step 2:** Find argument
```
arg(z) = tan⁻¹(4/3) ≈ 53.13° (first quadrant, both parts positive)
```

**Final Answer:** |z| = 5, arg(z) = tan⁻¹(4/3)

---

## Example 2: Argument in Different Quadrants

**Problem:** Find the argument of z = -1 + i.

**Key Concepts:** Argument depends on which quadrant z lies in (not just tan⁻¹(b/a))

**Detailed Solution:**

**Step 1:** Identify quadrant
```
Real part = -1 (negative), Imaginary part = 1 (positive)
z is in second quadrant
```

**Step 2:** Calculate
```
Reference angle = tan⁻¹(1/1) = π/4
Since second quadrant: arg(z) = π - π/4 = 3π/4
```

**Final Answer:** arg(z) = 3π/4

**Common Mistakes:**
- Not adjusting for quadrant (just using tan⁻¹(b/a) always)
- Quadrant rules: Q1: θ, Q2: π-θ, Q3: -(π-θ), Q4: -θ

---

## Example 3: Division Using Conjugate

**Problem:** Simplify (1 + i)/(1 - i)

**Key Concepts:** Multiply by conjugate to make denominator real.

**Detailed Solution:**

**Step 1:** Multiply by conjugate of denominator
```
(1+i)/(1-i) × (1+i)/(1+i)
= (1+i)² / [(1-i)(1+i)]
```

**Step 2:** Expand
```
Numerator: (1+i)² = 1 + 2i + i² = 1 + 2i - 1 = 2i
Denominator: 1 - i² = 1 + 1 = 2
```

**Step 3:** Simplify
```
= 2i/2 = i
```

**Final Answer:** i

**Verification:** i(1-i) = i - i² = i + 1 = 1 + i ✓

---

## Example 4: Nature of Roots (Discriminant)

**Problem:** Determine the nature of roots of x² - 4x + 5 = 0.

**Key Concepts:**
- D = b² - 4ac
- D > 0: two distinct real roots
- D = 0: two equal real roots
- D < 0: two complex conjugate roots

**Detailed Solution:**

**Step 1:** Identify a, b, c
```
a = 1, b = -4, c = 5
```

**Step 2:** Calculate discriminant
```
D = (-4)² - 4(1)(5) = 16 - 20 = -4
```

**Step 3:** Interpret
```
D = -4 < 0 → Roots are complex conjugates
```

**Step 4:** Find the roots
```
x = (4 ± √(-4))/2 = (4 ± 2i)/2 = 2 ± i
```

**Final Answer:** Roots are 2 + i and 2 - i (complex conjugate pair)

---

## Example 5: Relation Between Roots and Coefficients

**Problem:** If α, β are roots of x² - 7x + 10 = 0, find α² + β².

**Key Concepts (Vieta's Formulas):**
- Sum of roots: α + β = -b/a
- Product of roots: αβ = c/a
- α² + β² = (α + β)² - 2αβ

**Detailed Solution:**

**Step 1:** Find sum and product
```
α + β = 7
αβ = 10
```

**Step 2:** Use identity
```
α² + β² = (α + β)² - 2αβ
        = 49 - 20
        = 29
```

**Final Answer:** α² + β² = 29

**More useful identities:**
- α³ + β³ = (α + β)³ - 3αβ(α + β)
- |α - β| = √(D)/|a| = √((α+β)² - 4αβ)
- 1/α + 1/β = (α + β)/(αβ)

---

## Example 6: Finding Maximum/Minimum of Quadratic

**Problem:** Find the maximum value of f(x) = -2x² + 8x - 3.

**Key Concepts:**
- For ax² + bx + c: vertex at x = -b/(2a)
- If a < 0 → maximum, if a > 0 → minimum
- Extreme value = f(-b/(2a)) = c - b²/(4a)

**Detailed Solution:**

**Step 1:** Find vertex x-coordinate
```
x = -b/(2a) = -8/(2×(-2)) = 2
```

**Step 2:** Find maximum value
```
f(2) = -2(4) + 8(2) - 3 = -8 + 16 - 3 = 5
```

**Final Answer:** Maximum value = 5 at x = 2

---

## Example 7: Cube Roots of Unity

**Problem:** Find the cube roots of unity and verify ω² + ω + 1 = 0.

**Key Concepts:**
- Three cube roots of 1: 1, ω, ω²
- ω = (-1 + i√3)/2, ω² = (-1 - i√3)/2
- Properties: 1 + ω + ω² = 0, ω³ = 1

**Detailed Solution:**

**Step 1:** Solve x³ = 1
```
x³ - 1 = 0
(x-1)(x² + x + 1) = 0
```

**Step 2:** From x² + x + 1 = 0
```
x = (-1 ± √(1-4))/2 = (-1 ± i√3)/2
```

**Step 3:** Define ω
```
ω = (-1 + i√3)/2
ω² = (-1 - i√3)/2
```

**Step 4:** Verify
```
ω² + ω + 1 = (-1-i√3)/2 + (-1+i√3)/2 + 1
            = (-1-i√3-1+i√3)/2 + 1
            = -2/2 + 1 = 0 ✓
```

**Final Answer:** Cube roots: 1, (-1+i√3)/2, (-1-i√3)/2. Verified ω²+ω+1=0.

## Key Formulas Reference

- Quadratic formula: x = (-b ± √D)/(2a) where D = b²-4ac
- Vieta's: α+β = -b/a, αβ = c/a
- |z₁z₂| = |z₁||z₂|
- arg(z₁z₂) = arg(z₁) + arg(z₂)
- z·z̄ = |z|²
- De Moivre: (cosθ + i sinθ)^n = cos(nθ) + i sin(nθ)
