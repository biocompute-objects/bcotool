#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#validate
'''
Validation functions for BioCompute Objects.
'''

import io
import sys
import json
import jsonref
import jsonschema
from hashlib import sha256

def validate_etag( options ):
    """
    checks etag
    https://docs.python.org/3/library/hashlib.html#hash-algorithms
    https://stackoverflow.com/questions/26539366/how-to-use-sha256-hash-in-python
    """

    bco_dict = bcoutils.load_bco( options )
    bco_etag = bco_dict['etag']
    data = bco_dict
    del data['object_id'], data['spec_version'], data['etag']
    etag = sha256(json.dumps(data).encode('utf-8')).hexdigest()
    print(etag, '\n', bco_etag)
    print(bco_etag == etag)

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
    bco_dict = bcoutils.load_bco(options.bco)

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