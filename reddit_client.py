import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_token():
    auth = requests.auth.HTTPBasicAuth(
        os.getenv("REDDIT_CLIENT_ID"),
        os.getenv("REDDIT_CLIENT_SECRET")
    )
    data = {"grant_type": "client_credentials"}
    headers = {"User-Agent": os.getenv("REDDIT_USER_AGENT")}
    response = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=auth, data=data, headers=headers
    )
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Errore autenticazione Reddit: {response.status_code}")
        return None

def get_reddit_posts(keyword, limit=20):
    url = f"https://www.reddit.com/search.json?q={keyword}&limit={limit}&sort=relevance"
    headers = {"User-Agent": "SentimentScope/1.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore: {response.status_code}")
        return None