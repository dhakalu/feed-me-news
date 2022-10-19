from typing import Dict, List
from xml.etree import ElementTree
from feed.articles.NewsArticleImage import NewsArticleImage
from feed.articles.NewsArticleSummary import NewsArticleSummary
import feed.utils.request as r
from feed.utils.xml import (
    get_namespaces,
    extract_text_from_attr,
    extract_text_from_tag
)

def mapper(item: ElementTree.Element, name_spaces) -> NewsArticleSummary:
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

def parse(xml_string: ElementTree.Element, name_spaces: Dict[str, str]) -> List[NewsArticleSummary]:
    """Given the full XML of NY times feed, it returns list of NewsArticleSummary"""
    channel = xml_string.findall('channel')[0]
    return list(map(lambda x: mapper(x, name_spaces), channel.findall('item')))
        


def get_home() -> List[NewsArticleSummary]:
    """
    Fetches list of news articles published on NYTime's HomePage
    """
    ny_times_home, schema = r.get_xml('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
    name_spaces = get_namespaces(schema)
    return parse(ny_times_home.getroot(), name_spaces)

# Using a CMD tool to see today's news
if __name__ == "__main__":
    articles = get_home()
    print(articles)