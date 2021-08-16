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
outputs:
  - id: blast_results
    outputSource:
      - blastn/blast_results
    type: File
steps:
  - id: makeblastdb
    in:
      - id: database
        source: database
    out:
      - id: blastdbcmd_results
    run: ./makeblastdb.cwl
    label: makeblastdb
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
requirements: []
