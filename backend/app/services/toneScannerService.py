MARKETING_WORDS = [
    "cutting-edge",
    "best",
    "powerful",
    "revolutionary",
    "world-class",
    "leading",
]

def compute_tone_score(text: str) -> float:
    lower = text.lower()
    hits = sum(word in lower for word in MARKETING_WORDS)

    penalty = hits * 10
    return max(100 - penalty, 0)
