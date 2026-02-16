import { useState } from "react";
import { runAudit } from "../services/api";
import { ClipLoader } from "react-spinners";
import CRIGauge from "../components/CRIGauge";
import RadarPanel from "../components/RadarPanel";
import HeatmapPanel from "../components/HeatmapPanel";
import RiskPanel from "../components/RiskPanel";
import SectionPanel from "../components/SectionPanel";
import MetricCard from "../components/MetricCard";

export default function Dashboard() {
  const [url, setUrl] = useState("");
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleAudit = async () => {
    if (!url) return;
    setLoading(true);
    setData(null);
    try {
      const result = await runAudit(url);
      setData(result);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1 style={{ marginBottom: 20 }}>
        Citation Readiness <span style={{ color: "#FF6B35" }}>Engine</span>
      </h1>

      <div className="panel" style={{ marginBottom: 24 }}>
        <input
          placeholder="Enter URL to audit"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={handleAudit}>Run Audit</button>
      </div>

      {loading && (
        <div style={{ textAlign: "center", marginTop: 80 }}>
          <ClipLoader color="#FF6B35" size={70} />
        </div>
      )}

      {data && !loading && (
        <div className="fade-in">
          <div className="dashboard-grid">
            <CRIGauge
              score={data.citation_readiness_index}
              probability={data.citation_probability}
            />
            <RadarPanel data={data} />
          </div>

          <div className="metric-grid">
            <MetricCard label="DOM Score" value={data.dom_score} />
            <MetricCard label="Fact Density" value={data.fact_density} />
            <MetricCard label="Entity Clarity" value={data.entity_clarity} />
            <MetricCard label="Retrieval Score" value={data.retrieval_simulation} />
          </div>

          <HeatmapPanel heatmap={data.retrieval_heatmap} />
          <RiskPanel risks={data.risk_flags} />

          {data.section_breakdown.map((section: any, i: number) => (
            <SectionPanel key={i} section={section} />
          ))}
        </div>
      )}
    </div>
  );
}
