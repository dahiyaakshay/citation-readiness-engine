import re

def clean_text(text: str) -> str:
    if not text:
        return ""

    # Remove excessive whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove non-printable characters
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    # Strip leading/trailing spaces
    return text.strip()
