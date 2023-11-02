
from src.routers import router
from dotenv import load_dotenv

load_dotenv( override=True)

if __name__ == '__main__':
    query = "Can you summarize the key takeaways from pages 5-7?"
    router(query=query)