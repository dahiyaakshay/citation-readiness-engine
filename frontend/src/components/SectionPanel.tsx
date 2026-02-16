import { useState } from "react";

export default function SectionPanel({ section }: any) {
  const [open, setOpen] = useState(false);

  return (
    <div className="panel" style={{ marginTop: 16 }}>
      <div
        onClick={() => setOpen(!open)}
        style={{ cursor: "pointer", fontWeight: 600 }}
      >
        {section.heading}
      </div>

      {open && (
        <div style={{ marginTop: 12 }}>
          <p>Fact Density: {section.fact_density}</p>
          <p>Entity Clarity: {section.entity_clarity}</p>
          <p>Tone Neutrality: {section.tone_neutrality}</p>
        </div>
      )}
    </div>
  );
}
