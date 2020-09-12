import os


class Config:
    """
    General config parent class
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    ARTICLE_URL = 'https://newsapi.org/v2/everything?q=trending&language=en&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')