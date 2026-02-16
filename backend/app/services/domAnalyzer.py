from bs4 import BeautifulSoup

def analyze_dom(html: str) -> float:
    soup = BeautifulSoup(html, "html.parser")

    semantic_tags = soup.find_all(["h1", "h2", "h3", "p", "ul", "ol"])
    generic_tags = soup.find_all(["div", "span"])

    total = len(semantic_tags) + len(generic_tags) + 1
    semantic_ratio = len(semantic_tags) / total

    headings = [tag.name for tag in soup.find_all(["h1", "h2", "h3"])]
    heading_score = 1.0 if headings == sorted(headings) else 0.6

    max_depth = max([len(list(tag.parents)) for tag in soup.find_all()]) if soup.find_all() else 1
    depth_penalty = min(max_depth / 25, 1)

    score = (
        semantic_ratio * 40 +
        heading_score * 30 +
        (1 - depth_penalty) * 30
    )

    return round(score, 2)
