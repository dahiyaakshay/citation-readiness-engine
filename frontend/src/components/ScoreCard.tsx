import { useEffect, useState } from "react";

function getScoreColor(score: number) {
  if (score < 40) return "score-red";
  if (score < 65) return "score-orange";
  return "score-green";
}

export default function ScoreCard({ score, probability }: any) {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const timer = setTimeout(() => {
      setProgress(score);
    }, 300);
    return () => clearTimeout(timer);
  }, [score]);

  const radius = 70;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset =
    circumference - (progress / 100) * circumference;

  return (
    <div className="panel" style={{ textAlign: "center" }}>
      <h2>Overall Citation Readiness</h2>

      <svg width="180" height="180">
        <circle
          cx="90"
          cy="90"
          r={radius}
          stroke="#333"
          strokeWidth="12"
          fill="transparent"
        />
        <circle
          cx="90"
          cy="90"
          r={radius}
          stroke="#FF6B35"
          strokeWidth="12"
          fill="transparent"
          strokeDasharray={circumference}
          strokeDashoffset={strokeDashoffset}
          strokeLinecap="round"
          style={{ transition: "stroke-dashoffset 1s ease" }}
        />
      </svg>

      <h1 className={getScoreColor(score)} style={{ marginTop: "-120px", fontSize: "42px" }}>
        {score}
      </h1>

      <p>
        Probability: <strong>{probability.probability_label}</strong>
      </p>
    </div>
  );
}
