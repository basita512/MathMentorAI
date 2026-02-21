# Integral Calculus – Comprehensive Worked Examples (JEE Level)

## Example 1: Basic Indefinite Integrals

**Problem:** Evaluate ∫(3x² + 2x - 5) dx

**Key Concepts:** Power rule: ∫x^n dx = x^(n+1)/(n+1) + C

**Detailed Solution:**
```
∫(3x² + 2x - 5) dx = 3·x³/3 + 2·x²/2 - 5x + C
                    = x³ + x² - 5x + C
```

**Final Answer:** x³ + x² - 5x + C

**Common Mistakes:**
- Forgetting the constant of integration C
- Wrong power rule application

---

## Example 2: Integration by Substitution

**Problem:** Evaluate ∫2x·cos(x²) dx

**Key Concepts:**
- Substitution: if f(g(x))·g'(x) appears, let u = g(x)
- Look for "function and its derivative" pattern

**Detailed Solution:**

**Step 1:** Identify substitution
```
Let u = x² ⇒ du = 2x dx
```

**Step 2:** Transform integral
```
∫2x·cos(x²) dx = ∫cos(u) du
```

**Step 3:** Integrate and back-substitute
```
= sin(u) + C = sin(x²) + C
```

**Final Answer:** sin(x²) + C

**Related Patterns:**
- ∫f'(x)/f(x) dx = ln|f(x)| + C
- ∫f(x)^n · f'(x) dx = f(x)^(n+1)/(n+1) + C

---

## Example 3: Integration by Parts

**Problem:** Evaluate ∫x·e^x dx

**Key Concepts:**
- Formula: ∫u dv = uv - ∫v du
- ILATE rule for choosing u: Inverse trig > Log > Algebraic > Trig > Exponential

**Detailed Solution:**

**Step 1:** Choose u and dv (ILATE: x is Algebraic, e^x is Exponential)
```
u = x     → du = dx
dv = e^x dx → v = e^x
```

**Step 2:** Apply formula
```
∫x·e^x dx = x·e^x - ∫e^x dx
           = x·e^x - e^x + C
           = e^x(x - 1) + C
```

**Final Answer:** e^x(x - 1) + C

**Verification:** d/dx[e^x(x-1)] = e^x(x-1) + e^x = xe^x ✓

---

## Example 4: Partial Fractions

**Problem:** Evaluate ∫1/(x² - 1) dx

**Key Concepts:**
- Factor denominator: x² - 1 = (x-1)(x+1)
- Decompose: A/(x-1) + B/(x+1)

**Detailed Solution:**

**Step 1:** Factor and decompose
```
1/(x²-1) = A/(x-1) + B/(x+1)
1 = A(x+1) + B(x-1)
```

**Step 2:** Find A and B
```
Put x = 1: 1 = 2A → A = 1/2
Put x = -1: 1 = -2B → B = -1/2
```

**Step 3:** Integrate
```
∫[1/2·1/(x-1) - 1/2·1/(x+1)] dx
= (1/2)ln|x-1| - (1/2)ln|x+1| + C
= (1/2)ln|(x-1)/(x+1)| + C
```

**Final Answer:** (1/2)ln|(x-1)/(x+1)| + C

---

## Example 5: Definite Integral

**Problem:** Evaluate ∫₀^π sin x dx

**Detailed Solution:**

**Step 1:** Find antiderivative
```
∫sin x dx = -cos x
```

**Step 2:** Apply limits
```
[-cos x]₀^π = -cos(π) - (-cos(0))
            = -(-1) + 1
            = 1 + 1 = 2
```

**Final Answer:** 2

---

## Example 6: Properties of Definite Integrals

**Problem:** Evaluate ∫₀^(π/2) sin^n(x)/(sin^n(x) + cos^n(x)) dx

**Key Concepts:**
- Property: ∫₀^a f(x) dx = ∫₀^a f(a-x) dx
- King's rule: Add original and transformed integrals

**Detailed Solution:**

**Step 1:** Let I = ∫₀^(π/2) sinⁿx/(sinⁿx + cosⁿx) dx

**Step 2:** Apply property with a = π/2
```
I = ∫₀^(π/2) cosⁿx/(cosⁿx + sinⁿx) dx  (replacing x by π/2 - x)
```

**Step 3:** Add original and transformed
```
2I = ∫₀^(π/2) (sinⁿx + cosⁿx)/(sinⁿx + cosⁿx) dx
2I = ∫₀^(π/2) 1 dx = π/2
```

**Step 4:** Solve
```
I = π/4
```

**Final Answer:** π/4 (independent of n!)

**Key Insight:** This is a classic JEE problem. The answer π/4 works for ANY value of n.

---

## Example 7: Area Under Curve

**Problem:** Find area bounded by y = x², x-axis, x = 0, and x = 3.

**Detailed Solution:**

**Step 1:** Set up integral
```
Area = ∫₀³ x² dx
```

**Step 2:** Evaluate
```
= [x³/3]₀³ = 27/3 - 0 = 9
```

**Final Answer:** Area = 9 square units

---

## Example 8: Area Between Two Curves

**Problem:** Find area between y = x² and y = x.

**Detailed Solution:**

**Step 1:** Find intersection points
```
x² = x → x² - x = 0 → x(x-1) = 0
x = 0 or x = 1
```

**Step 2:** Determine which function is on top
```
For x ∈ (0,1): x > x² (line is above parabola)
```

**Step 3:** Integrate
```
Area = ∫₀¹ (x - x²) dx
     = [x²/2 - x³/3]₀¹
     = 1/2 - 1/3 = 1/6
```

**Final Answer:** Area = 1/6 square units

## Essential Integration Formulas Reference

| Integral | Result |
|----------|--------|
| ∫x^n dx | x^(n+1)/(n+1) + C |
| ∫1/x dx | ln\|x\| + C |
| ∫e^x dx | e^x + C |
| ∫sin x dx | -cos x + C |
| ∫cos x dx | sin x + C |
| ∫sec²x dx | tan x + C |
| ∫1/(1+x²) dx | tan⁻¹(x) + C |
| ∫1/√(1-x²) dx | sin⁻¹(x) + C |
