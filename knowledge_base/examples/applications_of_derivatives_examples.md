# Applications of Derivatives – Comprehensive Worked Examples (JEE Level)

## Example 1: Rate of Change

**Problem:** Find the rate of change of y = x³ at x = 2.

**Key Concepts:** Rate of change = value of derivative at the given point

**Detailed Solution:**

**Step 1:** Differentiate y = x³
```
dy/dx = 3x²
```

**Step 2:** Substitute x = 2
```
dy/dx|_{x=2} = 3(2)² = 3 × 4 = 12
```

**Final Answer:** Rate of change = 12

**Interpretation:** At x = 2, the function y = x³ is increasing at a rate of 12 units of y per unit of x.

---

## Example 2: Equation of Tangent and Normal

**Problem:** Find equation of tangent and normal to y = x² at x = 1.

**Key Concepts:**
- Slope of tangent = dy/dx at the point
- Slope of normal = -1/(slope of tangent)
- Point-slope form: y - y₁ = m(x - x₁)

**Detailed Solution:**

**Step 1:** Find the point
```
At x = 1: y = 1² = 1
Point: (1, 1)
```

**Step 2:** Find slope of tangent
```
dy/dx = 2x
At x = 1: slope = 2(1) = 2
```

**Step 3:** Equation of tangent
```
y - 1 = 2(x - 1)
y = 2x - 1
```

**Step 4:** Equation of normal (perpendicular to tangent)
```
Slope of normal = -1/2
y - 1 = (-1/2)(x - 1)
2y - 2 = -x + 1
x + 2y = 3
```

**Final Answer:** Tangent: y = 2x - 1, Normal: x + 2y = 3

**Common Mistakes:**
- Forgetting to find the y-coordinate of the point
- Using wrong sign for normal slope
- Not simplifying the final equation

---

## Example 3: Increasing and Decreasing Functions

**Problem:** Find intervals where f(x) = x³ - 3x² + 2 is increasing or decreasing.

**Key Concepts:**
- f(x) is increasing where f'(x) > 0
- f(x) is decreasing where f'(x) < 0
- Critical points where f'(x) = 0

**Detailed Solution:**

**Step 1:** Find f'(x)
```
f'(x) = 3x² - 6x = 3x(x - 2)
```

**Step 2:** Find critical points
```
3x(x - 2) = 0
x = 0 or x = 2
```

**Step 3:** Sign analysis using number line
```
Interval     | Test point | f'(x) sign | Behavior
(-∞, 0)      | x = -1     | 3(-1)(-3) = +9  | Increasing ↑
(0, 2)       | x = 1      | 3(1)(-1) = -3   | Decreasing ↓
(2, ∞)       | x = 3      | 3(3)(1) = +9    | Increasing ↑
```

**Final Answer:** Increasing on (-∞, 0) ∪ (2, ∞), Decreasing on (0, 2)

**Common Mistakes:**
- Not testing ALL intervals between critical points
- Confusing increasing/decreasing with positive/negative values of f(x)

---

## Example 4: Maxima and Minima

**Problem:** Find local maxima and minima of f(x) = x³ - 6x² + 9x + 1.

**Key Concepts:**
- First derivative test: sign change of f'(x)
- Second derivative test: f''(c) > 0 → minimum, f''(c) < 0 → maximum

**Detailed Solution:**

**Step 1:** Find f'(x)
```
f'(x) = 3x² - 12x + 9 = 3(x² - 4x + 3) = 3(x - 1)(x - 3)
```

**Step 2:** Critical points
```
x = 1 and x = 3
```

**Step 3:** Second derivative test
```
f''(x) = 6x - 12

At x = 1: f''(1) = 6 - 12 = -6 < 0 → Local MAXIMUM
At x = 3: f''(3) = 18 - 12 = 6 > 0 → Local MINIMUM
```

**Step 4:** Find the values
```
f(1) = 1 - 6 + 9 + 1 = 5 (local maximum)
f(3) = 27 - 54 + 27 + 1 = 1 (local minimum)
```

**Final Answer:** Local maximum = 5 at x = 1, Local minimum = 1 at x = 3

**Common Mistakes:**
- Confusing maximum and minimum (check sign of f'')
- Forgetting to find the actual max/min VALUES (not just locations)
- Not factoring f'(x) correctly

---

## Example 5: Error Approximation (Linear Approximation)

**Problem:** Approximate the value of √(25.2).

**Key Concepts:**
- Linear approximation: f(a + h) ≈ f(a) + h·f'(a)
- Choose a where f(a) is easy to compute

**Detailed Solution:**

**Step 1:** Set up
```
f(x) = √x, a = 25, h = 0.2
f(a) = √25 = 5
```

**Step 2:** Find f'(x)
```
f'(x) = 1/(2√x)
f'(25) = 1/(2×5) = 0.1
```

**Step 3:** Apply linear approximation
```
√(25.2) ≈ f(25) + 0.2 × f'(25)
         = 5 + 0.2 × 0.1
         = 5 + 0.02
         = 5.02
```

**Final Answer:** √(25.2) ≈ 5.02

**Verification:** Calculator gives √(25.2) ≈ 5.01996, so approximation is excellent!

---

## Example 6: Point of Inflection

**Problem:** Find points of inflection of f(x) = x⁴ - 4x³.

**Key Concepts:**
- Inflection point: where concavity changes
- Find where f''(x) = 0 AND changes sign

**Detailed Solution:**

**Step 1:** Find f''(x)
```
f'(x) = 4x³ - 12x²
f''(x) = 12x² - 24x = 12x(x - 2)
```

**Step 2:** Set f''(x) = 0
```
12x(x - 2) = 0
x = 0 or x = 2
```

**Step 3:** Check sign change of f''(x)
```
x < 0: f''(-1) = 12(-1)(-3) = 36 > 0 (concave up)
0 < x < 2: f''(1) = 12(1)(-1) = -12 < 0 (concave down)
x > 2: f''(3) = 12(3)(1) = 36 > 0 (concave up)
```

Both x = 0 and x = 2 have sign changes → both are inflection points.

**Step 4:** Find coordinates
```
f(0) = 0 → (0, 0)
f(2) = 16 - 32 = -16 → (2, -16)
```

**Final Answer:** Points of inflection at (0, 0) and (2, -16)

**Common Mistakes:**
- Not verifying sign change (f'' = 0 alone is NOT sufficient!)
- Missing inflection points

---

## Example 7: Rolle's Theorem

**Problem:** Verify Rolle's Theorem for f(x) = x² - 4x + 3 on [1, 3].

**Key Concepts:**
- Conditions: f continuous on [a,b], differentiable on (a,b), f(a) = f(b)
- Conclusion: ∃ c ∈ (a,b) such that f'(c) = 0

**Detailed Solution:**

**Step 1:** Verify conditions
```
f(1) = 1 - 4 + 3 = 0
f(3) = 9 - 12 + 3 = 0
f(1) = f(3) ✓
f is polynomial → continuous and differentiable ✓
```

**Step 2:** Find c
```
f'(x) = 2x - 4
f'(c) = 0 → 2c - 4 = 0 → c = 2
c = 2 ∈ (1, 3) ✓
```

**Final Answer:** Rolle's Theorem is verified with c = 2

---

## Example 8: L'Hôpital's Rule with Derivatives

**Problem:** Evaluate lim(x→0) (e^x - 1 - x)/x²

**Key Concepts:**
- L'Hôpital's Rule: if 0/0 or ∞/∞, differentiate numerator and denominator
- May need to apply multiple times

**Detailed Solution:**

**Step 1:** Check form
```
At x = 0: (e⁰ - 1 - 0)/0² = 0/0 (indeterminate)
```

**Step 2:** Apply L'Hôpital's Rule
```
= lim(x→0) (e^x - 1)/(2x) = 0/0 still
```

**Step 3:** Apply again
```
= lim(x→0) e^x/2 = 1/2
```

**Final Answer:** 1/2

## Key Formulas Reference

- Rate of change: dy/dx at the point
- Tangent: y - y₁ = f'(x₁)(x - x₁)
- Normal: y - y₁ = (-1/f'(x₁))(x - x₁)
- Increasing: f'(x) > 0
- Maximum: f'(c) = 0, f''(c) < 0
- Minimum: f'(c) = 0, f''(c) > 0
- Linear approximation: f(a+h) ≈ f(a) + hf'(a)
