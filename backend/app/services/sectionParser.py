from bs4 import BeautifulSoup


def extract_sections(html: str):
    soup = BeautifulSoup(html, "html.parser")
    sections = {}

    # 1️⃣ Try heading-based extraction first
    headings = soup.find_all(["h2", "h3"])

    if headings:
        for heading in headings:
            content = []
            for sibling in heading.find_next_siblings():
                if sibling.name in ["h2", "h3"]:
                    break
                if sibling.name in ["p", "ul", "ol"]:
                    content.append(sibling.get_text())

            if content:
                sections[heading.get_text().strip()] = " ".join(content)

        if sections:
            return sections

    # 2️⃣ Detect bold/strong pseudo-headings
    paragraphs = soup.find_all("p")

    current_heading = None
    buffer = []

    for p in paragraphs:
        strong = p.find("strong")

        if strong and len(strong.get_text().strip()) < 120:
            if current_heading and buffer:
                sections[current_heading] = " ".join(buffer)
                buffer = []

            current_heading = strong.get_text().strip()
        else:
            if current_heading:
                buffer.append(p.get_text().strip())

    if current_heading and buffer:
        sections[current_heading] = " ".join(buffer)

    if sections:
        return sections

    # 3️⃣ Fallback: chunk paragraphs into blocks of ~3
    sections = {}
    chunk_size = 3
    for i in range(0, len(paragraphs), chunk_size):
        chunk = paragraphs[i:i + chunk_size]
        text = " ".join(p.get_text().strip() for p in chunk)
        if text:
            sections[f"Section {i//chunk_size + 1}"] = text

    return sections
