export default function Heatmap({ heatmap }: any) {
  const sorted = Object.entries(heatmap).sort(
    (a: any, b: any) => b[1] - a[1]
  );

  return (
    <div className="panel">
      <h2>Retrieval Heatmap</h2>

      {sorted.map(([key, value]: any) => (
        <div key={key} style={{ marginBottom: "12px" }}>
          <strong>{key}</strong>
          <div
            style={{
              background: "#333",
              borderRadius: "8px",
              overflow: "hidden",
              marginTop: "6px",
            }}
          >
            <div
              style={{
                width: `${value}%`,
                background:
                  value < 40
                    ? "#ff4d4f"
                    : value < 65
                    ? "#FF6B35"
                    : "#52c41a",
                padding: "6px",
                textAlign: "right",
              }}
            >
              {value}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
