import requests
from xml.etree.ElementTree import fromstring, ElementTree

def get_xml(url):
    xml_string =  requests.get(url).text
    return ElementTree(fromstring(xml_string)), xml_string
