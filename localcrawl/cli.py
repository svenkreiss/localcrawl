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
    parser.add_argument('--run', default=None, nargs=argparse.REMAINDER,
                        help='run a background process')
    parser.add_argument('--run-delay', default=3.0, type=float,
                        help='wait after run process')
    parser.add_argument('--flat-output', default=False, action='store_true',
                        help='outputs are flat files (more robust)')
    parser.add_argument('--output-encoding', default=None,
                        help='output encoding')
    args = parser.parse_args()

    logging.basicConfig(level=logging.WARNING)
    Crawler(args.start, args.out, max_depth=args.depth,
            run=args.run, run_delay=args.run_delay,
            get_pdf=args.pdf, flat_output=args.flat_output,
            output_encoding=args.output_encoding).crawl()
