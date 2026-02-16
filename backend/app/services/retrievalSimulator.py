import faiss
import numpy as np
from app.utils.embeddingLoader import get_embedding_model
from app.services.queryGenerator import generate_queries_from_content


def compute_retrieval_analysis(sections: dict):

    if not sections:
        return {
            "overall_score": 0.0,
            "heatmap": {}
        }

    texts = list(sections.values())
    headings = list(sections.keys())

    model = get_embedding_model()
    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)

    normalized_embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    index.add(normalized_embeddings.astype("float32"))

    dynamic_queries = generate_queries_from_content(sections)

    section_scores = {heading: [] for heading in headings}

    for query in dynamic_queries:

        q_embed = model.encode([query])
        q_embed = q_embed / np.linalg.norm(q_embed, axis=1, keepdims=True)

        D, I = index.search(q_embed.astype("float32"), k=len(texts))

        similarities = D[0]
        indices = I[0]

        for rank, idx in enumerate(indices):
            heading = headings[idx]
            score = similarities[rank] * 100
            section_scores[heading].append(score)

    heatmap = {
        heading: round(np.mean(scores), 2)
        for heading, scores in section_scores.items()
    }

    overall_score = round(np.mean(list(heatmap.values())), 2)

    return {
        "overall_score": overall_score,
        "heatmap": heatmap
    }
