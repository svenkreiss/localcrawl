from .scraper import Scraper
import hashlib
import io
import logging
import os
import string
import subprocess
import time

FILEPATH_CHARS = '/-_.()# {}{}'.format(string.ascii_letters, string.digits)
log = logging.getLogger(__name__)


class Crawler(object):
    def __init__(self, start, out='_crawled/', max_depth=3,
                 force_url_prefix=None, run=None, run_delay=3.0,
                 get_pdf=False, scraper=None, flat_output=False,
                 output_encoding=None):
        start = self.absolute_path(start)
        self.urls = [(start, 0)]
        self.out = out
        self.max_depth = max_depth
        self.force_url_prefix = force_url_prefix or self.guess_prefix(start)
        self.run = run
        self.run_delay = run_delay
        self.get_pdf = get_pdf
        self.scraper = scraper or Scraper()
        self.flat_output = flat_output
        self.output_encoding = output_encoding

        self.done = set()

    def absolute_path(self, path):
        if '://' in path:
            return path
        if os.path.isfile(path):
            return 'file://{}'.format(os.path.abspath(path))
        return path

    def guess_prefix(self, path):
        if path.startswith('http'):
            path = self.complete_url(path)
        base, sep, _ = path.rpartition('/')
        return base + sep

    def complete_url(self, url):
        if url.endswith('/'):
            return url + 'index.html'
        if url[-1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return url + '/index.html'
        if '.' not in url.rpartition('/')[2]:
            return url + '/index.html'
        return url

    def crawl(self):
        count = 0
        process = None
        if self.run:
            process = subprocess.Popen(self.run)
            time.sleep(self.run_delay)

        while self.urls:
            url, depth = self.urls.pop(0)
            log.debug('============== {} ({}) ============'.format(url, depth))

            complete_url = self.complete_url(url)
            if complete_url in self.done:
                log.debug('{} already crawled.'.format(complete_url))
                continue
            if not complete_url.startswith(self.force_url_prefix):
                log.warn('{} outside of {}.'.format(complete_url,
                                                    self.force_url_prefix))
                continue

            crawled = self.crawl_page(complete_url)
            if crawled is None:
                continue

            if depth < self.max_depth:
                self.urls += [(lurl, depth + 1) for lurl in crawled]

            count += 1

        if process is not None:
            process.terminate()

        return count

    def crawl_page(self, url):
        log.debug('Crawl url: {}'.format(url))
        html = self.scraper.html(url)
        if not html:
            log.warn('Invalid {}. Skipping.'.format(url))
            return None

        filename = ''.join(c
                           for c in url[len(self.force_url_prefix):]
                           if c in FILEPATH_CHARS)
        if self.flat_output:
            md5 = hashlib.md5(html.encode()).hexdigest()
            filename = '{}.html'.format(md5)

        path = os.path.abspath(os.path.join(self.out, filename))
        if not path.startswith(os.path.abspath(self.out)):
            log.warn('Path {} is outside of {}. Skipping.'
                     ''.format(path, self.out))
            return None
        log.debug('Writing file: {}'.format(path))
        dirname = os.path.dirname(path)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        with io.open(path, 'w', encoding=self.output_encoding) as f:
            f.write(html)
        if self.get_pdf:
            self.scraper.pdf(url, path.replace('.html', '') + '.pdf')
        self.done.add(url)

        return self.scraper.link_urls(url)
