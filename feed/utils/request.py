import requests
from xml.etree.ElementTree import fromstring, ElementTree
from bs4 import BeautifulSoup

def get_xml(url):
    xml_string =  requests.get(url).text
    return ElementTree(fromstring(xml_string)), xml_string

def get_soup(url):
    page = requests.get(url) 
    soup = BeautifulSoup(page.content, "html.parser")

