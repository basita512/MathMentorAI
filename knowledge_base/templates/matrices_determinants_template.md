# Matrices & Determinants - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Covers matrix operations, determinant evaluation, inverse, and solving linear systems. Formulas are in `matrices_determinants.json`.

---

## Problem Type Identification & Approach

### Type 1: Matrix Operations
**Key rules to remember**:
- Multiplication: inner dimensions must match (m x n)(n x p) = (m x p)
- AB != BA in general (NOT commutative)
- AB = O does NOT mean A = O or B = O (zero divisors exist for matrices)
- Transpose reverses order: (AB)^T = B^T * A^T

### Type 2: Evaluate Determinant
**Strategy**: Simplify BEFORE expanding.
1. Use row/column operations (R_i -> R_i + k*R_j) to create zeros - this does NOT change the determinant
2. Expand along the row/column with the most zeros
3. For 3x3: use Sarrus' rule or cofactor expansion

**Properties to exploit** (saves computation):
- Two identical rows/columns -> det = 0
- One row/column all zeros -> det = 0
- Factor out common factor from a row -> it multiplies the determinant
- Interchange two rows -> determinant changes sign

**CRITICAL**: |kA| = k^n * |A| for n x n matrix (NOT k|A|, this is the #1 mistake)

### Type 3: Find Inverse

**Procedure (3x3)**:
1. Compute |A|. If |A| = 0, inverse does NOT exist.
2. Find cofactor matrix
3. Transpose cofactor matrix -> adj(A)
4. A^(-1) = adj(A) / |A|

**For 2x2**: Swap diagonal elements, negate off-diagonal, divide by determinant.

**Properties**:
- (AB)^(-1) = B^(-1) * A^(-1) (order reverses)
- (A^T)^(-1) = (A^(-1))^T

### Type 4: Solve System of Linear Equations

**Step-by-step procedure**:
1. Write system as AX = B
2. Compute Det = |A|

| Det | Delta_i values | Result |
|-----|---------------|--------|
| != 0 | Any | Unique solution (use Cramer's rule or A^(-1)B) |
| = 0 | All Delta_i = 0 | Infinite solutions |
| = 0 | Any Delta_i != 0 | No solution (inconsistent) |

- Delta_i = determinant with ith column of A replaced by B

**For homogeneous system** (AX = O):
- Always has trivial solution (X = O)
- Non-trivial solution exists iff |A| = 0

### Type 5: Cayley-Hamilton Theorem
**Use**: Every matrix satisfies its own characteristic equation.
- Find characteristic equation |A - lambda*I| = 0
- Replace lambda by A in that equation
- Use to find A^(-1) or higher powers of A without direct computation

### Type 6: Symmetric/Skew-Symmetric
**Decomposition**: Any square matrix A = (1/2)(A + A^T) + (1/2)(A - A^T) = symmetric part + skew-symmetric part

---

## Common Mistakes
- |kA| = k^n|A|, NOT k|A| (most common mistake in JEE)
- AB = O does NOT imply A = O or B = O
- Trying to find inverse when |A| = 0
- Wrong sign in cofactor: C_ij = (-1)^(i+j) * M_ij
- Not converting to row echelon form for system of equations analysis
- Forgetting that (AB)^(-1) = B^(-1)A^(-1) (not A^(-1)B^(-1))

---

## JEE Problem-Solving Checklist
- Check determinant BEFORE attempting inverse
- Use row/column operations to simplify determinant evaluation
- For systems: classify using |A| and Delta_i values systematically
- |kA| = k^n|A| (n = order of matrix)
- AB = O does NOT mean A or B is zero
- For Cayley-Hamilton: find characteristic equation first
