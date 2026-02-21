# Binomial Theorem – Comprehensive Worked Examples (JEE Level)

## Example 1: Basic Expansion

**Problem:** Expand (x + y)⁴

**Key Concepts:**
- (x+y)^n = Σ nCr · x^(n-r) · y^r for r = 0 to n
- nCr = n!/(r!(n-r)!)
- Pascal's triangle for coefficients

**Detailed Solution:**
```
(x+y)⁴ = 4C0·x⁴ + 4C1·x³y + 4C2·x²y² + 4C3·xy³ + 4C4·y⁴
       = x⁴ + 4x³y + 6x²y² + 4xy³ + y⁴
```

**Final Answer:** x⁴ + 4x³y + 6x²y² + 4xy³ + y⁴

---

## Example 2: General Term

**Problem:** Find the general term of (2x - 3)⁵

**Key Concepts:**
- General term: T_{r+1} = nCr · (first term)^(n-r) · (second term)^r
- Watch for negative signs!

**Detailed Solution:**
```
T_{r+1} = 5Cr · (2x)^(5-r) · (-3)^r
        = 5Cr · 2^(5-r) · (-3)^r · x^(5-r)
```

**Example:** Find T₃ (r = 2)
```
T₃ = 5C2 · (2x)³ · (-3)²
   = 10 · 8x³ · 9
   = 720x³
```

**Common Mistakes:**
- Forgetting the negative sign in (-3)^r
- Off-by-one error: T_{r+1} not T_r

---

## Example 3: Middle Term

**Problem:** Find the middle term of (x + 1/x)⁸

**Key Concepts:**
- If n is even: one middle term = T_{n/2 + 1}
- If n is odd: two middle terms = T_{(n+1)/2} and T_{(n+3)/2}

**Detailed Solution:**

**Step 1:** n = 8 (even), so middle term = T₅ (r = 4)
```
T₅ = 8C4 · x⁴ · (1/x)⁴
   = 70 · x⁴ · x⁻⁴
   = 70
```

**Final Answer:** Middle term = 70

---

## Example 4: Term Independent of x

**Problem:** Find the term independent of x in (x² + 1/x)⁶

**Key Concepts:**
- Find general term, compute power of x, set it to zero

**Detailed Solution:**

**Step 1:** Write general term
```
T_{r+1} = 6Cr · (x²)^(6-r) · (1/x)^r
        = 6Cr · x^(12-2r) · x^(-r)
        = 6Cr · x^(12-3r)
```

**Step 2:** Set power of x = 0
```
12 - 3r = 0
r = 4
```

**Step 3:** Find the term
```
T₅ = 6C4 · 1 = 15
```

**Final Answer:** Term independent of x = 15

---

## Example 5: Sum of Coefficients

**Problem:** Find the sum of all coefficients in (1 + x)¹⁰

**Key Concepts:** Put x = 1 to get sum of coefficients

**Detailed Solution:**
```
Sum of coefficients = (1+1)¹⁰ = 2¹⁰ = 1024
```

**Final Answer:** 1024

---

## Example 6: Greatest Coefficient

**Problem:** Find the greatest coefficient in (1 + x)¹⁰

**Key Concepts:**
- Greatest coefficient in (1+x)^n is nC(n/2) when n is even
- nC(n/2) is the largest binomial coefficient

**Detailed Solution:**
```
Greatest coefficient = 10C5 = 252
```

**Final Answer:** 252

---

## Example 7: Binomial Approximation

**Problem:** Find approximate value of (1.02)⁵

**Key Concepts:**
- (1+x)^n ≈ 1 + nx + n(n-1)x²/2 for small x
- More terms → better approximation

**Detailed Solution:**

**Step 1:** Write as (1 + 0.02)⁵
```
n = 5, x = 0.02
```

**Step 2:** First approximation (two terms)
```
≈ 1 + 5(0.02) = 1.10
```

**Step 3:** Better approximation (three terms)
```
≈ 1 + 5(0.02) + 10(0.02)² = 1 + 0.1 + 0.004 = 1.104
```

**Final Answer:** (1.02)⁵ ≈ 1.104

---

## Example 8: Coefficient of Specific Term

**Problem:** Find the coefficient of x⁵ in (1 + x)⁸

**Detailed Solution:**
```
Coefficient of x⁵ = 8C5 = 8!/(5!3!) = 56
```

**Final Answer:** 56

## Key Properties Summary

- Sum of coefficients: put x = 1
- Sum of coefficients with alternating signs: put x = -1
- nC0 + nC1 + ... + nCn = 2^n
- nC0 - nC1 + nC2 - ... = 0
- nCr = nC(n-r)
- nCr + nC(r-1) = (n+1)Cr (Pascal's rule)
