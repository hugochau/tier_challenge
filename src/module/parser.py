"""
parser.py

Defines Parser
"""

__version__ = '1.0'
__author__ = 'Hugo Chauvary'
__email__ = 'chauvary.hugo@gmail.com'

import argparse

from util.util import log_item


class Parser:
    @staticmethod
    @log_item
    def parse() -> dict:
        """
        Parse and validate CLI arguments

        returns:
            -dict: validated CLI arguments in a dictionary
        """
        # define parser
        description = 'CLI arguments parser for tier app'
        parser = argparse.ArgumentParser(description=description)

        # parse arguments
        parser.add_argument('filename',
                            help='the filename to load')
        args = parser.parse_args()

        return args
