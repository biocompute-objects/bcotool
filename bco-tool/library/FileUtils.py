# --- SOURCES --- #

# For finding files.
import glob

# For writing.
import os

import json


# --- MAIN --- #

class FileUtils:



    def pathalizer(self, directory, pattern):

        # Description
        # -----------

        # Construct a search path with regex.

        # Arguments
        # ---------

        # directory
        # ---------
        #
        # Description:  where to look within the project directory.
        # Values:  any folder

        # pattern
        # -------
        #
        # Description:  the regex.
        # Values:  any regex

        # Outputs
        # -------

        # A directory + pattern string.
        print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), directory + pattern))
        # Kick back the string.
        return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), directory + pattern)



    def create_files(self, payload, output_directory, file_extension):

        # Description

        # Write a list of files a list of files in a directory matching a regex.

        # Arguments

        # payload
        # ----------------
        #
        # Description:  what are we writing?
        # Values:  must be a dictionary where the keys are *ORIGINAL*  full file names and values are file contents.

        # output_directory
        # ----------------
        #
        # Description:  where are we writing to?
        # Values:  any extant directory - MUST BE AN ABSOLUTE PATH

        # file_extension
        # ----------------
        #
        # Description:  what extension are we appending to the *ORIGINAL* file name?
        # Values:  any string

        # Outputs

        # A list of files.

        # Construct the output path for each file and write.
        for original_filename, contents in payload.items():

            with open(self.pathalizer(output_directory, original_filename + file_extension), mode='w') as f:

                # Check for object type.
                if type(contents) is str:

                    f.write(contents)

                elif type(contents) is dict:

                    f.write(json.dumps(contents, indent=4, sort_keys=True))

                elif type(contents) is list:

                    f.write(json.dumps(contents, indent=4, sort_keys=True))



    def read_files(self, input_directory, regex):

        # Description

        # Retrieve a list of files in a directory matching a regex.

        # Arguments

        # input_directory
        # ----------------
        #
        # Description:  where are the files we're assigning?
        # Values:  any extant directory - MUST BE AN ABSOLUTE PATH

        # regex
        # ----------------
        #
        # Description:  what regex are we using to search the directory?
        # Values:  any regex

        # Outputs

        # A list of matching files.

        # Search the input directory for matching files.

        # Source:  https://stackoverflow.com/questions/39293968/python-how-do-i-search-directories-and-find-files-that-match-regex
        # Source:  https://stackoverflow.com/questions/30218802/get-parent-of-current-directory-from-python-script

        return glob.glob(self.pathalizer(input_directory, regex))
