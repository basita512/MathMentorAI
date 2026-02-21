# Sets, Relations & Functions - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Covers set operations, types of relations, function classification, and composition. Formulas are in `sets_relations_functions.json`.

---

## Problem Type Identification & Approach

### SETS

### Type 1: Set Operations and Counting
**Approach**: Use Venn diagrams for 2 or 3 sets.
- Draw the diagram, fill in from the innermost region outward
- Apply inclusion-exclusion for counting: |A union B| = |A| + |B| - |A intersect B|
- De Morgan's Laws for complements: (A union B)' = A' intersect B'

### Type 2: Power Set
- P(A) = set of ALL subsets of A, including empty set and A itself
- |P(A)| = 2^n where n = |A|
- Number of proper subsets = 2^n - 1

---

### RELATIONS

### Type 3: Check Relation Properties
**Systematic procedure**:

| Property | What to Check |
|----------|---------------|
| **Reflexive** | Is (a,a) present for ALL a in set? Check every element. |
| **Symmetric** | For every (a,b), is (b,a) also present? |
| **Transitive** | For every chain (a,b) and (b,c), is (a,c) present? |
| **Anti-symmetric** | If (a,b) and (b,a) both present, then a = b? |
| **Equivalence** | All of: reflexive + symmetric + transitive |

**Key insight**: An equivalence relation partitions the set into disjoint equivalence classes.

### Type 4: Count Relations
- Total relations from A to B: 2^(|A| x |B|)
- Reflexive relations on set of n: 2^(n^2 - n) (diagonal elements are fixed)
- Symmetric relations: 2^(n(n+1)/2)

---

### FUNCTIONS

### Type 5: Determine Function Type

**Decision tree**:
1. Is it a valid function? (Each input maps to exactly ONE output)
2. **Injective (one-one)?**
   - Test: f(a) = f(b) implies a = b?
   - Graphical: horizontal line cuts graph at most once
   - For continuous functions: strictly monotonic => injective
3. **Surjective (onto)?**
   - Test: For every y in codomain, there exists x with f(x) = y
   - Check: Range = Codomain?
4. **Bijective?** Both injective AND surjective. Requires |Domain| = |Codomain|.

### Type 6: Find Domain and Range

**Domain restrictions (common traps)**:
- Denominator != 0
- Expression under sqrt >= 0
- Argument of log > 0
- For sin^(-1), cos^(-1): argument in [-1, 1]
- For tan^(-1): argument in R (no restriction)

**Finding range**:
- Method 1: Set y = f(x), solve for x in terms of y. Values of y for which real x exists = range.
- Method 2: Use calculus (find max and min of f)
- Method 3: Graphical approach

### Type 7: Composition and Inverse

**Composition**: (f o g)(x) = f(g(x)) - apply g first, then f.
- Domain of (f o g): values where g(x) is in domain of f
- f o g != g o f in general

**Inverse**:
- Exists only if f is BIJECTIVE
- To find: set y = f(x), solve for x = g(y), then f^(-1)(x) = g(x)
- Verify: f(f^(-1)(x)) = x

### Type 8: Even and Odd Functions
- Even: f(-x) = f(x), graph symmetric about y-axis
- Odd: f(-x) = -f(x), graph symmetric about origin
- Any function = even part + odd part: f = [(f(x)+f(-x))/2] + [(f(x)-f(-x))/2]

---

## Common Mistakes
- Confusing domain with range
- Assuming onto when range is a proper subset of codomain
- Not checking all elements for reflexivity (checking just a few)
- For transitivity: missing chains (a,b) + (b,c) -> (a,c)
- Confusing (f o g) with (g o f) - order matters!
- Assuming inverse exists without verifying bijectivity

---

## JEE Problem-Solving Checklist
- For sets: draw Venn diagrams when possible
- For relations: check each property systematically using the table above
- For functions: identify domain restrictions FIRST
- Inverse exists ONLY if function is bijective
- For composition: domain of f o g must account for range of g
- Use mapping diagrams to visualize one-one and onto properties
