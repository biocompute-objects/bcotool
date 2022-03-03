class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
id: makeblastdb
baseCommand:
  - makeblastdb
inputs:
  - id: database
    type: File
    inputBinding:
      position: 0
      prefix: '-in'
outputs:
  - id: blastdbcmd_results
    type: File
    outputBinding:
      glob: $(inputs.database.basename)
    secondaryFiles:
      - .nhr
      - .nin
      - .nsq
label: makeblastdb
arguments:
  - position: 0
    prefix: '-dbtype'
    valueFrom: nucl
requirements:
  - class: InitialWorkDirRequirement
    listing:
      - $(inputs.database)
  - class: InlineJavascriptRequirement
