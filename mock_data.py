from datetime import datetime

MOCK_POSTS = [
    {"title": "AI is revolutionizing healthcare", "selftext": "Artificial intelligence is helping doctors diagnose diseases faster and more accurately. This is a fantastic development.", "subreddit": "technology", "score": 2400, "created_utc": 1710000000, "url": "https://reddit.com/fake1"},
    {"title": "I hate how AI is taking over jobs", "selftext": "This is terrible. Millions of people are losing their jobs because of automation. The future looks horrible.", "subreddit": "news", "score": 980, "created_utc": 1710003600, "url": "https://reddit.com/fake2"},
    {"title": "New AI model released today", "selftext": "A new model was released. It has some improvements over the previous version.", "subreddit": "MachineLearning", "score": 540, "created_utc": 1710007200, "url": "https://reddit.com/fake3"},
    {"title": "AI art is absolutely amazing", "selftext": "I love what AI can do with images. The results are beautiful and inspiring.", "subreddit": "Art", "score": 3100, "created_utc": 1710010800, "url": "https://reddit.com/fake4"},
    {"title": "AI is dangerous and we should be scared", "selftext": "Nobody is talking about how dangerous this technology really is. It is a disaster waiting to happen.", "subreddit": "worldnews", "score": 1200, "created_utc": 1710014400, "url": "https://reddit.com/fake5"},
    {"title": "Using AI to learn programming faster", "selftext": "I have been using AI tools to learn Python and it is going great. Highly recommend it to everyone.", "subreddit": "learnprogramming", "score": 870, "created_utc": 1710018000, "url": "https://reddit.com/fake6"},
    {"title": "AI chatbots are so annoying", "selftext": "Every website now has an AI chatbot that never understands what you need. It is frustrating and useless.", "subreddit": "mildlyinfuriating", "score": 4200, "created_utc": 1710021600, "url": "https://reddit.com/fake7"},
    {"title": "AI helped me write my thesis", "selftext": "I used AI tools to help structure my research and it was a wonderful experience. I could not have done it without it.", "subreddit": "college", "score": 650, "created_utc": 1710025200, "url": "https://reddit.com/fake8"},
    {"title": "The AI bubble will burst soon", "selftext": "All these companies investing in AI will lose everything. This is just hype with no real value.", "subreddit": "investing", "score": 720, "created_utc": 1710028800, "url": "https://reddit.com/fake9"},
    {"title": "AI tools for productivity", "selftext": "I have been testing various AI tools this week. Some are okay, some are not that useful.", "subreddit": "productivity", "score": 310, "created_utc": 1710032400, "url": "https://reddit.com/fake10"},
]

def get_mock_posts():
    return MOCK_POSTS