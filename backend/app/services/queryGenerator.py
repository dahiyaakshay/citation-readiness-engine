import spacy

nlp = spacy.load("en_core_web_sm")


def generate_queries_from_content(sections: dict):

    full_text = " ".join(sections.values())
    doc = nlp(full_text)

    # Extract top entities
    entities = [ent.text for ent in doc.ents if len(ent.text) > 3]

    unique_entities = list(set(entities))[:5]

    queries = []

    for entity in unique_entities:
        queries.append(f"What is {entity}?")
        queries.append(f"How does {entity} work?")

    # Fallback generic queries
    if not queries:
        queries = [
            "What is this topic?",
            "How does this system work?",
        ]

    return queries[:6]
