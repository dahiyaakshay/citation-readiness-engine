import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer,
} from "recharts";

export default function RadarChartComponent({ data }: any) {
  const chartData = [
    { subject: "DOM", value: data.dom_score },
    { subject: "Fact", value: data.fact_density },
    { subject: "Entity", value: data.entity_clarity },
    { subject: "Tone", value: data.tone_neutrality },
    { subject: "Retrieval", value: data.retrieval_simulation },
  ];

  return (
    <div className="panel">
      <h2>Score Breakdown</h2>

      <ResponsiveContainer width="100%" height={300}>
        <RadarChart data={chartData}>
          <PolarGrid stroke="#555" />
          <PolarAngleAxis dataKey="subject" stroke="#aaa" />
          <PolarRadiusAxis stroke="#777" />
          <Radar
            dataKey="value"
            stroke="#FF6B35"
            fill="#FF6B35"
            fillOpacity={0.6}
          />
        </RadarChart>
      </ResponsiveContainer>

      <div style={{ marginTop: "20px", fontSize: "14px", opacity: 0.8 }}>
        Retrieval Score: <strong>{data.retrieval_simulation}</strong>
      </div>
    </div>
  );
}
