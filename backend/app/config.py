import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

RETRIEVAL_TEST_QUERIES = [
    "How does this system work?",
    "What increases citation probability?",
    "How are AI search engines selecting sources?",
]
