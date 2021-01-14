class: Workflow
cwlVersion: v1.0
id: blastn_homologs
doc: >-
  Run blastn to identify homologs. This is an essentual "Hello, World!" for
  bioinformatics. The input file is a HCV 1a isolate H77 complete genome [taxid:
  63746] (nucinput.fa) nucleotide sequence. The database (nucdb.fa) is a
  collection of HCV sequences.


  Step 1. Make blast database 

      makeblastdb -in nucdb.fa -dbtype nucl. 


  Step 2. Run nucleotide blast 

      blastn -db nucdb.fa -query nucinput.fa -out result.
label: blastn-homologs
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
inputs:
  - id: database
    type: File
    'sbg:x': 48.53886413574219
    'sbg:y': -104.66351318359375
  - id: query
    type: File
    'sbg:x': 187.08053588867188
    'sbg:y': -190.08018493652344
outputs:
  - id: blast_results
    outputSource:
      - blastn/blast_results
    type: File
    'sbg:x': 452.7055358886719
    'sbg:y': -121.3301773071289
steps:
  - id: makeblastdb
    in:
      - id: database
        source: database
    out:
      - id: blastdbcmd_results
    run: ./makeblastdb.cwl
    label: makeblastdb
    'sbg:x': 194.5833282470703
    'sbg:y': -43.5
  - id: blastn
    in:
      - id: database
        source: makeblastdb/blastdbcmd_results
      - id: query
        source: query
    out:
      - id: blast_results
    run: ./blastn.cwl
    label: blastn
    'sbg:x': 344.3721923828125
    'sbg:y': -55.70518112182617
requirements: []
