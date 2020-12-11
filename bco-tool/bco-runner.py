#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

################################################################################
                        ##bco-toold##
'''reads text file and makes BCO.'''
################################################################################

import json
import jsonref
import os
import sys
import argparse
from optparse import OptionParser

__version__="1.0"
__status__ = "Dev"

#______________________________________________________________________________#
def arguments():
    """
    functional arguments for process
    """

    FUNCTION_MAP = {'top20' : my_top20_func,
                    'listapps' : my_listapps_func }

    parser.add_argument('command', choices=FUNCTION_MAP.keys())
    
    
#______________________________________________________________________________#
def options():
    """
    Command line options to be fed into each of the functions.
    #TODO will have to indicate which options can be used for which functions 
    """

    usage = "\n%prog  [options]"
    opt_parser = OptionParser(usage,version="%prog " + __version__)
    opt_parser.add_option('-j','--json', help="json to validate")
#    opt_parser.add_option('-schema', type=argparse.FileType('r'), help="root json schema to validate against")
    (options, args) = opt_parser.parse_args()
    # opt_parser.print_help()
#______________________________________________________________________________#
def validate():
    """
    validationo oof a BioCompute Object
    """
#______________________________________________________________________________#
def main():
    """
    some text
    """

    options()
    
#______________________________________________________________________________#
if __name__ == "__main__":
    main()