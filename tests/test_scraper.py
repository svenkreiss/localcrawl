import localcrawl
import unittest


class ScraperTest(unittest.TestCase):
    def test_index(self):
        c = localcrawl.Scraper()
        html = c.html('tests/data/simple_site/index.html')
        self.assertIn('<title>Simple Site</title>', html)

    def test_link(self):
        c = localcrawl.Scraper()
        html = c.html('tests/data/linked_page/index.html')
        self.assertIn('<title>Linked Page</title>', html)

        urls = c.link_urls('tests/data/linked_page/index.html')
        self.assertIn('page2.html', urls[0])
