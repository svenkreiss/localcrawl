from .scraper import Scraper
import logging
import os
import string

FILENAME_CHARS = '-_.() %s%s' % (string.ascii_letters, string.digits)
log = logging.getLogger(__name__)


class Crawler(object):
    def __init__(self, start, out='_crawled/', max_depth=3, scraper=None):
        self.urls = [(start, 0)]
        self.done = set()
        self.out = out
        self.max_depth = max_depth
        self.scraper = scraper or Scraper()

        if not os.path.isdir(self.out):
            os.makedirs(self.out)
        else:
            log.warn('Output directory already exists. Continuing.')

    def crawl(self):
        count = 0
        while self.urls:
            url, depth = self.urls.pop(0)
            if url in self.done:
                continue

            log.debug('Crawl url: {}'.format(url))
            html = self.scraper.html(url)

            filename = ''.join(c for c in url if c in FILENAME_CHARS)
            path = os.path.join(self.out, filename)
            with open(path, 'w') as f:
                f.write(html)
            self.done.add(url)
            count += 1

            if depth >= self.max_depth:
                continue

            self.urls += [(lurl, depth + 1)
                          for lurl in self.scraper.link_urls(url)]

        return count
