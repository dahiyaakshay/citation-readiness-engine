import {
  Radar, RadarChart, PolarGrid,
  PolarAngleAxis, PolarRadiusAxis,
  ResponsiveContainer
} from "recharts";

export default function RadarPanel({ data }: any) {
  const chartData = [
    { subject: "DOM", value: data.dom_score },
    { subject: "Fact", value: data.fact_density },
    { subject: "Entity", value: data.entity_clarity },
    { subject: "Tone", value: data.tone_neutrality },
    { subject: "Retrieval", value: data.retrieval_simulation }
  ];

  return (
    <div className="panel">
      <h2>Score Breakdown</h2>
      <ResponsiveContainer width="100%" height={340}>
        <RadarChart data={chartData}>
          <PolarGrid stroke="#555" />
          <PolarAngleAxis dataKey="subject" stroke="#aaa" />
          <PolarRadiusAxis stroke="#777" />
          <Radar dataKey="value" stroke="#FF6B35" fill="#FF6B35" fillOpacity={0.6} />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}
