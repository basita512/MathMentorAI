# Binomial Theorem - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Covers binomial expansion, general term, coefficient properties, and approximations. Formulas are in `binomial_theorem.json`.

---

## Problem Type Identification & Approach

### Type 1: Find a Specific Term in Expansion
**Approach**:
1. Write the general term T_(r+1) using binomial formula
2. Apply the specific condition (r = value, or condition on power)
3. Compute

**Critical sign handling for (a - b)^n**:
- T_(r+1) includes (-1)^r factor -> signs ALTERNATE: +, -, +, -, ...
- Many errors come from forgetting this sign

### Type 2: Find Term Independent of x
**Procedure**:
1. Write general term T_(r+1) for the given expression like (x^p + 1/x^q)^n
2. Compute the total power of x: p*(n-r) - q*r (or similar)
3. Set total power = 0, solve for r
4. If r is a non-negative integer <= n -> that term exists
5. If r is not an integer -> no term independent of x

### Type 3: Find Middle Term
**Decision based on n**:
- n is EVEN: single middle term = T_(n/2 + 1)
- n is ODD: two middle terms = T_((n+1)/2) and T_((n+3)/2)

### Type 4: Greatest Term / Greatest Coefficient
**For greatest coefficient**: Always the middle binomial coefficient
- n even: C(n, n/2)
- n odd: C(n, (n-1)/2) = C(n, (n+1)/2)

**For greatest term in (a + b)^n**:
1. Compute T_(r+1)/T_r
2. Find r where this ratio crosses 1 (goes from > 1 to < 1)
3. That r gives the greatest term

### Type 5: Coefficient Sums and Identities
**Approach**: Use substitution and calculus on (1 + x)^n

| To Find | Method |
|---------|--------|
| Sum of all coefficients | Put x = 1 -> result is 2^n |
| Alternating sum | Put x = -1 -> result is 0 |
| Sum of r * C(n,r) | Differentiate (1+x)^n, put x = 1 |
| Sum of C(n,r)/(r+1) | Integrate (1+x)^n, evaluate at limits |
| Sum of C(n,r)^2 | Use Vandermonde's identity |

### Type 6: Binomial Approximation (for fractional/negative exponents)
**When to use**: When |x| << 1
- (1 + x)^n approximately equals 1 + nx (first two terms)
- Valid for ANY real n (not just positive integers)
- IMPORTANT: Only valid when |x| < 1 for convergence

### Type 7: Multinomial Expansion (Advanced)
**Approach**: Number of terms in (x1 + x2 + ... + xk)^n = C(n+k-1, k-1)
- Use multinomial coefficients: n! / (r1! * r2! * ... * rk!)

---

## Common Mistakes
- Forgetting (-1)^r in (a - b)^n expansions
- Off-by-one error in term number: T_(r+1) is the (r+1)th term, not rth
- Setting up power of x incorrectly for "independent of x" problems
- Forgetting to check if r is a valid integer in term-finding problems
- Using infinite binomial expansion when |x| >= 1
- Confusing greatest coefficient with greatest term (they are different!)

---

## JEE Problem-Solving Checklist
- Always write T_(r+1) as the first step
- Include (-1)^r for subtraction expansions
- For independent term: set power of x = 0 and verify r is valid
- For middle term: check even/odd n
- For coefficient identities: use x = 1, x = -1, differentiate, or integrate
- For approximation: verify |x| < 1
