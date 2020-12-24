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
from jsonschema import validate
from optparse import OptionParser
from optparse import OptionGroup

__version__="1.0"
__status__ = "Dev"

#______________________________________________________________________________#
def usr_args():
    """
    functional arguments for process
    https://stackoverflow.com/questions/27529610/call-function-based-on-argparse
    """

    parser = argparse.ArgumentParser()


    parser = argparse.ArgumentParser(
            prog='bco', 
            usage='%(prog)s [options]')

    parser.add_argument(
            '-v', '--version', 
            action='version', 
            version='%(prog)s ' + __version__)

    # create subparser objects
    subparsers = parser.add_subparsers()

    # Create a validate subcommand    
    parser_validate = subparsers.add_parser('validate', 
            help = "Validation options. "
            "Used to test a BCO against a JSON schema. "
            "If no schema is supplied the ieee-2791-schema is used as the"
            "default")

    parser_validate.add_argument('-b', '--bco',  
            required = True,
            type = argparse.FileType('r'), 
            help = "json to validate")

    parser_validate.add_argument('-s', '--schema',
            help="root json schema to validate against")

    parser_validate.set_defaults(func=validate_bco)

    # Create a run_CWL subcommand       
    parser_run_CWL = subparsers.add_parser('run_CWL', 
            help='run a CWL ')

    parser_run_CWL.add_argument('-b', '--bco',  
            required = True,
            type = argparse.FileType('r'), 
            help = "json to extract CWL from")


    parser_run_CWL.set_defaults(func=run_CWL)

    # Create a listapps subcommand       
    parser_listapps = subparsers.add_parser('functions', 
            help='list all available functions')

    parser_listapps.set_defaults(func=listapps)

    # Print usage message if no args are supplied.
    if len(sys.argv) <= 1:
      sys.argv.append('--help')

    options = parser.parse_args()
    # Run the appropriate function 
    options.func(options)

    # If you add command-line options, consider passing them to the function,
    # e.g. `options.func(options)`
  
#______________________________________________________________________________#
def run_CWL( options ):
    """
    run a CWL 
    """

    os.system('mkdir cwl_run')
    data = options.bco.read()
    bco_dict = json.loads(data)
    bco_scripts = bco_dict['execution_domain']['script']
    bco_inputs = bco_dict['io_domain']['input_subdomain']

    for script in bco_scripts:
        uri = script['uri']['uri']
        script = os.popen('curl '+ uri).read()
        script_name = 'cwl_run/'+str(uri.split('/')[-1])
        with open( script_name, 'w' ) as file:
            file.write(script)
        os.system('cwltool --validate ' + script_name)
    
    for infile in bco_inputs:
        uri = infile['uri']['uri']
        print(uri)
        infile = os.popen('curl '+ uri).read()
        infile_name = 'cwl_run/'+str(uri.split('/')[-1])
        with open( infile_name, 'w' ) as file:
            file.write(infile)

    os.system('cwltool cwl_run/blastn-homologs.cwl --database cwl_run/HepC-DB.fasta --query cwl_run/M67463-HepC.fa')
    #     os.system('cwltool --validate ' + script_name)
    # os.system('cwltool ')


#______________________________________________________________________________#
def listapps( options ):
    """
    
    """
    argparse.ArgumentParser().print_help()

#______________________________________________________________________________#
def validate_bco( options ):
    """
    Validation of a BioCompute Object.
    """

    data = options.bco.read()
    bco_dict = json.loads(data)

    if options.schema is not None:
        base_uri = 'file://{}/'.format(os.path.dirname(args.schema.name))
        schema = jsonref.load(schema, base_uri=base_uri, jsonschema=True)
    else:
        schema = jsonref.load_uri('https://opensource.ieee.org/2791-object/ieee-2791-schema/-/raw/master/2791object.json')
    print("Schema: ", schema['title'])
    print("BioCompute Object: ", bco_dict['provenance_domain']['name'])
    validate(bco_dict, schema)

    print("BCO is valid against Schema")
#______________________________________________________________________________#
def main():
    """
    some text
    """

    usr_args()

#______________________________________________________________________________#
if __name__ == "__main__":
    main()