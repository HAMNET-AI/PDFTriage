import os
from src.routers import router
from src.triage import fetch_pages
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

if __name__ == '__main__':
    query = "Can you summarize the key takeaways from pages 5?"
    router(query)
