# Sequences & Series – Comprehensive Worked Examples (JEE Level)

## Example 1: nth Term of Arithmetic Progression

**Problem:** Find the 15th term of AP: 3, 7, 11, 15, ...

**Key Concepts:**
- nth term: aₙ = a + (n-1)d
- a = first term, d = common difference

**Detailed Solution:**

**Step 1:** Identify a and d
```
a = 3, d = 7 - 3 = 4
```

**Step 2:** Apply formula
```
a₁₅ = 3 + (15-1)(4) = 3 + 56 = 59
```

**Final Answer:** a₁₅ = 59

---

## Example 2: Sum of Arithmetic Progression

**Problem:** Find the sum of first 20 terms of AP: 5, 9, 13, ...

**Key Concepts:**
- Sₙ = n/2[2a + (n-1)d]
- Alternatively: Sₙ = n/2(first term + last term)

**Detailed Solution:**

**Step 1:** Identify a = 5, d = 4, n = 20

**Step 2:** Apply formula
```
S₂₀ = 20/2[2(5) + (19)(4)]
    = 10[10 + 76]
    = 10 × 86
    = 860
```

**Final Answer:** S₂₀ = 860

---

## Example 3: Arithmetic Mean

**Problem:** Insert 3 arithmetic means between 4 and 20.

**Key Concepts:**
- If m₁, m₂, ..., mₖ are k AMs between a and b:
  Common difference d = (b-a)/(k+1)

**Detailed Solution:**

**Step 1:** Find common difference
```
d = (20-4)/(3+1) = 16/4 = 4
```

**Step 2:** Find the means
```
m₁ = 4 + 4 = 8
m₂ = 8 + 4 = 12
m₃ = 12 + 4 = 16
```

**Final Answer:** The three AMs are 8, 12, 16

**Verification:** 4, 8, 12, 16, 20 → d = 4 for all consecutive pairs ✓

---

## Example 4: Sum of Infinite Geometric Series

**Problem:** Find sum of infinite GP: 4 + 2 + 1 + 1/2 + ...

**Key Concepts:**
- Sum = a/(1-r) only when |r| < 1
- a = first term, r = common ratio

**Detailed Solution:**

**Step 1:** Identify a and r
```
a = 4, r = 2/4 = 1/2
|r| = 1/2 < 1, so convergent ✓
```

**Step 2:** Apply formula
```
S = 4/(1 - 1/2) = 4/(1/2) = 8
```

**Final Answer:** Sum = 8

**Common Mistakes:**
- Applying formula when |r| ≥ 1 (series diverges!)
- Confusing a and r

---

## Example 5: Sum of Special Series (Squares)

**Problem:** Find 1² + 2² + 3² + ... + n²

**Key Concepts:**
- Standard formulas for sum of powers
- Σk = n(n+1)/2
- Σk² = n(n+1)(2n+1)/6
- Σk³ = [n(n+1)/2]²

**Detailed Solution:**
```
Σk² = n(n+1)(2n+1)/6
```

**Example:** For n = 10:
```
= 10(11)(21)/6 = 2310/6 = 385
```

**Final Answer:** Σk² (k=1 to n) = n(n+1)(2n+1)/6

---

## Example 6: Telescoping Series

**Problem:** Find 1/(1×2) + 1/(2×3) + 1/(3×4) + ... + 1/(n(n+1))

**Key Concepts:**
- Partial fractions: 1/(k(k+1)) = 1/k - 1/(k+1)
- Most terms cancel (telescope)

**Detailed Solution:**

**Step 1:** Decompose using partial fractions
```
1/(k(k+1)) = 1/k - 1/(k+1)
```

**Step 2:** Write out the sum
```
S = (1/1 - 1/2) + (1/2 - 1/3) + (1/3 - 1/4) + ... + (1/n - 1/(n+1))
```

**Step 3:** Cancel terms (telescoping)
```
S = 1 - 1/(n+1) = n/(n+1)
```

**Final Answer:** S = n/(n+1)

**For n = 9:** S = 9/10

---

## Example 7: Geometric Mean

**Problem:** Find the geometric mean between 2 and 18.

**Key Concepts:**
- GM of a and b = √(ab)
- GM of n numbers: (a₁·a₂·...·aₙ)^(1/n)
- AM ≥ GM ≥ HM (always!)

**Detailed Solution:**
```
GM = √(2 × 18) = √36 = 6
```

**Final Answer:** GM = 6

**Verification:** 2, 6, 18 → ratio = 3 for all ✓

---

## Example 8: Sum of GP

**Problem:** Find the sum of first 8 terms of GP: 3, 6, 12, ...

**Key Concepts:**
- Sₙ = a(rⁿ - 1)/(r - 1) when r > 1
- Sₙ = a(1 - rⁿ)/(1 - r) when r < 1

**Detailed Solution:**

**Step 1:** Identify a = 3, r = 2, n = 8

**Step 2:** Apply formula
```
S₈ = 3(2⁸ - 1)/(2 - 1) = 3(256 - 1)/1 = 3 × 255 = 765
```

**Final Answer:** S₈ = 765

---

## Example 9: AM-GM Inequality Application

**Problem:** If x > 0, find the minimum value of x + 4/x.

**Key Concepts:**
- AM ≥ GM: (a+b)/2 ≥ √(ab)
- Equality when a = b

**Detailed Solution:**

**Step 1:** Apply AM-GM
```
(x + 4/x)/2 ≥ √(x · 4/x) = √4 = 2
x + 4/x ≥ 4
```

**Step 2:** Find when equality holds
```
x = 4/x → x² = 4 → x = 2 (since x > 0)
```

**Final Answer:** Minimum value = 4, achieved at x = 2

## Key Formulas Summary

| Formula | Expression |
|---------|-----------|
| AP nth term | a + (n-1)d |
| AP sum | n/2[2a + (n-1)d] |
| GP nth term | arⁿ⁻¹ |
| GP sum (finite) | a(rⁿ-1)/(r-1) |
| GP sum (infinite) | a/(1-r) for \|r\|<1 |
| Σk | n(n+1)/2 |
| Σk² | n(n+1)(2n+1)/6 |
| Σk³ | [n(n+1)/2]² |
| AM-GM | AM ≥ GM always |
