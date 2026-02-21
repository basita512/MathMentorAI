# Limits, Continuity & Differentiability – Comprehensive Worked Examples (JEE Level)

## Example 1: Standard Trigonometric Limit

**Problem:** Evaluate lim(x→0) (sin x)/x

**Key Concepts:** This is the most fundamental limit in JEE. Must be memorized.

**Detailed Solution:**

**Method 1 - Standard result:**
```
lim(x→0) sin(x)/x = 1  (x in radians)
```

**Method 2 - Squeeze Theorem:**
```
For 0 < x < π/2:
cos(x) ≤ sin(x)/x ≤ 1

As x → 0: cos(0) = 1 and upper bound = 1
By squeeze theorem: lim = 1
```

**Related Standard Limits:**
- lim(x→0) tan(x)/x = 1
- lim(x→0) (1 - cos x)/x² = 1/2
- lim(x→0) sin(ax)/sin(bx) = a/b
- lim(x→0) (e^x - 1)/x = 1
- lim(x→0) ln(1+x)/x = 1
- lim(x→0) (a^x - 1)/x = ln(a)

---

## Example 2: Algebraic Limit (Factorization)

**Problem:** Evaluate lim(x→2) (x² - 4)/(x - 2)

**Key Concepts:**
- Direct substitution gives 0/0 (indeterminate)
- Factor to cancel common terms

**Detailed Solution:**

**Step 1:** Check direct substitution
```
Substituting x = 2: (4-4)/(2-2) = 0/0 (indeterminate)
```

**Step 2:** Factor numerator
```
x² - 4 = (x+2)(x-2)
```

**Step 3:** Cancel and evaluate
```
lim(x→2) (x+2)(x-2)/(x-2) = lim(x→2) (x+2) = 4
```

**Final Answer:** 4

**Common Mistakes:**
- Trying to evaluate 0/0 directly
- Forgetting to factor before canceling

---

## Example 3: L'Hôpital's Rule

**Problem:** Evaluate lim(x→0) (e^x - 1 - x)/x²

**Key Concepts:** When limit is 0/0 or ∞/∞, differentiate top and bottom separately.

**Detailed Solution:**

**Step 1:** Check form: (1-1-0)/0 = 0/0 ✓

**Step 2:** Apply L'Hôpital's
```
= lim(x→0) (e^x - 1)/(2x) → still 0/0
```

**Step 3:** Apply again
```
= lim(x→0) e^x/2 = 1/2
```

**Final Answer:** 1/2

---

## Example 4: Limit at Infinity

**Problem:** Evaluate lim(x→∞) (3x² + 2x)/(5x² - 1)

**Key Concepts:** Divide by highest power of x in denominator.

**Detailed Solution:**

**Step 1:** Divide numerator and denominator by x²
```
= lim(x→∞) (3 + 2/x)/(5 - 1/x²)
```

**Step 2:** As x → ∞, terms with x in denominator → 0
```
= (3 + 0)/(5 - 0) = 3/5
```

**Final Answer:** 3/5

**Rule of Thumb:**
- If degree(numerator) = degree(denominator): limit = ratio of leading coefficients
- If degree(num) < degree(den): limit = 0
- If degree(num) > degree(den): limit = ±∞

---

## Example 5: Continuity Check

**Problem:** Check continuity of f(x) = |x| at x = 0.

**Key Concepts:**
- f is continuous at x = a if: (1) f(a) exists, (2) lim f(x) exists, (3) they're equal

**Detailed Solution:**

**Step 1:** Check f(0)
```
f(0) = |0| = 0 ✓ (exists)
```

**Step 2:** Find left-hand limit
```
LHL = lim(x→0⁻) |x| = lim(x→0⁻) (-x) = 0
```

**Step 3:** Find right-hand limit
```
RHL = lim(x→0⁺) |x| = lim(x→0⁺) x = 0
```

**Step 4:** Compare
```
LHL = RHL = f(0) = 0
```

**Final Answer:** f(x) = |x| IS continuous at x = 0

---

## Example 6: Differentiability Check

**Problem:** Check differentiability of f(x) = |x| at x = 0.

**Key Concepts:**
- f is differentiable at x = a if left-hand derivative = right-hand derivative
- Differentiable ⇒ Continuous (but NOT vice versa!)

**Detailed Solution:**

**Step 1:** Left-hand derivative (LHD)
```
LHD = lim(h→0⁻) [f(0+h) - f(0)]/h
    = lim(h→0⁻) |h|/h
    = lim(h→0⁻) (-h)/h = -1
```

**Step 2:** Right-hand derivative (RHD)
```
RHD = lim(h→0⁺) [f(0+h) - f(0)]/h
    = lim(h→0⁺) |h|/h
    = lim(h→0⁺) h/h = 1
```

**Step 3:** Compare
```
LHD = -1 ≠ 1 = RHD
```

**Final Answer:** f(x) = |x| is NOT differentiable at x = 0

**Key Insight:** |x| is continuous but not differentiable at x = 0. This is a classic example showing continuity does NOT imply differentiability.

---

## Example 7: Derivative from First Principles

**Problem:** Find derivative of f(x) = x² using first principles.

**Key Concepts:** f'(x) = lim(h→0) [f(x+h) - f(x)]/h

**Detailed Solution:**

**Step 1:** Write the definition
```
f'(x) = lim(h→0) [(x+h)² - x²]/h
```

**Step 2:** Expand
```
= lim(h→0) [x² + 2xh + h² - x²]/h
= lim(h→0) [2xh + h²]/h
```

**Step 3:** Simplify
```
= lim(h→0) (2x + h) = 2x
```

**Final Answer:** f'(x) = 2x

---

## Example 8: Piecewise Function Continuity

**Problem:** Find value of k so that f(x) is continuous at x = 2:
f(x) = { kx + 1, x ≤ 2 ; 3x - 1, x > 2 }

**Detailed Solution:**

**Step 1:** For continuity at x = 2, LHL = RHL = f(2)

**Step 2:** Calculate each
```
f(2) = k(2) + 1 = 2k + 1

LHL = lim(x→2⁻) (kx + 1) = 2k + 1
RHL = lim(x→2⁺) (3x - 1) = 5
```

**Step 3:** Set equal
```
2k + 1 = 5
k = 2
```

**Final Answer:** k = 2

---

## Example 9: Mean Value Theorem

**Problem:** Verify MVT for f(x) = x² on [1, 3] and find c.

**Key Concepts:**
- Conditions: f continuous on [a,b], differentiable on (a,b)
- Conclusion: ∃ c ∈ (a,b) such that f'(c) = [f(b) - f(a)]/(b - a)

**Detailed Solution:**

**Step 1:** Verify conditions
```
f(x) = x² is polynomial → continuous and differentiable everywhere ✓
```

**Step 2:** Calculate RHS
```
[f(3) - f(1)]/(3-1) = (9-1)/2 = 4
```

**Step 3:** Find c
```
f'(x) = 2x
f'(c) = 4 → 2c = 4 → c = 2
c = 2 ∈ (1,3) ✓
```

**Final Answer:** MVT verified, c = 2

## Key Formulas Reference

| Limit | Value |
|-------|-------|
| lim(x→0) sin(x)/x | 1 |
| lim(x→0) tan(x)/x | 1 |
| lim(x→0) (e^x-1)/x | 1 |
| lim(x→0) ln(1+x)/x | 1 |
| lim(x→0) (1-cos x)/x² | 1/2 |
| lim(x→∞) (1+1/x)^x | e |
| lim(x→0) (1+x)^(1/x) | e |
