CREATE TABLE IF NOT EXISTS audits (
    id SERIAL PRIMARY KEY,
    url TEXT,
    cri_score NUMERIC,
    dom_score NUMERIC,
    fact_score NUMERIC,
    entity_score NUMERIC,
    tone_score NUMERIC,
    retrieval_score NUMERIC,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS sections (
    id SERIAL PRIMARY KEY,
    audit_id INTEGER REFERENCES audits(id) ON DELETE CASCADE,
    heading TEXT,
    fact_score NUMERIC,
    entity_score NUMERIC,
    tone_score NUMERIC,
    retrieval_score NUMERIC
);
