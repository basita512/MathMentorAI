# Integral Calculus - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Integration covers indefinite integrals, definite integrals, and area under curves. Formulas are in `integral_calculus.json`.

---

## Method Selection Decision Tree

When faced with an integral, follow this order:

1. **Is it a standard integral?** -> Apply formula directly from the standard integrals table
2. **Can you simplify first?** -> Factor, expand, use trig identities, or split fractions before integrating
3. **Is it a substitution candidate?** -> Look for f(g(x)) * g'(x) pattern. Let u = g(x).
4. **Is it a product of two different types?** -> Use integration by parts (ILATE priority)
5. **Is it a rational function P(x)/Q(x)?** -> Use partial fractions (factor denominator first)
6. **Does it contain sqrt(ax^2 + bx + c)?** -> Complete the square, then use trig substitution
7. **Is it a trig integral (sin^n * cos^m)?** -> Use reduction strategies or half-angle formulas

---

## Approach by Problem Type

### Type 1: Indefinite Integrals

#### Substitution Method
- **When**: You see a composite function f(g(x)) and g'(x) is present (or close to it)
- **Standard substitutions**:
  - sqrt(a^2 - x^2): put x = a sin(theta)
  - sqrt(a^2 + x^2): put x = a tan(theta)
  - sqrt(x^2 - a^2): put x = a sec(theta)
  - Integrals with e^x: put t = e^x
  - 1/(a + b cos x) type: put t = tan(x/2) (Weierstrass substitution)

#### Integration by Parts
- **When**: Integrand is a product of two different types
- **ILATE rule** for choosing u (first in this order): Inverse trig > Log > Algebraic > Trig > Exponential
- **Special pattern**: int(e^x [f(x) + f'(x)]) dx = e^x * f(x) + C (recognize this!)
- Apply parts repeatedly if needed (tabular method for polynomial * exponential/trig)

#### Partial Fractions
- **When**: Integrand is a proper rational function
- **Step 1**: If improper (degree numerator >= denominator), do polynomial division first
- **Step 2**: Factor denominator completely
- **Step 3**: Decompose: linear -> A/(x-a), repeated -> A/(x-a) + B/(x-a)^2, quadratic -> (Ax+B)/(x^2+bx+c)

### Type 2: Definite Integrals

#### Which Property to Use?
- **King's Rule** (replace x by a-x): Use when limits are 0 to a, especially for sin^n/(sin^n + cos^n) type
- **Even/Odd property**: Use when limits are symmetric (-a to a). Check: f(-x) = f(x)? -> even, double the integral from 0 to a. f(-x) = -f(x)? -> odd, integral = 0.
- **Periodic property**: Use when limits span multiple periods. Integral over n periods = n times integral over one period.
- **Splitting at discontinuity/sign change**: If integrand has |f(x)| or piecewise definition, split at the transition points
- **Leibniz Rule**: Use when asked to differentiate an integral w.r.t. a parameter in the limits

#### Definite Integral as Limit of Sum
- Convert sum to integral: lim(1/n) * sum(f(r/n)) = int_0^1 f(x) dx
- Recognize: r/n -> x, 1/n -> dx, sum from r=1 to n -> integral from 0 to 1

### Type 3: Area Under Curves
- **Step 1**: ALWAYS sketch the curves first
- **Step 2**: Find intersection points (these are your limits)
- **Step 3**: Identify which curve is above and which is below
- **Step 4**: Area = int |f(x) - g(x)| dx (upper minus lower)
- **For area w.r.t. y-axis**: Integrate x as function of y
- **When curve crosses axis**: Split integral at crossing points and take absolute value of each part

---

## Common Mistakes
- Forgetting + C in indefinite integrals
- Wrong ILATE choice leading to more complex integrals
- Not simplifying before integrating (missing easy simplification)
- Applying King's rule when limits are NOT 0 to a
- Not splitting at sign-change points for area problems
- Confusing area (always positive) with definite integral value (can be negative)
- Forgetting to change limits when doing substitution in definite integrals

---

## JEE Problem-Solving Checklist
- Simplify the integrand FIRST (use identities, algebra)
- Try substitution before parts (substitution is simpler)
- Use definite integral properties BEFORE computing (can save significant effort)
- For area problems: ALWAYS sketch and find intersection points
- Never forget + C for indefinite integrals
- When substituting in definite integrals: change limits OR back-substitute (not both)
