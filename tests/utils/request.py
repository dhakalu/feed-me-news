import unittest
from unittest.mock import patch
from feed.utils.request import get_xml

class MockRequestResponse:

    def __init__(self, text: str) -> None:
        self.text = text

class RequestUtilsTest(unittest.TestCase):

    @patch('requests.get')
    def test_get_xml(self, get_mock):
        xml_text = 'Hello!'
        expected_xml_str = f'<channel>{xml_text}</channel>'
        get_mock.return_value = MockRequestResponse(expected_xml_str)
        result, actual_xml_str = get_xml("http://example.com")
        self.assertEqual(result.getroot().text, xml_text)
        self.assertEqual(actual_xml_str, expected_xml_str)

if __name__ == "__main__":
    unittest.main()