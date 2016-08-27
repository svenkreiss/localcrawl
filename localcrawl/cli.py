"""Crawl rendered JavaScript templates from a local server."""

import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start', default='_build/html/index.html',
                        help='start url or file')
    parser.add_argument('-o', '--out', default='_crawled/',
                        help='output directory')
    args = parser.parse_args()

