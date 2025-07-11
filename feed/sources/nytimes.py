"""
NYTimesSource is a class that represents a news source for fetching articles from the New York Times RSS feed. 
It extends the `Source` class and provides functionality to parse and map XML data into `NewsArticleSummary` objects.
Methods:
---------
- __init__():
    Initializes the NYTimesSource instance with a source identifier 'nyt'.
- mapper(item: ElementTree.Element, name_spaces) -> NewsArticleSummary:
    Converts an XML Element representing a news item into a `NewsArticleSummary` object. 
    Extracts details such as title, link, publication date, description, author, categories, and associated image metadata.
    Parameters:
    - item: An XML Element representing a news item.
    - name_spaces: A dictionary of XML namespaces used for parsing.
    Returns:
    - A `NewsArticleSummary` object containing the parsed data.
- get_feed() -> List[NewsArticleSummary]:
    Fetches the list of news articles published on the New York Times homepage by parsing the RSS feed.
    Returns:
    - A list of `NewsArticleSummary` objects representing the articles in the feed.
Dependencies:
--------------
- NewsArticleImage: Represents metadata for an article's image.
- NewsArticleSummary: Represents a summary of a news article.
- Source: Base class for news sources.
- feed.utils.request: Utility for making HTTP requests and fetching XML data.
- feed.utils.xml: Utilities for parsing XML data, extracting text, and handling namespaces.

"""

from typing import Dict, List
from xml.etree import ElementTree
from feed.articles.NewsArticleImage import NewsArticleImage
from feed.articles.NewsArticleSummary import NewsArticleSummary
from feed.sources.Source import Source 
import feed.utils.request as r
from feed.utils.xml import (
    get_namespaces,
    extract_text_from_attr,
    extract_text_from_tag
)

class NYTimesSource(Source):

    def __init__(self):
        super().__init__('nyt')
    
    def mapper(self, item: ElementTree.Element, name_spaces) -> NewsArticleSummary:
        """
            Converts xml Element of item to NewsArticleSummary
        """
        summary = NewsArticleSummary()
        summary.title = extract_text_from_tag(item, 'title')
        summary.link = extract_text_from_tag(item, 'link')
        summary.published_on = extract_text_from_tag(item, 'pubDate')
        summary.description = extract_text_from_tag(item, 'description')
        summary.written_by =extract_text_from_tag(item, "dc:creator", name_spaces)
        summary.categories = [x.text for x in item.findall('category')]
        image_url = extract_text_from_attr(item.find("media:content", name_spaces), "url")
        image_alt = extract_text_from_tag(item, "media:description", name_spaces)
        image_credit = extract_text_from_tag(item, "media:credit", name_spaces)
        summary.image = NewsArticleImage(image_url, image_credit, image_alt)
        return summary



    def get_feed(self) -> List[NewsArticleSummary]:
        """
        Fetches list of news articles published on NYTime's HomePage
        """
        ny_times_home, schema = r.get_xml('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
        name_spaces = get_namespaces(schema)
        return self.parse(ny_times_home.getroot(), name_spaces)

