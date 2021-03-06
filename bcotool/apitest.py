#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#bcotool

import requests
import json

#______________________________________________________________________________#
def main():
    """
    
    """
    thing = json.dumps("{POST_read_object: [{table: 'bco_draft',object_id: 'https://beta.portal.aws.biochemistry.gwu.edu/BCO_DRAFT_706f97bdcafa4cd89056fbbfc9d5d325'}]}")
    POST_read_object = {'table': 'bco_draft','object_id': 'https://beta.portal.aws.biochemistry.gwu.edu/BCO_DRAFT_706f97bdcafa4cd89056fbbfc9d5d325'}
    print(thing)
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    data = {}
    print(headers)
    r = requests.post('https://beta.portal.aws.biochemistry.gwu.edu/bco/objects/read/', data, verify=False, headers=headers)
    print(r.url)
    print(r.text)

#______________________________________________________________________________#
if __name__ == "__main__":
    main()