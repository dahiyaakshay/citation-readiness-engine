export default function HeatmapPanel({ heatmap }: any) {
  const sorted = Object.entries(heatmap).sort(
    (a: any, b: any) => b[1] - a[1]
  );

  return (
    <div className="panel" style={{ marginTop: 24 }}>
      <h2>Retrieval Heatmap</h2>
      {sorted.map(([k, v]: any) => (
        <div key={k} style={{ marginBottom: 12 }}>
          <strong>{k}</strong>
          <div style={{ background: "#333", borderRadius: 8, marginTop: 6 }}>
            <div
              style={{
                width: `${v}%`,
                background:
                  v < 40 ? "#ff4d4f" :
                  v < 65 ? "#FF6B35" :
                  "#52c41a",
                padding: 6,
                textAlign: "right"
              }}
            >
              {v}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
