# Citation Readiness Engine

AI-powered citation-readiness scoring engine that evaluates structural integrity, entity coherence, retrieval strength, and section-level dominance to simulate AI search citation likelihood.

---

## Overview

Citation Readiness Engine is a full-stack AI intelligence system designed to estimate how likely a webpage is to be cited by AI-powered retrieval systems.

It combines structural analysis, semantic modeling, entity dominance scoring, and retrieval simulation to generate a composite Citation Readiness Index (CRI).

This project demonstrates:

- Retrieval-aware scoring
- Section-level visibility heatmaps
- Entity coherence modeling
- DOM complexity analysis
- Risk detection engine
- Full-stack analytics dashboard

---

## Architecture

```
Frontend (React + Vite)
        ↓
FastAPI Backend
        ↓
Scoring & Retrieval Engine
        ↓
PostgreSQL Persistence
```

---

## Core Scoring Components

### 1. DOM Structural Analysis

Measures structural extractability and semantic integrity.

### 2. Fact Density Engine

Detects definitional patterns, verb structures, and informational signals.

### 3. Entity Coherence Model

Evaluates dominant entity ratio and terminology consistency.

### 4. Retrieval Simulation

Uses sentence-transformers embeddings + FAISS similarity search to simulate AI-style retrieval dominance.

### 5. Risk Flag Engine

Identifies weak sections and structural issues.

---

## Output Metrics

- Citation Readiness Index (0–100)
- Citation Probability Classification
- Retrieval Heatmap
- Section-Level Diagnostics
- Risk Flags

---

## Tech Stack

### Backend

- FastAPI
- PostgreSQL
- Sentence Transformers
- FAISS
- spaCy
- NumPy

### Frontend

- React (TypeScript)
- Vite
- Recharts
- Axios

---

## Running Locally

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs at: `http://127.0.0.1:8000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## Example Use Case

Audit a page to determine:

- Is it structurally citation-ready?
- Which sections dominate retrieval?
- Where does entity fragmentation occur?
- What suppresses citation probability?

---

## Status

This repository represents a fully functional Proof of Concept demonstrating AI citation-readiness modeling and analytics visualization.

---

## Future Expansion Ideas

- Audit history tracking
- Competitive comparison
- AI rewrite suggestions
- PDF report export
- Trend analysis dashboard
