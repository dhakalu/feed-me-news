from io import StringIO
from xml.etree import ElementTree
from feed.articles.NewsArticleImage import NewsArticleImage
from feed.articles.NewsArticleSummary import NewsArticleSummary
from feed.utils.request import get_xml

def extract_text_from_tag(xml: ElementTree.Element, tag_name: str, name_space=None):
    """
    Extracts the text of the given tag. If the tag does not exist it returns empty string.

    Args:
        xml: Element that contains the tag
        tag_name: name of the tag to extract text from

    Returns:
        Text with in the tag
    """
    value = xml.find(tag_name, name_space)
    if value is None:
        return ''
    return value.text

def extract_text_from_attr(xml: ElementTree.Element, attr_name: str):
    """
    Extracts the text of the given tag. If the tag does not exist it returns empty string.

    Args:
        xml: Element that contains the tag
        tag_name: name of the tag to extract text from

    Returns:
        Text with in the tag
    """
    try:
        value = xml.attrib.get('url')
        if value is None:
           return ''
        return value
    except AttributeError:
        return ''
    

# def get_namespaces(schema):
#     return dict([ node for _, node in schema])

def mapper(item: ElementTree.Element, name_spaces) -> NewsArticleSummary:
    """
        Converts xml Element of item to NewsArticleSummary
    """
    summary = NewsArticleSummary()
    # print(item.tag)
    # name_spaces = get_namespaces(item)
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

def parse(xml_string, name_spaces):
    """Given the full """
    channel = xml_string.findall('channel')[0]
    return list(map(lambda x: mapper(x, name_spaces), channel.findall('item')))
        
def get_namespaces(xml_string):
    """
        Given the xml string finds all the namespaces for the xml.
        Example: 
            Given:
                <rss xln:dc="abc" xln:media="xyz">....</rss>
            Returns:
                {'dc': 'abc', 'media': 'zyz'}
    """
    namespaces = dict([
            node for _, node in ElementTree.iterparse(
                StringIO(xml_string), events=['start-ns']
            )
    ])
    return namespaces

def get_today():
    ny_times_home, schema = get_xml('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
    name_spaces = get_namespaces(schema)
    return parse(ny_times_home.getroot(), name_spaces)

# Using a CMD tool to see today's news
if __name__ == "__main__":
    articles = get_today()
    print(articles)