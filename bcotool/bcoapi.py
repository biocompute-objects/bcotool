#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#BCO API operations
'''API tools for BioCompute Objects.'''

__version__="1.1.0"
__status__ = "Production"

import bcoutils

#______________________________________________________________________________#
def usr_args():
    """
    functional arguments for process
    https://stackoverflow.com/questions/27529610/call-function-based-on-argparse
    """

    # initialize parser
    parser = argparse.ArgumentParser()

    # set usages options
    parser = argparse.ArgumentParser(
            prog='bcoapi',
            usage='%(prog)s [options]')

    # version
    parser.add_argument(
            '-v', '--version',
            action='version',
            version='%(prog)s ' + __version__)

    # create subparser objects
    subparsers = parser.add_subparsers()

    # Create parent subparser. Note `add_help=False` & creation via `argparse.`
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('-b', '--bco',
            required = True,
            help = "BioCompute json to process")
#______________________________________________________________________________#

#______________________________________________________________________________#
def main():
    """
    Main function
    """

    usr_args()