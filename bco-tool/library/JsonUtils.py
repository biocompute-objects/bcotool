# For JSON parsing and schema validation.
import jsonschema
import json

# For catching print output.
import sys
import io

class JsonUtils:

    # Class Description
    # -----------------

    # These are methods for checking for valid JSON objects.
    # This is a modified version of the API class JsonUtils.

    def check_object_against_schema(self, object_pass, schema_pass):

        # Check for schema compliance.

        # Arguments
        # ---------

        # object_pass:  the object being checked.
        
        # Check the object against the provided schema.

        # Define a validator.
        validator = jsonschema.Draft7Validator(schema_pass)

        # Define the errors list.
        errors = validator.iter_errors(object_pass)
        error_string = ''

        # We have to use a bit of tricky output re-direction, see https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-variable-in-python

        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        # We ALSO have to use a bit of tricky flagging to indicate
        # that there were errors since generators can't use the norma len(list(generator)) idiom.
        error_flag = 0

        for e in errors:

            # There is at least 1 error.
            error_flag = 1

            print(e)
            print('=================')

        error_string = error_string + new_stdout.getvalue()
        sys.stdout = old_stdout

        # Return based on whether or not there were any errors.
        if error_flag != 0:

            print('Schema failure with given payload.  This message will only show up in the terminal.')

            # Collapse and return the errors.
            return error_string


    def check_for_field(self, json_file, key):
        # Check for the existence of a key in a json file.

        # Arguments
        # ---------

        # json_file:  the json file to be checked.

        # Returns
        # -------

        # A true or false flag indicating if the field exists.

        # Set the key flag as a boolean
        key_flag = None

        # Open the json file.
        with open(json_file, 'r') as file:
            json = json.load(file)

            # Check if the key exists.
            if key in json:
                # If the key exists return the flag as True.
                key_flag = True

            else:
                # If the key does not exist return the flag as False.
                key_flag = False

        return key_flag

    def convert_json_path_to_keys(self, json_path):
        # Take a json path and convert it to a key path for a dictionary.

        # Arguments
        # ---------

        # json_path:  the json path to be converted.

        # Returns
        # -------

        # A key path.


        # This version assumes there are no quoted fields.
        # Only works for a top level array, not nested arras i.e. [key][1][2][3]

        # Remove the left and right quotation marks.
        json_path = json_path[1:]
        json_path = json_path[:-1]

        # Split the json path.
        split_path = json_path.split('.')

        # Make a list to hold the processed path.
        processed_path = []

        # Indices for items in split path that has an array.
        has_array = []

        # Process arrays in the path.
        for index in range(0, len(split_path)):

            # Check for an array.
            if split_path[index].find(']') >= 0:

                split_path[index] = split_path[index].replace(']', '')
                split_path[index] = split_path[index].replace('[', '"][')

                has_array.append(index)

            processed_path.append(split_path[index])

        print('test')
        print(processed_path)

        for index in range(0, len(processed_path) - 1):

            # Check if the index is found in the array list has_array.
            try:
                has_array.index(index)

                processed_path[index] = processed_path[index] + ']["'

            except:

                processed_path[index] = processed_path[index] + '"]["'

        print(processed_path)

        # Join the split path.
        key_path = '["' + ''.join(processed_path) + '"]'
        print(key_path)

        return key_path







