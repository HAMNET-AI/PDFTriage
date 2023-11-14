from src.routers import router
from dotenv import load_dotenv
load_dotenv(override=True)

if __name__ == '__main__':
    query = "The second figure of the paper is mainly about related work"
    router(query=query)
