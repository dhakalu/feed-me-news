import requests
import xml.etree.ElementTree as ET

def get_xml(url):
    content =  requests.get(url).text
    return ET.fromstring(content)
