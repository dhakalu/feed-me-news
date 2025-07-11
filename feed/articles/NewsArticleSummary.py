"""
<|cursor|>
This module provides the `NewsArticleSummary` class, which encapsulates the essential details 
of a news article in a summarized format. It is designed to represent key attributes of a news 
article, such as its title, link, description, publication date, author, categories, and an 
associated image.

Classes:
    - NewsArticleSummary: Represents a summarized version of a news article.

Dependencies:
    - typing.List: Used for type hinting the list of categories.
    - feed.articles.NewsArticleImage: Represents the image associated with the news article.

Usage:
    This module can be used to create instances of `NewsArticleSummary` for storing and 
    accessing summarized details of news articles. It is particularly useful for applications 
    that need to display or process news articles in a compact format.
"""

from typing import List
import feed.articles.NewsArticleImage as NewsArticleImage

class NewsArticleSummary:
    """
    NewsArticleSummary is a class that represents a summarized version of a news article. 
    It contains attributes such as the title, link, description, publication date, author, 
    categories, and an associated image. This class is designed to encapsulate the essential 
    details of a news article for easy access and representation.
    Attributes:
        title (str): The title of the news article.
        link (str): The URL link to the full news article.
        description (str): A brief summary or description of the news article.
        published_on (str): The publication date of the news article.
        written_by (str): The author of the news article.
        categories (List[str]): A list of categories or tags associated with the news article.
        image (NewsArticleImage): An object representing the image associated with the news article.
    """


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
            Image: {self.image.url}
        '''