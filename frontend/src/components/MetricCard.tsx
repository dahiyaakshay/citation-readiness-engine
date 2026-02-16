export default function MetricCard({ label, value }: any) {
  return (
    <div className="panel" style={{ textAlign: "center" }}>
      <h4 style={{ opacity: 0.7 }}>{label}</h4>
      <h2 style={{ color: "#FF6B35" }}>{value}</h2>
    </div>
  );
}
