#!/usr/bin/env python3
"""GlyGen move
"""

import os
import json
import sys
import argparse

__version__ = "0.0.1"
__status__ = "BETA"
ROOT_ID = 'http://127.0.0.1:8000'

DRAFT = {
    "prefix": "gly",
    "owner_group": "gly_drafter",
    "object_id": "",
    "schema": "IEEE",
    "contents": {}
}

def usr_args():
    """ initialize parser
    """

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

    parser.add_argument('-b', '--bco',
        required=True,
        help="path to BioCompute JSONs to process.")

    if len(sys.argv) <= 1:
        sys.argv.append('--help')

    options = parser.parse_args()
    return options

def load_bcos(file_path):
    """Load BCOs
    """
    post_publish = {"POST_api_objects_publish": []}
    post_draft ={"POST_api_objects_draft_create": []}

    file_list = [filename for filename in os.listdir(file_path) if '.json' in filename]
    for item in file_list:

        publish = {
            "prefix": "gly",
            "owner_group": "gly_publisher",
            "object_id": "",
            "schema": "IEEE",
            "contents": {}
        }

        draft = {
            "prefix": "gly",
            "owner_group": "gly_drafter",
            "object_id": "",
            "schema": "IEEE",
            "contents": {}
        }

        bco_file = file_path + item
        print(bco_file)
        with open(bco_file, 'r', encoding='utf-8') as file:
            bco = json.load(file)
            bco_id = bco['object_id'].split('/')
            object_id = ('/').join([ROOT_ID, bco_id[-2], bco_id[-1]])
            draft_id = ('/').join([ROOT_ID, bco_id[-2], 'DRAFT'])
            publish['object_id'] = object_id
            publish['contents'] = bco
            publish['contents']['object_id'] = object_id
            post_publish['POST_api_objects_publish'].append(publish)
            draft['object_id'] = draft_id
            draft['contents'] = bco
            draft['contents']['object_id'] = draft_id
            post_draft['POST_api_objects_draft_create'].append(draft)
            print(draft_id, object_id)
    # print(json.dumps(post_draft))
    # print(json.dumps(post_publish))
    with open(str(file_path+'draft.json'), 'w', encoding='utf-8') as draft_file:
        draft_file.write(json.dumps(post_draft))
    with open(str(file_path+'publish.json'), 'w', encoding='utf-8') as publish_file:
        publish_file.write(json.dumps(post_publish))

def main():
    """
    Main function
    """
    options = usr_args()
    load_bcos(options.bco)
    # print('main', DRAFT, PUBLISH, options)

if __name__ == "__main__":
    main()
