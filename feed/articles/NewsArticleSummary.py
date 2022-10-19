from typing import List
import feed.articles.NewsArticleImage as NewsArticleImage

class NewsArticleSummary:

    def __init__(self):
        self.title: str = ''
        self.link: str = ''
        self.description: str = ''
        self.published_on: str = ''
        self.written_by: str = ''
        self.categories: List[str] = []
        self.image: NewsArticleImage = None

    def __repr__(self):
        return f'''
            Title: {self.title}
            Link: {self.link}
            Description: {self.description}
            PublishedOn: {self.published_on}
            WrittenBy: {self.written_by}
            Categories: {self.categories}
            Image: {self.image}
        '''