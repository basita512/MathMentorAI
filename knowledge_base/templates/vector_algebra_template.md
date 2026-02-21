# Vector Algebra - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Covers vector operations, products, and applications. Formulas are in `vector_algebra.json`.

---

## Which Product to Use? (MOST IMPORTANT Decision)

| Goal | Product | Result Type |
|------|---------|-------------|
| Find angle between vectors | Dot product | Scalar |
| Check perpendicularity | Dot product (= 0?) | Scalar |
| Project one vector onto another | Dot product | Scalar/Vector |
| Compute work done | Dot product | Scalar |
| Find perpendicular vector | Cross product | Vector |
| Check parallelism | Cross product (= 0?) | Vector |
| Compute area (parallelogram/triangle) | Cross product magnitude | Scalar |
| Compute torque | Cross product | Vector |
| Compute volume (parallelepiped) | Scalar triple product | Scalar |
| Check coplanarity | Scalar triple product (= 0?) | Scalar |

---

## Problem Type Approaches

### Type 1: Find Angle Between Vectors
**Approach**: Use dot product.
- cos(theta) = (a . b) / (|a| * |b|)
- If result is 0 -> vectors are perpendicular

### Type 2: Prove Perpendicularity
**Approach**: Show dot product = 0.
- a . b = a1*b1 + a2*b2 + a3*b3 = 0

### Type 3: Prove Collinearity/Parallelism
**Approach**: Show cross product = 0 OR one vector is scalar multiple of other.
- a x b = 0 <=> a is parallel to b

### Type 4: Find Area
- **Parallelogram** (adjacent sides a, b): Area = |a x b|
- **Triangle** (two sides a, b): Area = (1/2)|a x b|
- Compute cross product first, then take magnitude

### Type 5: Find Volume
- **Parallelepiped**: V = |a . (b x c)| = |scalar triple product|
- **Tetrahedron**: V = (1/6)|a . (b x c)|
- Compute cross product first, then dot product

### Type 6: Check Coplanarity
- Four points A, B, C, D are coplanar iff [AB, AC, AD] = 0
- Three vectors are coplanar iff their scalar triple product = 0

### Type 7: Projection Problems
- **Scalar projection** of a on b: (a . b) / |b|
- **Vector projection** of a on b: [(a . b) / |b|^2] * b
- Useful for resolving forces, finding components

### Type 8: Vector Triple Product (Advanced)
- a x (b x c) = b(a . c) - c(a . b) (BAC-CAB rule)
- Result is ALWAYS in the plane of b and c
- Note: (a x b) x c != a x (b x c) (NOT associative!)
- (a x b) x c = b(a . c) - a(b . c) (different from above)

### Type 9: Section Formula (Vector Form)
- Internal division (m:n): r = (m*b + n*a) / (m + n)
- Midpoint: r = (a + b) / 2
- Centroid of triangle: G = (a + b + c) / 3

---

## Key Procedural Notes

### Cross Product Computation
- Use determinant form: |i j k; a1 a2 a3; b1 b2 b3|
- REMEMBER: anti-commutative. a x b = -(b x a). Order matters!

### Scalar Triple Product
- [a b c] = a . (b x c) = determinant of component matrix
- Cyclic order: [a b c] = [b c a] = [c a b]
- Swapping any two: changes sign

### Lagrange's Identity
- |a x b|^2 = |a|^2 * |b|^2 - (a . b)^2
- Useful for proving: |a x b|^2 + (a . b)^2 = |a|^2 * |b|^2

---

## Common Mistakes
- Wrong cross product order (a x b != b x a)
- Confusing scalar result (dot product) with vector result (cross product)
- Applying cross product associativity (it's NOT associative)
- Using wrong formula for vector triple product
- Not normalizing when unit vector is needed
- Computing scalar triple product with wrong cyclic order

---

## JEE Problem-Solving Checklist
- Use the product selection table above FIRST
- Dot product for: angles, perpendicularity, projections, work
- Cross product for: areas, perpendicular vectors, parallelism test, torque
- Scalar triple product for: volumes, coplanarity
- Always check: is the answer a scalar or vector?
- Cross product: order matters (anti-commutative)
- For coplanarity of 4 points: compute [AB, AC, AD] and check if = 0
