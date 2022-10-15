import unittest
from unittest.mock import patch
from request_utils import get_xml

class MockRequestResponse:

    def __init__(self, text: str) -> None:
        self.text = text

class RequestUtilsTest(unittest.TestCase):

    @patch('requests.get')
    def test_get_xml(self, get_mock):
        xml_text = 'Hello!'
        get_mock.return_value = MockRequestResponse(f'<channel>{xml_text}</channel>')
        result = get_xml("http://example.com")
        assert(result.text == xml_text)

if __name__ == "__main__":
    unittest.main()