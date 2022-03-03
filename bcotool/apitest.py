#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#bcotool

import requests
import json

import bcoutils

#______________________________________________________________________________#
def update_bco():
    """

    """
    bco = '/Users/hadleyking/GitHub/hadleyking/bcotool/data_tests/cwl-blastn-homologs.json'
    
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    bco_dict = bcoutils.load_bco(bco)

    creator = {
            'POST_create_new_object':[
                {
                    'object_id': 'https://beta.portal.aws.biochemistry.gwu.edu/BCO_31/1.0',
                    'table': 'bco_publish',
                    'schema': 'IEEE',
                    'contents': bco_dict,
                    'state': 'PUBLISHED'
                }
            ]
        }
    creator = json.dumps(creator)

    r = requests.post(
        'https://beta.portal.aws.biochemistry.gwu.edu/bco/objects/create/',
        data = creator, verify=False, headers=headers)

    return (r.text)
#______________________________________________________________________________#
def publish_bco():
    """

    """
    bco = '/Users/hadleyking/GitHub/hadleyking/bcotool/data_tests/cwl-blastn-homologs.json'
    
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    bco_dict = bcoutils.load_bco(bco)

    creator = {
            'POST_create_new_object':[
                {
                    'table': 'bco_publish',
                    'schema': 'IEEE',
                    'contents': bco_dict,
                    'state': 'PUBLISHED'
                }
            ]
        }
    creator = json.dumps(creator)

    r = requests.post(
        'https://beta.portal.aws.biochemistry.gwu.edu/bco/objects/create/',
        data = creator, verify=False, headers=headers)

    return (r.text
    )

#______________________________________________________________________________#
def read_bco():
    """

    """

    headers = {'Content-type': 'application/json; charset=UTF-8'}

    req_list = [
        ('bco_draft', 'https://beta.portal.aws.biochemistry.gwu.edu/BCO_DRAFT_706f97bdcafa4cd89056fbbfc9d5d325'),
        ('bco_publish', 'https://beta.portal.aws.biochemistry.gwu.edu/BCO_3/1.0')
    ]

    req_dict = {}
    req_dict['POST_read_object'] = []

    for i in req_list:
        print(i[0])
        req_dict['POST_read_object'].append(
            {
                'table': i[0],
                'object_id': i[1]
            }
        )
    # reader = {
    #         'POST_read_object':[
    #             {
    #                 'table': 'bco_draft',
    #                 'object_id': 'https://beta.portal.aws.biochemistry.gwu.edu/BCO_DRAFT_706f97bdcafa4cd89056fbbfc9d5d325'
    #             },
    #             {
    #                 'table': 'bco_publish',
    #                 'object_id': 'https://beta.portal.aws.biochemistry.gwu.edu/BCO_3/1.0'
    #             }
    #         ]
    #     }
    print(req_dict)


    read = json.dumps(req_dict)

    r = requests.post(
        'https://beta.portal.aws.biochemistry.gwu.edu/bco/objects/read/',
        data = read, verify=False, headers=headers)

    return (r.text)

#______________________________________________________________________________#
def main():
    # resp = read_bco()
    resp = publish_bco()
    resp = update_bco()
    print(resp)
#______________________________________________________________________________#
if __name__ == "__main__":
    main()