import spacy

nlp = spacy.load("en_core_web_sm")

DEFINITION_PATTERNS = [
    " is ",
    " are ",
    " refers to ",
    " defined as ",
    " means ",
]

ENUMERATION_TOKENS = ["first", "second", "third", "1.", "2.", "3."]


def compute_fact_density(text: str) -> float:
    doc = nlp(text)
    sentences = list(doc.sents)

    factual_score = 0

    for sent in sentences:
        sentence_text = sent.text.lower()

        # 1️⃣ Definition patterns
        if any(pattern in sentence_text for pattern in DEFINITION_PATTERNS):
            factual_score += 2

        # 2️⃣ Enumeration detection
        if any(token in sentence_text for token in ENUMERATION_TOKENS):
            factual_score += 1.5

        # 3️⃣ Verb presence (informational indicator)
        verbs = [token for token in sent if token.pos_ == "VERB"]
        if verbs:
            factual_score += 1

        # 4️⃣ Sentence length bonus (but not strict)
        if 8 <= len(sent.text.split()) <= 35:
            factual_score += 1

    if not sentences:
        return 0.0

    density = factual_score / len(sentences)

    return round(min(density * 20, 100), 2)
