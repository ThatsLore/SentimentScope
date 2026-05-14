import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_posts(keyword, limit=100):
    url = f"https://www.reddit.com/search.json?q={keyword}&limit={limit}&sort=relevance"
    headers = {"User-Agent": "SentimentScope/1.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore: {response.status_code}")
        return None