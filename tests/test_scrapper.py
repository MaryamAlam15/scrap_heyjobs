import unittest

from constants import HEYJOBS_JOB_URL
from scrapper import parse_page


class TestScrapper(unittest.TestCase):

    def setUp(self):
        self.web_link = HEYJOBS_JOB_URL

    def test_parse_page(self):
        uuids, titles = parse_page(self.web_link)

        self.assertIsNotNone(uuids)
        self.assertIsNotNone(titles)
