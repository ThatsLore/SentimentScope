import requests
import os
from dotenv import load_dotenv
from mock_data import get_mock_posts

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
    # USA MOCK DATA finché l'API Reddit non è approvata
    print(f"[MOCK] Returning mock data for keyword: {keyword}")
    return get_mock_posts()