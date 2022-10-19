import unittest
import xml.etree.ElementTree as ET
from feed.articles.NewsArticleImage import NewsArticleImage

class NyTimesTest(unittest.TestCase):

    def test_parse(self):        
        result = ET.parse("mock_nytimes.xml")
        assert(len(result) == 2)

        first_item = result[0]
        self.assertEqual(first_item.title, "Poll Shows Voters See Democracy in Peril, but Saving It Isn’t a Priority")
        self.assertEqual(first_item.link, "https://www.nytimes.com/2022/10/18/us/politics/midterm-election-voters-democracy-poll.html")
        self.assertEqual(first_item.categories, ["Project Democracy", "Polls and Public Opinion", "Voting and Voters", "Democratic Party", "Republican Party", "Midterm Elections (2022)", "Democracy (Theory and Philosophy)", "United States Politics and Government", "Presidential Election of 2020", "Rumors and Misinformation"])
        self.assertEqual(first_item.categories, ["Project Democracy", "Polls and Public Opinion", "Voting and Voters", "Democratic Party", "Republican Party", "Midterm Elections (2022)", "Democracy (Theory and Philosophy)", "United States Politics and Government", "Presidential Election of 2020", "Rumors and Misinformation"])
        self.assertEqual(first_item.description, "A New York Times/Siena College poll found that other problems have seized voters’ focus — even as many do not trust this year’s election results and are open to anti-democratic candidates.")
        self.assertEqual(first_item.written_by, "Nick Corasaniti, Michael C. Bender, Ruth Igielnik and Kristen Bayrakdarian")
        self.assertEqual(first_item.image, NewsArticleImage(
            "https://static01.nyt.com/images/2022/10/17/us/oct-poll-comfortable-voting-election-denier-promo/oct-poll-comfortable-voting-election-denier-promo-moth.png",
            "",
            ""
        ))
        self.assertEqual(first_item.published_on, "Tue, 18 Oct 2022 07:00:13 +0000")
if __name__ == "__main__":
    unittest.main()