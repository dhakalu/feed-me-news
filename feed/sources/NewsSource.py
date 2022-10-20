
from typing import List
from abc import abstractmethod, ABC
from feed.articles.NewsArticleSummary import NewsArticleSummary

class NewsSource(ABC):

    @abstractmethod
    def get_articles(self, start: str) -> List[NewsArticleSummary]:
        """
            Returns list of NewsSummaryArticle

            Args:
                start: Start Date. Articles published only after this date are returned.
        """
        pass
