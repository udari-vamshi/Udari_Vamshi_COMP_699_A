import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

from database.models import Issue
from database.db import db

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    score = sia.polarity_scores(text)

    if score['compound'] <= -0.5:
        return "urgent"
    elif score['compound'] < 0.2:
        return "neutral"
    else:
        return "negative"


def run_clustering():
    issues = Issue.query.all()

    if len(issues) < 2:
        return

    texts = [i.description for i in issues]

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)

    k = min(3, len(issues))
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(X)

    for i, issue in enumerate(issues):
        issue.cluster_id = int(labels[i])

    db.session.commit()


def process_new_issue(issue):
    tone = analyze_sentiment(issue.description)
    issue.tone = tone

    db.session.commit()

    run_clustering()