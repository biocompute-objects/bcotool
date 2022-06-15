# Author(s): 

from pprint import pprint

class BioComputeObject:
    def __init__(this, metaData, usability_Domain, provenance_Domain, execution_Domain, extension_Domain, description_Domain, error_Domain, io_Domain):
        this.metaData = metaData                       
        this.usability_Domain = usability_Domain    
        this.provenance_Domain = provenance_Domain   
        this.execution_Domain = execution_Domain     
        this.extension_Domain = extension_Domain    
        this.description_Domain = description_Domain 
        this.error_Domain = error_Domain
        this.io_Domain = io_Domain

    def validate(this, metaData, usability_Domain, provenance_Domain, execution_Domain, extension_Domain, description_Domain, error_Domain, io_Domain):
        reqArgs = [usability_Domain, provenance_Domain, execution_Domain, description_Domain, io_Domain]
        for i in reqArgs:
            if i is None:
                print("INVALID BIOCOMPUTE OBJECT: " ,'\n', "- missing required argument")
                return False
        
        argTypes = {
            metaData : Meta,
            usability_Domain : str,
            provenance_Domain : ProvenanceDomain,
            execution_Domain : ExecutionDomain,
            extension_Domain : ExtensionSchema,
            description_Domain : DescriptionDomain,
            error_Domain : ErrorDomain,
            io_Domain : IODomain
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                print("INVALID BIOCOMPUTE OBJECT: " , '\n',  "- incorrect type")
                return False
        print("VALID BIOCOMPUTE OBJECT")
        return True

    def getInputs(this):
        return io_139


class Meta:
    def __init__(this, bco_Id, etag, spec_Version):
        this.bco_Id = bco_Id
        this.etag = etag
        this.spec_Version = spec_Version
    
    def validate(this, bco_Id, etag, spec_Version):
        argTypes = {
            bco_Id : ObjectID,
            etag : str,
            spec_Version : URI
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) or x is None:
                return False
        return True
    

class ProvenanceDomain:
    def __init__(this, name, license, version, created, modified, contributors, review, embargo, obsolete_After, derived_From):
        this.name = name
        this.license = license
        this.version = version
        this.created = created
        this.modified = modified
        this.contributors = contributors
        this.review = review
        this.embargo = embargo
        this.obsolete_After = obsolete_After
        this.derived_From = derived_From

    def validate(this, name, license, version, created, modified, contributors, review, embargo, obsolete_After, derived_From):
        reqArgs = [name, license, version, created, modified, contributors]
        for r in reqArgs:
            if r is None:
                return False

        argTypes = {
            name : str,
            license : str,
            version : SemanticVersion,
            created : DateTime,
            modified : DateTime,
            embargo : Embargo,
            obsolete_After : DateTime,
            derived_From : ObjectID
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False

        #lists are not hashable, they cannot be used in map, need to check these types sparately
        if not isinstance(contributors, list) and not contributors is None:
            return False
        elif not isinstance(review, list) and not review is None:
            return False
        return True


class Contributor:
    def __init__(this, contribution, name, affiliation, email, orcid):
        this.contribution = contribution
        this.name = name
        this.affiliation = affiliation
        this.email = email
        this.orcid = orcid

    def validate(this, contribution, name, affiliation, email, orcid):
        if name is None:
            return False    #Name is the only required field of Contributor

        argTypes = {
            contribution : str, 
            name : str,
            affiliation : str,
            email : str,
            orcid : str
        }
        
        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False
        return True




class Review:
    def __init__(this, date, status, reviewer_Comment, contributor):
        this.date = date
        this.status = status
        this.reviewer_Comment = reviewer_Comment
        this.contributor = contributor

    def validate(this, date, status, reviewer_Comment, contributor):
        if status is None or contributor is None:
            return False

        argTypes = {
            date : DateTime,
            status : str,
            reviewer_Comment : str,
            contributor : Contributor
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False
        return True



class Embargo:
    def __init__(this, start_Time, end_Time):
        this.start_Time = start_Time
        this.end_Time = end_Time

    def validate(this, start_Time, end_Time):
        argTypes = {
            start_Time : DateTime,
            end_Time : DateTime
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False
        return True


class ExecutionDomain:
    def __init__(this, script, script_Driver, software_Prerequisites, external_Data_Endpoints, environment_Variables):
        this.script = script
        this.script_Driver = script_Driver
        this.software_Prerequisites = software_Prerequisites
        this.external_Data_Endpoints = external_Data_Endpoints
        this.environment_Variables = environment_Variables

    def validate(this, script, script_Driver, software_Prerequisites, external_Data_Endpoints, environment_Variables):
        reqArgs = [script, script_Driver, software_Prerequisites, external_Data_Endpoints]
        for r in reqArgs:
            if r is None:
                return False

        listArgs = [script, software_Prerequisites, external_Data_Endpoints, environment_Variables]
        if not isinstance(script_Driver, str) and not script_Driver is None:
            return False

        #lists are not hashable, they cannot be used in map, need to check these types sparately
        for y in listArgs:
            if not isinstance(y, list) and not y is None:
                return False
        return True




class EnvironmentVariable:
    def __init__(this, name, variable):
        this.name = name
        this.variable = variable

    def validate(this, name, variable):
        argTypes = {
            name : str,
            variable : str
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) or x is None:
                return False
        return True


class SoftwarePrerequisites: #Add non required arguments: Filename, access time, SHA1 checksum
    def __init__(this, name, version, uri, filename, access_Time, sha1_Checksum):
        this.name = name
        this.version = version
        this.uri = uri
        this.filename = filename
        this.access_Time = access_Time
        this.sha1_Checksum = sha1_Checksum

    def validate(this, name, version, uri, filename, access_Time, sha1_Checksum):
        reqArgs = [name, version, uri]
        for r in reqArgs:
            if r is None:
                return False

        argTypes = {
            name : str,
            version : SemanticVersion,
            uri : URI,
            filename : str,
            access_Time : DateTime,
            sha1_Checksum : str
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False
        return True

        


class ExternalDataEndpoints:
    def __init__(this, name, uri):
        this.name = name
        this.uri = uri

    def validate(this, name, uri):
        argTypes = {
            name : str,
            uri : URI,
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) or x is None:
                return False
        return True

        


class ExtensionSchema:
    def __init__(self):
        print("empty contructor")



class DescriptionDomain:
    def __init__(this, keywords, pipeline_Step, platform, xref):
        this.keywords = keywords
        this.pipeline_Step = pipeline_Step
        this.platform = platform
        this.xref = xref

    def validate(this, keywords, pipeline_Step, platform, xref):
        if pipeline_Step is None:
            return False
        
        argTypes = [keywords, pipeline_Step, platform, xref]
        
        #lists are not hashable, they cannot be used in map, need to check these types sparately
        for x in argTypes:
            if not isinstance(x, list) and not x is None:
                return False
        return True


class PipelineSteps:
    def __init__(this, step_Number, name, description, input_List, output_List, version):
        this.step_Number = step_Number
        this.name = name
        this.description = description
        this.input_List = input_List
        this.output_List = output_List
        this.version = version

    def validate(this, step_Number, name, description, input_List, output_List, version):
        reqArgs = [step_Number, name, description, input_List, output_List]
        for r in reqArgs:
            if r is None:
                return False

        argTypes = {
            step_Number : int,
            name : str, 
            description : str,
            version : SemanticVersion
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False

        #lists are not hashable, they cannot be used in map, need to check these types sparately
        if not isinstance(input_List, list):
            return False
        elif not isinstance(output_List, list):
            return False
        return True


class Input:
    def __init__(this, uri, filename, access_Time, sha1_Checksum):
        this.uri = uri
        this.filename = filename
        this.access_Time = access_Time
        this.sha1_Checksum = sha1_Checksum

    def validate(this, uri, filename, access_Time, sha1_Checksum):
        if uri is None:
            return False

        argTypes = {
            uri : URI,
            filename : str,
            access_Time : DateTime,
            sha1_Checksum : str
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False
        return True




class Output:
    def __init__(this, uri, filename, access_Time, sha1_Checksum):
        this.uri = uri
        this.filename = filename
        this.access_Time = access_Time
        this.sha1_Checksum = sha1_Checksum

    def validate(this, uri, filename, access_Time, sha1_Checksum):
        if uri is None:
            return False

        argTypes = {
            uri : URI,
            filename : str,
            access_Time : DateTime,
            sha1_Checksum : str
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False
        return True


class Prerequisite:
    def __init__(this, name, uri, filename, access_Time, sha1_Checksum):
        this.name = name
        this.uri = uri
        this.filename = filename
        this.access_Time = access_Time
        this.sha1_Checksum = sha1_Checksum

    def validate(this, name, uri, filename, access_Time, sha1_Checksum):
        if uri is None:
            return False
    
        argTypes = {
            name : str, 
            uri : URI,
            filename : str,
            access_Time : DateTime,
            sha1_Checksum : str
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False
        return True

class Xref:
    def __init__(this, namespace, name, ids, access_Time):
        this.namespace = namespace
        this.name = name
        this.ids = ids
        this.access_Time = access_Time

    def validate(this, namespace, name, ids, access_Time):
        argTypes = {
            namespace : str,
            name : str,
            access_Time : DateTime
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) or x is None:
                return False

        #lists are not hashable, they cannot be used in map, need to check these types sparately
        if not isinstance(ids, list) and not ids is None:
            return False
        return True


class ErrorDomain:
    def __init__(this, empirical_Error, algorithmic_Error):
        this.empirical_Error = empirical_Error
        this.algorithmic_Error = algorithmic_Error

    def validate(this, empirical_Error, algorithmic_Error):
        argTypes = [empirical_Error, algorithmic_Error]

        #lists are not hashable, they cannot be used in map, need to check these types sparately
        for x in argTypes:
            if not isinstance(x, list) and not x is None:
                return False
        return True
        


# empirically determined values such as limits of detectability, false positives, false negatives, statistical confidence of outcomes, etc.
class EmpiricalError:
    def __init__(this, empError):
        this.empError = empError

    def validate(this, empError):
        if empError is None or not isinstance(empError, list):
            return False


class AlgorithmicError:
    def __init__(this, algError):
        this.algError = algError

    def validate(this, algError):
        if algError is None or not isinstance(algError, list):
            return False


class InputSubdomain:
    def __init__(this, uri, filename):
        this.uri = uri
        this.filename = filename

    def validate(this, uri, filename):
        if uri is None or not isinstance(uri, URI):
            return False
        elif not filename is None or not isinstance(filename, str):
            return False
        return True


class OutputSubdomain:
    def __init__(this, uri, filename):
        this.uri = uri
        this.filename = filename

    def validate(uri, filename):
        if uri is None or not isinstance(uri, URI):
            return False
        elif not filename is None or not isinstance(filename, str):
            return False
        return True

class IODomain:
    def __init__(this, input_Subdomain, output_Subdomain):
        this.input_Subdomain = input_Subdomain
        this.output_Subdomain = output_Subdomain

    def validate(this, input_Subdomain, output_Subdomain):
        if input_Subdomain is None or not isinstance(input_Subdomain, list):
            return False
        elif output_Subdomain is None or not isinstance(output_Subdomain, list):
            return False
        return True

    def getInput(this):
        return this.input_Subdomain

    def getOutputs(this):
        return this.output_Subdomain




class Utilities:
    def __init__():
        print("empty contructor")

    def validateDate(date):
        return False

    def validateURI(uri):
        return False

    def validateURL(url):
        return False

    def validateObjectID(object_Id):
        return False


# DateTime Object matches ISO 8601 format
class DateTime:
    def __init__(this, year, month, day, hour, minute, second, secondFrac, timeZoneOffSet):
        this.year = year
        this.month = month
        this.day = day
        this.hour = hour
        this.minute = minute
        this.second = second
        this.secondFrac = secondFrac
        this.timeZoneOffSet= timeZoneOffSet

    def validate(this, year, month, day, hour, minute, second, secondFrac, timeZoneOffSet):
        reqArgs = [year, month, day, hour, minute, second, secondFrac, timeZoneOffSet]
        for r in reqArgs:
            if r is None:
                return False

        argTypes = {
            year : int,
            month : int,
            day : int,
            minute : int,
            second : int,
            secondFrac : float,
            timeZoneOffSet : int
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) or x is None:
                return False
        return True



class ObjectID:
    def __init__(this, BCO_Id_Str):
        this.BCO_Id_Str = BCO_Id_Str

    def validate(this, BCO_Id_Str):
        if BCO_Id_Str is None or not isinstance(BCO_Id_Str, str):
            return False
        


class SemanticVersion:
    def __init__(this, major, minor, patch):
        this.major = major
        this.minor = minor
        this.patch = patch

    def validate(this, major, minor, patch):
        argTypes = {
            major : int,
            minor : int,
            patch : int
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) or x is None:
                return False
        return True


class URI:
    def __init__(this, uri_Str):
        this.uri_Str = uri_Str

    def validate(this, uri_str):

        return False



# ************************* INITIALIZE OBJECT ARGUMENTS TO MAKE BIOCOMPUTE CLASS OBJECT (BCO_00139) *****************************

# META
meta_URI = URI("https://w3id.org/ieee/ieee-2791-schema/")
meta_ObjId = ObjectID("https://portal.aws.biochemistry.gwu.edu/bco/BCO_00067092")
meta_139 = Meta(meta_ObjId, "ca34683b739b6c283adc89bd9bdcbaa5c5f1056037164a8b2934567955a60420", meta_URI)


# PROVINANCE DOMAIN
created = DateTime(2022, 5, 17, 18, 54, 48, 0.876, 0)
modified = DateTime(2022, 6, 1, 13, 8, 45, 0.481, 0)
version1 = SemanticVersion(3, 0, 0)

contr1 = Contributor("authoredBy", "David P. Astling", "Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine", "david.astling@example.com", "https://orcid.org/0000-0001-8179-0304")
contr2 = Contributor("authoredBy", "Ilea E. Heft", "Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine", "ilea.heft@example.com", "https://orcid.org/0000-0002-7759-7007")
contr3 = Contributor("authoredBy", "James M. Sikela", 'Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine', "james.sikela@example.com", 'https://orcid.org/0000-0001-5820-2762')
contr4 = Contributor("authoredBy", "Kenneth L. Jones", "Department of Pediatrics, University of Colorado School of Medicine" , "kenneth.jones@example.com", None)
contr5 = Contributor("createdBy", "Jonathon Keeney", "GWU", "keeneyjg@gwu.edu", None)
contr6 = Contributor("createdBy", "Alex Nguyen", "UVA", "tan5um@virginia.edu", None)
contr7 = Contributor("ceatedBy", "Mike Taylor", "GWU", None, "https://orcid/0000-0002-1003-5675")
contributorsList = [contr1, contr2, contr3, contr4, contr5, contr6]

rev1 = Review(None, "unreviewed", None, contr7)
reviewersList = [rev1]
prov_139 = ProvenanceDomain("WGS Simulation of DUF1220 Regions", "https://opensource.org/licenses/MIT", version1, created, modified, contributorsList, reviewersList, None, None, None)


# DESCRIPTION DOMAIN
keywordsArr = ["Copy Number Variation", "CNV", "DUF1220", "Genome Informatics", "Next-generation sequencing", "Bioinformatics"]

# Each pipeline step needs its own 2 arrays of inputs and outputs
input_0_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/1_download.sh")
output_0_URI = URI("https://github.com/dpastling/plethora/blob/master/data/1000Genomes_samples.txt")
input_0 = Input(input_0_URI, None, None, None)
output_0 = Output(output_0_URI, None, None, None)
inputArr0 = [input_0]
outputArr0 = [output_0]
pipelineStp0 = PipelineSteps(0, "Script to download fastq files from the 1000 Genomes Project", "This script downloads the fastq files for each sample from the 1000 Genomes site as specified in a sample_index file", inputArr0, outputArr0, None)

input_1_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/2_trim.sh")
output_1_URI = URI("https://github.com/dpastling/plethora/blob/master/logs/trim_stats.txt")
input_1 = Input(input_1_URI, None, None, None)
output_1 = Output(output_1_URI, None, None, None)
inputArr1 = [input_1]
outputArr1 = [output_1]
pipelineStp1 = PipelineSteps(1, "Script to trim and filter the reads", "This script automates the task of trimming low quality bases from the 3' ends of the reads and removes any that are shorter than 80 bp.", inputArr1, outputArr1, None)

input_2_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/3_batch_bowtie.sh")
output_2_URI = URI("https://github.com/dpastling/plethora/blob/master/align_report.txt")
input_2 = Input(input_2_URI, None, None, None)
output_2 = Output(output_2_URI, None, None, None)
inputArr2 = [input_2]
outputArr2 = [output_2]
pipelineStp2 = PipelineSteps(2, "Script to align reads to the genome", "This script aligns reads to the genome with Bowtie2.", inputArr2, outputArr2, None)

input_3_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/5_batch_make_bed.sh")
output_3_URI = URI("https://github.com/dpastling/plethora/blob/master/results/test_read_depth.bed")
input_3 = Input(input_3_URI, None, None, None)
output_3 = Output(output_3_URI, None, None, None)
inputArr3 = [input_3]
outputArr3 = [output_3]
pipelineStp3 = PipelineSteps(3, "Script to calculate coverage for each DUF1220 domain", "This script: Coverts the .bam alignment file into bed format. Parses the reads Calls the merge_pairs.pl script (described below) to combined proper pairs into a single fragment. Finds overlaps with the reference bed file containing the regions of interest (e.g. DUF1220). Calculates the average coverage for each region: (number of bases that overlap) / (domain length)", inputArr3, outputArr3, None)

pipelineSteps = [pipelineStp0, pipelineStp1, pipelineStp2, pipelineStp3]
descrpt_139 = DescriptionDomain(keywordsArr, pipelineSteps, None, None)


# EXECUTION DOMAIN
softwrePrereq1_URI = URI("http://bowtie-bio.sourceforge.net/bowtie2/index.shtml")
softwrePrereq2_URI = URI("https://bedtools.readthedocs.io/en/latest/")
softwrePrereq3_URI = URI("http://samtools.sourceforge.net/")
softwrePrereq4_URI = URI("https://cutadapt.readthedocs.io/en/stable/")

bow_Version = SemanticVersion(2, 2, 9)
bed_Version = SemanticVersion(2, 17, 0)
sam_Version = SemanticVersion(0, 1, 19) #"0.1.19-44428cd"
ca_Version = SemanticVersion(1, 12, 0) 

softwrePrereq1 = SoftwarePrerequisites("Bowtie 2", bow_Version, softwrePrereq1_URI, None, None, None)
softwrePrereq2 = SoftwarePrerequisites("Bed Tools", bed_Version, softwrePrereq2_URI, None, None, None)
softwrePrereq3 = SoftwarePrerequisites("Sam Tools", sam_Version, softwrePrereq3_URI, None, None, None)
softwrePrereq4 = SoftwarePrerequisites("Cut Adapt", ca_Version, softwrePrereq4_URI, None, None, None)
softwrePrereqs = [softwrePrereq1, softwrePrereq2, softwrePrereq3, softwrePrereq4]

edep_URI = URI("https://www.internationalgenome.org/")
externalDataEndpoint1 = ExternalDataEndpoints("IGSR", edep_URI)
extDataEndPts = [externalDataEndpoint1]

script1_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/1_download.sh")
script2_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/2_trim.sh")
script3_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/3_batch_bowtie.sh")
script4_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/5_batch_make_bed.sh")
scripts = [script1_URI, script2_URI, script3_URI, script4_URI]

env_Var1 = EnvironmentVariable("HOSTTYPE: ", "x86_64-linux")
env_Var2 = EnvironmentVariable("EDITOR: ", "vim")
environment_Variables = [env_Var1, env_Var2]

excn_139 = ExecutionDomain(scripts, "Shell", softwrePrereqs, extDataEndPts, environment_Variables)


# IO DOMAIN
inputSub1_URI = URI("https://github.com/dpastling/plethora/blob/master/fastq/test_1.fastq.gz")
inputSub2_URI = URI("https://github.com/dpastling/plethora/blob/master/fastq/test_2.fastq.gz")
outputSub_URI = URI("https://github.com/dpastling/plethora/blob/master/results/test_read_depth.bed")
inputSub1 = InputSubdomain(inputSub1_URI, None)
inputSub2 = InputSubdomain(inputSub2_URI, None)
outputSub = OutputSubdomain(outputSub_URI, "test_read_depth.bed")

inputSubDmn = [inputSub1, inputSub2]
outputSubDmn = [outputSub]
io_139 = IODomain(inputSubDmn, outputSubDmn)


# ERROR DOMAIN
empError1 = EmpiricalError("CON1: 1.55")
empError2 = EmpiricalError("CON2: 0.91")
empError3 = EmpiricalError("CON3: 0.26")
empError4 = EmpiricalError("HLS1: 0.99")
empError5 = EmpiricalError("HLS2: 1.90")
empError6 = EmpiricalError("HLS3: 1.67")

root_Mean_Sqr_Error = [empError1, empError2, empError3, empError4, empError5, empError6]
error_139 = ErrorDomain(root_Mean_Sqr_Error, None)


# EXTENSION DOMAIN SHOULD BE SET TO None
# USABIITY DOMAIN IS A STRING DOES NOT NEED TO BE MADE AN OBJECT
use_139 = "Pipeline for identifying copy number of genetic sequences independent of the genes in which they occur, and with higher fidelity than existing methods. Approximately 25 individuals were randomly chosen from each of the CEU, YRI, CHB, JPT, MXL, CLM, PUR, ASW, LWK, CHS, TSI, IBS, FIN, and BGR populations for a total of 324 individuals. Where domains were more than 1 kb apart, the boundaries of the domains were extended up to 250 bp to allow the possibility of capturing unique sequence directly adjacent to the domain. No intermediate files were generated because the commands were run executed as a pipe at the command line, so T:/dev/tmpfs was used for the file IOs in the Description Domain. This example pipeline was created based on the work of Astling et al. doi: 10.1186/s12864-017-3976-z"

# BIOCOMPUTE CLASS OBJECT
BCO_000139 = BioComputeObject(meta_139, use_139, prov_139, excn_139, None, descrpt_139, error_139, io_139)

# PRINT BIOCOMPUTE CLASS OBJECT
# pprint(vars(BCO_000139))
# pprint(vars(BCO_000139.description_Domain))
# pprint(vars(BCO_000139.execution_Domain))
# pprint(vars(BCO_000139.provenance_Domain))



# ************************************ DOMAIN VALIDATE() TESTING *******************************************

# BIOCOMPUTE OBJECT:
# badMeta = DescriptionDomain("k", "p", "p", "x") # Bad Object made to test validation function
# BCO_000139.validate(badMeta, use_139, prov_139, excn_139, None, descrpt_139, None, io_139) # tests type error
# BCO_000139.validate(meta_139, None, prov_139, excn_139, None, descrpt_139, None, io_139) # tests required argument error
BCO_000139.validate(meta_139, use_139, prov_139, excn_139, None, descrpt_139, None, io_139) # tests valid BCO

# PROVENANCE DOMAIN:
# print(BCO_000139.provenance_Domain.validate("WGS Simulation of DUF1220 Regions", "https://opensource.org/licenses/MIT", version1, created, modified, contributorsList, reviewersList, None, None, None)) # tests valid provenance domain
# print(BCO_000139.provenance_Domain.validate(None, "https://opensource.org/licenses/MIT", version1, created, modified, contributorsList, reviewersList, None, None, None)) # tests required argument error in provenance domain
# print(BCO_000139.provenance_Domain.validate(21, "https://opensource.org/licenses/MIT", version1, created, modified, contributorsList, reviewersList, None, None, None)) # tests type error in provenance domain


# DESCRIPTION DOMAIN:
# print(BCO_000139.description_Domain.validate(keywordsArr, pipelineSteps, None, None)) # tests valid description domain
# print(BCO_000139.description_Domain.validate(keywordsArr, None, None, None)) # tests required argument error in description domain
# print(BCO_000139.description_Domain.validate(21, pipelineSteps, None, None)) # tests type error in description domain

# EXECUTION DOMAIN:
# print(BCO_000139.execution_Domain.validate(scripts, "Shell", softwrePrereqs, extDataEndPts, environment_Variables)) # tests valid execution domain 
# print(BCO_000139.execution_Domain.validate(21, "Shell", softwrePrereqs, extDataEndPts, environment_Variables)) # tests type error in execution domain 
# print(BCO_000139.execution_Domain.validate(None, "Shell", softwrePrereqs, extDataEndPts, environment_Variables)) # tests required argument error in execution domain 

# ERROR DOMAIN:
# print(BCO_000139.error_Domain.validate(21, None)) # type error
# print(BCO_000139.error_Domain.validate(root_Mean_Sqr_Error, None)) # valid 

# IO DOMAIN:
# print(BCO_000139.io_Domain.validate(inputSubDmn, outputSubDmn)) # valid
# print(BCO_000139.io_Domain.validate(21, outputSubDmn)) # type error
# print(BCO_000139.io_Domain.validate(None, outputSubDmn))  # required error

# META:
# print(BCO_000139.metaData.validate(meta_ObjId, "ca34683b739b6c283adc89bd9bdcbaa5c5f1056037164a8b2934567955a60420", meta_URI)) # valid Meta
# print(BCO_000139.metaData.validate(meta_ObjId, 21.2, meta_URI)) # type error 
# print(BCO_000139.metaData.validate(None, "ca34683b739b6c283adc89bd9bdcbaa5c5f1056037164a8b2934567955a60420", meta_URI)) # required argument error
# print(BCO_000139.metaData.validate("ID", "ca34683b739b6c283adc89bd9bdcbaa5c5f1056037164a8b2934567955a60420", meta_URI)) # type error

print("Finished")

# NOTES: 
# All domain validate() functions have been tested
# No lower level validate() functions have been tested
# If pprint() is not explicitly called on obejct or container of objects, memory address is printed
# Type checking lists of obejcts is odd, lists can hold different types so just checked that that an argument is of type 'list'
# lists are not hashable, they cannot be the key in a map, so they had to be checked separatey because either a list object was the key or 
# 'list' python object was the key and both are unhashable.
