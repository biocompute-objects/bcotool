# BCO-TOOL

This is the BioCompute Tool. 

## To install:

Run the Git Clone command in the location you would like the repostory:

1. `cd path/to/my/github/repositories`

2. `git clone https://github.com/HadleyKing/bco-tool.git`

Add the main bco-tool program to your path

4. `cd bco-tool`

5. `cp bco-tool/bco_runner.py  /usr/local/bin/bco`


## Commands that are supported:

```
usage: bco [options]

positional arguments:
  {functions,license,validate,run_cwl}
    functions           list all available functions
    license             Prints BCO License
    validate            Validation options. Used to test a BCO against a JSON                       schema. If no schema is supplied the ieee-2791-schema                       is used as the default
    run_cwl             run a CWL

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

```

### BCO functions
```
usage: bco_runner.py [-h]

optional arguments:
  -h, --help  show this help message and exit
```

### BCO License
```
usage: bco [options] license [-h] -b BCO

optional arguments:
  -h, --help         show this help message and exit
  -b BCO, --bco BCO  BioCompute json to process
```

### BCO validate
```
usage: bco [options] validate [-h] -b BCO [-s SCHEMA]

optional arguments:
  -h, --help            show this help message and exit
  -b BCO, --bco BCO     json to validate
  -s SCHEMA, --schema SCHEMA
                        root json schema to validate against
``` 

### BCO run_cwl
```
usage: bco [options] run_cwl [-h] -b BCO

optional arguments:
  -h, --help         show this help message and exit
  -b BCO, --bco BCO  json to extract CWL from

```
