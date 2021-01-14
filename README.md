# BCO-TOOL

This is the BioCompute package. 

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
  {validate,run_cwl,functions}
    validate            Validation options. Used to test a BCO against a JSON
                        schema. If no schema is supplied the ieee-2791-schema
                        is used as thedefault
    run_cwl             run a CWL
    functions           list all available functions

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
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

### BCO functions
```
usage: bco_runner.py [-h]

optional arguments:
  -h, --help  show this help message and exit
```
## Examples of commands that are PLANNED to be supported:

Prints licence
>bco -licence

Lists the current programs supported.
>bco -programs

Run a workflow
>bco -ib bco012345 -p bco-runner -w cwl

- ib == input bco file

- p == (bco-runner/bco-validator/bco-comparator)

- w == (workflow used cwl/wdl/nextflow)
