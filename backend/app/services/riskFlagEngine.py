def generate_risk_flags(dom, fact, entity, tone, retrieval, heatmap):

    flags = []

    if dom < 40:
        flags.append("DOM structure is complex. High extraction cost.")

    if fact < 50:
        flags.append("Low fact density detected. Increase definitional clarity.")

    if entity < 45:
        flags.append("Entity fragmentation risk. Inconsistent terminology.")

    if tone < 70:
        flags.append("Promotional tone detected. AI citation confidence reduced.")

    if retrieval < 50:
        flags.append("Weak retrieval confidence. Sections compete ambiguously.")

    weak_sections = [
        heading for heading, score in heatmap.items()
        if score < 40
    ]

    if weak_sections:
        flags.append(
            f"{len(weak_sections)} sections show low retrieval strength."
        )

    if not flags:
        flags.append("No major citation risks detected.")

    return flags
