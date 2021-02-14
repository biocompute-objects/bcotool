#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
                        ##bco-toold##
'''CLI tools for BioCompute Objects.'''
################################################################################

__version__="1.1.0"
__status__ = "Production"

import os
import io
import sys
import json
import argparse
from pathlib import Path

import requests
import jsonschema
import jsonref
import functions

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
            help = "BioCompute json to process")

    parent_parser.add_argument('-s', '--schema',
            # type = argparse.FileType('r'),
            help = "root json schema to validate against")

    # Create a functions subcommand
    parser_listapps = subparsers.add_parser('functions',
            help='list all available functions')
    parser_listapps.set_defaults(func=listapps)

    # Create the bco_license
    parser_license = subparsers.add_parser('license',
            parents = [parent_parser],
            help = 'Prints BCO License ')
    parser_license.set_defaults(func=bco_license)

    # Create a validate subcommand
    parser_validate = subparsers.add_parser('validate',
            parents = [parent_parser],
            help = "Validation options. "
            "Used to test a BCO against a JSON schema. "
            "If no schema is supplied the ieee-2791-schema is used as the "
            "default")
    parser_validate.set_defaults(func=validate_bco)

    # Create a run_cwl subcommand
    parser_run_cwl = subparsers.add_parser('run_cwl',
            parents = [parent_parser],
            help = 'run a CWL ')
    parser_run_cwl.set_defaults(func=run_cwl)

    # Print usage message if no args are supplied.
    if len(sys.argv) <= 1:
        sys.argv.append('--help')

    # Run the appropriate function
    options = parser.parse_args()
    if parser.parse_args().func is listapps:
        options.func( parser )
    else:
        options.func(options)
#______________________________________________________________________________#

#______________________________________________________________________________#

#______________________________________________________________________________#
def listapps( parser ):
    """
    List all functions and options available in app
    https://stackoverflow.com/questions/7498595/python-argparse-add-argument-to-multiple-subparsers
    """

    print('Function List')
    subparsers_actions = [
        # pylint: disable=protected-access
        action for action in parser._actions
        # pylint: disable=W0212
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
def bco_license( options ):
    """
    Prints BCO bco_license
    """

    bco_dict = load_bco(options.bco)
    bco_license_obj = bco_dict['provenance_domain']['license']

    # checks if bco_license is valid URL
    if url_valid(bco_license_obj) is True:
        bco_license_name = str(bco_license_obj.split('/')[-1])
        bco_license_content = os.popen('curl '+ bco_license_obj).read()
    else:
        bco_license_content = str(bco_dict['provenance_domain']['license'])

    # write to file
    with open(bco_license_name, 'w+') as file:
        file.write(bco_license_content)

    print('BCO bco_license written to '+ bco_license_name)
    return bco_license_content
#______________________________________________________________________________#
def run_cwl( options ):
    """
    run a CWL
    """

    Path('cwl_run').mkdir(parents=True, exist_ok=True)

    bco_dict = load_bco(options.bco)
    bco_scripts = bco_dict['execution_domain']['script']
    bco_inputs = bco_dict['io_domain']['input_subdomain']

    # load scripts via URL and write to local directory
    for script in bco_scripts:
        uri = script['uri']['uri']
        script = os.popen('curl '+ uri).read()
        script_name = 'cwl_run/'+str(uri.split('/')[-1])
        with open( script_name, 'w' ) as file:
            file.write(script)

        # Identify YAML file for cli
        if script_name.split('.')[-1] == 'yml':
            input_yaml = ' ' + script_name

        # Check for file type before cwltool validation
        if script_name.split('.')[-1] == 'cwl':
            print("CWL File")

            # Find the Workflow definition and assign to variable
            with open ( script_name, 'r' ) as file:
                if file.readline().rstrip() == 'class: Workflow':
                    workflow_definition = ' ' + script_name

            # run cwltool validation via cli
            os.system('cwltool --validate ' + script_name)

    # Download input files parsed from BCO
    for infile in bco_inputs:
        uri = infile['uri']['uri']
        print(uri)
        infile = os.popen('curl '+ uri).read()
        infile_name = 'cwl_run/'+str(uri.split('/')[-1])
        with open( infile_name, 'w' ) as file:
            file.write(infile)

    # Run cwltool command
    os.popen('cwltool' + workflow_definition + input_yaml).read()
#______________________________________________________________________________#
def validate_bco( options ):
    """
    # Check for schema compliance.
    # Arguments
    # ---------
    # object_pass:  the object being checked.
    # Check the object against the provided schema.
    """

    error_flags = 0
    error_strings = ''
    bco_dict = functions.load_bco(options.bco)

    if options.schema is None:
        try:
            schema = jsonref.load_uri(bco_dict['spec_version'])
            print("Loaded Schema: ", schema['title'], ' from ', bco_dict['spec_version'] )

        except KeyError:
            print('Failed to load the provided Schema OR none was provided.' \
            + ' Using default instead')
            schema = jsonref.load_uri(str('https://opensource.ieee.org/2791-object'\
                                + '/ieee-2791-schema/-/raw/master/2791object.json'))

        except json.decoder.JSONDecodeError:
            print('Failed to load the provided Schema OR none was provided.' \
            + ' Using default instead')
            schema = jsonref.load_uri(str('https://opensource.ieee.org/2791-object'\
                                + '/ieee-2791-schema/-/raw/master/2791object.json'))
            print("Loaded default schema: ", schema['title'])
            print("BioCompute Object: ", bco_dict['provenance_domain']['name'])

        except ValueError:
            print('Failed to load the provided Schema OR none was provided.' \
            + ' Using default instead')
            schema = jsonref.load_uri(str('https://opensource.ieee.org/2791-object'\
                                + '/ieee-2791-schema/-/raw/master/2791object.json'))

    else:
        if os.path.exists(options.schema):
            base_uri = 'file://{}/'.format(os.path.dirname \
                        (os.path.abspath(options.schema.name)))
            print(base_uri)
            schema = jsonref.load \
                        (options.schema, base_uri=base_uri, jsonschema=True)
            try:
                print("Schema: ", schema['title'])
                print("File location: ", base_uri)
                print("BioCompute Object: ", bco_dict['provenance_domain']['name'])

            except json.decoder.JSONDecodeError:
                pass

        elif url_valid(options.schema):
            try:
                schema = jsonref.load_uri(options.schema)
                print("Loaded Schema: ", schema['title'], ' from ', options.schema )

            except json.decoder.JSONDecodeError:
                print('Failed to load the provided Schema.' \
                + ' Using default instead')
                schema = jsonref.load_uri(str('https://opensource.ieee.org/2791-object'\
                                    + '/ieee-2791-schema/-/raw/master/2791object.json'))

    error_string, error_flag = bco_validator(schema, bco_dict)
    error_flags += error_flag
    error_strings += error_string

    if 'extension_domain' in bco_dict.keys():
        for extension in bco_dict['extension_domain']:
            error_string, error_flag = validate_extension(extension)
            error_flags += error_flag
            error_strings += error_string

    if error_flags == 0:
        print('BCO VALID \U0001F389')

    else:
        with open ('error.log', 'w') as file:
            file.write(error_strings)
        print('Encountered', error_flags, 'errors while validating. \U0001F61E' \
            + '\n See "error.log" for more detail')
#______________________________________________________________________________#
def validate_extension ( extension ):
    """
    Validation of the extension domain if one is included.
    """

    error_flag = 0
    error_string = ''

    if isinstance(extension, dict):
        try:
            schema = jsonref.load_uri(extension['extension_schema'])
            try:
                print("Loaded Extension Schema: ", schema['title'] )
                name = schema['title']
                error_string, error_flag = bco_validator(schema, extension)

            # For if the schema has no ['title']
            except KeyError:
                print("Loaded Extension Schema: ", schema['$id'] )
                name = schema['$id']

        except json.decoder.JSONDecodeError:
            print('Failed to load extension schema', schema['$id'])
            error_flag += 1

        except TypeError:
            print('Failed to load extension schema. \nInvalid format ', )
            print(extension)
            error_string += json.dumps(extension)
            error_flag += 1

    else:
        print('Invalid BCO extension format')
        error_string += json.dumps(extension)
        error_flag = 1


    if error_flag == 0:
        print(name + ' PASSED \U0001F44D')
    return error_string, error_flag
#______________________________________________________________________________#
def bco_validator ( schema, bco_dict ):
    """
    Generalized JSON validation script
    """

    # Define a validator.
    validator = jsonschema.Draft7Validator(schema)

    # Define the errors list.
    errors = validator.iter_errors(bco_dict)
    error_string = ''

    # We have to use a bit of tricky output re-direction,
    # see https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-variable-in-python

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    # We ALSO have to use a bit of tricky flagging to indicate
    # that there were errors since generators can't use the norma len(list(generator)) idiom.
    error_flag = 0

    for exp in errors:

        # There is at least 1 error.
        error_flag += 1

        print(exp)
        print('===============================================================')

    error_string = error_string + new_stdout.getvalue()
    sys.stdout = old_stdout

    # Return based on whether or not there were any errors.
    # if error_flag != 0:
    #
    #     print('\nSchema failure with given payload. ' \
    #         + 'This message will only show up in the terminal.')

    # Collapse and return the errors.
    return error_string, error_flag
#______________________________________________________________________________#
def main():
    """
    Main function
    """

    usr_args()

#______________________________________________________________________________#
if __name__ == "__main__":
    main()
