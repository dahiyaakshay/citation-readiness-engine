export default function RiskPanel({ risks }: any) {
  if (!risks.length) return null;

  return (
    <div className="panel" style={{ marginTop: 24 }}>
      <h2>Risk Flags</h2>
      {risks.map((r: string, i: number) => (
        <div
          key={i}
          style={{
            background: "rgba(255,77,79,0.1)",
            borderLeft: "4px solid #ff4d4f",
            padding: 10,
            marginBottom: 10
          }}
        >
          {r}
        </div>
      ))}
    </div>
  );
}
