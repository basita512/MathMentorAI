# Complex Numbers & Quadratic Equations - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Covers complex number algebra, geometric interpretation, and quadratic equations. Formulas are in `complex_numbers_quadratic.json`.

---

## Problem Type Identification & Approach

### COMPLEX NUMBERS

### Type 1: Simplify / Compute
**Approach**: Choose the right form based on operation.
- **Addition/Subtraction**: Use Cartesian form z = a + ib
- **Multiplication/Division**: Use polar form z = r*e^(i*theta) (multiply moduli, add arguments)
- **Powers**: Use De Moivre's theorem
- **Division by complex number**: Multiply numerator and denominator by conjugate of denominator

### Type 2: Find Modulus and Argument
**Approach**:
- Modulus: |z| = sqrt(a^2 + b^2)
- Argument: MUST check quadrant manually
  - Q1 (a > 0, b > 0): arg = theta
  - Q2 (a < 0, b > 0): arg = pi - theta
  - Q3 (a < 0, b < 0): arg = -pi + theta
  - Q4 (a > 0, b < 0): arg = -theta
  - where theta = tan^-1(|b/a|) (always positive)

### Type 3: Locus Problems (Argand Plane)
**Approach**: Translate geometric condition to algebraic equation.
- |z - z1| = r -> circle with centre z1, radius r
- |z - z1| = |z - z2| -> perpendicular bisector of segment z1-z2
- arg(z - z1) = theta -> ray from z1 at angle theta
- |z - z1| + |z - z2| = 2a -> ellipse with foci z1, z2

### Type 4: nth Roots
**Approach**: Use De Moivre's theorem.
- z^n = w has n roots, equally spaced on a circle of radius |w|^(1/n)
- For cube roots of unity: remember 1 + omega + omega^2 = 0 and omega^3 = 1
- Product of all nth roots of unity: (-1)^(n+1)

### QUADRATIC EQUATIONS

### Type 5: Find Nature of Roots
**Approach**: Compute discriminant D = b^2 - 4ac.
- D > 0: two distinct real roots
  - D is perfect square (and coefficients rational) -> rational roots
  - Otherwise -> irrational roots (conjugate pairs: p +/- sqrt(q))
- D = 0: repeated real root
- D < 0: complex conjugate pair

### Type 6: Find Roots or Form Equation
**Approach**:
- Use quadratic formula, OR
- Use Vieta's formulas: sum = -b/a, product = c/a
- To form equation from roots alpha, beta: x^2 - (sum)x + (product) = 0
- For symmetric functions like alpha^2 + beta^2: express in terms of sum and product

### Type 7: Common Roots
**Approach**:
- One common root: use the condition (c1*a2 - c2*a1)^2 = (b1*c2 - b2*c1)(a1*b2 - a2*b1)
- Both roots common: coefficients must be proportional a1/a2 = b1/b2 = c1/c2

### Type 8: Location of Roots
**Approach**: Draw rough parabola and apply conditions.
- Both roots > k: D >= 0, vertex > k, f(k) > 0 (for a > 0)
- Both roots < k: D >= 0, vertex < k, f(k) > 0 (for a > 0)
- k lies between roots: f(k) < 0 (for a > 0)
- Both roots in (p, q): D >= 0, p < vertex < q, f(p) > 0, f(q) > 0

### Type 9: Maximum/Minimum of Quadratic Expression
**Approach**: Vertex at x = -b/2a.
- a > 0 -> minimum at vertex, no maximum (parabola opens up)
- a < 0 -> maximum at vertex, no minimum (parabola opens down)

---

## Common Mistakes
- Wrong quadrant for argument (not checking signs of a and b)
- Confusing |z1 + z2| with |z1| + |z2| (triangle inequality, not equality)
- Assuming mutually exclusive: irrational roots vs complex roots (they are different D > 0 vs D < 0)
- Forgetting that irrational and complex roots come in CONJUGATE pairs (for equations with rational/real coefficients)
- Not verifying discriminant conditions for location of roots problems
- Using Vieta's formulas with wrong signs

---

## JEE Problem-Solving Checklist
- Use polar form for multiplication/division/powers
- Use Cartesian form for addition/subtraction
- Always check quadrant for argument manually
- For quadratics: compute discriminant first
- For location of roots: draw parabola and apply conditions systematically
- Remember: conjugate pairs for irrational (p +/- sqrt(q)) and complex (a +/- ib) roots
