from flask import Flask, render_template, request, redirect, url_for
from reddit_client import get_reddit_posts
from sentiment import analyze_sentiment
from db import save_post, get_all_posts
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form["keyword"]
        return redirect(url_for("dashboard", keyword=keyword))
    return render_template("index.html")

@app.route("/dashboard/<keyword>")
def dashboard(keyword):
    posts_data = get_reddit_posts(keyword)
    if posts_data:
        for post in posts_data["data"]["children"]:
            post_data = post["data"]
            title = post_data["title"]
            text = post_data["selftext"]
            sentiment = analyze_sentiment(text)
            subreddit = post_data["subreddit"]
            score = post_data["score"]
            date = datetime.fromtimestamp(post_data["created_utc"])
            link = post_data["url"]
            save_post(title, text, sentiment, subreddit, score, date, link)

    posts = get_all_posts()
    posts_list = []
    for post in posts:
        posts_list.append({
            "title": post[1],
            "sentiment": post[3],
            "subreddit": post[4],
            "date": post[6]
        })

    posts_json = json.dumps(posts_list)
    return render_template("dashboard.html", keyword=keyword, posts=posts_list, posts_json=posts_json)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
