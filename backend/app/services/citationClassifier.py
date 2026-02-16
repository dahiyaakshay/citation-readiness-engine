def classify_citation_probability(cri_score):

    if cri_score >= 80:
        return {
            "probability_label": "High",
            "probability_score": 0.85
        }

    elif cri_score >= 65:
        return {
            "probability_label": "Moderate",
            "probability_score": 0.65
        }

    elif cri_score >= 50:
        return {
            "probability_label": "Low-Moderate",
            "probability_score": 0.45
        }

    else:
        return {
            "probability_label": "Low",
            "probability_score": 0.20
        }
