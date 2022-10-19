import unittest
from unittest.mock import patch
from xml.etree.ElementTree import ElementTree, fromstring
from feed.articles.NewsArticleImage import NewsArticleImage
from os.path import abspath
from feed.sources.nytimes import get_home
# from feed.utils.request import get_xml


# class Mock
mock_xml_file = abspath('./tests/sources/data.xml')
with open(mock_xml_file) as f:
    mock_xml_raw = f.read()

class NyTimesTest(unittest.TestCase):


    @patch('feed.utils.request.get_xml')
    def test_get_home(self, get_mock):  
        mock_xml_tree = ElementTree(fromstring(mock_xml_raw))
        get_mock.return_value = mock_xml_tree, mock_xml_raw
        # self.assertEqual(len(result.getroot()), 2)

        articles = get_home()
        first_article = articles[0]
        self.assertEqual(first_article.title, "Poll Shows Voters See Democracy in Peril, but Saving It Isn’t a Priority")
        self.assertEqual(first_article.link, "https://www.nytimes.com/2022/10/18/us/politics/midterm-election-voters-democracy-poll.html")
        self.assertEqual(first_article.categories, ["Project Democracy", "Polls and Public Opinion", "Voting and Voters", "Democratic Party", "Republican Party", "Midterm Elections (2022)", "Democracy (Theory and Philosophy)", "United States Politics and Government", "Presidential Election of 2020", "Rumors and Misinformation"])
        self.assertEqual(first_article.categories, ["Project Democracy", "Polls and Public Opinion", "Voting and Voters", "Democratic Party", "Republican Party", "Midterm Elections (2022)", "Democracy (Theory and Philosophy)", "United States Politics and Government", "Presidential Election of 2020", "Rumors and Misinformation"])
        self.assertEqual(first_article.description, "A New York Times/Siena College poll found that other problems have seized voters’ focus — even as many do not trust this year’s election results and are open to anti-democratic candidates.")
        self.assertEqual(first_article.written_by, "Nick Corasaniti, Michael C. Bender, Ruth Igielnik and Kristen Bayrakdarian")
        self.assertEqual(first_article.image, NewsArticleImage(
            "https://static01.nyt.com/images/2022/10/17/us/oct-poll-comfortable-voting-election-denier-promo/oct-poll-comfortable-voting-election-denier-promo-moth.png",
            "",
            ""
        ))
        self.assertEqual(first_article.published_on, "Tue, 18 Oct 2022 07:00:13 +0000")
if __name__ == "__main__":
    unittest.main()