# BCO-TOOL

This is the BioComput package. 


For noow it can only print help text:
```
Usage: 
bco-runner.py  [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -j JSON, --json=JSON  json to validate
````

### Goals
1. help text == `bco -h` or `bco` or `bco --help`
2. version == `bco -v` or `bco --version`
3. workflow extraction == `bco extract_workflow -w cwl`
4. validation == bco -j bco12345 -s https://opensource.ieee.org/2791-object/ieee-2791-schema/-/raw/master/2791object.json
5. evaluate reproducibility based on available resources == bco bco-runner -w cwl 
