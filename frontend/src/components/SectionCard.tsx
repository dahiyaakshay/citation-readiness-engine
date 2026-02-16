export default function SectionCard({ section }: any) {
  return (
    <div className="panel">
      <h3 className="accent">{section.heading}</h3>
      <p>Fact Density: {section.fact_density}</p>
      <p>Entity Clarity: {section.entity_clarity}</p>
      <p>Tone Neutrality: {section.tone_neutrality}</p>
    </div>
  );
}
