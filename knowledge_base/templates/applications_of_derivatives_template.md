# Applications of Derivatives - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Covers rate of change, tangents/normals, monotonicity, maxima/minima, and approximations. Formulas are in `applications_of_derivatives.json`.

---

## Problem Type Identification & Approach

### Type 1: Rate of Change
**Approach**: Identify the dependent and independent variables, differentiate the relation.
- For related rates: differentiate the connecting equation w.r.t. time
- Velocity = ds/dt, Acceleration = dv/dt = d^2s/dt^2

### Type 2: Tangent and Normal
**Approach**:
1. Find dy/dx (the slope function)
2. Evaluate slope at the given point: m = f'(x1)
3. Write tangent equation: y - y1 = m(x - x1)
4. Write normal equation: y - y1 = (-1/m)(x - x1)

**Edge cases**:
- If f'(x1) = 0: tangent is horizontal (y = y1), normal is vertical (x = x1)
- If f'(x1) -> infinity: tangent is vertical (x = x1), normal is horizontal (y = y1)

**Angle between two curves**: Find slopes at intersection point, use angle formula.

### Type 3: Increasing/Decreasing (Monotonicity)
**Procedure**:
1. Compute f'(x)
2. Find critical points: f'(x) = 0 or f'(x) undefined
3. Create a sign chart of f'(x) on intervals between critical points
4. f'(x) > 0 -> increasing, f'(x) < 0 -> decreasing

### Type 4: Maxima and Minima

#### Local Extrema - Two Tests Available

**First Derivative Test** (always works):
- f' changes + to - at c -> local MAXIMUM
- f' changes - to + at c -> local MINIMUM
- f' does NOT change sign -> neither (inflection point)

**Second Derivative Test** (faster when f'' is easy):
- f'(c) = 0 and f''(c) < 0 -> local MAXIMUM
- f'(c) = 0 and f''(c) > 0 -> local MINIMUM
- f'(c) = 0 and f''(c) = 0 -> INCONCLUSIVE (use first derivative test)

#### Global (Absolute) Extrema on Closed Interval [a, b]
1. Find ALL critical points in (a, b)
2. Evaluate f at critical points AND at endpoints a and b
3. Largest value = absolute max, smallest = absolute min

#### Optimization Problems
1. Define the function to optimize and the constraint
2. Use constraint to eliminate one variable
3. Differentiate, set equal to zero, solve
4. Verify using second derivative or endpoint check
5. Common types: maximize area given perimeter, minimize distance, maximize volume given surface area

### Type 5: Points of Inflection
- Find where f''(x) = 0
- Verify f'' CHANGES SIGN at that point (f'' = 0 alone is NOT sufficient)
- Concavity: f'' > 0 -> concave up, f'' < 0 -> concave down

### Type 6: Approximations
- Use linear approximation: f(a + h) approximately equals f(a) + h*f'(a) for small h
- Relative error = delta(y)/y, percentage error = relative error * 100%

### Type 7: Mean Value Theorems (JEE Advanced)
**Rolle's Theorem**: Check 3 conditions -> continuous on [a,b], differentiable on (a,b), f(a) = f(b). Then find c where f'(c) = 0.

**Lagrange's MVT**: Check 2 conditions -> continuous on [a,b], differentiable on (a,b). Then find c where f'(c) = [f(b) - f(a)]/(b - a). Geometric meaning: tangent at c is parallel to secant line.

---

## Common Mistakes
- Not finding ALL critical points (forgetting where f' is undefined)
- Concluding max/min when f' = 0 without checking sign change
- Using second derivative test when f'' = 0 (it's inconclusive!)
- Forgetting to check endpoints for absolute max/min on closed intervals
- Not defining the constraint properly in optimization problems
- Assuming f''(c) = 0 means inflection point (must verify sign change)

---

## JEE Problem-Solving Checklist
- Find ALL critical points (both f' = 0 and f' undefined)
- Use sign chart for increasing/decreasing analysis
- For tangent/normal: find slope first, then write equation
- For optimization: clearly state function and constraint
- Check endpoints for absolute extrema on closed intervals
- Verify using second derivative test when feasible
