

from typing import List
from feed.utils.request import get_soup
from feed.sources.NewsSource import NewsSource
from feed.articles.NewsArticleSummary import NewsArticleSummary

# todo move this to utility as this logic can be reused across the sources
def filter_news(articles: List[NewsArticleSummary], start: str):
    # todo change this logic to do date comparison
    return filter(lambda a: a == start, articles)

HOME_URL = 'https://news.yahoo.com'

class Yahoo(NewsSource):

        
    def get_articles(self, start):
        self.last_read = start
        self._parse(start)
    
    def _parse(self, start):
        soup = get_soup(HOME_URL)
        articles = []
        return filter_news(articles, start)