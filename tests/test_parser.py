import unittest
from unittest import MagickMock
from pathlib import Path
from bs4 import BeautifulSoup
from src.parser import ForumParser
from src.loader import PageLoader

FIXTURE = Path(__file__).parent / 'fixtures' / 'page.html'

class TestParser(unittest.TestCase):

    def setUp(self):
        self.page = FIXTURE.read_text(encoding='utf-8')
        self.loader = MagickMock(spec=PageLoader)
        self.loader.get_page.return_value = BeautifulSoup(self.page, 'lxml')
        self.parser = ForumParser(repository=self.repo, loader=self.loader)

    def test_parse_comments(self):
        res = self.parser.parse_page('')
        self.assertEqual(len(res), 5)