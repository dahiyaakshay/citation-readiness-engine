import requests

def fetch_html_from_url(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text
