""" Static Function for BCO tools
""" 

import os
import json
from urllib.parse import urlparse

def load_bco( bco ):
    """
    Import of a BioCompute Object. Values can be a local file path or a URI.
    """

    # Declare source of BioCompute Object
    print('\nRemote BCO supplied: ', url_valid(bco), \
         '\t Local BCO supplied: ', os.path.exists(bco))

    if url_valid(bco):
        try:
            bco_dict = json.loads(requests.get(bco).content)
            print('Remote BioCompute loaded as ', bco_dict['provenance_domain']['name'])

        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            sys.exit('Loading remote JSON has failed \U0001F61E\nExiting')

    elif os.path.exists(bco):
        try:
            with open(bco, 'r') as data:
                bco_dict = json.load(data)
            print('Local BioCompute loaded as ', bco_dict['provenance_domain']['name'])

        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            sys.exit("Importing local JSON has failed \U0001F61E\nExiting")

    # If bco is not a valid FILE or URI program will exit
    else:
        print('BioCompute loading FAILED \n')
        sys.exit("Please provide a valid URI or PATH")

    return bco_dict

def url_valid( url ):
    """
    Validate a URL
    """

    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
