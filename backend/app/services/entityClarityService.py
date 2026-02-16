import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")


def compute_entity_clarity(text: str) -> float:
    doc = nlp(text)

    entities = [ent.text.strip().lower() for ent in doc.ents]

    if not entities:
        return 60.0  # neutral fallback

    entity_counts = Counter(entities)
    total_mentions = sum(entity_counts.values())

    # 1️⃣ Dominant entity ratio
    most_common_entity, most_common_count = entity_counts.most_common(1)[0]
    dominance_ratio = most_common_count / total_mentions

    # 2️⃣ Entity concentration score
    unique_entities = len(entity_counts)

    # Ideal range: 3–10 unique entities for informational page
    if unique_entities <= 2:
        diversity_score = 60
    elif 3 <= unique_entities <= 10:
        diversity_score = 90
    elif 11 <= unique_entities <= 20:
        diversity_score = 70
    else:
        diversity_score = 50

    # 3️⃣ Combine dominance + diversity
    clarity_score = (
        dominance_ratio * 50 +
        diversity_score * 0.5
    )

    return round(min(clarity_score, 100), 2)
