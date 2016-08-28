import selenium.webdriver
import time


class Scraper(object):
    def __init__(self, driver=None, sleep=0.1):
        self.driver = driver or selenium.webdriver.PhantomJS()
        self.sleep = sleep
        self._current_url = None
        self._invalid = True

    def _get(self, url):
        if url == self._current_url:
            return

        self._current_url = url
        old_source = self.driver.page_source
        self.driver.get(url)
        time.sleep(self.sleep)
        self._invalid = old_source == self.driver.page_source

    def html(self, url):
        self._get(url)
        if self._invalid:
            return ''
        return self.driver.page_source

    def link_urls(self, url):
        self._get(url)
        if self._invalid:
            return []
        links = self.driver.find_elements_by_tag_name('a')
        return [l.get_attribute('href') for l in links]
