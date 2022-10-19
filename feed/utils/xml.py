from io import StringIO
from xml.etree import ElementTree

def extract_text_from_tag(element: ElementTree.Element, tag_name: str, name_space=None):
    """
    Extracts the text of the given tag. If the tag does not exist it returns empty string.

    Args:
        element: Element that contains the tag
        tag_name: name of the tag to extract text from
        name_space: XML namespaces for the given xml element

    Returns:
        Text with in the tag
    """
    value = element.find(tag_name, name_space)
    if value is None:
        return ''
    return value.text

def extract_text_from_attr(element: ElementTree.Element, attr_name: str):
    """
    Extracts the text of the given attribute. If the attribute does not exist it returns empty string.

    Args:
        element: Element that contains the tag
        attr_name: name of the attribute to extract text for

    Returns:
        Text with in the attribute
    """
    try:
        value = element.attrib.get(attr_name)
        if value is None:
           return ''
        return value
    except AttributeError:
        return ''

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