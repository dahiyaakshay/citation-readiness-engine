from app.utils.htmlFetcher import fetch_html_from_url
from app.services.domAnalyzer import analyze_dom
from app.services.sectionParser import extract_sections
from app.services.factDensityService import compute_fact_density
from app.services.entityClarityService import compute_entity_clarity
from app.services.toneScannerService import compute_tone_score
from app.services.retrievalSimulator import compute_retrieval_analysis
from app.services.scoringEngine import calculate_final_score
from app.services.riskFlagEngine import generate_risk_flags
from app.services.citationClassifier import classify_citation_probability
from app.utils.textCleaner import clean_text
from app.database.repository import save_audit


def run_citation_audit(request):

    if request.url:
        html = fetch_html_from_url(request.url)
        source_url = request.url
    elif request.html:
        html = request.html
        source_url = None
    else:
        return {"error": "Provide either url or html"}

    dom_score = analyze_dom(html)
    sections = extract_sections(html)

    if not sections:
        return {"error": "No sections detected for analysis"}

    fact_scores = []
    entity_scores = []
    tone_scores = []
    section_breakdown = []

    for heading, text in sections.items():

        cleaned = clean_text(text)

        fact = compute_fact_density(cleaned)
        entity = compute_entity_clarity(cleaned)
        tone = compute_tone_score(cleaned)

        fact_scores.append(fact)
        entity_scores.append(entity)
        tone_scores.append(tone)

        section_breakdown.append({
            "heading": heading,
            "fact_density": round(fact, 2),
            "entity_clarity": round(entity, 2),
            "tone_neutrality": round(tone, 2),
        })

    fact_avg = sum(fact_scores) / len(fact_scores)
    entity_avg = sum(entity_scores) / len(entity_scores)
    tone_avg = sum(tone_scores) / len(tone_scores)

    retrieval_analysis = compute_retrieval_analysis(sections)
    retrieval_score = retrieval_analysis["overall_score"]
    heatmap = retrieval_analysis["heatmap"]

    cri = calculate_final_score(
        dom_score,
        fact_avg,
        entity_avg,
        tone_avg,
        retrieval_score,
    )

    probability = classify_citation_probability(cri)

    risk_flags = generate_risk_flags(
        dom_score,
        fact_avg,
        entity_avg,
        tone_avg,
        retrieval_score,
        heatmap
    )

    save_audit(
        source_url,
        cri,
        dom_score,
        fact_avg,
        entity_avg,
        tone_avg,
        retrieval_score,
        section_breakdown,
    )

    return {
        "citation_readiness_index": cri,
        "citation_probability": probability,
        "dom_score": dom_score,
        "fact_density": round(fact_avg, 2),
        "entity_clarity": round(entity_avg, 2),
        "tone_neutrality": round(tone_avg, 2),
        "retrieval_simulation": retrieval_score,
        "retrieval_heatmap": heatmap,
        "risk_flags": risk_flags,
        "sections_analyzed": len(sections),
        "section_breakdown": section_breakdown,
    }
