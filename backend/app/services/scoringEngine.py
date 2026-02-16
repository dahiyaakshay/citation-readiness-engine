import math


def normalize(score):
    return max(min(score, 100), 0)


def weighted_sigmoid(score):
    """
    Smooth scoring curve.
    Prevents inflated mid-range scores.
    """
    return 100 / (1 + math.exp(-0.08 * (score - 50)))


def calculate_final_score(dom, fact, entity, tone, retrieval):

    dom = normalize(dom)
    fact = normalize(fact)
    entity = normalize(entity)
    tone = normalize(tone)
    retrieval = normalize(retrieval)

    # Non-linear weighting
    fact_adj = weighted_sigmoid(fact)
    retrieval_adj = weighted_sigmoid(retrieval)

    # Penalize weak structural foundation
    structural_penalty = 0
    if dom < 40:
        structural_penalty += 10
    if entity < 40:
        structural_penalty += 10

    composite = (
        dom * 0.20 +
        fact_adj * 0.25 +
        entity * 0.20 +
        tone * 0.10 +
        retrieval_adj * 0.25
    )

    final_score = composite - structural_penalty

    return round(max(final_score, 0), 2)
