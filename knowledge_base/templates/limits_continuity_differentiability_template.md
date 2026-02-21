# Limits, Continuity & Differentiability - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Covers evaluation of limits, checking continuity and differentiability, and computing derivatives. Formulas are in `limits_continuity_differentiability.json`.

---

## Problem Type Identification & Approach

### Type 1: Evaluate a Limit

#### Step-by-Step Method
1. **Try direct substitution first**. If you get a finite value, that IS the answer.
2. If you get an **indeterminate form**, identify which type:

| Form | Strategy |
|------|----------|
| 0/0 | Factor, rationalize, use standard limits, or L'Hopital |
| inf/inf | Divide by highest power, or L'Hopital |
| 0 * inf | Rewrite as 0/0 or inf/inf, then apply L'Hopital |
| inf - inf | Combine into single fraction, then evaluate |
| 1^inf | Use: limit = e^(lim (f-1)*g) where expression is f^g |
| 0^0 or inf^0 | Take logarithm first, evaluate, then exponentiate |

#### When to Use Which Technique
- **Algebraic limits (0/0)**: Try factoring (x^n - a^n formula) or rationalization first
- **Trigonometric limits**: Reduce to standard forms like sin(x)/x -> 1
- **Exponential/Log limits**: Reduce to standard forms like (e^x - 1)/x -> 1
- **L'Hopital's Rule**: Use when other methods fail. Only for 0/0 or inf/inf forms. Can apply repeatedly.
- **Squeeze theorem**: When function is bounded between two functions with known limits

#### Common Traps
- sin(x)/x -> 1 ONLY when x -> 0 (NOT x -> infinity)
- (1 + 1/n)^n -> e when n -> infinity (NOT n -> 0)
- x must be in RADIANS for standard trig limits
- L'Hopital: differentiate numerator and denominator SEPARATELY (not quotient rule)

### Type 2: Check Continuity

#### Procedure for Piecewise Functions
1. Within each piece: usually automatically continuous (polynomial, trig, etc.)
2. **At each boundary point x = a**:
   - Compute LHL: lim(x -> a-) f(x)
   - Compute RHL: lim(x -> a+) f(x)
   - Compute f(a)
   - Continuous iff LHL = RHL = f(a)

#### Types of Discontinuity
- **Removable**: Limit exists but f(a) is undefined or different. Can fix by redefining f(a).
- **Jump**: LHL != RHL. Jump = |LHL - RHL|. Cannot be fixed.
- **Infinite**: Function goes to +/- infinity. Cannot be fixed.

#### Functions to Watch
- |x|: continuous everywhere
- [x] (greatest integer / floor): discontinuous at ALL integers
- {x} (fractional part): discontinuous at all integers
- 1/x: discontinuous at x = 0

### Type 3: Check Differentiability

#### Key Relationship
- **Differentiable => Continuous** (always true)
- **Continuous => Differentiable** (NOT always true, e.g., |x| at 0)
- So: check continuity FIRST. If not continuous, automatically not differentiable.

#### Procedure
1. Check continuity at the point
2. Compute LHD (left-hand derivative) and RHD (right-hand derivative)
3. Differentiable iff LHD = RHD

#### Points of Non-Differentiability
- Sharp corners / cusps (like |x| at 0)
- Vertical tangent (like x^(1/3) at 0)
- Points of discontinuity

### Type 4: Find Derivatives
- Identify the correct rule: power, product, quotient, or chain
- **Implicit differentiation**: When y cannot be isolated. Differentiate both sides w.r.t. x, treat y as function of x.
- **Logarithmic differentiation**: For f(x)^g(x) type. Take ln both sides first.
- **Parametric differentiation**: If x = f(t), y = g(t), then dy/dx = (dy/dt)/(dx/dt)

### Type 5: Rolle's Theorem / MVT Problems
- **Before applying**: Verify ALL conditions (continuous on [a,b], differentiable on (a,b))
- For Rolle's: additionally need f(a) = f(b)
- Find c by solving f'(c) = 0 (Rolle's) or f'(c) = [f(b)-f(a)]/(b-a) (MVT)

---

## Common Mistakes
- Applying L'Hopital when form is NOT indeterminate
- Using L'Hopital with quotient rule instead of differentiating separately
- Confusing continuity with differentiability
- Not checking LHL and RHL separately at boundary points
- Applying Rolle's/MVT without verifying all conditions
- Forgetting that [x] and {x} are discontinuous at integers

---

## JEE Problem-Solving Checklist
- Always try direct substitution FIRST for limits
- Identify the indeterminate form before choosing technique
- For piecewise functions: check each boundary point
- Check continuity BEFORE differentiability
- For Rolle's/MVT: verify ALL conditions before applying
- Be careful with |x|, [x], {x} type functions at special points
