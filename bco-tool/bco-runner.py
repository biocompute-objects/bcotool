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

    
#______________________________________________________________________________#
def options():
    """
    Command line options to be fed into each of the functions.
    #TODO will have to indicate which options can be used for which functions 
    """

    usage = "\n%prog  [options]"
    parser = OptionParser(usage,version="%prog " + __version__)
    parser.add_option('-j','--json', help="json to validate")
#    parser.add_option('-schema', type=argparse.FileType('r'), help="root json schema to validate against")
    (options, args) = parser.parse_args()
    # parser.print_help()
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