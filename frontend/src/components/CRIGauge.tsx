function getColor(score: number) {
  if (score < 40) return "score-red";
  if (score < 65) return "score-orange";
  return "score-green";
}

export default function CRIGauge({ score, probability }: any) {
  const radius = 90;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (score / 100) * circumference;

  return (
    <div className="panel" style={{ textAlign: "center" }}>
      <h2>Overall Citation Readiness</h2>
      <svg width="260" height="260">
        <circle cx="130" cy="130" r={radius} stroke="#333" strokeWidth="14" fill="none" />
        <circle
          cx="130"
          cy="130"
          r={radius}
          stroke="#FF6B35"
          strokeWidth="14"
          fill="none"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          strokeLinecap="round"
          style={{ transition: "stroke-dashoffset 1s ease" }}
        />
      </svg>
      <h1 className={getColor(score)} style={{ marginTop: -170, fontSize: 56 }}>
        {score}
      </h1>
      <p>{probability.probability_label}</p>
    </div>
  );
}
