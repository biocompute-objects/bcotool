#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
                        ##bco-toold##
'''reads text file and makes BCO.'''
################################################################################

import os
import sys
import argparse
import json
import jsonref
from jsonschema import validate

__version__="1.0"
__status__ = "Dev"

#______________________________________________________________________________#
def usr_args():
    """
    functional arguments for process
    https://stackoverflow.com/questions/27529610/call-function-based-on-argparse
    https://stackoverflow.com/questions/7498595/python-argparse-add-argument-to-multiple-subparsers
    """

    # initialize parser
    parser = argparse.ArgumentParser()

    # set usages options
    parser = argparse.ArgumentParser(
            prog='bco',
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
            type = argparse.FileType('r'),
            help = "BioCompute json to process")

    # Create a validate subcommand
    parser_validate = subparsers.add_parser('validate',
            parents = [parent_parser],
            help = "Validation options. "
            "Used to test a BCO against a JSON schema. "
            "If no schema is supplied the ieee-2791-schema is used as the"
            "default")

    parser_validate.add_argument('-s', '--schema',
            type = argparse.FileType('r'),
            help = "root json schema to validate against")

    parser_validate.set_defaults(func=validate_bco)

    # Create a run_cwl subcommand
    parser_run_cwl = subparsers.add_parser('run_cwl',
            parents = [parent_parser],
            help = 'run a CWL ')

    parser_run_cwl.set_defaults(func=run_cwl)

    # Create a listapps subcommand
    parser_listapps = subparsers.add_parser('functions',
            help='list all available functions')

    parser_listapps.set_defaults(func=listapps)

    # Print usage message if no args are supplied.
    if len(sys.argv) <= 1:
        sys.argv.append('--help')

    # Run the appropriate function
    options = parser.parse_args()
    if parser.parse_args().func == listapps:
        options.func(options, parser)
    else:
        options.func(options)
    
    # If you add command-line options, consider passing them to the function,
    # e.g. `options.func(options)`

#______________________________________________________________________________#
def listapps( options, parser ):
    """
    hello
    """

    print('Function List')
    subparsers_actions = [
        action for action in parser._actions 
        if isinstance(action, argparse._SubParsersAction)]
    # there will probably only be one subparser_action,
    # but better safe than sorry
    for subparsers_action in subparsers_actions:
        # get all subparsers and print help
        for choice, subparser in subparsers_action.choices.items():
            print("Function: '{}'".format(choice))
            print(subparser.format_help())
    # print(parser.format_help())
#______________________________________________________________________________#
def load_bco( options ):
    """
    Import and parsing of a BioCompute Object.
    """

    data = options.bco.read()
    bco_dict = json.loads(data)
    print('BioCompute loaded as ', bco_dict['provenance_domain']['name'])
    print('BCO provided schema: ', bco_dict['spec_version'])

    return bco_dict
#______________________________________________________________________________#
def run_cwl( options ):
    """
    run a CWL
    """

    try:
        Path('cwl_run').mkdir(parents=True, exist_ok=True)
    except:
        Exception

    data = options.bco.read()
    bco_dict = json.loads(data)
    bco_scripts = bco_dict['execution_domain']['script']
    bco_inputs = bco_dict['io_domain']['input_subdomain']

    workflow_definition = bco_scripts[2]['uri']['uri']

    # for script in bco_scripts:
    #     uri = script['uri']['uri']
    #     script = os.popen('curl '+ uri).read()
    #     script_name = 'cwl_run/'+str(uri.split('/')[-1])
    #     with open( script_name, 'w' ) as file:
    #         file.write(script)
    #     with open ( script_name, 'r' ) as file:
    #         if file.readline().rstrip() == 'class: Workflow':
    #             workflow_definition = script_name
    #     os.system('cwltool --validate ' + script_name)

    # for infile in bco_inputs:
    #     uri = infile['uri']['uri']
    #     print(uri)
    #     infile = os.popen('curl '+ uri).read()
    #     infile_name = 'cwl_run/'+str(uri.split('/')[-1])
    #     with open( infile_name, 'w' ) as file:
    #         file.write(infile)

    os.popen('cwltool '+workflow_definition+' cwl_run/blastn-homologs.yml').read()
#______________________________________________________________________________#
def validate_bco( options ):
    """
    Validation of a BioCompute Object.
    """

    bco_dict = load_bco(options)

    if options.schema is not None:
        base_uri = 'file://{}/'.format(os.path.dirname \
                    (os.path.abspath(options.schema.name)))
        print(base_uri)
        schema = jsonref.load \
                    (options.schema, base_uri=base_uri, jsonschema=True)
        print("Schema: ", schema['title'])
        print("File location: ", base_uri)
        print("BioCompute Object: ", bco_dict['provenance_domain']['name'])

    else:
        try:
            schema = jsonref.load_uri(bco_dict['spec_version'])
            print("Loaded Schema: ", schema['title'], ' from ', )
        except:
            print('Failed to load the provided Schema. Using default instead')
            schema = jsonref.load_uri(str('https://opensource.ieee.org/2791-object'\
                                + '/ieee-2791-schema/-/raw/master/2791object.json'))
            print("Loaded default schema: ", schema['title'])
            print("BioCompute Object: ", bco_dict['provenance_domain']['name'])

    validate(bco_dict, schema)

    print("BCO is valid against Schema")
#______________________________________________________________________________#
def main():
    """
    Main function
    """

    usr_args()

#______________________________________________________________________________#
if __name__ == "__main__":
    main()
