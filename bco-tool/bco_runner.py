#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
##bco-toold##
'''CLI tools for BioCompute Objects.'''
################################################################################

__version__ = "1.1.0"
__status__ = "Production"

import os
import io
import sys
import json
import argparse
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from random import random
from urllib.parse import urlparse

import requests
import jsonschema
import jsonref
import re

"""
Default mapping that is used when no mapping file is provided
"""
default_mapping = {
    "bco_id": {
        "value": "object_id",
        "mode": "swap"
    },

    "bco_spec_version": {
        "value": "spec_version",
        "mode": "swap"
    },

    "checksum": {
        "value": "etag",
        "mode": "swap"
    },

    "sha1_chksum": {
        "value": "sha1_checksum",
        "mode": "swap"

    },

    "extension_domain": {
        "value": 'extension_domain',
        "mode": "delete"
    }
}


# ______________________________________________________________________________#
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
                               required=True,
                               help="BioCompute JSON to process.")

    parent_parser.add_argument('-s', '--schema',
                               # type = argparse.FileType('r'),
                               help="Root json schema to validate against.")

    parent_parser.add_argument('-m', '--mappingFile',
                               # type = argparse.FileType('r'),
                               help="Mapping file to convert BioCompute json with.")

    # Create a functions subcommand
    parser_listapps = subparsers.add_parser('functions',
                                            help='List all available functions.')
    parser_listapps.set_defaults(func=listapps)

    # Create the bco_license
    parser_license = subparsers.add_parser('license',
                                           parents=[parent_parser],
                                           help='Saves HTML version of BCO License.')
    parser_license.set_defaults(func=bco_license)

    # Create a validate subcommand
    parser_validate = subparsers.add_parser('validate',
                                            parents=[parent_parser],
                                            help="Validation options. "
                                                 "Used to test a BCO against a JSON schema. "
                                                 "If no schema is supplied the ieee-2791-schema "
                                                 "is used as the "
                                                 "default.")
    parser_validate.set_defaults(func=validate_bco)

    parser_validate = subparsers.add_parser('convert',
                                            parents=[parent_parser],
                                            help="Converting options "
                                                 "Used to convert a JSON into a schema (default "
                                                 "is ieee-2791-schema). If no mapping file is "
                                                 "provided, performs default conversions.")
    parser_validate.set_defaults(func=map_bcos)


    parser_validate = subparsers.add_parser('update',
                                            parents=[parent_parser],
                                            help="Update option"
                                                 "Updates last modified and etag on BCO. Updates modified time to current time.")
    parser_validate.set_defaults(func=update_bco)

    parser_validate = subparsers.add_parser('map',
                                            parents=[parent_parser],
                                            help="Mapping options "
                                                 "Used to generate a mapping file for a bco/bcos.")
    parser_validate.set_defaults(func=map_bcos)

    # Create a run_cwl subcommand
    parser_run_cwl = subparsers.add_parser('run_cwl',
                                           parents=[parent_parser],
                                           help='Run a CWL described in a BCO.')
    parser_run_cwl.set_defaults(func=run_cwl)

    # Print usage message if no args are supplied.
    if len(sys.argv) <= 1:
        sys.argv.append('--help')

    # Run the appropriate function
    options = parser.parse_args()
    if parser.parse_args().func is listapps:
        options.func(parser)
    else:
        options.func(options)


# ______________________________________________________________________________#
def load_bco(options):
    """
    Import of a BioCompute Object. Values can be a local file path or a URI.
    """

    # Declare source of BioCompute Object
    print('\nRemote BCO supplied: ', url_valid(options.bco), \
          '\t Local BCO supplied: ', os.path.exists(options.bco))

    if url_valid(options.bco):
        try:
            bco_dict = json.loads(requests.get(options.bco).content)
            print('Remote BioCompute loaded as ', bco_dict['provenance_domain']['name'])

        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            sys.exit('Loading remote JSON has failed \U0001F61E\nExiting')

    elif os.path.exists(options.bco):
        print(options.bco)
        try:
            with open(options.bco, 'r') as data:
                bco_dict = json.load(data)
            print('Local BioCompute loaded as ', bco_dict['provenance_domain']['name'])

        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            sys.exit("Importing local JSON has failed \U0001F61E\nExiting")

    # If options.bco is not a valid FILE or URI program will exit
    else:
        print('BioCompute loading FAILED \n')
        sys.exit("Please provide a valid URI or PATH")

    return bco_dict

# ______________________________________________________________________________#
def update_bco(options):
    new_bco = load_bco(options)
    try:
        new_bco['provenance_domain'][
            'modified'] = datetime.now().isoformat()  # change date to current

        temp_bco = dict(new_bco)
        del temp_bco['object_id'], temp_bco['etag'], temp_bco['spec_version']

        new_bco['spec_version'] = "https://w3id.org/ieee/ieee-2791-schema/2791object.json"
        new_bco["etag"] = sha256(json.dumps(temp_bco).encode('utf-8')).hexdigest()
    except KeyError:  # Vital field was missing, will be caught by final error checker
        pass
    file = open(options.bco, "w")
    json.dump(new_bco, file, indent=4)


# ______________________________________________________________________________#
def url_valid(url):
    """
    Validate a URL
    """

    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


# ______________________________________________________________________________#
def listapps(parser):
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


# ______________________________________________________________________________#
def bco_license(options):
    """
    Prints BCO bco_license
    """

    bco_dict = load_bco(options)
    bco_license_obj = bco_dict['provenance_domain']['license']

    # checks if bco_license is valid URL
    if url_valid(bco_license_obj) is True:
        bco_license_name = str(bco_license_obj.split('/')[-1])
        bco_license_content = os.popen('curl ' + bco_license_obj).read()
    else:
        bco_license_content = str(bco_dict['provenance_domain']['license'])

    # write to file
    with open(bco_license_name, 'w+') as file:
        file.write(bco_license_content)

    print('BCO bco_license written to ' + bco_license_name)
    return bco_license_content


# ______________________________________________________________________________#
def run_cwl(options):
    """
    run a CWL
    """

    Path('cwl_run').mkdir(parents=True, exist_ok=True)

    bco_dict = load_bco(options)
    bco_scripts = bco_dict['execution_domain']['script']
    bco_inputs = bco_dict['io_domain']['input_subdomain']

    # load scripts via URL and write to local directory
    for script in bco_scripts:
        uri = script['uri']['uri']
        script = os.popen('curl ' + uri).read()
        script_name = 'cwl_run/' + str(uri.split('/')[-1])
        with open(script_name, 'w') as file:
            file.write(script)

        # Identify YAML file for cli
        if script_name.split('.')[-1] == 'yml':
            input_yaml = ' ' + script_name

        # Check for file type before cwltool validation
        if script_name.split('.')[-1] == 'cwl':
            print("CWL File")

            # Find the Workflow definition and assign to variable
            with open(script_name, 'r') as file:
                if file.readline().rstrip() == 'class: Workflow':
                    workflow_definition = ' ' + script_name

            # run cwltool validation via cli
            os.system('cwltool --validate ' + script_name)

    # Download input files parsed from BCO
    for infile in bco_inputs:
        uri = infile['uri']['uri']
        print(uri)
        infile = os.popen('curl ' + uri).read()
        infile_name = 'cwl_run/' + str(uri.split('/')[-1])
        with open(infile_name, 'w') as file:
            file.write(infile)

    # Run cwltool command
    os.popen('cwltool' + workflow_definition + input_yaml).read()


# ______________________________________________________________________________#
def validate_bco(options):
    """
    # Check for schema compliance.
    # Arguments
    # ---------
    # object_pass:  the object being checked.
    # Check the object against the provided schema.
    """

    error_flags = 0
    error_strings = ''
    bco_dict = load_bco(options)

    if options.schema is None:
        try:
            schema = jsonref.load_uri(bco_dict['spec_version'])
            print("Loaded Schema: ", schema['title'], ' from ', bco_dict['spec_version'])

        except KeyError:
            print('Failed to load the provided Schema OR none was provided.' \
                  + ' Using default instead')
            schema = jsonref.load_uri(str('https://opensource.ieee.org/2791-object' \
                                          + '/ieee-2791-schema/-/raw/master/2791object.json'))

        except json.decoder.JSONDecodeError:
            print('Failed to load the provided Schema OR none was provided.' \
                  + ' Using default instead')
            schema = jsonref.load_uri(str('https://opensource.ieee.org/2791-object' \
                                          + '/ieee-2791-schema/-/raw/master/2791object.json'))
            print("Loaded default schema: ", schema['title'])
            print("BioCompute Object: ", bco_dict['provenance_domain']['name'])

        except ValueError:
            print('Failed to load the provided Schema OR none was provided.' \
                  + ' Using default instead')
            schema = jsonref.load_uri(str('https://opensource.ieee.org/2791-object' \
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
                print("Loaded Schema: ", schema['title'], ' from ', options.schema)

            except json.decoder.JSONDecodeError:
                print('Failed to load the provided Schema.' \
                      + ' Using default instead')
                schema = jsonref.load_uri(str('https://opensource.ieee.org/2791-object' \
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
        try:
            os.remove("error.log")
        except OSError:
            pass


    else:
        with open('error.log', 'w') as file:
            file.write(error_strings)
        print('Encountered', error_flags, 'errors while validating. \U0001F61E' \
              + '\n See "error.log" for more detail')


# ______________________________________________________________________________#
def validate_extension(extension):
    """
    Validation of the extension domain if one is included.
    """

    error_flag = 0
    error_string = ''

    if isinstance(extension, dict):
        try:
            schema = jsonref.load_uri(extension['extension_schema'])
            try:
                print("Loaded Extension Schema: ", schema['title'])
                name = schema['title']
                error_string, error_flag = bco_validator(schema, extension)

            # For if the schema has no ['title']
            except KeyError:
                print("Loaded Extension Schema: ", schema['$id'])
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


# ______________________________________________________________________________#
def bco_validator(schema, bco_dict):
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
        error_flag = 1

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


# ______________________________________________________________________________#
def convert_schema(bco, filename, mapping_dict):
    """
    Converts a BCO dict according to a mapping_dict, and writes the result at filename

    :param bco: BCO to convert
    :type bco: dict
    :param filename: name of file to write converted BCO to
    :type filename: str
    :param mapping_dict: dictionary containing value mapping for bco
    :type mapping_dict: dict
    """
    for item in mapping_dict['to_swap']:
        value_list = mapping_dict['to_swap'][item]
        for i in range(0, len(value_list)):
            rename_dict_key_HELPER(bco, value_list[i]['index'],
                                   value_list[i]['value'])  # Change key name

    for item in mapping_dict['to_delete']:
        value_list = mapping_dict['to_delete'][item]
        for i in range(0, len(value_list)):
            delete_key_HELPER(bco, value_list[i]['index'], value_list[i]['value'])  # delete key

    for item in mapping_dict['to_add']:
        value_list = mapping_dict['to_add'][item]
        for i in range(0, len(value_list)):
            set_key_in_dict_HELPER(bco, value_list[i]['index'], value_list[i]['value'])  # add key

    new_bco = bco
    try:
        new_bco['provenance_domain'][
            'modified'] = datetime.now().isoformat()  # change date to current

        temp_bco = dict(new_bco)
        del temp_bco['object_id'], temp_bco['etag'], temp_bco['spec_version']

        new_bco['spec_version'] = "https://w3id.org/ieee/ieee-2791-schema/2791object.json"
        new_bco["etag"] = sha256(json.dumps(temp_bco).encode('utf-8')).hexdigest()
    except KeyError:  # Vital field was missing, will be caught by final error checker
        pass
    file = open(filename, "w")
    json.dump(new_bco, file, indent=4)


# ______________________________________________________________________________#
def create_master_mapping_file(options, bcos_to_map):
    """
    Takes a list of bco's and creates a master mapping file

    :param options: tool options
    :type options: dict
    :param bcos_to_map: list of bco names
    :type bcos_to_map: list
    """
    mapping_dict = {
        "missing": {

        },

        "additional": {

        }
    }

    for bco in bcos_to_map:

        filename = os.path.splitext(bco)[0] + "mapping.txt"

        options.bco = bco
        create_mapping_file(options)

        addition_mode = False

        with open(filename) as mapping_file:
            for line in mapping_file:
                if line.startswith("#"):  # Skip comments explaining mapping file
                    continue
                if line.startswith("===="):  # Switch modes. Starts false -> true -> false
                    addition_mode = not addition_mode
                    continue
                key_path = line.split("-->")[0]
                value = line.split("-->")[1].strip(":")

                if addition_mode:
                    if key_path not in mapping_dict["missing"]:
                        mapping_dict["missing"][key_path] = [value, [bco]]
                    else:
                        mapping_dict["missing"][key_path][1].append(bco)
                else:
                    if key_path not in mapping_dict["additional"]:
                        mapping_dict["additional"][key_path] = [value, [bco]]
                    else:
                        mapping_dict["additional"][key_path][1].append(bco)
        os.remove(filename)


    with open("mastermappingfile.txt", "w") as masterfile:  # write dict to
        # single file with
        masterfile.writelines(
"""# Use this file to provide mapping values for multiple bcos.
# fill out the values for each bco listed.
# MISSING PROPERTIES/FIELDS lists properties/fields that are missing from bco
# NONALLOWED PROPERTIES/FIELDS shows properties that are not allowed
# Syntax for specifying values
# To delete a value
# PATH --> FIELD: DELETE
# To add a value
# PATH --> FIELD: ADD-value_to_add
# To rename a field name
# PATH --> FIELD: RENAME-new_field_name
# To swap a field name with another current field name
# PATH --> FIELD: SWAP-other_field_name
# Blank values will be skipped. Data does not need to be double represented
# For example, 
# if <bco_id> needs renamed to <object_id>, either
# ['object_id'] --> object_id: 
# SWAP-bco_id
# OR 
# ['bco_id'] -->  bco_id: RENAME:object_id 
# will work. No need to fill out both values.
""")
        masterfile.write("====MISSING PROPERTIES/FIELDS=====\n")
        for key in mapping_dict["missing"]:
            attribute = mapping_dict["missing"][key]
            value = attribute[0]

            masterfile.write(key + "-->" + value)
            for bco_name in attribute[1]:
                masterfile.write("     " + os.path.basename(bco_name) + ":\n")
            masterfile.write("-----------------------\n")
        masterfile.write("=====ADDITONAL PROPERTIES/FIELDS=====\n")
        for key in mapping_dict["additional"]:
            attribute = mapping_dict["additional"][key]
            value = attribute[0]
            masterfile.write(key + "-->" + value)
            for bco_name in attribute[1]:
                masterfile.write("     " + os.path.basename(bco_name) + ":\n")
            masterfile.write("-----------------------\n")


# ______________________________________________________________________________#
def parse_master_mapping_file(master_mapping_file, bcos):
    """
    Parses a mastering mapping file into individual mapping files for each
    bco in bcos.

    :param master_mapping_file: name of master mapping file to parse
    :type master_mapping_file: str
    :param bcos: list of bco names in master mapping file
    :type bcos: string list
    :return: list containing new filenames of mapping files
    :rtype: string list
    """
    bco_names = []

    mapping_dict = {
    }

    for bco in bcos:
        bco_names.append(os.path.splitext(os.path.basename(bco))[0])
        mapping_dict[os.path.splitext(os.path.basename(bco))[0]] = {
            "missing": {

            },
            "additional": {
            }
        }
    addition_mode = False
    with open(master_mapping_file, 'r') as mapping_file:
        for line in mapping_file:
            if line.startswith("#"):  # skip comments
                continue
            if line.startswith("===="):
                addition_mode = not addition_mode  # switch mode when header is reached
                continue
            path = line.split("-->")[0]
            value = line.split("-->")[1].strip(":\n")

            line = mapping_file.readline().removeprefix("     ")
            while line.startswith("----") is False:  # while there are still bcos with that error
                bco = os.path.splitext(line.split(":")[0])[0]
                if bco not in bco_names:
                    print("INVALID MAPPING FILE " + bco + " NOT IN DIRECTORY")
                    return ValueError
                if addition_mode:
                    mode = "missing"
                else:
                    mode = "additional"
                # add error line to bco
                mapping_dict[bco][mode][path] = str(path + "-->" + value + ":" + line.split(':')[1])
                line = mapping_file.readline().removeprefix("     ")
    list_files = {}
    for bco in bco_names:
        list_files[bco] = (bco + "mapping.txt")
        with open(bco + "mapping.txt", "w") as file_to_map:
            file_to_map.write("====MISSING PROPERTIES/FIELDS====\n")
            for data in mapping_dict[bco]["missing"]:
                file_to_map.write(mapping_dict[bco]["missing"][data])
            file_to_map.write("====NONALLOWED PROPERTIES/FIELDS====\n")
            for data in mapping_dict[bco]["additional"]:
                file_to_map.write(mapping_dict[bco]["additional"][data])

    return list_files


# ______________________________________________________________________________#
def parse_mapping_file(mapping_file, default, check_file):
    """
    Parses a mapping file into a dict.

    :param mapping_file: name of mapping file
    :type mapping_file: string
    :param default: check default mapping
    :type default: boolean
    :param check_file: check file mapping
    :type check_file: boolean
    :return:
    :rtype:
    """
    mapping_dict = {
        "to_add": {},
        "to_delete": {},
        "to_swap": {}
    }
    with open(mapping_file) as file:
        for line in file:
            if line.startswith("#"):  # ignore comments
                continue
            if line.startswith("===="):  # ignore headers
                continue
            field_name = line.split('-->')[1].split(":")[0]  # get field name

            if check_file:  # if checking mapping file
                mode = line.split(':')[1].strip(" ").strip("\n")  # get value from file
                if mode == "":  # skip blank values
                    continue
                if mode == "DELETE":  # field value to delete = field name
                    field_value = field_name
                else:
                    field_value = mode.split("-")[1]
                    mode = mode.split("-")[0]

            if default:  # read value from default mapping value
                try:
                    mode = default_mapping[field_name]["mode"]
                    field_value = default_mapping[field_name]["value"]
                except KeyError:
                    continue

            key_list = []
            keys = line.split("-->")[0]
            key_reg = r"\[(.*?)\]"
            keys = re.findall(key_reg, keys)  # get each key in keylist
            for key in keys:
                key_list.append(key.strip("[").strip("]").strip("'"))  # get string from key
            if mode.lower() == "delete":
                add_or_update_list_HELPER(mapping_dict["to_delete"],
                                          field_name,
                                          {"index": key_list, "value": field_value}
                                          )
            if mode.lower() == "swap":  # swap value with field name
                add_or_update_list_HELPER(mapping_dict["to_swap"],
                                          field_name,
                                          {"index": key_list, "value": field_value}
                                          )
            if mode.lower() == "add":
                add_or_update_list_HELPER(mapping_dict["to_add"],
                                          field_name,
                                          {"index": key_list, "value": field_value},
                                          )
            if mode.lower() == "rename":  # swap field name with value
                add_or_update_list_HELPER(mapping_dict["to_swap"],
                                          field_value,
                                          {"index": key_list, "value": field_name}
                                          )

    return mapping_dict


# ______________________________________________________________________________#
def map_bcos(options):
    """
    Function called when convert feature is called
    Four possible routes.

    Single bco, no mapping file -> maps bco with default

    single bco, mapping file -> maps bco with mapping file

    directory, no mapping file -> maps each bco in directory with default

    directory, mapping file -> maps each bco in directory with mapping file
    """
    if os.path.isfile(options.bco):  # single bco
        if options.mappingFile is None:  # no provided mapping file
            create_mapping_file(options)  # making mapping file to get indexes of missing values
            mapping_file = os.path.splitext(options.bco)[0] + "mapping.txt"
            read_from_default_mapping = True  # get values from default mapping
            read_from_mapping_file = False  # don't get values from mapping file
        else:  # mapping file provided
            mapping_file = options.mappingFile
            read_from_mapping_file = True  # don't get values from default mapping
            read_from_default_mapping = False  # get values from mapping file

        bco = options.bco
        basename = str(os.path.splitext(bco)[0])  # get bco name without extension

        # convert schema, passing loaded bco, new file name, and mapping file (created by calling
        # parse_mapping_file)
        convert_schema(load_bco(options),
                       basename + "[converted].json",
                       parse_mapping_file(mapping_file,
                                          read_from_default_mapping,
                                          read_from_mapping_file))

        options.bco = basename + "[converted].json"  # switch options.bco to new bco
        validate_bco(options)  # validate bco
        if os.path.isfile("error.log"):  # if there were any errors
            create_mapping_file(options)  # create a mapping file for new bco
            print("\n\n Conversion impossible. \n Unconvertable fields can be found in <"
                  + options.bco + "mapping.txt>.")
        else:
            print("BCO converted successfully. Converted BCO named " + options.bco +
                  "[converted.json]")

    if os.path.isdir(options.bco):  # directory was provided

        output_directory = options.bco + "/converted"
        if not os.path.isdir(output_directory):
            os.mkdir(output_directory)

        converted_bcos = [options.bco + "/" + f for f in os.listdir(options.bco) if os.path.isfile(
            os.path.join(
                options.bco,
                f))]  # Get all files in provided directory

        for bco_name in converted_bcos:
            print("Found BCO " + bco_name)

        if options.mappingFile is None:  # no mapping file provided
            create_master_mapping_file(options, converted_bcos)  # make mapping file
            mapping_file = parse_master_mapping_file("mastermappingfile.txt",
                                                     converted_bcos)  # parse mapping file
            read_from_default_mapping = True  # read values from default mapping
            read_from_mapping_file = False  # don't read values from mapping file
        else:
            mapping_file = parse_master_mapping_file(options.mappingFile, converted_bcos)
            read_from_mapping_file = True  # dont' read values from default mapping
            read_from_default_mapping = False  # read values from mapping file
        for bco in converted_bcos:
            options.bco = bco  # set options.bco to current bco
            bco_name = os.path.splitext(os.path.basename(bco))[0]

            # convert schema for bco
            convert_schema(load_bco(options),
                           output_directory + "/" + bco_name + "[converted].json",
                           parse_mapping_file(
                               mapping_file[bco_name],
                               read_from_default_mapping,
                               read_from_mapping_file
                           )
                           )
        converted_bcos = [output_directory + "/" + f for f in os.listdir(output_directory) if
                          os.path.isfile(
                              os.path.join(
                                  output_directory,
                                  f))]  # get list of converted bcos from output directory

        for file in mapping_file:  # remove mapping files from individual bcos
            os.remove(mapping_file[file])

        os.remove("mastermappingfile.txt")  # remove master mapping file

        errors = []
        # get bcos that have errors
        for bco_name in converted_bcos:
            options.bco = bco_name
            validate_bco(options)
            if os.path.isfile("error.log"):
                errors.append(bco_name)

        options.bco = errors  # set bco to be files with errors
        if len(errors) == 0:
            print("Successful conversion. Converted BCOs can be found at " + output_directory)
        else:
            print("Unsuccessful conversion. Unconvertable BCO's were: \n")
            for error in errors:
                print(error + "\n")
            create_master_mapping_file(options, errors)  # create master mapping file from errors
            print("Mapping file showing unconvertable fields can be found at"
                  "<mastermappingfile.txt>")


# ______________________________________________________________________________#
def create_mapping_file(options):
    """

    Creates a single mapping file for a bco
    Writes the mapping file to <bco filename>mapping.txt

    :param options:
    :type options:
    :return:
    :rtype:
    """

    mapping_file = open(os.path.splitext(options.bco)[0] + "mapping.txt", 'w')
    mapping_file.writelines(
"""# Use this file to provide mapping values for a bco.
# MISSING PROPERTIES/FIELDS lists properties/fields that are missing from bco
# NONALLOWED PROPERTIES/FIELDS shows properties that are not allowed
# Syntax for specifying values
# To delete a value
# PATH --> FIELD: DELETE
# To add a value
# PATH --> FIELD: ADD-value_to_add
# To rename a field name
# PATH --> FIELD: RENAME-new_field_name
# To swap a field name with another current field name
# PATH --> FIELD: SWAP-other_field_name
# Blank values will be skipped. Data does not need to be double represented
# For example, 
# if <bco_id> needs renamed to <object_id>, either
# ['object_id'] --> object_id: 
# SWAP-bco_id
# OR 
# ['bco_id'] -->  bco_id: RENAME:object_id 
# will work. No need to fill out both values.
"""
)
    validate_bco(options)

    missing_reg = r'(.*?) is a required property'  # missing required property
    additional_reg = r'Additional properties are not allowed (.*?)'  # unalloewd extra property

    attribute_reg = r"'(.*?)'"  # getting an attribute (field surronded by single quotes)
    index_reg = r"On instance(.*?)"  # getting key path

    failed_validation_reg = r'Failed validating (.*?)'  # invalid type

    missing = []
    additional = []
    invalid = []

    path = {}

    with open('error.log') as errors:
        for line in errors:
            if re.match(missing_reg, line):  # if there is a missing property
                to_add = re.findall(attribute_reg, line)
                for match in to_add:
                    missing.append(match)
            elif re.match(additional_reg, line):  # if there is an additional property
                to_add = re.findall(attribute_reg, line)
                for match in to_add:
                    additional.append(match)
            elif re.match(failed_validation_reg, line):  # if a property is invalid
                # additional and required properties are already represnted by the above regexes,
                # so skip
                if line.__contains__("'additionalProperties'") is False \
                        and line.__contains__("'required'") is False:
                    to_add = [line.split("schema")[1].split("['")[-1].strip("']:\n")]
                    invalid.append(to_add[0])

            # field contains an index for some attribute
            # this attribute will be the last attribute found the above regexes, and is stored in
            # to_add
            if re.match(index_reg, line):
                keys = ""
                index_path = line.removeprefix("On instance").removesuffix(":\n")
                if index_path is not None:
                    keys = str(index_path)
                if len(to_add) > 0:  # if there are any attributes to add
                    for item in to_add:
                        add_or_update_list_HELPER(path, str(item), keys + "['" + str(item) +
                                                                    "']")
                to_add = [] # reset to_add
        mapping_file.write("====MISSING PROPERTIES/FIELDS====\n")
        for attribute in missing:
            mapping_file.write(str(path[attribute][0]) + "-->" + str(attribute) + ":\n")
            path[attribute].pop(0)

        mapping_file.write("====NONALLOWED PROPERTIES/FIELDS====\n")
        for attribute in additional:
            mapping_file.write(str(path[attribute][0]) + "-->" + str(attribute) + ":\n")
            path[attribute].pop(0)
        for attribute in invalid:
            mapping_file.write(str(path[attribute][0]).split("]")[0]
                               + "]-->" + str(attribute) + ":\n")
            path[attribute].pop(0)

        return mapping_file.name


# ______________________________________________________________________________#
def rename_dict_key_HELPER(data_dict, key_list, new_key_name):
    """
    Takes a dict, a key path, and renames the last key in the list

    :param data_dict: dictionary to add key to
    :type data_dict: dict
    :param key_list: list of nested keys
    :type key_list: list
    :param new_key_name: name for new key
    :type new_key_name:  str
    """
    data = get_key_from_dict_HELPER(data_dict, key_list)
    delete_key_HELPER(data_dict, key_list, key_list[-1])
    if data != "":
        key_list.pop()
        key_list.append(new_key_name)
        set_key_in_dict_HELPER(data_dict, key_list, data)


# ______________________________________________________________________________#
def delete_key_HELPER(data_dict, key_list, key_to_delete):
    """
    Deletes a key from a dictionary

    :param data_dict: dictionary to add key to
    :type data_dict: dict
    :param key_list: list of nested keys
    :type key_list: list
    :param key_to_delete: name of key to delete
    :type key_to_delete: str
    """
    data_dict = get_key_from_dict_HELPER(data_dict, key_list[:-1])
    data_dict.pop(key_to_delete)
    return data_dict


# ______________________________________________________________________________#
def get_key_from_dict_HELPER(data_dict, key_list):
    """
    Returns a value from a dictionary given a nested key list

    :param data_dict: dictionary to add key to
    :type data_dict: dict
    :param key_list: list of nested keys
    :type key_list: list
    """
    for item in key_list:
        try:
            item = int(item)  # try to convert item to int in case it is an array index
        except ValueError:
            item = item
        data_dict = data_dict[item]
    return data_dict


# ______________________________________________________________________________#
def set_key_in_dict_HELPER(data_dict, key_list, value_to_add):
    """
    Sets a new key in a dictionary
    :param data_dict: dictionary to add key to
    :type data_dict: dict
    :param key_list: list of nested keys
    :type key_list: list
    :param value_to_add: value to add
    :type value_to_add: any
    """
    data_dict = get_key_from_dict_HELPER(data_dict, key_list[:-1])
    data_dict[key_list[-1]] = value_to_add


# ______________________________________________________________________________#
def add_or_update_list_HELPER(data_dict, key, value):
    """
    Takes a dictionary, key, and value. Creates a list containing the value with key
    if key is not in dictionary. Otherwise appends value to list.
    """
    if key in data_dict:
        data_dict[key].append(value)
    else:
        data_dict[key] = [value]


# ______________________________________________________________________________#
def reorder_dict_HELPER(dict, key_list):
    """

    Reorders the keys in a dict.
    Currently assumes the key_list to be a plain list, but could be tweaked
    to call itself recursively to completely reorder dict.

    :param dict: dictionary to reoder
    :type dict: dict
    :param key_list: order of keys
    :type key_list: list
    """
    temp_dict = {}

    for key in key_list:
        try:
            temp_dict[key] = dict[key]
        except KeyError:
            continue

    dict = temp_dict


# ______________________________________________________________________________#
def main():
    """
    Main function
    """

    usr_args()


# ______________________________________________________________________________#
if __name__ == "__main__":
    main()
