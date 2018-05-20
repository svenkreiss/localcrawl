import localcrawl
import os
import selenium.webdriver
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

    def test_index_chrome(self):
        chrome_options = selenium.webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        driver = selenium.webdriver.Chrome(chrome_options=chrome_options)

        c = localcrawl.Scraper(driver)
        url = 'file://' + os.getcwd() + '/tests/data/simple_site/index.html'
        html = c.html(url)
        self.assertIn('<title>Simple Site</title>', html)
