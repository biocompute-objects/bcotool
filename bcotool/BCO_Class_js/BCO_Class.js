/* Author: Sean Keeney
Date: 6/3/2022

Implementation of BCO class and necessary classes/functions
Most "domains" will need class. Domain objects will be needed to be arguments for the BCO class constructor.

NOTES: 
- Comments to clarify memeber variable types
- No default contructors
- Member function validate() within each class
- Utility class to house "global" functions needed
- Arguments not needed (unrequired) in creation of BCO are set to null.
*/


class BioComputeObject{
    constructor(metaData, usability_Domain, provenance_Domain, execution_Domain, extension_Domain, description_Domain, error_Domain, io_Domain){
        this.metaData = metaData;                       //Meta Object
        this.usability_Domain = usability_Domain;       //string
        this.provenance_Domain = provenance_Domain;     //ProvenanceDomain Object
        this.execution_Domain = execution_Domain;       //ExecutionDomain Object
        this.extension_Domain = extension_Domain;       //ExtensionSchema Object
        this.description_Domain = description_Domain;   //DescriptionDomain Object
        this.error_Domain = error_Domain;               //ErrorDomain Object
        this.io_Domain = io_Domain;                     //IODomain Object
    }

    // validate(metaData, usability_Domain, provenance_Domain, execution_Domain, extension_Domain, description_Domain, error_Domain, io_Domain){

    //     const args = [metaData, usability_Domain, provenance_Domain, execution_Domain, extension_Domain, description_Domain, error_Domain, io_Domain];
    //     const types = [Meta, "string", ProvenanceDomain, ExecutionDomain, ExtensionSchema, DescriptionDomain, ErrorDomain, IODomain];

    //     const map1 = new Map();
    //     map1.set(metaData, Meta);
    //     map1.set(usability_Domain, "string");
    //     map1.set(provenance_Domain, ProvenanceDomain);
    //     map1.set(execution_Domain, ExecutionDomain);
    //     map1.set(extension_Domain, ExtensionSchema);
    //     map1.set(description_Domain, DescriptionDomain);
    //     map1.set(error_Domain, ErrorDomain);
    //     map1.set(io_Domain, IODomain);

    //     for(var i = 0; i < args.length; i++){
    //         for(var j = 0; j < types.length; j++){
    //             if(args[i] !== null){
    //                 if((!(args[i] instanceof types[j]))||(args[i] !== types[j])){
    //                     console.log("INVALID ARGUMENT AT: " + args[i]);
    //                     return false;
    //                 }
    //             }
                
    //         }
    //         return true;
    //     }
    // }
}

class Meta{
    constructor(bco_Id, etag, spec_Version){
        this.bco_Id = bco_Id;                   //object id
        this.etag = etag;                       //string
        this.spec_Version = spec_Version;       //semantic
    }
    validate(){
        return false;
    }
}

class ProvenanceDomain{
    constructor(name, license, version, created, modified, contributors, review, embargo, obsolete_After, derived_From){
        this.name = name;
        this.license = license;
        this.version = version;
        this.created = created;
        this.modified = modified;
        this.contributors = contributors;
        this.review = review;
        this.embargo = embargo;
        this.obsolete_After = obsolete_After;
        this.derived_From = derived_From;
    }

    validate(){
        return false;
    }
}

class Contributor{
    constructor(contribution, name, affiliation, email, orcid){
        this.contribution = contribution;
        this.name = name;
        this.affiliation = affiliation;
        this.email = email;
        this.orcid = orcid;
    }

    validate(){
        return false;
    }
}

class Review{
    constructor(date, status, reviewer_Comment, contributor){
        this.date = date;
        this.status = status;
        this.reviewer_Comment = reviewer_Comment;
        this.contributor = contributor;
    }

    validate(){
        return false;
    }
}

class Embargo{
    constructor(start_Time, end_Time){
        this.start_Time = start_Time; 
        this.end_Time = end_Time;
    }

    validate(){
        return false;
    }
}

class ExecutionDomain{
    constructor(script, script_Driver, software_Prerequisites, external_Data_Endpoints, environment_Variables){
        this.script = script;
        this.script_Driver = script_Driver;
        this.software_Prerequisites = software_Prerequisites;
        this.external_Data_Endpoints = external_Data_Endpoints;
        this.environment_Variables = environment_Variables;
    }

    validate(){
        return false;
    }
}

class EnvironmentVariable{
    constructor(name, variable){
        this.name = name;
        this.variable = variable;
    }

    validate(){
        return false;
    }
}

class SoftwarePrerequisites{
    constructor(name, version, uri){
        this.name = name;
        this.version = version;
        this.uri = uri;
    }

    validate(){
        return false;
    }
}

class ExternalDataEndpoints{
    constructor(name, uri){
        this.name = name;
        this.uri = uri;
    }

    validate(){
        return false;
    }
}

class ExtensionSchema{
    constructor(){

    }
    //validate()? 
}

//NOTE: Be sure to check Description Domain in UML Diagram for completeness.
class DescriptionDomain{
    constructor(keywords, pipeline_Step, platform, xref){
        this.keywords = keywords;                  //list of strings
        this.pipeline_Step = pipeline_Step;        //list of object PipelineStep objects
        this.platform = platform;                  //list of strings
        this.xref = xref;                          //list of Xref objects
    }

    validate(){
        return false;
    }
}

class PipelineSteps{
    constructor(step_Number, name, description, input_List, output_List, version){
        this.step_Number = step_Number;
        this.name = name;
        this.description = description;
        this.input_List = input_List;
        this.output_List = output_List;
        this.version = version;
    }

    validate(){
        return false;
    }
}

class Input{
    constructor(uri, filename){
        this.uri = uri;
        this.filename = filename;
    }

    validate(){
        return false;
    }
}

class Output{
    constructor(uri, filename){
        this.uri = uri;
        this.filename = filename;
    }

    validate(){
        return false;
    }
}

class Prerequisite{
    constructor(name, uri){
        this.name = name;
        this.uri = uri;
    }

    validate(){
        return false;
    }
}

class Xref{
    constructor(namespace, name, ids, access_Time){
        this.namespace = namespace;
        this.name = name;
        this.ids = ids;
        this.access_Time = access_Time;
    }

    validate(){
        return false;
    }
}

class ErrorDomain{
    constructor(empirical_Error, algorithmic_Error){
        this.empirical_Error = empirical_Error;
        this.algorithmic_Error = algorithmic_Error;
    }

    validate(){
        return false;
    }
}

// empirically determined values such as limits of detectability, false positives, false negatives, statistical confidence of outcomes, etc.
class EmpiricalError{
    constructor(empError){
        this.empError = empError;
    }

    validate(){
        return false;
    }
}

class AlgorithmicError{
    constructor(algError){
        this.algError = algError;
    }

    validate(){
        return false;
    }
}

class IODomain{
    constructor(input_Subdomain, output_Subdomain){
        this.input_Subdomain = input_Subdomain;
        this.output_Subdomain = output_Subdomain;
    }

    validate(){
        return false;
    }
}

class InputSubdomain{
    constructor(uri, filename){
        this.uri = uri;
        this.filename = filename;
    }

    validate(){
        return false;
    }
}

class OutputSubdomain{
    constructor(uri, filename){
        this.uri = uri;
        this.filename = filename;
    }

    validate(){
        return false;
    }
}

class Utilities{
    constructor(){

    }

    validateDate(date){
        return false;
    }

    validateURI(uri){
        return false;
    }

    validateURL(url){
        return false;
    }

    validateObjectID(object_Id){
        return false;
    }
}

//URI?

//DateTime Object matches ISO 8601 format
class DateTime{
    constructor(year, month, day, hour, minute, second, secondFrac, timeZoneOffSet){
        this.year = year;
        this.month = month;
        this.day = day;
        this.hour = hour;
        this.minute = minute;
        this.second = second;
        this.secondFrac = secondFrac;
        this.timeZoneOffSet= timeZoneOffSet;
    }
}

class ObjectID{
    constructor(BCO_Id_Str){
        this.BCO_Id_Str = BCO_Id_Str;
    }
}


class SemanticVersion{
    constructor(major, minor, patch){
        this.major = major;
        this.minor = minor;
        this.patch = patch;
    }
}



// Make BCO_139

// META
meta_URI = "https://w3id.org/ieee/ieee-2791-schema/"; // spec version
var meta_139 = new Meta("https://portal.aws.biochemistry.gwu.edu/bco/BCO_00067092", "ca34683b739b6c283adc89bd9bdcbaa5c5f1056037164a8b2934567955a60420", meta_URI);

// PROVINANCE DOMAIN
var created = new DateTime(2022, 05, 17, 18, 54, 48, 0.876, 0);
var modified = new DateTime(2022, 06, 01, 13, 08, 45, 0.481, 0);
var version1 = new SemanticVersion(3, 0, 0);
var contr1 = new Contributor("authoredBy", "David P. Astling", "Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine", "david.astling@example.com", "https://orcid.org/0000-0001-8179-0304");
var contr2 = new Contributor("authoredBy", "Ilea E. Heft", "Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine", "ilea.heft@example.com", "https://orcid.org/0000-0002-7759-7007");
var contr3 = new Contributor("authoredBy", "James M. Sikela", 'Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine', "james.sikela@example.com", 'https://orcid.org/0000-0001-5820-2762');
var contr4 = new Contributor("authoredBy", "Kenneth L. Jones", "Department of Pediatrics, University of Colorado School of Medicine" , "kenneth.jones@example.com", null);
var contr5 = new Contributor("createdBy", "Jonathon Keeney", "GWU", "keeneyjg@gwu.edu", null);
var contr6 = new Contributor("createdBy", "Alex Nguyen", "UVA", "tan5um@virginia.edu", null);
var contr7 = new Contributor("ceatedBy", "Mike Taylor", "GWU", null, "https://orcid/0000-0002-1003-5675");
const contributorsList = [contr1, contr2, contr3, contr4, contr5, contr6];
var rev1 = new Review(null, "unreviewed", null, contr7);
var reviewersList = [rev1];
var prov_139 = new ProvenanceDomain("WGS Simulation of DUF1220 Regions", "https://opensource.org/licenses/MIT", version1, created, modified, contributorsList, reviewersList, null, null, null);


// DESCRIPTION DOMAIN
const keywordsArr = ["Copy Number Variation", "CNV", "DUF1220", "Genome Informatics", "Next-generation sequencing", "Bioinformatics"];

// Each pipeline step needs its own 2 arrays of inputs and outputs.
input_0_URI = "https://github.com/dpastling/plethora/blob/master/code/1000genomes/1_download.sh";
output_0_URI = "https://github.com/dpastling/plethora/blob/master/data/1000Genomes_samples.txt";
var input_0 = new Input(input_0_URI, null);
var output_0 = new Output(output_0_URI, null);
const inputArr0 = [input_0];
const outputArr0 = [output_0];
var pipelineStp0 = new PipelineSteps(0, "Script to download fastq files from the 1000 Genomes Project", "This script downloads the fastq files for each sample from the 1000 Genomes site as specified in a sample_index file", inputArr0, outputArr0, null);

input_1_URI = "https://github.com/dpastling/plethora/blob/master/code/1000genomes/2_trim.sh";
output_1_URI = "https://github.com/dpastling/plethora/blob/master/logs/trim_stats.txt";
var input_1 = new Input(input_1_URI, null);
var output_1 = new Output(output_1_URI, null);
const inputArr1 = [input_1];
const outputArr1 = [output_1];
var pipelineStp1 = new PipelineSteps(1, "Script to trim and filter the reads", "This script automates the task of trimming low quality bases from the 3' ends of the reads and removes any that are shorter than 80 bp.", inputArr1, outputArr1, null);

input_2_URI = "https://github.com/dpastling/plethora/blob/master/code/1000genomes/3_batch_bowtie.sh";
output_2_URI = "https://github.com/dpastling/plethora/blob/master/align_report.txt";
var input_2 = new Input(input_2_URI, null);
var output_2 = new Output(output_2_URI, null);
const inputArr2 = [input_2];
const outputArr2 = [output_2];
var pipelineStp2 = new PipelineSteps(2, "Script to align reads to the genome", "This script aligns reads to the genome with Bowtie2.", inputArr2, outputArr2, null);

input_3_URI = "https://github.com/dpastling/plethora/blob/master/code/1000genomes/5_batch_make_bed.sh";
output_3_URI = "https://github.com/dpastling/plethora/blob/master/results/test_read_depth.bed";
var input_3 = new Input(input_3_URI, null);
var output_3 = new Output(output_3_URI, null);
const inputArr3 = [input_3];
const outputArr3 = [output_3];
var pipelineStp3 = new PipelineSteps(3, "Script to calculate coverage for each DUF1220 domain", "This script: Coverts the .bam alignment file into bed format. Parses the reads Calls the merge_pairs.pl script (described below) to combined proper pairs into a single fragment. Finds overlaps with the reference bed file containing the regions of interest (e.g. DUF1220). Calculates the average coverage for each region: (number of bases that overlap) / (domain length)", inputArr3, outputArr3, null);

const pipelineSteps = [pipelineStp0, pipelineStp1, pipelineStp2, pipelineStp3];
var descrpt_139 = new DescriptionDomain(keywordsArr, pipelineSteps, null, null);


// EXECUTION DOMAIN
softwrePrereq1_URI = "http://bowtie-bio.sourceforge.net/bowtie2/index.shtml";
softwrePrereq2_URI = "https://bedtools.readthedocs.io/en/latest/";
softwrePrereq3_URI = "http://samtools.sourceforge.net/";
softwrePrereq4_URI = "https://cutadapt.readthedocs.io/en/stable/";

var bow_Version = new SemanticVersion(2, 2, 9);
var bed_Version = new SemanticVersion(2, 17, 0);
var sam_Version = new SemanticVersion(0, 1, 19); //"0.1.19-44428cd"
var ca_Version = new SemanticVersion(1, 12, 0); 
softwrePrereq1 = new SoftwarePrerequisites("Bowtie 2", bow_Version, softwrePrereq1_URI);
var softwrePrereq2 = new SoftwarePrerequisites("Bed Tools", bed_Version, softwrePrereq2_URI);
var softwrePrereq3 = new SoftwarePrerequisites("Sam Tools", sam_Version, softwrePrereq3_URI);
var softwrePrereq4 = new SoftwarePrerequisites("Cut Adapt", ca_Version, softwrePrereq4_URI);
const softwrePrereqs = [softwrePrereq1, softwrePrereq2, softwrePrereq3, softwrePrereq4];
var externalDataEndpoint1 = new ExternalDataEndpoints("IGSR", "https://www.internationalgenome.org/");
const extDataEndPts = [externalDataEndpoint1];
script1_URI = "https://github.com/dpastling/plethora/blob/master/code/1000genomes/1_download.sh";
script2_URI = "https://github.com/dpastling/plethora/blob/master/code/1000genomes/2_trim.sh";
script3_URI = "https://github.com/dpastling/plethora/blob/master/code/1000genomes/3_batch_bowtie.sh";
script4_URI = "https://github.com/dpastling/plethora/blob/master/code/1000genomes/5_batch_make_bed.sh";
const scripts = [script1_URI, script2_URI, script3_URI, script4_URI];
env_Var1 = new EnvironmentVariable("HOSTTYPE: ", "x86_64-linux");
env_Var2 = new EnvironmentVariable("EDITOR: ", "vim");
environment_Variables = [env_Var1, env_Var2];
var excn_139 = new ExecutionDomain(scripts, "Shell", softwrePrereqs, extDataEndPts, environment_Variables);



//IO DOMAIN
inputSub1_URI = "https://github.com/dpastling/plethora/blob/master/fastq/test_1.fastq.gz";
inputSub2_URI = "https://github.com/dpastling/plethora/blob/master/fastq/test_2.fastq.gz";
outputSub_URI = "https://github.com/dpastling/plethora/blob/master/results/test_read_depth.bed";
var inputSub1 = new InputSubdomain(inputSub1_URI, null);
var inputSub2 = new InputSubdomain(inputSub2_URI, null);
var outputSub = new OutputSubdomain(outputSub_URI, "test_read_depth.bed");
const inputSubDmn = [inputSub1, inputSub2];
const outputSubDmn = [outputSub];
var io_139 = new IODomain(inputSubDmn, outputSubDmn);


//ERROR DOMAIN
empError1 = new EmpiricalError("CON1: 1.55");
empError2 = new EmpiricalError("CON2: 0.91");
empError3 = new EmpiricalError("CON3: 0.26");
empError4 = new EmpiricalError("HLS1: 0.99");
empError5 = new EmpiricalError("HLS2: 1.90");
empError6 = new EmpiricalError("HLS3: 1.67");
root_Mean_Sqr_Error = [empError1, empError2, empError3, empError4, empError5, empError6];
error_139 = new ErrorDomain(root_Mean_Sqr_Error, null);

// EXTENSION DOMAIN SHOULD BE SET TO null
// USABIITY DOMAIN IS A STRING DOES NOT NEED TO BE MADE AN OBJECT

var BCO_000139 = new BioComputeObject(meta_139,    "Pipeline for identifying copy number of genetic sequences independent of the genes in which they occur, and with higher fidelity than existing methods. Approximately 25 individuals were randomly chosen from each of the CEU, YRI, CHB, JPT, MXL, CLM, PUR, ASW, LWK, CHS, TSI, IBS, FIN, and BGR populations for a total of 324 individuals. Where domains were more than 1 kb apart, the boundaries of the domains were extended up to 250 bp to allow the possibility of capturing unique sequence directly adjacent to the domain. No intermediate files were generated because the commands were run executed as a pipe at the command line, so T:/dev/tmpfs was used for the file IOs in the Description Domain. This example pipeline was created based on the work of Astling et al. doi: 10.1186/s12864-017-3976-z"
, prov_139, excn_139, null, descrpt_139, null, io_139);


//BCO_000139.validate(meta_139, "Pipeline for identifying copy number of genetic sequences independent of the genes in which they occur, and with higher fidelity than existing methods. Approximately 25 individuals were randomly chosen from each of the CEU, YRI, CHB, JPT, MXL, CLM, PUR, ASW, LWK, CHS, TSI, IBS, FIN, and BGR populations for a total of 324 individuals. Where domains were more than 1 kb apart, the boundaries of the domains were extended up to 250 bp to allow the possibility of capturing unique sequence directly adjacent to the domain. No intermediate files were generated because the commands were run executed as a pipe at the command line, so T:/dev/tmpfs was used for the file IOs in the Description Domain. This example pipeline was created based on the work of Astling et al. doi: 10.1186/s12864-017-3976-z"
//, prov_139, excn_139, null, descrpt_139, null, io_139);

console.log(BCO_000139, '\n');
console.log('\n', BCO_000139.description_Domain, '\n');
console.log('\n', BCO_000139.execution_Domain, '\n')
console.log('\n', BCO_000139.provenance_Domain, '\n')
console.log("Finished");



// MORE NOTES: 
// URI string
// Create an array for contributions 
// Create ORCID object
