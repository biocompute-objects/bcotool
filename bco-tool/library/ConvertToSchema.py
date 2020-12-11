# For JSON.
import json

# For exiting the program.
import sys

# For regular expressions
import re

# For checking objects against schema.

from . import JsonUtils

from . import FileUtils


class ConvertToSchema:

    # Class Description
    # -----------------

    # These methods are for taking a BCO and making it fit into a schema. More broadly, this script takes a JSON and converts it into JSON with a provided schema.
    # Stores each BCO as an array, but a modification is to store each BCO with the BCO ID as keys and the BCO contents as the values (not written here)

    # Load a schema to force the provided JSON to fit.
    def load_schema(self, schema_location, location_type):


        # Arguments
        # ---------

        # schema_location:  either the URI or the file location of the schema.

        #   location_type:  either 'URI', or 'file'

        # Returns
        # -------

        # A JSON object derived from the provided schema.


        # First, determine the location type.
        
        if location_type == 'URI':

            # ...for Chris
            print('hi')

        elif location_type == 'file':

            # Open the file.
            with open(schema_location, mode='r') as file:
                schema = json.load(file)

        # Return our new ID.
        return schema

    # Define a function to load multiple BCO files.
    def load_bco_files(self, file_locations):


        # Arguments
        # ---------

        # file_locations:  a list of BCO file locations.

        # *** Develop a check to make sure that a file with multiple BCOs are in an array. ***

        # Returns
        # -------

        # A dictionary of BCOs where the key is the file and the value is the BCO index.
        # Each of these values also contains a dictionary with the BCO contents.

        # Declare the dictionary that will return the BCO.
        bcos = {}

        # Create a flag that indicates there was a JSON conversion error.
        json_conversion_error = 0

        # Go over each file.
        for current_file in file_locations:

            # Open the file and store it.
            with open(current_file, mode='r') as file:

                # Try to see if the file actually has legitimate JSON.
                try:

                    bco = json.load(file)

                    # Store the BCO.
                    bcos[current_file] = bco

                except:

                    # Print the error to the command line.
                    print('Provided file ' + current_file + ' was unable to be converted to JSON.  The conversion error is listed below.')
                    print(json.load(file))

                    # Change the flag.
                    json_conversion_error = 1

        # If there was a JSON conversion error, stop the program.
        if json_conversion_error == 1:

            # Exit the program completely.
            sys.exit(2)

        else:

            # Dictionary for itemized BCOS from each file.
            processed_bcos = {}

            # Go over each file and its BCO(s) and assign a number to each BCO.
            for filename, contents in bcos.items():

                # Declare the filename key.
                processed_bcos[filename] = {}

                # Determine the type of contents.
                if type(contents) == list:

                    # Iterate over each item in the list.
                    for index in range(0, len(contents)):
                        processed_bcos[filename][str(index)] = contents[index]

                else:
                    processed_bcos[filename]['0'] = contents

            # Return all the processed BCOs.
            return processed_bcos

    # Create a file with field discrepancies between the original object and the schema.
    def create_comparison_file(self, p_bcos, incoming_schema):

        # Arguments
        # ---------

        # p_bcos is the processed BCOs from ConvertToSchema().load_bco_files.
        # incoming_schema is the schema from ConvertToSchema().load_schema.

        # Returns
        # -------

        # something


        for file, contents in p_bcos.items():

            for key, bco_list in contents.items():

                for bco in bco_list:
                    print(incoming_schema)
                    print(x)

                    # Compare the single object against the schema.
                    comparison = JsonUtils.JsonUtils().check_object_against_schema(object_pass=bco, schema_pass=incoming_schema)

                    # Make an error file for each bco and ride the output from check_object_against_schema.
                    if comparison is not None:

                        error_file = file + '.error'

                        # Make an error file for each bco.
                        with open(error_file, 'a') as f:
                            f.write('BCO number ' + key + ' did not pass schema check. Below is the error report:\n\n')
                            f.write(comparison)
                            f.write('\n\n\n+++++++++++++++++++++++++++++++++++\n\n\n')




    def read_mapping_files(self, mapping_locations):

        # Arguments
        # ---------

        # mapping_locations is a path with the mapping files.

        # Returns
        # -------

        # A dictionary where each key is the mapping file and each value is the instructions for that file.

        # Declare the dictionary that will return the mappings.
        mappings = {}

        # Go over each mapping file.
        for current_file in mapping_locations:

            print(current_file)

            # Open the mapping file and store it.
            with open(current_file, mode='r') as file:

                # Initialize mappings[current_file]
                mappings[current_file] = {}

                for line_number, line in enumerate(file, 1):

                    print(line_number)
                    # Check each line for compliance with CRD with regex, quit on failure.
                    # Source: https://stackoverflow.com/questions/8888567/match-a-line-with-multiple-regex-using-python
                    # *** Find JSON path regex
                    # Regex accepts any values for JSON path and old/new values
                    # Source for file path regex: https://stackoverflow.com/questions/28989672/regex-to-tell-if-a-string-contains-a-linux-file-path-or-if-a-linux-file-path-as
                    # if not any re.match(line) for re in['^(/[^/ ]*)+/?bco_set_\d+.txt,https://portal.aws.biochemistry.gwu.edu/bco/BCO_\d+,CREATE,[\"(.*?)\"],[\"(.*?)\"]$', '^FILE_PATH_REGEX,URI_REGEX,CONVERT,[\"(.*?)\"],[\"(.*?)\"],[\"(.*?)\"]$', '^FILE_PATH_REGEX,URI_REGEX,DELETE,[\"(.*?)\"]$']:
                    #if not any(re.match(regex, line) for regex in ['^(/[^/ ]*)+/?bco_set_\d+\.txt\,https://portal\.aws\.biochemistry\.gwu\.edu/bco/BCO_\d+\,CREATE\,(\"(.*?)\")\,(\"(.*?)\")$', '^(/[^/ ]*)+/?bco_set_\d+\.txt\,https://portal\.aws\.biochemistry\.gwu\.edu/bco/BCO_\d+\,CONVERT\,(\"(.*?)\")\,(\"(.*?)\")\,(\"(.*?)\")$', '^(/[^/ ]*)+/?bco_set_\d+\.txt\,https://portal\.aws\.biochemistry\.gwu\.edu/bco/BCO_\d+\,DELETE\,(\"(.*?)\")$']):
                    if not any(re.match(regex, line) for regex in [
                        '^(/[^/ ]*)+/?bco_set_\d+\.txt\,http://data\.glygen\.org/GLY_\d+\,CREATE\,(\"(.*?)\")\,(\"(.*?)\")$',
                        '^(/[^/ ]*)+/?bco_set_\d+\.txt\,http://data\.glygen\.org/GLY_\d+\,CONVERT\,(\"(.*?)\")\,(\"(.*?)\")\,(\"(.*?)\")$',
                        '^(/[^/ ]*)+/?bco_set_\d+\.txt\,http://data\.glygen\.org/GLY_\d+\,DELETE\,(\"(.*?)\")$']):
                        # Print the error to the command line.
                        # *** How do you print the line number
                        print('Provided mapping file ' + current_file + ' had invalid instruction formatting at line number ' + str(line_number))

                        # Exit the program completely.
                        #sys.exit(2)

                    else:
                        # Strip new line off the end if it exists.
                        # Source: https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline

                        line = line.rstrip('\r\n')

                        # Store the mappings.
                        print(line)
                        split_line = line.split(',')
                        print(split_line)
                        print(mappings[current_file])

                        # Check if the BCO file is already defined in mappings dict.
                        if split_line[0] not in mappings[current_file]:
                            mappings[current_file][split_line[0]] = {split_line[1]: [','.join(split_line[2:])]}

                        else:

                            # Check if the BCO URI is already defined in BCO file dict.
                            # Append the instructions after the BCO URI if the BCO URI is already defined.
                            if split_line[1] not in mappings[current_file][split_line[0]]:

                                mappings[current_file][split_line[0]][split_line[1]] = [','.join(split_line[2:])]

                            # If the BCO URI is not already defined, define it and make it a list populated with the instructions.
                            else:
                                mappings[current_file][split_line[0]][split_line[1]].append(','.join(split_line[2:]))
            print('-----------------\n\n\n\n\n')
        return mappings

    def create_bco_from_mappings(self, bco_dict, mappings_dict, out_directory):

        # Arguments
        # ---------

        # Take in the dictionary from read_mapping_files (mappings_dict) and the BCOs from load_bco_files.
        # Output the new bcos to out_directory.

        # Returns
        # -------

        # A dictionary where the key is the new BCO file name and the value is the new BCO contents.

        # Possible errors:
        # - file existence has already been checked in previous functions
        # - an instruction is given in mappings_dict for an object in bco_dict that does not exist
        # - an instruction is given in mappings_dict for a field that does not exist in an existing object in bco_dict

        # Future modifications:
        # Add path dependency check to commands. Check for backward dependency i.e. does a command depend on previous commands to be valid?

        # Tell the user to only use one bco_id per mapping file, do not replicate bco_ids across mapping files.
        # In the future we can collapse all mapping files to master mapping list.

        # Run new BCO back through schema check to generate any remaining errors.

        # Create a dictionary to hold the new jsons and their contents.
        new_bco_dict = bco_dict

        # Instantiate JsonUtils
        ju = JsonUtils.JsonUtils()

        # Iterate through the mappings files dict.
        for mappings_file, mappings_contents in mappings_dict.items():

            # Iterate through the mappings contents dict, where each key is a bco_file and each value is a bco_id within that file.
            for bco_file, bco_file_mappings in mappings_contents.items():
                print(bco_file)
                print(bco_file_mappings)
                # print(json.dumps(bco_dict, sort_keys=True, indent=4))

                # Iterate over each of the BCOs in the bco file.
                for bco_id, bco_commands in bco_file_mappings.items():

                    # Check that bco_id exists in the bco. If so, run all commands.
                    # if bco_id in bco:

                    # Loop through the file contents to find the index associated with the BCO id.
                    for index, bco in new_bco_dict[bco_file].items():

                        # If the object ID matches the BCO ID then set the index key.
                        # Searching for 'bco_id' as a temporary fix.
                        if bco_id == bco['bco_id'] or bco_id == bco['object_id']:

                            # Iterate through the commands for that bco.
                            for command in bco_commands:

                                print(command)

                                # Split the command string into blocks.
                                split_command = command.split(',')

                                print(split_command)

                                # Perform the CREATE command.
                                if split_command[0] == 'CREATE':

                                    print('00000000000000000000000000000000000000000000000000000000')
                                    print('new_bco_dict["' + bco_file + '"]["' + index + '"]' + ju.convert_json_path_to_keys(json_path=split_command[1]) + ' = ' + split_command[2])
                                    exec('new_bco_dict["' + bco_file + '"]["' + index + '"]' + ju.convert_json_path_to_keys(json_path=split_command[1]) + ' = ' + split_command[2])

                                    # Check if new field already exists
                                    #if split_command[3] not in new_bco:
                                        # If it does not exit then create the new field with the new value.

                                    #else:
                                        #If it already exists then print error message.
                                        #print("Field " + split_command[4] + "already exists in " + new_bco)


                                # Perform the CONVERT command.
                                elif split_command[0] == 'CONVERT':

                                    # Save the value of the field.
                                    exec('old_value = ' + 'new_bco_dict["' + bco_file + '"]["' + index + '"]' + ju.convert_json_path_to_keys(json_path=split_command[1]))

                                    # Delete the old field.
                                    exec('del new_bco_dict["' + bco_file + '"]["' + index + '"]' + ju.convert_json_path_to_keys(json_path=split_command[1]))

                                    # Check if old value should be used for the new field name.
                                    print('+++++++++++++++++++++++++++++++++++++++++++++')
                                    print(split_command[3])
                                    print('+++++++++++++++++++++++++++++++++++++++++++++')
                                    if split_command[3] == '"USE_CURRENT_VALUE"':
                                        exec('new_bco_dict["' + bco_file + '"]["' + index + '"]' + ju.convert_json_path_to_keys(json_path=split_command[2]) + ' = old_value')

                                    else:
                                        exec('new_bco_dict["' + bco_file + '"]["' + index + '"]' + ju.convert_json_path_to_keys(json_path=split_command[2]) + ' = ' + split_command[3])


                                    # Check if field to be converted exists.
                                    #if split_command[3] in new_bco:
                                        # If it does exist then replace the old field with the new field and new value.

                                    #else:
                                        # If it does not exist print an error message.
                                        #print("Field " + split_command[4] + "does not exist in " + new_bco)


                                # Perform the DELETE command.
                                elif split_command[0] == 'DELETE':

                                    exec('del new_bco_dict["' + bco_file + '"]["' + index + '"]' + ju.convert_json_path_to_keys(json_path=split_command[1]))

                                    # Delete the old field.
                                    #exec('new_bco_dict["' + bco_file + '"]["' + index + '"].pop(' + ju.convert_json_path_to_keys(json_path=split_command[1]) + ', None)')

                                    # Check that field to be deleted exists.
                                    #if split_command[3] in new_bco:
                                        # Delete the field.

                                    #else:
                                        # If field does not exists print error message.
                                        #print("Field " + split_command[4] + "does not exist in " + new_bco)

                            # Error statement if bco_id was not found.
                            # else:
                                # print(bco_id + ' was not found in ' + bco_file)

        # Instantiate FileUtils
        fu = FileUtils.FileUtils()

        # Collapse new BCO dictionary to lists.
        # The dictionary that will hold the converted lists.
        final_bco_dict = {}

        # Loop through each bco contained in a file.
        for bco_file, bco_index in new_bco_dict.items():
            # The array that will hold the bco objects.
            bco_array = []

            # Add each bco to the array
            for bco_index, bco_object in new_bco_dict[bco_file].items():
                bco_array.append(bco_object)

            # Add the bco to the new dictionary where each key is ONLY the file name, not the full path.
            # Each value is the list of bcos.
            final_bco_dict[bco_file.split('/')[-1]] = bco_array

        # Write each converted bco into a new bco file.
        for bco_file, bco_array in final_bco_dict.items():
            fu.create_files(payload=final_bco_dict, output_directory=out_directory, file_extension='.converted')









