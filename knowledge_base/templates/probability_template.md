# Probability - Problem Solving Methodology (JEE Main + Advanced)

## Topic Overview
Covers classical probability, conditional probability, Bayes' theorem, and distributions. Formulas are in `probability.json`.

---

## Problem Type Identification & Approach

### Type 1: Classical Probability
**When**: All outcomes equally likely.
**Approach**:
1. Define sample space S clearly
2. Count favorable outcomes (using P&C techniques)
3. P(E) = favorable / total

### Type 2: Combined Events (Union/Intersection)
**Approach**: Use addition theorem.
- For "A or B": P(A union B) = P(A) + P(B) - P(A intersect B)
- For "neither A nor B": P(A' intersect B') = 1 - P(A union B)
- Mutually exclusive: P(A intersect B) = 0, so P(A or B) = P(A) + P(B)

### Type 3: Conditional Probability
**When**: One event has already occurred.
**Approach**:
- P(A|B) = P(A intersect B) / P(B)
- Multiplication rule: P(A intersect B) = P(B) * P(A|B)

**CRITICAL distinction**: Independence vs Mutual Exclusivity
- **Independent**: P(A intersect B) = P(A) * P(B). Knowing B doesn't change P(A).
- **Mutually exclusive**: P(A intersect B) = 0. They cannot happen together.
- Mutually exclusive events with non-zero probabilities are NEVER independent!

### Type 4: Bayes' Theorem (Reverse Conditional)
**When**: You know the effect has occurred and want to find which cause was responsible.
**Step-by-step procedure**:
1. Identify all possible causes B1, B2, ..., Bn (they must partition S)
2. List prior probabilities: P(B1), P(B2), ..., P(Bn)
3. List likelihoods: P(A|B1), P(A|B2), ..., P(A|Bn)
4. Compute P(A) using total probability: P(A) = sum of P(Bi) * P(A|Bi)
5. Apply: P(Bi|A) = P(Bi) * P(A|Bi) / P(A)

**Tip**: Draw a tree diagram for clarity. Branches = causes, leaves = effects.

### Type 5: Binomial Distribution
**When**: Fixed number of independent trials, each with same success probability.
**Conditions to verify**:
1. Fixed number of trials n
2. Each trial is independent
3. Two outcomes (success/failure)
4. Constant probability p for each trial

**Key calculations**: 
- P(X = k) uses binomial formula
- Mean = np, Variance = npq
- Mode: value around (n+1)p

### Type 6: "At Least One" Problems
**Best approach**: Complement method.
- P(at least one) = 1 - P(none)
- P(at least one six in n rolls) = 1 - (5/6)^n
- Much easier than calculating P(exactly 1) + P(exactly 2) + ...

### Type 7: Geometric Probability (Advanced)
**When**: Continuous sample space (length, area, etc.)
**Approach**: P = favorable measure / total measure (area ratio, length ratio)

---

## Common Problem Setups

### Dice
- One die: 6 outcomes, each probability 1/6
- Two dice: 36 outcomes. Sum = 7 has the most ways (6 ways).

### Cards
- 52 cards = 4 suits x 13 ranks
- Drawing without replacement: dependent events
- Drawing with replacement: independent events

### Urns/Balls
- Usually involves conditional probability or Bayes'
- Draw a tree diagram to track all possibilities

---

## Common Mistakes
- Confusing independent events with mutually exclusive events
- Not defining sample space clearly before counting
- Using P(A) * P(B) when events are NOT independent
- Not using complement for "at least one" problems
- Forgetting that drawing without replacement creates dependent events
- Applying binomial when trials are not independent

---

## JEE Problem-Solving Checklist
- Define sample space clearly FIRST
- Check: are outcomes equally likely?
- For sequential events: draw tree diagram
- For "at least one": use complement (1 - P(none))
- Check independence vs mutual exclusivity carefully
- For Bayes': identify causes and effects, use tree diagram
- For binomial: verify all 4 conditions
