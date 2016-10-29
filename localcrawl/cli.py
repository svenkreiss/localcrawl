"""Crawl and render JavaScript templates."""

from .crawler import Crawler
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--start', default='_build/index.html',
                        help='start url or file')
    parser.add_argument('-o', '--out', default='_crawled/',
                        help='output directory')
    parser.add_argument('--depth', default=3, type=int,
                        help='depth of the crawl')
    parser.add_argument('--pdf', default=False, action='store_true',
                        help='also store a PDF version')
    args = parser.parse_args()

    logging.basicConfig(level=logging.WARNING)
    Crawler(args.start, args.out,
            max_depth=args.depth, get_pdf=args.pdf).crawl()
