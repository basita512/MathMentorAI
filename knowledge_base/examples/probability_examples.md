# Probability – Comprehensive Worked Examples (JEE Level)

## Example 1: Basic Probability

**Problem:** Two dice are thrown. Find probability that the sum is 7.

**Key Concepts:**
- P(E) = Favorable outcomes / Total outcomes
- Two dice: total outcomes = 36

**Detailed Solution:**

**Step 1:** List favorable outcomes for sum = 7
```
(1,6), (2,5), (3,4), (4,3), (5,2), (6,1) → 6 outcomes
```

**Step 2:** Calculate probability
```
P(sum = 7) = 6/36 = 1/6
```

**Final Answer:** 1/6

---

## Example 2: Addition Theorem (Union)

**Problem:** A card is drawn from a standard deck. Find probability that it is a king OR a heart.

**Key Concepts:**
- P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- Inclusion-exclusion principle

**Detailed Solution:**

**Step 1:** Identify probabilities
```
P(King) = 4/52
P(Heart) = 13/52
P(King AND Heart) = 1/52 (King of Hearts)
```

**Step 2:** Apply addition theorem
```
P(King OR Heart) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13
```

**Final Answer:** 4/13

**Common Mistakes:**
- Forgetting to subtract the intersection (double counting)

---

## Example 3: Conditional Probability

**Problem:** A bag contains 3 red and 5 blue balls. Two balls are drawn without replacement. Find probability that second is red given first was blue.

**Key Concepts:**
- P(A|B) = P(A ∩ B)/P(B)
- Without replacement: probabilities change after first draw

**Detailed Solution:**

**Step 1:** After first blue ball is drawn
```
Remaining: 3 red + 4 blue = 7 balls
```

**Step 2:** Probability second is red
```
P(2nd red | 1st blue) = 3/7
```

**Final Answer:** 3/7

---

## Example 4: Independent Events

**Problem:** A coin is tossed 3 times. Find probability of getting exactly 2 heads.

**Key Concepts:**
- Coin tosses are independent events
- Use binomial probability: P(X=k) = nCk × p^k × q^(n-k)

**Detailed Solution:**

**Step 1:** Identify parameters
```
n = 3, k = 2, p = 1/2, q = 1/2
```

**Step 2:** Apply binomial formula
```
P(X = 2) = 3C2 × (1/2)² × (1/2)¹
         = 3 × 1/4 × 1/2
         = 3/8
```

**Final Answer:** 3/8

**Alternative:** List favorable: HHT, HTH, THH → 3/8

---

## Example 5: Bayes' Theorem

**Problem:** Box A has 3 red, 2 blue balls. Box B has 2 red, 3 blue balls. A box is chosen at random and a ball drawn is red. Find probability it came from Box A.

**Key Concepts:**
- Bayes' theorem: P(A|E) = P(E|A)·P(A) / P(E)
- P(E) = P(E|A)·P(A) + P(E|B)·P(B)

**Detailed Solution:**

**Step 1:** Define events
```
P(Box A) = 1/2, P(Box B) = 1/2
P(Red | Box A) = 3/5
P(Red | Box B) = 2/5
```

**Step 2:** Find P(Red) using total probability
```
P(Red) = P(Red|A)·P(A) + P(Red|B)·P(B)
       = (3/5)(1/2) + (2/5)(1/2)
       = 3/10 + 2/10 = 1/2
```

**Step 3:** Apply Bayes' theorem
```
P(Box A | Red) = P(Red|A)·P(A) / P(Red)
               = (3/10) / (1/2)
               = 3/5
```

**Final Answer:** P(Box A | Red) = 3/5

---

## Example 6: Binomial Distribution

**Problem:** A fair coin is tossed 5 times. Find P(at least 3 heads).

**Key Concepts:**
- "At least 3" = P(3) + P(4) + P(5)
- Or use complement: 1 - P(0) - P(1) - P(2)

**Detailed Solution:**

**Step 1:** Calculate each
```
P(3) = 5C3 × (1/2)⁵ = 10/32
P(4) = 5C4 × (1/2)⁵ = 5/32
P(5) = 5C5 × (1/2)⁵ = 1/32
```

**Step 2:** Add
```
P(≥3) = 10/32 + 5/32 + 1/32 = 16/32 = 1/2
```

**Final Answer:** 1/2

---

## Example 7: Mean and Variance of Random Variable

**Problem:** X takes values 0, 1, 2 with probabilities 1/4, 1/2, 1/4. Find E(X) and Var(X).

**Key Concepts:**
- E(X) = Σ xᵢP(xᵢ)
- Var(X) = E(X²) - [E(X)]²

**Detailed Solution:**

**Step 1:** Find E(X)
```
E(X) = 0(1/4) + 1(1/2) + 2(1/4)
     = 0 + 1/2 + 1/2 = 1
```

**Step 2:** Find E(X²)
```
E(X²) = 0²(1/4) + 1²(1/2) + 2²(1/4)
      = 0 + 1/2 + 1 = 3/2
```

**Step 3:** Find Var(X)
```
Var(X) = E(X²) - [E(X)]² = 3/2 - 1 = 1/2
```

**Final Answer:** E(X) = 1, Var(X) = 1/2, SD = 1/√2

---

## Example 8: Geometric Probability

**Problem:** A point is selected at random inside a circle of radius 5. Find probability that it falls inside a concentric circle of radius 3.

**Key Concepts:** Geometric probability = favorable area / total area

**Detailed Solution:**
```
P = Area of inner circle / Area of outer circle
  = π(3²) / π(5²)
  = 9/25
```

**Final Answer:** 9/25

## Key Formulas Reference

| Concept | Formula |
|---------|--------|
| P(A ∪ B) | P(A) + P(B) - P(A ∩ B) |
| P(A\|B) | P(A ∩ B)/P(B) |
| Bayes | P(Aᵢ\|B) = P(B\|Aᵢ)P(Aᵢ)/ΣP(B\|Aⱼ)P(Aⱼ) |
| Independence | P(A ∩ B) = P(A)·P(B) |
| Binomial | P(X=k) = nCk·p^k·q^(n-k) |
| E(X) | Σ xᵢP(xᵢ) |
| Var(X) | E(X²) - [E(X)]² |
