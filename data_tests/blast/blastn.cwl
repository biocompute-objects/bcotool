class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
id: blastn
baseCommand:
  - blastn
inputs:
  - id: database
    type: File
    inputBinding:
      position: 0
      prefix: '-db'
    secondaryFiles:
      - .nhr
      - .nin
      - .nsq
  - id: query
    type: File
    inputBinding:
      position: 0
      prefix: '-query'
  - id: out_flag
    type: string 
    default: "blast-out.txt"
    inputBinding:
        position: 0
        prefix: -out
outputs:
  - id: blast_results
    type: File
    outputBinding:
        glob: $(inputs.out_flag)
label: blastn
