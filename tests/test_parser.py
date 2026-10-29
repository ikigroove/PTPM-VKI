import unittest
from unittest.mock import MagicMock
from pathlib import Path
from bs4 import BeautifulSoup
from src.parser import ForumParser
from src.loader import PageLoader
from src.database import DatabaseRepository



class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        fixture_path = Path(__file__).parent / 'fixtures' / 'page.html'

        with open(fixture_path, 'r', encoding='utf-8') as f:
            cls.mock_html = f.read()

    def setUp(self):
        self.page = self.mock_html
        self.repository = DatabaseRepository(':memory:')
        self.loader = MagicMock(spec=PageLoader)
        self.parser = ForumParser(repository=self.repository, loader=self.loader)

    def test_parse_comments(self):
        self.loader.get_page.return_value = BeautifulSoup(self.page, 'lxml')
        res = self.parser.parse_page('')
        self.assertEqual(len(res), 5)

    def test_parse_empty_page(self):
        self.loader.get_page.return_value = BeautifulSoup('<html><body></body></html>', 'lxml')
        res = self.parser.parse_page('')
        self.assertEqual(res, [])

if __name__ == '__main__':
    unittest.main()