from xml.etree import ElementTree
from feed.articles.NewsArticleSummary import NewsArticleSummary
from typing import List, Dict

class Source:
    """Source
    A base class for all feed sources. This class provides a structure for fetching and parsing feed data 
    from various sources. Subclasses should implement the `mapper` method to convert feed items into 
    `NewsArticleSummary` objects and override the `get_feed` method to fetch feed data.
    Attributes:
        name (str): The name of the feed source.
    Methods:
        __init__(name: str):
            Initializes the Source object with a name.
        mapper(item: ElementTree.Element, name_spaces: Dict[str, str]) -> NewsArticleSummary:
            Converts an XML item element into a `NewsArticleSummary` object. This method must be 
            implemented by subclasses.
        get_feed() -> List[NewsArticleSummary]:
            Fetches the feed data and returns a list of `NewsArticleSummary` objects. This method 
            should be overridden by subclasses.
        parse(xml_string: ElementTree.Element, name_spaces: Dict[str, str]) -> List[NewsArticleSummary]:
            Parses the XML feed and returns a list of `NewsArticleSummary` objects. This method uses 
            the `mapper` function to convert individual feed items into summaries.
    """

    def __init__(self, name: str):
        self.name = name

    def mapper(self, item: ElementTree.Element, name_spaces) -> NewsArticleSummary:
        """
        Converts an item to a NewsArticleSummary.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def get_feed(self) -> List[NewsArticleSummary]:
        """
        Fetch the feed data.
        This method should be overridden by subclasses.
        """
        return []
    
    def parse(self, xml_string: ElementTree.Element, name_spaces: Dict[str, str]) -> List[NewsArticleSummary]:
        """Given the full XML of feed, it returns list of NewsArticleSummary"""
        channel = xml_string.findall('channel')[0]
        items = channel.findall('item')
        summaries =  map(lambda x: self.mapper(x, name_spaces), items)
        return list(summaries)