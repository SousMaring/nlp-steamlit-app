# src/sentiment.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    """Returns sentiment scores for the given text."""
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)