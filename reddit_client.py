import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_posts(keyword, limit=10):
    url = f"https://www.reddit.com/r/all/search.json?q={keyword}&limit={limit}"
    headers = {"User-Agent": os.getenv("REDDIT_USER_AGENT")}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore nella richiesta a Reddit: {response.status_code}")
        return None
