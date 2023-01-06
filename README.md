# BCO-TOOL


This is a Command Line Tool that allows for the manipulation of [BioCompute Objects](https://www.biocomputeobject.org/). Serveral functionalites are provided (detailed more below in supported modes).

## To install:

Run the Git Clone command in the location you would like the repostory:

1. Choose location for repository

        cd path/to/my/github/repositories

2. Clone repo

        git clone https://github.com/biocompute-objects/bcotool.git

### To add the main bco-tool program to your path

4. Enter directory

        cd bcotool

5. Create and/or activate a [python virtual environment](https://virtualenv.pypa.io/en/latest/user_guide.html):

        virtualenv [path_to_environment]

5. Install requirements in the virtual environment

        pip install -r requirements.txt

6. Copy the executable program file to the user local  bin:

        cp bco-tool/bco_runner.py  /usr/local/bin/bco


## Supported modes
* **convert** - takes a  BCO and converts it to the current BCO standard:  [ieee-2791-schema](https://opensource.ieee.org/2791-object/ieee-2791-schema). Can optionally provide a mapping file to specify mapping fields (template generated through **map** function), otherwise default mappingis performed.
* **validate** - takes a BCO and validates it against a schema. Can provide a schema, otherwise ieee-2791-schema is used.
* **map** - takes a BCO and generates a template mapping file to use for convert method.
* **license** - takes a BCO and gives a license.
* **functions** - Lists all functions in app.
* **run_cwl** - taks a BCO describing a [CWL Workflow](https://www.commonwl.org/) and runs it

* **--help/-h** - gives detailed help message
* **--version/-v** - gives information about version

### Optional arguments
* **--schema/-s** - provides schema for the **validate**, **convert**, or **map** functions, to check BCO against. Default schema is ieee-2971-schema.
* **--bco/b** - URL or path to JSON file of BCO to manipulate.
* **--mappingFile/-m** - path to mapping file to use for **convert** function.


