# BCO-TOOL

This is the BioCompute package. 

## To install:

Run the Git Clone command in the location you would like the repostory:

1. `cd path/to/my/github/repositories`

2. `git clone https://github.com/HadleyKing/bco-tool.git`

Add the main bco-tool program to your path

4. `cd bco-tool`

5. `cp bco-tool/bco-runner.py/usr/local/bin/bco`


## Examples of commands that are supported:

Prints version
>bco -version

Prints help
>bco -h

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
