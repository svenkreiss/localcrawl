"""Crawl and render JavaScript templates."""

from .crawler import Crawler
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start', default='_build/index.html',
                        help='start url or file')
    parser.add_argument('-o', '--out', default='_crawled/',
                        help='output directory')
    parser.add_argument('--depth', default=3, type=int,
                        help='depth of the crawl')
    args = parser.parse_args()

    logging.basicConfig(level=logging.WARNING)
    Crawler(args.start, args.out, max_depth=args.depth).crawl()
