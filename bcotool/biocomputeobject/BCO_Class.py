# Author(s):

import itertools
from pprint import pprint
# import subprocess
import json
import requests
# ************************************** BIOCOMPUTE + DOMAIN + HELPER CLASS DEFINITIONS  ***************************************

class BioComputeObject:
    def __init__(self, metaData, usability_Domain, provenance_Domain, execution_Domain, extension_Domain, description_Domain, error_Domain, io_Domain, parametric_Domain):
        self.metaData = metaData                       
        self.usability_Domain = usability_Domain    
        self.provenance_Domain = provenance_Domain   
        self.execution_Domain = execution_Domain     
        self.extension_Domain = extension_Domain    
        self.description_Domain = description_Domain 
        self.error_Domain = error_Domain
        self.io_Domain = io_Domain
        self.parametric_Domain = parametric_Domain

    def __repr__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(self.metaData, self.usability_Domain, self.provenance_Domain, self.execution_Domain, self.extension_Domain, self.description_Domain, self.error_Domain, self.io_Domain, self.parametric_Domain)
    # TESTED
    def validate(self, metaData, usability_Domain, provenance_Domain, execution_Domain, extension_Domain, description_Domain, error_Domain, io_Domain, parametric_Domain):
        reqArgs = [usability_Domain, provenance_Domain, execution_Domain, description_Domain, io_Domain]
        for i in reqArgs:
            if i is None:
                print("INVALID BIOCOMPUTE CLASS OBJECT: " ,'\n', "- missing required argument")
                return False

        argTypes = {
            metaData : Meta,
            provenance_Domain : ProvenanceDomain,
            execution_Domain : ExecutionDomain,
            extension_Domain : ExtensionDomain,
            description_Domain : DescriptionDomain,
            error_Domain : ErrorDomain,
            io_Domain : IODomain
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                print("INVALID BIOCOMPUTE CLASS OBJECT: " , '\n',  "- incorrect type")
                return False
        if not isinstance(parametric_Domain, list) and not parametric_Domain is None:
            return False
        if not isinstance(usability_Domain, list) or usability_Domain is None:
            return False
        print("VALID BIOCOMPUTE CLASS OBJECT")
        return True

    

    @property
    def meta(self):
        return self.metaData

    @meta.setter
    def meta(self, metaObj):
        self.metaData = metaObj

    @property
    def use(self):
        return self.usability_Domain

    @use.setter
    def use(self, usability):
        if usability is None:
            print("This is a required field")
            raise ValueError
        self.usability_Domain = usability

    @property
    def prov(self):
        return self.provenance_Domain

    @prov.setter
    def prov(self, prov):
        if prov is None:
            print("This is a required field")
            raise ValueError
        self.provenance_Domain = prov

    @property
    def execution(self):
        return self.execution_Domain
 
    @execution.setter
    def execution(self, execution):
        if execution is None:
            print("This is a required field")
            raise ValueError
        self.execution_Domain = execution

    @property
    def extension(self):
        return self.extension

    @extension.setter
    def extension(self, ext):
        self.extension_Domain = ext
    
    @property
    def description(self):
        return self.description_Domain

    @description.setter
    def description(self, desc):
        if desc is None:
            print("This is a required field")
            raise ValueError
        self.description_Domain = desc

    @property
    def error(self):
        return self.error_Domain

    @error.setter
    def error(self, err):
        self.error_Domain = err

    @property
    def io(self):
        return self.io_Domain

    @io.setter
    def io(self, IO):
        if IO is None:
            print("This is a required field")
            raise ValueError
        self.io_Domain = IO
        
    def updateMeta(self, newMeta):
        self.meta = newMeta
        return self.metaData
    
    def updateProvenance(self, newProv):
        self.prov = newProv
        return self.provenance_Domain

    def updateUsability(self, newUse):
        self.use = newUse
        return self.usability_Domain

    def updateExecution(self, newExe):
        self.execution = newExe
        return self.execution_Domain

    def updateExtention(self, newExt):
        self.extension = newExt
        return self.extension_Domain

    def updateDescription(self, newDesc):
        self.description = newDesc
        return self.description_Domain

    def updateError(self, newErr):
        self.error = newErr
        return self.error_Domain

    def updateIO(self, newIO):
        self.io = newIO
        return self.io_Domain

class Meta:
    def __init__(self, bco_Id, etag, spec_Version):
        self.bco_Id = bco_Id
        self.etag = etag
        self.spec_Version = spec_Version
    
    def __repr__(self):
        return '{} {} {}'.format(self.bco_Id, self.etag, self.spec_Version)
    # TESTED
    def validate(self, bco_Id, etag, spec_Version):
        argTypes = {
            bco_Id : ObjectID,
            etag : str,
            spec_Version : URI
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) or x is None:
                return False
        return True

    @property
    def bcoId(self):
        return self.bco_Id

    @bcoId.setter
    def bcoId(self, id):
        if id is None:
            print("This is a required field")
            raise ValueError
        self.io_Domain = id

    @property
    def e_tag(self):
        return self.etag

    @e_tag.setter
    def e_tag(self, tag):
        if tag is None:
            print("This is a required field")
            raise ValueError
        self.etag = tag

    @property
    def version(self):
        return self.spec_Version

    @version.setter
    def version(self, specVers):
        if specVers is None:
            print("This is a required field")
            raise ValueError
        self.spec_Version = specVers
    

class ProvenanceDomain:
    def __init__(self, name, license, version, created, modified, contributors, review, embargo, obsolete_After, derived_From):
        self.name = name
        self.license = license
        self.version = version
        self.created = created
        self.modified = modified
        self.contributors = contributors
        self.review = review
        self.embargo = embargo
        self.obsolete_After = obsolete_After
        self.derived_From = derived_From

    def __repr__(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.name, self.license, self.version, self.created, self.modified, self.contributors, self.review, self.embargo, self.obsolete_After, self.derived_From)

    # TESTED
    def validate(self, name, license, version, created, modified, contributors, review, embargo, obsolete_After, derived_From):
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

    @property
    def provName(self):
        return self.name

    @provName.setter
    def provName(self, nm):
        if nm is None:
            print("This is a required field")
            raise ValueError
        self.name = nm

    @property
    def provLicense(self):
        return self.license

    @provLicense.setter
    def provLicense(self, lnse):
        if lnse is None:
            print("This is a required field")
            raise ValueError
        self.license = lnse

    @property
    def provVersion(self):
        return self.version

    @provVersion.setter
    def provVersion(self, versn):
        if versn is None:
            print("This is a required field")
            raise ValueError
        self.version = versn

    @property
    def provCreated(self):
        return self.created

    @provCreated.setter
    def provCreated(self, create):
        if create is None:
            print("This is a required field")
            raise ValueError
        self.created = create

    @property
    def provModified(self):
        return self.modified

    @provModified.setter
    def provModified(self, mod):
        if mod is None:
            print("This is a required field")
            raise ValueError
        self.modified = mod

    @property
    def provContributors(self):
        return self.contributors

    @provContributors.setter
    def provContributors(self, cont):
        if cont is None:
            print("This is a required field")
            raise ValueError
        self.contributors = cont

    @property
    def provReview(self):
        return self.review

    @provReview.setter
    def provReview(self, rev):
        self.review = rev

    @property
    def provEmbargo(self):
        return self.embargo

    @provEmbargo.setter
    def provEmbargo(self, emb):
        self.embargo = emb

    @property
    def provObsolete(self):
        return self.obsolete_After

    @provObsolete.setter
    def provObsolete(self, obs):
        self.obsolete_After = obs

    @property
    def provDerived(self):
        return self.derived_From

    @provDerived.setter
    def provDerived(self, drv):
        self.derived_From = drv


class Contributor:
    def __init__(self, contribution, name, affiliation, email, orcid):
        self.contribution = contribution
        self.name = name
        self.affiliation = affiliation
        self.email = email
        self.orcid = orcid

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.contribution, self.name, self.affiliation, self.email, self.orcid)

    # TESTED
    def validate(self, contribution, name, affiliation, email, orcid):
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

    @property
    def contName(self):
        return self.name

    @contName.setter
    def contName(self, n):
        if n is None:
            print("This is a required field")
            raise ValueError
        self.name = n

    @property
    def contContribution(self):
        return self.contribution

    @contContribution.setter
    def contContribution(self, contr):
        self.contribution = contr

    @property
    def contAffiliation(self):
        return self.affiliation

    @contAffiliation.setter
    def contAffiliation(self, aff):
        self.affiliation = aff

    @property
    def contEmail(self):
        return self.email

    @contEmail.setter
    def contEmail(self, em):
        self.email = em

    @property
    def contOrcid(self):
        return self.orcid

    @contOrcid.setter
    def contOrcid(self, orc):
        self.orcid = orc


class Review:
    def __init__(self, date, status, revName, reviewer_Comment, contribution, affiliation, email, orcid):
        self.date = date
        self.status = status
        self.revName = revName
        self.reviewer_Comment = reviewer_Comment
        self.contribution = contribution
        self.affiliation = affiliation
        self.email = email
        self.orcid = orcid

    def __repr__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.date, self.status, self.revName, self.reviewer_Comment, self.contribution, self.affiliation, self.email, self.orcid)

    # TESTED
    def validate(self, date, status, revName, reviewer_Comment, contribution, affiliation, email, orcid):
        if status is None or revName is None:
            return False

        argTypes = {
            date : DateTime,
            status : str,
            revName : str,
            reviewer_Comment : str,
            contribution : str,
            affiliation : str,
            email : str,
            orcid : str
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False
        return True

    @property
    def revStatus(self):
        return self.status

    @revStatus.setter
    def revStatus(self, stat):
        if stat is None:
            print("This is a required field")
            raise ValueError
        self.status = stat

    @property
    def revContributor(self):
        return self.contributor

    @revContributor.setter
    def revContributor(self, con):
        if con is None:
            print("This is a required field")
            raise ValueError
        self.contributor = con

    @property
    def revDate(self):
        return self.date

    @revDate.setter
    def revDate(self, dt):
        self.date = dt

    @property
    def revComm(self):
        return self.reviewer_Comment

    @revComm.setter
    def revComm(self, rc):
        self.reviewer_Comment = rc


class Embargo:
    def __init__(self, start_Time, end_Time):
        self.start_Time = start_Time
        self.end_Time = end_Time

    def __repr__(self):
        return '{} {}'.format(self.start_Time, self.end_Time)

    # NOT TESTED
    def validate(self, start_Time, end_Time):
        argTypes = {
            start_Time : DateTime,
            end_Time : DateTime
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and x is None:
                return False
        return True

    @property
    def start(self):
        return self.start_Time

    @start.setter
    def start(self, st):
        if st is None:
            print("This is a required field")
            raise ValueError
        self.start_Time = st

    @property
    def end(self):
        return self.end_Time

    @end.setter
    def end(self, et):
        if et is None:
            print("This is a required field")
            raise ValueError
        self.end_Time = et


class ExecutionDomain:
    def __init__(self, script, script_Driver, software_Prerequisites, external_Data_Endpoints, environment_Variables):
        self.script = script
        self.script_Driver = script_Driver
        self.software_Prerequisites = software_Prerequisites
        self.external_Data_Endpoints = external_Data_Endpoints
        self.environment_Variables = environment_Variables

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.script, self.script_Driver, self.software_Prerequisites, self.external_Data_Endpoints, self.environment_Variables)

    # TESTED
    def validate(self, script, script_Driver, software_Prerequisites, external_Data_Endpoints, environment_Variables):
        reqArgs = [script, script_Driver, software_Prerequisites, external_Data_Endpoints]
        for r in reqArgs:
            if r is None:
                return False

        listArgs = [script, software_Prerequisites, external_Data_Endpoints]
        if not isinstance(script_Driver, str) and not script_Driver is None:
            return False

        if not isinstance( environment_Variables, EnvironmentVariable) and not environment_Variables is None:
            return False

        #lists are not hashable, they cannot be used in map, need to check these types sparately
        for y in listArgs:
            if not isinstance(y, list) and not y is None:
                return False
        return True

    @property
    def exScript(self):
        return self.script

    @exScript.setter
    def exScript(self, scpt):
        if scpt is None:
            print("This is a required field")
            raise ValueError
        self.script = scpt

    @property
    def scriptDr(self):
        return self.script_Driver

    @scriptDr.setter
    def scriptDr(self, sd):
        if sd is None:
            print("This is a required field")
            raise ValueError
        self.script_Driver = sd

    @property
    def swPrereqs(self):
        return self.software_Prerequisites

    @swPrereqs.setter
    def swPrereqs(self, swp):
        if swp is None:
            print("This is a required field")
            raise ValueError
        self.software_Prerequisites = swp

    @property
    def extDataEP(self):
        return self.external_Data_Endpoints

    @extDataEP.setter
    def extDataEP(self, edep):
        if edep is None:
            print("This is a required field")
            raise ValueError
        self.external_Data_Endpoints = edep

    @property
    def envVars(self):
        return self.environment_Variables

    @envVars.setter
    def envVars(self, enVrs):
        self.environment_Variables = enVrs


class EnvironmentVariable:
    def __init__(self, name, variable):
        self.name = name
        self.variable = variable

    def __repr__(self):
        return '{} {}'.format(self.name, self.variable)

    # TESTED
    def validate(self, name, variable):
        # argTypes = {
        #     name : str,
        #     variable : str
        # }
        args = [name, variable]

        for x in args:
            if not isinstance(x, list) or x is None:
                return False
        return True

    @property
    def envVarName(self):
        return self.name

    @envVarName.setter
    def envVarName(self, n):
        if n is None:
            print("This is a required field")
            raise ValueError
        self.name = n

    @property
    def envVariable(self):
        return self.variable

    @envVariable.setter
    def envVariable(self, var):
        if var is None:
            print("This is a required field")
            raise ValueError
        self.variable = var

class SoftwarePrerequisites:
    def __init__(self, name, version, uri, filename, access_Time, sha1_Checksum):
        self.name = name
        self.version = version
        self.uri = uri
        self.filename = filename
        self.access_Time = access_Time
        self.sha1_Checksum = sha1_Checksum

    def __repr__(self):
        return '{} {} {} {} {} {}'.format(self.name, self.version, self.uri, self.filename, self.access_Time, self.sha1_Checksum)

    # TESTED
    def validate(self, name, version, uri, filename, access_Time, sha1_Checksum):
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

    @property
    def spName(self):
        return self.name

    @spName.setter
    def spName(self, nm):
        if nm is None:
            print("This is a required field")
            raise ValueError
        self.name = nm

    @property
    def spVersion(self):
        return self.version

    @spVersion.setter
    def spVersion(self, vers):
        if vers is None:
            print("This is a required field")
            raise ValueError
        self.version = vers

    @property
    def spUri(self):
        return self.uri

    @spUri.setter
    def spUri(self, URI):
        if URI is None:
            print("This is a required field")
            raise ValueError
        self.uri = URI

    @property
    def spFileName(self):
        return self.fileName

    @spFileName.setter
    def spFileName(self, fn):
        self.fileName = fn

    @property
    def spAccess(self):
        return self.access_Time

    @spAccess.setter
    def spAccess(self, at):
        self.access_Time = at

    @property
    def check(self):
        return self.sha1_Checksum

    @check.setter
    def check(self, shCh):
        self.sha1_Checksum = shCh

class ExternalDataEndpoints:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return '{} {}'.format(self.name, self.url)

    # TESTED
    def validate(self, name, url):
        argTypes = {
            name : str,
            url : str
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) or x is None:
                return False
        return True

    @property
    def extName(self):
        return self.name

    @extName.setter
    def extName(self, nm):
        if nm is None:
            print("This is a required field")
            raise ValueError
        self.name = nm

    @property
    def extUri(self):
        return self.uri

    @extUri.setter
    def extUri(self, URI):
        if URI is None:
            print("This is a required field")
            raise ValueError
        self.uri = URI


class ExtensionDomain:
    def _init_(self, extension_schema, extension_scm):
        self.extension_schema = extension_schema
        self.extension_scm = extension_scm
    def __repr__(self):
        return '{} {} {} {}'.format(self.extension_schema, self.extension_scm) 
    
    def validate(self, extension_schema, extension_scm):
        if extension_schema is None:
            return None
        if extension_scm is None:
            return None
        
        argTypes = [extension_schema]
        if not extension_schema is None:
             for x in argTypes:
                 if not isinstance(x, list) and not x is None:
                    return False
             return True
    
    @property
    def extensionSchema(self):
        return self.extension_schema
    
    @extensionSchema.setter
    def extensionSchema(self, sch):
        self.extension_schema = sch
        
    @property
    def extension_scm(self):
        return self.extension_scm
    
    @extension_scm.setter
    def extension_scm(self, scm):
        self.extension_scm = scm


class DescriptionDomain:
    def __init__(self, keywords, pipeline_Step, platform, xref):
        self.keywords = keywords
        self.pipeline_Step = pipeline_Step
        self.platform = platform
        self.xref = xref

    def __repr__(self):
        return '{} {} {} {}'.format(self.keywords, self.pipeline_Step, self.platform, self.xref)

    # TESTED
    def validate(self, keywords, pipeline_Step, platform, xref):
        if pipeline_Step is None:
            return False
    
        argTypes = [keywords, pipeline_Step, platform, xref]
        
        #lists are not hashable, they cannot be used in map, need to check these types sparately
        for x in argTypes:
            if not isinstance(x, list) and not x is None:
                return False
        return True

    @property
    def pipeLine(self):
        return self.pipeline_Step

    @pipeLine.setter
    def pipeLine(self, pipe):
        if pipe is None:
            print("This is a required field")
            raise ValueError
        self.pipeline_Step = pipe

    @property
    def descKeyword(self):
        return self.keywords

    @descKeyword.setter
    def descKeyword(self, kw):
        self.keywords = kw

    @property
    def descPlatform(self):
        return self.platform

    @descPlatform.setter
    def descPlatform(self, pf):
        self.platform = pf

    @property
    def descXref(self):
        return self.xref

    @descXref.setter
    def descXref(self, xr):
        self.xref = xr


class PipelineSteps:
    def __init__(self, step_Number, name, description, input_List, output_List, version, prerequisites_List):
        self.step_Number = step_Number
        self.name = name
        self.description = description
        self.input_List = input_List
        self.output_List = output_List
        self.version = version
        self.prerequisites_List = prerequisites_List

    def __repr__(self):
        return '{} {} {} {} {} {} {}'.format(self.step_Number, self.name, self.version, self.description, self.input_List, self.output_List, self.prerequisites_List)

    # TESTED
    def validate(self, step_Number, name, description, input_List, output_List, version, prerequisites_List):
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
        elif not isinstance(prerequisites_List, list):
            return False
        return True

    @property
    def step(self):
        return self.step_Number

    @step.setter
    def step(self, sn):
        if sn is None:
            print("This is a required field")
            raise ValueError
        self.step_Number = sn

    @property
    def psName(self):
        return self.name

    @psName.setter
    def psName(self, nm):
        if nm is None:
            print("This is a required field")
            raise ValueError
        self.name = nm

    @property
    def psDescription(self):
        return self.description

    @psDescription.setter
    def psDescription(self, desc):
        if desc is None:
            print("This is a required field")
            raise ValueError
        self.description = desc

    @property
    def input(self):
        return self.input_List

    @input.setter
    def input(self, inlst):
        if inlst is None:
            print("This is a required field")
            raise ValueError
        self.input_List = inlst

    @property
    def output(self):
        return self.output_List

    @output.setter
    def output(self, outlst):
        if outlst is None:
            print("This is a required field")
            raise ValueError
        self.output_List = outlst

    @property
    def psVersion(self):
        return self.version

    @psVersion.setter
    def psVersion(self, vrs):
        if vrs is None:
            print("This is a required field")
            raise ValueError
        self.version = vrs


class Input:
    def __init__(self, uri, filename, access_Time, sha1_Checksum):
        self.uri = uri
        self.filename = filename
        self.access_Time = access_Time
        self.sha1_Checksum = sha1_Checksum

    def __repr__(self):
        return '{} {} {} {}'.format(self.uri, self.filename, self.access_Time, self.sha1_Checksum)

    # TESTED
    def validate(self, uri, filename, access_Time, sha1_Checksum):
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

    @property
    def inUri(self):
        return self.uri

    @inUri.setter
    def inUri(self, URI):
        if URI is None:
            print("This is a required field")
            raise ValueError
        self.uri = URI

    @property
    def inFilename(self):
        return self.filename

    @inFilename.setter
    def inFilename(self, fn):
        self.filename = fn

    @property
    def accessTime(self):
        return self.access_Time

    @accessTime.setter
    def accessTime(self, at):
        self.access_Time = at

    @property
    def shCheck(self):
        return self.sha1_Checksum

    @shCheck.setter
    def shCheck(self, sc):
        self.sha1_Checksum = sc


class Output:
    def __init__(self, uri, filename, access_Time, sha1_Checksum):
        self.uri = uri
        self.filename = filename
        self.access_Time = access_Time
        self.sha1_Checksum = sha1_Checksum

    def __repr__(self):
        return '{} {} {} {}'.format(self.uri, self.filename, self.access_Time, self.sha1_Checksum)

    # TESTED
    def validate(self, uri, filename, access_Time, sha1_Checksum):
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

    @property
    def outUri(self):
        return self.uri

    @outUri.setter
    def outUri(self, URI):
        if URI is None:
            print("This is a required field")
            raise ValueError
        self.uri = URI

    @property
    def outFilename(self):
        return self.filename

    @outFilename.setter
    def outFilename(self, fn):
        self.filename = fn

    @property
    def accessTime(self):
        return self.access_Time

    @accessTime.setter
    def accessTime(self, at):
        self.access_Time = at

    @property
    def shCheck(self):
        return self.sha1_Checksum

    @shCheck.setter
    def shCheck(self, sc):
        self.sha1_Checksum = sc


class Prerequisite:
    def __init__(self, name, uri, filename, access_Time, sha1_Checksum):
        self.name = name
        self.uri = uri
        self.filename = filename
        self.access_Time = access_Time
        self.sha1_Checksum = sha1_Checksum

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.name, self.uri, self.filename, self.access_Time, self.sha1_Checksum)

    # NOT TESTED
    def validate(self, name, uri, filename, access_Time, sha1_Checksum):
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

    @property
    def preUri(self):
        return self.uri

    @preUri.setter
    def preUri(self, URI):
        if URI is None:
            print("This is a required field")
            raise ValueError
        self.uri = URI

    @property
    def preName(self):
        return self.name

    @preName.setter
    def preName(self, nm):
        self.name = nm

    @property
    def preFilename(self):
        return self.filename

    @preFilename.setter
    def preFilename(self, fn):
        self.filename = fn

    @property
    def accessTime(self):
        return self.access_Time

    @accessTime.setter
    def accessTime(self, at):
        self.access_Time = at

    @property
    def shCheck(self):
        return self.sha1_Checksum

    @shCheck.setter
    def shCheck(self, sc):
        self.sha1_Checksum = sc

class Xref:
    def __init__(self, namespace, name, ids, access_Time):
        self.namespace = namespace
        self.name = name
        self.ids = ids
        self.access_Time = access_Time

    def __repr__(self):
        return '{} {} {} {}'.format(self.namespace, self.name, self.ids, self.access_Time)

    # NOT TESTED
    def validate(self, namespace, name, ids, access_Time):
        argTypes = {
            namespace : str,
            name : str,
            access_Time : DateTime,
            ids : int
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) or x is None:
                return False

        #lists are not hashable, they cannot be used in map, need to check these types sparately
        if not isinstance(ids, list) or ids is None:
            return False
        return True

    @property
    def xName(self):
        return self.name

    @xName.setter
    def xName(self, nm):
        self.name = nm

    @property
    def nspace(self):
        return self.namespace

    @nspace.setter
    def nspace(self, ns):
        self.namespace = ns

    @property
    def accessTime(self):
        return self.access_Time

    @accessTime.setter
    def accessTime(self, at):
        self.access_Time = at

    @property
    def id(self):
        return self.ids

    @id.setter
    def id(self, ID):
        self.ids = ID


class ErrorDomain:
    def __init__(self, empirical_Error, algorithmic_Error):
        self.empirical_Error = empirical_Error
        self.algorithmic_Error = algorithmic_Error

    def __repr__(self):
        return '{} {}'.format(self.empirical_Error, self.algorithmic_Error)

    # TESTED
    def validate(self, empirical_Error, algorithmic_Error):
        argTypes = [empirical_Error, algorithmic_Error]

        #lists are not hashable, they cannot be used in map, need to check these types sparately
        for x in argTypes:
            if not isinstance(x, str) and not x is None:
                return False
        return True

    @property
    def empErr(self):
        return self.empirical_Error

    @empErr.setter
    def empErr(self, er):
        self.empirical_Error = er

    @property
    def algErr(self):
        return self.algorithmic_Error

    @algErr.setter
    def algErr(self, ae):
        self.algorithmic_Error = ae
        

# empirically determined values such as limits of detectability, false positives, false negatives, statistical confidence of outcomes, etc.
class EmpiricalError:
    def __init__(self, empError):
        self.empError = empError

    def __repr__(self):
        return '{}'.format(self.empError)

    # TESTED
    def validate(self, empError):
        if empError is None or not isinstance(empError, str):
            return False
        return True

    @property
    def err(self):
        return self.empError

    @err.setter
    def err(self, er):
        if er is None:
            print("This is a required field")
            raise ValueError
        self.empError = er


class AlgorithmicError:
    def __init__(self, algError):
        self.algError = algError

    def __repr__(self):
        return '{}'.format(self.algError)

    # NOT TESTED
    def validate(self, algError):
        if algError is None or not isinstance(algError, str):
            return False
        return True

    @property
    def err(self):
        return self.algError

    @err.setter
    def err(self, ag):
        if ag is None:
            print("This is a required field")
            raise ValueError
        self.algError = ag


class InputSubdomain:
    def __init__(self, uri, filename, accessTime, checksum):
        self.uri = uri
        self.filename = filename
        self.accessTime = accessTime
        self.checksum = checksum

    def __repr__(self):
        return '{} {} {} {}'.format(self.uri, self.filename, self.accessTime, self.checksum)

    def validate(self, uri, filename, accessTime, checksum):
        if uri is None or not isinstance(uri, URI):
            return False
        elif not filename is None and not isinstance(filename, str):
            return False
        elif not accessTime is None and not isinstance(accessTime, DateTime):
            return False
        elif not checksum is None and not isinstance(checksum, str):
            return False
        return True

    @property
    def isUri(self):
        return self.uri

    @isUri.setter
    def isUri(self, URI):
        if URI is None:
            print("This is a required field")
            raise ValueError
        self.uri = URI

    @property
    def isFilename(self):
        return self.filename

    @isFilename.setter
    def isFilename(self, fn):
        if fn is None:
            print("This is a required field")
            raise ValueError
        self.filename = fn


class OutputSubdomain:
    def __init__(self, uri, filename, checksum, mediatype, accessTime):
        self.uri = uri
        self.filename = filename
        self.checksum = checksum
        self.mediatype = mediatype
        self.accessTime = accessTime

    def __repr__(self):
        return '{} {} {} {}'.format(self.uri, self.filename, self.checksum, self.mediatype, self.accessTime)

    def validate(self, uri, filename, checksum, mediatype, accessTime):
        if uri is None or not isinstance(uri, URI):
            return False
        elif not filename is None and not isinstance(filename, str):
            return False
        elif not mediatype is None and not isinstance(mediatype, str):
            return False
        elif not checksum is None and not isinstance(checksum, str):
            return False
        elif not accessTime is None and not isinstance(accessTime, DateTime):
            return False
        return True

    @property
    def osUri(self):
        return self.uri

    @osUri.setter
    def osUri(self, URI):
        if URI is None:
            print("This is a required field")
            raise ValueError
        self.uri = URI

    @property
    def osFilename(self):
        return self.filename

    @osFilename.setter
    def osFilename(self, fn):
        if fn is None:
            print("This is a required field")
            raise ValueError
        self.filename = fn


class IODomain:
    def __init__(self, input_Subdomain, output_Subdomain):
        self.input_Subdomain = input_Subdomain
        self.output_Subdomain = output_Subdomain

    def __repr__(self):
        return '{} {}'.format(self.input_Subdomain, self.output_Subdomain)

    # TESTED
    def validate(self, input_Subdomain, output_Subdomain):
        if input_Subdomain is None or not isinstance(input_Subdomain, list):
            return False
        elif output_Subdomain is None or not isinstance(output_Subdomain, list):
            return False
        return True

    @property
    def inputSD(self):
        return self.input_Subdomain

    @inputSD.setter
    def inputSD(self, isd):
        if isd is None:
            print("This is a required field")
            raise ValueError
        self.input_Subdomain = isd

    @property
    def outputSD(self):
        return self.output_Subdomain

    @outputSD.setter
    def outputSD(self, osd):
        if osd is None:
            print("This is a required field")
            raise ValueError
        self.output_Subdomain = osd


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
    def __init__(self, year, month, day, hour, minute, second, secondFrac, timeZoneOffSet):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.secondFrac = secondFrac
        self.timeZoneOffSet= timeZoneOffSet

    def __repr__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.year, self.month, self.day, self.hour, self.minute, self.second, self.secondFrac, self.timeZoneOffSet)

    # TESTED
    def validate(self, year, month, day, hour, minute, second, secondFrac, timeZoneOffSet):

        argTypes = {
            year : int,
            month : int,
            day : int,
            hour : int,
            minute : int,
            second : int,
            secondFrac : float,
            timeZoneOffSet : str
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) or x is None:
                return False
        return True

    @property
    def dtYear(self):
        return self.year

    @dtYear.setter
    def dtYear(self, yr):
        if yr is None:
            print("This is a required field")
            raise ValueError
        self.year = yr

    @property
    def dtMonth(self):
        return self.month

    @dtMonth.setter
    def dtMonth(self, m):
        if m is None:
            print("This is a required field")
            raise ValueError
        self.month = m

    @property
    def dtDay(self):
        return self.day

    @dtDay.setter
    def dtDay(self, d):
        if d is None:
            print("This is a required field")
            raise ValueError
        self.day = d

    @property
    def dtHour(self):
        return self.hour

    @dtHour.setter
    def dtHour(self, hr):
        if hr is None:
            print("This is a required field")
            raise ValueError
        self.hour = hr

    @property
    def dtMinute(self):
        return self.minute

    @dtMinute.setter
    def dtMinute(self, min):
        if min is None:
            print("This is a required field")
            raise ValueError
        self.minute = min

    @property
    def dtSecond(self):
        return self.second

    @dtSecond.setter
    def dtSecond(self, sec):
        if sec is None:
            print("This is a required field")
            raise ValueError
        self.second = sec

    @property
    def dtSecFraction(self):
        return self.secFraction

    @dtSecFraction.setter
    def dtSecFraction(self, sf):
        if sf is None:
            print("This is a required field")
            raise ValueError
        self.secondFraction = sf

    @property
    def tzone(self):
        return self.timeZoneOffSet

    @tzone.setter
    def tzone(self, tzo):
        if tzo is None:
            print("This is a required field")
            raise ValueError
        self.timeZoneOffSet = tzo


class ObjectID:
    def __init__(self, BCO_Id_Str):
        self.BCO_Id_Str = BCO_Id_Str

    def __repr__(self):
        return '{}'.format(self.BCO_Id_Str)

    # NOT TESTED
    def validate(self, BCO_Id_Str):
        if BCO_Id_Str is None or not isinstance(BCO_Id_Str, str):
            return False

    @property
    def idStr(self):
        return self.BCO_Id_Str

    @idStr.setter
    def idStr(self, BCOid):
        if BCOid is None:
            print("This is a required field")
            raise ValueError
        self.BCO_Id_Str = BCOid


class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __repr__(self):
        return '{} {} {}'.format(self.major, self.minor, self.patch)

    # TESTED
    def validate(self, major, minor, patch):
        argTypes = {
            major : int,
            minor : int,
            patch : int
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False
        return True

    @property
    def svMajor(self):
        return self.major

    @svMajor.setter
    def svMajor(self, mjr):
        if mjr is None:
            print("This is a required field")
            raise ValueError
        self.major = mjr

    @property
    def svMinor(self):
        return self.minor

    @svMinor.setter
    def svMinor(self, minr):
        if minr is None:
            print("This is a required field")
            raise ValueError
        self.minor = minr

    @property
    def svPatch(self):
        return self.patch

    @svPatch.setter
    def svPatch(self, pch):
        if pch is None:
            print("This is a required field")
            raise ValueError
        self.patch = pch


class URI:
    def __init__(self, uri_Str):
        self.uri_Str = uri_Str

    def __repr__(self):
        return '{}'.format(self.uri_Str)

    # NOT TESTED
    def validate(self, uri_str):
        # first four chars should be 'http'?
        return False

    @property
    def uri(self):
        return self.uri_str

    @uri.setter
    def uri(self, URI):
        if URI is None:
            print("This is a required field")
            raise ValueError
        self.uri_str = URI


class Script:
    def __init__(self, fileName, uri, accessTime, sha1_Checksum):
        self.fileName = fileName
        self.uri = uri
        self.accessTime = accessTime
        self.sha1_Checksum = sha1_Checksum

    def __repr__(self):
        return '{} {} {} {}'.format(self.fileName, self.uri, self.accessTime, self.sha1_Checksum)

    def validate(self, fileName, uri, accessTime, sha1_Checksum):
        if uri is None:
            return False

        argTypes = {
            fileName : str,
            uri : URI,
            accessTime : DateTime,
            sha1_Checksum : str
        }

        for x in argTypes:
            if not isinstance(x, argTypes[x]) and not x is None:
                return False
        return True

    @property
    def filename(self):
        return self.fileName

    @filename.setter
    def filename(self, FileName):
        self.fileName = FileName

    @property
    def sptURI(self):
        return self.uri

    @sptURI.setter
    def sptURI(self, newURI):
        self.uri = newURI
    
    @property
    def AccessTime(self):
        return self.accessTime

    @AccessTime.setter
    def AccessTime(self, at):
        self.accessTime = at


class Parametric():
    def __init__(self, step, parameter, value):
        self.step = step
        self. parameter = parameter
        self.value = value

    def __repr__(self):
        return '{} {} {}'.format(self.step, self.parameter, self.value)

    def validate(self, step, parameter, value):
        args = [step, parameter, value]
        for x in args:
            if not isinstance(x, str) or x is None:
                return False
        return True
    @property
    def stp(self):
        return self.step

    @stp.setter
    def stp(self, stepIn):
        self.fileName = stepIn

    @property
    def param(self):
        return self.parameter

    @param.setter
    def param(self, paramIn):
        self.parameter = paramIn
    
    @property
    def val(self):
        return self.value

    @val.setter
    def val(self, valIn):
        self.value = valIn
     





# ************************* INITIALIZE OBJECT ARGUMENTS TO MAKE BIOCOMPUTE CLASS OBJECT (BCO_00139) *****************************
# *************************************** TEST LOWER LEVEL VALIDATION FUNCTIONS *************************************************

# META
meta_URI = URI("https://w3id.org/ieee/ieee-2791-schema/")
meta_ObjId = ObjectID("https://portal.aws.biochemistry.gwu.edu/bco/BCO_00067092")
meta_139 = Meta(meta_ObjId, "ca34683b739b6c283adc89bd9bdcbaa5c5f1056037164a8b2934567955a60420", meta_URI)


# PROVINANCE DOMAIN
created = DateTime(2022, 5, 17, 18, 54, 48, 0.876, 0)
modified = DateTime(2022, 6, 1, 13, 8, 45, 0.481, 0)
version1 = SemanticVersion(3, 0, 0)
badCreated = DateTime(None, 5, 17, 18, 54, 48, 0.876, 0) # Datetime: required error
badModified = DateTime(2022, 6, 1, 13, 8, 45, 0.481, "East Coast") # Datetime: type error
badVersion1 = SemanticVersion("3", "0", "0") # type error
badVersion2 = SemanticVersion(None, 2, 1) # required error

# validate datetime and version objects
# print("created: ", created.validate(created.year, created.month, created.day, created.hour, created.minute, created.second, created.secondFrac, created.timeZoneOffSet))
# print("modified: ", modified.validate(modified.year, modified.month, modified.day, modified.hour, modified.minute, modified.second, modified.secondFrac, modified.timeZoneOffSet))
# print("version: ", version1.validate(version1.major, version1.minor, version1.patch))
# print("(testing datetime) badCreated: ", badCreated.validate(badCreated.year, badCreated.month, badCreated.day, badCreated.hour, badCreated.minute, badCreated.second, badCreated.secondFrac, badCreated.timeZoneOffSet))
# print("(testing datetime) badModified: ", badModified.validate(badModified.year, badModified.month, badModified.day, badModified.hour, badModified.minute, badModified.second, modified.secondFrac, badModified.timeZoneOffSet))
# print("badVersion1: ", badVersion1.validate(badVersion1.major, badVersion1.minor, badVersion1.patch))
# print("badVersion2: ", badVersion2.validate(badVersion2.major, badVersion2.minor, badVersion2.patch))


contr1 = Contributor("authoredBy", "David P. Astling", "Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine", "david.astling@example.com", "https://orcid.org/0000-0001-8179-0304")
contr2 = Contributor("authoredBy", "Ilea E. Heft", "Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine", "ilea.heft@example.com", "https://orcid.org/0000-0002-7759-7007")
contr3 = Contributor("authoredBy", "James M. Sikela", 'Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine', "james.sikela@example.com", 'https://orcid.org/0000-0001-5820-2762')
contr4 = Contributor("authoredBy", "Kenneth L. Jones", "Department of Pediatrics, University of Colorado School of Medicine" , "kenneth.jones@example.com", None)
contr5 = Contributor("createdBy", "Jonathon Keeney", "GWU", "keeneyjg@gwu.edu", None)
contr6 = Contributor("createdBy", "Alex Nguyen", "UVA", "tan5um@virginia.edu", None)
contr7 = Contributor("ceatedBy", "Mike Taylor", "GWU", None, "https://orcid/0000-0002-1003-5675")
badContr8 = Contributor("createdBy", None, "Colorado School of Mines", None, None) # Required Argument Error
badContr9 = Contributor(26.4, "Nemo", "Ocean University", None, None) # Type Error
contributorsList = [contr1, contr2, contr3, contr4, contr5, contr6]
# validate contributors
# i = 1
# for contr in contributorsList:
#     print("Contributor", i, contr.validate(contr.contribution, contr.name, contr.affiliation, contr.email, contr.orcid))
#     i += 1

# print("Bad Contributor 1:", badContr8.validate(badContr8.contribution, badContr8.name, badContr8.affiliation, badContr8.email, badContr8.orcid))
# print("Bad Contributor 2:", badContr9.validate(badContr9.contribution, badContr9.name, badContr9.affiliation, badContr9.email, badContr9.orcid))

rev1 = Review(None, "unreviewed", "Mike Taylor:", None, "createdBy", "GWU", None, "https://orcid/0000-0002-1003-5675")
badRev2 = Review(None, None, "Bad name", "bad reviewer", None, None, None, None) # Required argument error
badRev3 = Review("Dory", "unreviewed", "Firstname Lastname" , "Just keep swimming", contr5, None, None, None) # Type error
reviewersList = [rev1]
# print("Reviewer: ", rev1.validate(rev1.date, rev1.status, rev1.reviewer_Comment, rev1.contributor))
# print("Bad Reviewer1: ", badRev2.validate(badRev2.date, badRev2.status, badRev2.reviewer_Comment, badRev2.contributor))
# print("Bad Reviewer2: ", badRev3.validate(badRev3.date, badRev3.status, badRev3.reviewer_Comment, badRev3.contributor))
prov_139 = ProvenanceDomain("WGS Simulation of DUF1220 Regions", "https://opensource.org/licenses/MIT", version1, created, modified, contributorsList, reviewersList, None, None, None)


# DESCRIPTION DOMAIN
keywordsArr = ["Copy Number Variation", "CNV", "DUF1220", "Genome Informatics", "Next-generation sequencing", "Bioinformatics"]


# Each pipeline step needs its own 2 arrays of inputs and outputs
input_0_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/1_download.sh")
# input_0_URI2 = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/2_trim.sh")
output_0_URI = URI("https://github.com/dpastling/plethora/blob/master/data/1000Genomes_samples.txt")
input_0 = Input(input_0_URI, None, None, None)
# input_0_2 = Input(input_0_URI2, None, None, None)
# print("Input 0:", input_0.validate(input_0.uri, input_0.filename, input_0.access_Time, input_0.sha1_Checksum))
output_0 = Output(output_0_URI, None, None, None)
# print("Output 0:", output_0.validate(output_0.uri, output_0.filename, output_0.access_Time, output_0.sha1_Checksum))
inputArr0 = [input_0]
outputArr0 = [output_0]
prereqURI0 = URI("https://github.com")
prereq0 = Prerequisite("Prerequisite 0", prereqURI0, None, None, None)
prereqList0 = [prereq0]
pipelineStp0 = PipelineSteps(0, "Bowtie2", "self script downloads the fastq files for each sample from the 1000 Genomes site as specified in a sample_index file", inputArr0, outputArr0, None, prereqList0)

input_1_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/2_trim.sh")
output_1_URI = URI("https://github.com/dpastling/plethora/blob/master/logs/trim_stats.txt")
input_1 = Input(input_1_URI, None, None, None)
# print("Input 1:", input_1.validate(input_1.uri, input_1.filename, input_1.access_Time, input_1.sha1_Checksum))
output_1 = Output(output_1_URI, None, None, None)
inputArr1 = [input_1] 
outputArr1 = [output_1]
# print("Output 1:", output_1.validate(output_1.uri, output_1.filename, output_1.access_Time, output_1.sha1_Checksum))
prereqURI1 = URI("https://github.com/dpastling/plethora/blob/master")
prereq1 = Prerequisite("Prerequisite 1", prereqURI1, None, None, None)
prereqList1 = [prereq1]
pipelineStp1 = PipelineSteps(1, "Heptagon", "self script automates the task of trimming low quality bases from the 3' ends of the reads and removes any that are shorter than 80 bp.", inputArr1, outputArr1, None, prereqList1)

input_2_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/3_batch_bowtie.sh")
output_2_URI = URI("https://github.com/dpastling/plethora/blob/master/align_report.txt")
input_2 = Input(input_2_URI, None, None, None)
# print("Input 2:", input_2.validate(input_2.uri, input_2.filename, input_2.access_Time, input_2.sha1_Checksum))
output_2 = Output(output_2_URI, None, None, None)
# print("Output 2:", output_2.validate(output_2.uri, output_2.filename, output_2.access_Time, output_2.sha1_Checksum))
inputArr2 = [input_2]
outputArr2 = [output_2]
prereqURI2 = URI("https://github.com/dpastling/plethora/blob/master/code")
prereq2 = Prerequisite("Prerequisite 2", prereqURI2, None, None, None)
prereqList2 = [prereq2]
pipelineStp2 = PipelineSteps(2, "metaseqR", "self script aligns reads to the genome with Bowtie2.", inputArr2, outputArr2, None, prereqList2)

input_3_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/5_batch_make_bed.sh")
input_3_URI2 = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/3_batch_bowtie.sh")
output_3_URI = URI("https://github.com/dpastling/plethora/blob/master/results/test_read_depth.bed")
input_3 = Input(input_3_URI, None, None, None)
input_3_2 = Input(input_3_URI2, None, None, None)
# print("Input 3:", input_3.validate(input_3.uri, input_3.filename, input_3.access_Time, input_3.sha1_Checksum))
output_3 = Output(output_3_URI, None, None, None)
# print("Output 3:", output_3.validate(output_3.uri, output_3.filename, output_3.access_Time, output_3.sha1_Checksum))
inputArr3 = [input_3]
outputArr3 = [output_3]
prereqURI3 = URI("https://github.com/dpastling/plethora/blob/master/code")
prereq3 = Prerequisite("Prerequisite 3", prereqURI3, None, None, None)
prereqList3 = [prereq3]
pipelineStp3 = PipelineSteps(3, "dbSNP", "self script: Coverts the .bam alignment file into bed format. Parses the reads Calls the merge_pairs.pl script (described below) to combined proper pairs into a single fragment. Finds overlaps with the reference bed file containing the regions of interest (e.g. DUF1220). Calculates the average coverage for each region: (number of bases that overlap) / (domain length)", inputArr3, outputArr3, None, prereqList3)

badInput1 = Input(None, "bad", None, None) # required argument error
badInput2 = Input(input_0_URI, 12.3, None, None) # type error
# print("Bad Input 1:", badInput1.validate(badInput1.uri, badInput1.filename, badInput1.access_Time, badInput1.sha1_Checksum))
# print("Bad Input 2:", badInput2.validate(badInput2.uri, badInput2.filename, badInput2.access_Time, badInput2.sha1_Checksum))
badInputList = [badInput1, badInput2]
badOutput1 = Output(None, "bad too", None, None) # required argument error
badOutput2 = Output(output_0_URI, 12.3, None, None) # type error
# print("Bad Output 1:", badOutput1.validate(badOutput1.uri, badOutput1.filename, badOutput1.access_Time, badOutput1.sha1_Checksum))
# print("Bad Output 2:", badOutput2.validate(badOutput2.uri, badOutput2.filename, badOutput2.access_Time, badOutput2.sha1_Checksum))
badOutputList = [badOutput1, badOutput2]
#badPipelineStp4 = PipelineSteps("Four", "test step", "Bad Step", badInputList, badOutputList, None) # type error
#badPipelineStp5 = PipelineSteps(5, "step test", "bad step 2", None, badOutputList, None) # required argument error
pipelineSteps = [pipelineStp0, pipelineStp1, pipelineStp2, pipelineStp3]

# j = 0
# for step in pipelineSteps:
#     print("Pipline Step:", j, step.validate(step.step_Number, step.name, step.description, step.input_List, step.output_List, step.version))
#     j += 1
# print("Bad Step 1:", badPipelineStp4.validate(badPipelineStp4.step_Number, badPipelineStp4.name, badPipelineStp4.description, badPipelineStp4.input_List, badPipelineStp4.output_List, badPipelineStp4.version))
# print("Bad Step 2:", badPipelineStp5.validate(badPipelineStp5.step_Number, badPipelineStp5.name, badPipelineStp5.description, badPipelineStp5.input_List, badPipelineStp5.output_List, badPipelineStp5.version))

descrpt_139 = DescriptionDomain(keywordsArr, pipelineSteps, None, None)

# EXECUTION DOMAIN
softwrePrereq1_URI = URI("http://bowtie-bio.sourceforge.net/bowtie2/index.shtml")
softwrePrereq2_URI = URI("https://bedtools.readthedocs.io/en/latest/")
softwrePrereq3_URI = URI("http://samtools.sourceforge.net/")
softwrePrereq4_URI = URI("https://cutadapt.readthedocs.io/en/stable/")
softwrePrereq5_URI = URI("https://pip.pypa.io/en/stable/")

# Version validate already tested above. See lines 618, 619, 627, 628
bow_Version = SemanticVersion(2, 2, 9)
bed_Version = SemanticVersion(2, 17, 0)
sam_Version = SemanticVersion(0, 1, 19) #"0.1.19-44428cd"
ca_Version = SemanticVersion(1, 12, 0)
pip_Version = SemanticVersion(22, 1, 2)

softwrePrereq1 = SoftwarePrerequisites("Bowtie2", bow_Version, softwrePrereq1_URI, None, None, None)
softwrePrereq2 = SoftwarePrerequisites("Bedtools", bed_Version, softwrePrereq2_URI, None, None, None)
softwrePrereq3 = SoftwarePrerequisites("Samtools", sam_Version, softwrePrereq3_URI, None, None, None)
softwrePrereq4 = SoftwarePrerequisites("Cutadapt", ca_Version, softwrePrereq4_URI, None, None, None)

# added to test envTest() 
softwrePrereq5 = SoftwarePrerequisites('pip3', pip_Version, softwrePrereq5_URI, None, None, None)

badPrereq1 = SoftwarePrerequisites("bad prereq", None, softwrePrereq1_URI, None, None, None) # required error
badPrereq2 = SoftwarePrerequisites("Bowtie 2", bow_Version, "http://bowtie-bio.sourceforge.net/bowtie2/index.shtml", None, None, None) # type error
softwrePrereqs = [softwrePrereq1, softwrePrereq2, softwrePrereq3, softwrePrereq4, softwrePrereq5]

# k = 1
# for pre in softwrePrereqs:
#     print("Software Prereq", k, pre.validate(pre.name, pre.version, pre.uri, pre.filename, pre.access_Time, pre.sha1_Checksum))
#     k += 1
# print("Bad Prereq 1:", badPrereq1.validate(badPrereq1.name, badPrereq1.version, badPrereq1.uri, badPrereq1.filename, badPrereq1.access_Time, badPrereq1.sha1_Checksum))
# print("Bad Prereq 2:", badPrereq2.validate(badPrereq2.name, badPrereq2.version, badPrereq2.uri, badPrereq2.filename, badPrereq2.access_Time, badPrereq2.sha1_Checksum))

edep_URI = URI("https://www.internationalgenome.org/")
externalDataEndpoint1 = ExternalDataEndpoints("IGSR", edep_URI)
badEndpoint1 = ExternalDataEndpoints("Bad endpoint", None) # required error
badEndpoint2 = ExternalDataEndpoints("bad endpoint 2", "https://www.internationalgenome.org/") # type error
extDataEndPts = [externalDataEndpoint1]
# print("External Data Endpoint:", externalDataEndpoint1.validate(externalDataEndpoint1.name, externalDataEndpoint1.uri))
# print("Bad Endpoint 1:", badEndpoint1.validate(badEndpoint1.name, badEndpoint1.uri))
# print("Bad Endpoint 2", badEndpoint2.validate(badEndpoint2.name, badEndpoint2.uri))

script1_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/1_download.sh")
script2_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/2_trim.sh")
script3_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/3_batch_bowtie.sh")
script4_URI = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/5_batch_make_bed.sh")
scripts = [script1_URI, script2_URI, script3_URI, script4_URI]

env_Var1 = EnvironmentVariable("HOSTTYPE: ", "x86_64-linux")
env_Var2 = EnvironmentVariable("EDITOR: ", "vim")
environment_Variables = [env_Var1, env_Var2]
# print("Env Var1:", env_Var1.validate(env_Var1.name, env_Var1.variable))
# print("Env Var2:", env_Var2.validate(env_Var2.name, env_Var2.variable))

badEnvVar1 = EnvironmentVariable("Test", None) # required error
badEnvVar2 = EnvironmentVariable("Test2", script1_URI) # type error
# print("Bad Env Var1:", badEnvVar1.validate(badEnvVar1.name, badEnvVar1.variable))
# print("Bad Env Var2:", badEnvVar2.validate(badEnvVar2.name, badEnvVar2.variable))

excn_139 = ExecutionDomain(scripts, "Shell", softwrePrereqs, extDataEndPts, environment_Variables)


# IO DOMAIN
inputSub1_URI = URI("https://github.com/dpastling/plethora/blob/master/fastq/test_1.fastq.gz")
inputSub2_URI = URI("https://github.com/dpastling/plethora/blob/master/fastq/test_2.fastq.gz")
outputSub_URI = URI("https://github.com/dpastling/plethora/blob/master/results/test_read_depth.bed")
inputSub1 = InputSubdomain(inputSub1_URI, None, None, None)
inputSub2 = InputSubdomain(inputSub2_URI, None, None, None)
# print("Input 1:", inputSub1.validate(inputSub1.uri, inputSub1.filename))
# print("Input 2:", inputSub2.validate(inputSub2.uri, inputSub2.filename))
badInputSub1 = InputSubdomain(None, "No File", None, None) # required error
badInputSub2 = InputSubdomain("FILE URI", None, None, None) # type error
# print("Bad Input 1:", badInputSub1.validate(badInputSub1.uri, badInputSub1.filename))
# print("Bad Input 2:", badInputSub2.validate(badInputSub2.uri, badInputSub2.filename))
outputSub = OutputSubdomain(outputSub_URI, "test_read_depth.bed", None, None, None)
# print("Output:", outputSub.validate(outputSub.uri, outputSub.filename))
badOutputSub1 = OutputSubdomain(None, "test_read_depth.bed", None, None, None) # required error
badOutputSub2 = OutputSubdomain("outputSub_URI", "test_read_depth.bed", None, None, None) # type error
# print("Bad Output 1", badOutputSub1.validate(badOutputSub1.uri, badOutputSub1.filename))
# print("Bad Output 2", badOutputSub2.validate(badOutputSub2.uri, badOutputSub2.filename))
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
badEmpErr1 = EmpiricalError(25.6) # type error
badEmpErr2 = EmpiricalError(None) # required error

root_Mean_Sqr_Error = [empError1, empError2, empError3, empError4, empError5, empError6]
# errorNum = 1
# for err in root_Mean_Sqr_Error:
#     print("Empirical Error", errorNum, err.validate(err.empError))
#     errorNum += 1
# print("Bad Empirical Error 1:", badEmpErr1.validate(badEmpErr1.empError))
# print("Bad Empirical Error 2:", badEmpErr2.validate(badEmpErr2.empError))

error_139 = ErrorDomain(root_Mean_Sqr_Error, None)


# EXTENSION DOMAIN SHOULD BE SET TO None
# USABIITY DOMAIN IS A STRING DOES NOT NEED TO BE MADE AN OBJECT
use_139 = "Pipeline for identifying copy number of genetic sequences independent of the genes in which they occur, and with higher fidelity than existing methods. Approximately 25 individuals were randomly chosen from each of the CEU, YRI, CHB, JPT, MXL, CLM, PUR, ASW, LWK, CHS, TSI, IBS, FIN, and BGR populations for a total of 324 individuals. Where domains were more than 1 kb apart, the boundaries of the domains were extended up to 250 bp to allow the possibility of capturing unique sequence directly adjacent to the domain. No intermediate files were generated because the commands were run executed as a pipe at the command line, so T:/dev/tmpfs was used for the file IOs in the Description Domain. self example pipeline was created based on the work of Astling et al. doi: 10.1186/s12864-017-3976-z"
params_139 = None

# BIOCOMPUTE CLASS OBJECT
BCO_000139 = BioComputeObject(meta_139, use_139, prov_139, excn_139, None, descrpt_139, error_139, io_139, params_139)
# PRINT BIOCOMPUTE CLASS OBJECT
# pprint(vars(BCO_000139))
# pprint(vars(BCO_000139.description_Domain))
# pprint(vars(BCO_000139.description))
# pprint(vars(BCO_000139.description.pipeLine))
# pprint(vars(BCO_000139.execution))
# pprint(vars(BCO_000139.prov))







# *********************************************** DOMAIN VALIDATE() TESTING **********************************************

# BIOCOMPUTE OBJECT:
# badMeta = DescriptionDomain("k", "p", "p", "x") # Bad Object made to test validation function
# BCO_000139.validate(badMeta, use_139, prov_139, excn_139, None, descrpt_139, None, io_139) # tests type error
# BCO_000139.validate(meta_139, None, prov_139, excn_139, None, descrpt_139, None, io_139) # tests required argument error
# BCO_000139.validate(meta_139, use_139, prov_139, excn_139, None, descrpt_139, None, io_139) # tests valid BCO

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






# ************************************************* PRINT FUNCTIONS *************************************************

# def printInputs():
#     print("Input File(s):")
#     for i in inputSubDmn:
#         print(i.uri.uri_Str)
#     return None

# def printOutputs():
#     print("Output File(s):")
#     for out in outputSubDmn:
#         print(out.uri.uri_Str)
#     return None

# def printSoftwarePrereqs():
#     print('\n', "Software Prerequisites:")
#     for p in softwrePrereqs:
#         print(p.name, ":", p.uri.uri_Str)
#     return None

# def isAccepted():
#     print('\n', "Accepted BCO:")
#     for rev in reviewersList:
#         if rev.status == "Approved":
#             return True
#     return False


# need to get ACTUAL name to check if tool is installed ('bowtie2' instead of "Bowtie 2")
# def envCheck():

#     # subprocess.run(['pip3', '--version'])
#     envCheckNames = {
#         "Bowtie 2" : 'bowtie2',
#         "Bed Tools" : 'bedtools',
#         "Sam Tools" : 'samtools',
#         "Cut Adapt" : 'cutadapt'
#     }

#     print("Checking for Software Prerequisites...")
#     for req in softwrePrereqs:
#         try:
#             if subprocess.run([req.name, "--version"]):
#                 print('  ', "-", req.name, "installed.")
#         except:
#             print("You do not have", req.name, "installed.")
#         continue

#     return None

# def printContributors():
#     print("Contributors:")
#     for contr in contributorsList:
#         print("Name: ", contr.name, "    Contribution: ", contr.contribution,"   ORCID: ", contr.orcid)
#     return None

# def bcoTree():
#     stepInput = {}

#     for step in pipelineSteps:
#         for file in step.input_List:
#             stepInput[file.uri] = step.step_Number

#     for x in stepInput:
#         print("Step: ", stepInput[x])
#         pprint(vars(x))


# printSoftwarePrereqs()
# print('\n')
# printInputs()
# print('\n')
# printOutputs()
# print('\n')
# print(isAccepted())
# print('\n')
# envCheck()
# print('\n')
# bcoTree()
# print('\n')
# printContributors()
# print('\n')
# print("Finished")




# *************************************************** TEST GETTERS AND SETTERS **************************************************

# get user input for arguments then call setters to make/update BCO
# print(BCO_000139.meta)
# BCO_000139.use = None
# print(BCO_000139.use)

# tcreated = DateTime(2022, 5, 17, 18, 54, 48, 0.876, 0)
# tmodified = DateTime(2022, 6, 1, 13, 8, 45, 0.481, 0)
# tversion1 = SemanticVersion(3, 0, 0)

# tcontr1 = Contributor("authoredBy", "Elton John", "Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine", "david.astling@example.com", "https://orcid.org/0000-0001-8179-0304")
# tcontr2 = Contributor("authoredBy", "Freddie Mercury", "Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine", "ilea.heft@example.com", "https://orcid.org/0000-0002-7759-7007")
# tcontr3 = Contributor("authoredBy", "Billie Joel", 'Department of Biochemistry and Molecular Genetics, University of Colorado School of Medicine', "james.sikela@example.com", 'https://orcid.org/0000-0001-5820-2762')
# tcontr4 = Contributor("authoredBy", "David Bowie", "Department of Pediatrics, University of Colorado School of Medicine" , "kenneth.jones@example.com", None)
# tcontr5 = Contributor("createdBy", "Prince", "GWU", "keeneyjg@gwu.edu", None)
# tcontr6 = Contributor("createdBy", "", "UVA", "tan5um@virginia.edu", None)
# tcontr7 = Contributor("ceatedBy", "MJ", "GWU", None, "https://orcid/0000-0002-1003-5675")

# tcontributorsList = [tcontr1, tcontr2, tcontr3, tcontr4, tcontr5, tcontr6]
# validate contributors
# i = 1
# for contr in contributorsList:
#     print("Contributor", i, contr.validate(contr.contribution, contr.name, contr.affiliation, contr.email, contr.orcid))
#     i += 1

# print("Bad Contributor 1:", badContr8.validate(badContr8.contribution, badContr8.name, badContr8.affiliation, badContr8.email, badContr8.orcid))
# print("Bad Contributor 2:", badContr9.validate(badContr9.contribution, badContr9.name, badContr9.affiliation, badContr9.email, badContr9.orcid))

# trev1 = Review(None, "unreviewed", None, contr7)
# treviewersList = [trev1]
# print("Reviewer: ", rev1.validate(rev1.date, rev1.status, rev1.reviewer_Comment, rev1.contributor))
# print("Bad Reviewer1: ", badRev2.validate(badRev2.date, badRev2.status, badRev2.reviewer_Comment, badRev2.contributor))
# print("Bad Reviewer2: ", badRev3.validate(badRev3.date, badRev3.status, badRev3.reviewer_Comment, badRev3.contributor))
# testProv = ProvenanceDomain("Test Provenance", "TEST License", tversion1, tcreated, tmodified, tcontributorsList, treviewersList, None, None, None)

# BCO_000139.updateProvenance(testProv)
# pprint(vars(BCO_000139.provenance_Domain))
# testUse = "Usage message"







# ***************************************** MAKE BCO CLASS OBJECT FUNCTION + HELPER FUNCTIONS *********************************************

def makeMeta():
    print("META DATA:")
    newEtag = makeEtag()
    newBCOid = makeBCOid()
    newSpec = makeSpecVersion()

    newMeta = Meta(newBCOid, newEtag, newSpec)
    valMeta = newMeta.validate(newBCOid, newEtag, newSpec)
    if valMeta:
        return newMeta
    else:
        err = input("Invalid Meta Object, would you like to try to make a valid object? (y/n): ")
        if err == 'y':
            makeMeta()
        else:
            print("Exiting... 'None' returned")
            return None



def makeBCOid():
    id = input("Enter the BCO id: ")
    BCOid = ObjectID(id)
    return BCOid

def makeSpecVersion():
    temp = input("Enter spec version uri: ")
    newSpec = URI(temp)
    return newSpec

def makeEtag():
    tag = input("Enter the etag generated by the BioCompute Object builder: ")
    return tag


def makeExt():
    print("EXTENSION DOMAIN")
    numSchema = int(input("Enter the number of Schemas (Can be 0): "))
    numUserList = int(input("Enter the number of User Defined Attributes used (Can be 0): "))
    schemaList = []
    userDefinedList = []
    counter = 0
    userCounter = 0
    if numSchema == 0:
        return None
    while counter < numSchema:
        tempSchema = makeExtensionSchema()
        schemaList.append(tempSchema)
        counter+=1
    while userCounter < numUserList:
        tempUser = makeScmExt()
        userDefinedList.append(tempUser)
        userCounter+=1
   
    newExt = ExtensionDomain(schemaList, userDefinedList)
    return newExt

def makeExtensionSchema():
    schemaLink = input("Enter schemaLink: ")
    schemaReturn = ExtensionDomain(schemaLink, None)
    return schemaReturn
    
def makeScmExt():
    userIn = input("Enter the additional fields: ")
    return userIn


#Provenance Domain
def makeProv():
    print("PROVENANCE DOMAIN")
    #loop through number of contributors needed and call makeContributor inside loop, put them in list
    #same with reviewer
    numContrs = int(input("Enter the number of contributors: "))
    numRevs = int(input("Enter the number of reveiwers: "))
    contrsList = []
    revsList = []
    x = 0
    y = 0

    while x < numContrs:
        tempContr = makeContributor()
        contrsList.append(tempContr)
        x += 1
    
    while y < numRevs:
        tempRev = makeReviewer()
        revsList.append(tempRev)
        y += 1

    provName = input("Enter the name of the Pipeline: ")
    lnse = input("Enter the license: ")
    provVers = makeVersion()
    provDer = makeDerivedID()
    provCreated = makeCreated()
    provModified = makeModified()
    provObs = makeObsoleteDate()
    provEmb = makeEmbargo()
    
    newProvenance = ProvenanceDomain(provName, lnse, provVers, provCreated, provModified, contrsList, revsList, provEmb, provObs, provDer)
    val = newProvenance.validate(provName, lnse, provVers, provCreated, provModified, contrsList, revsList, provEmb, provObs, provDer)
    if val:
        return newProvenance
    else:
        print("Invalid Provenance Domain. Make sure all required fields are filled")
        makeProv()

def makeCreated():
    year = int(input("(int) Enter the year the BioCompute Object was created: "))
    month = int(input("(int) Enter the month the BioCompute Object was created: "))
    day = int(input("(int) Enter the day the BioCompute Object was created: "))
    hr = int(input("(int) Enter the hour the BioCompute Object was created: "))
    min = int(input("(int) Enter the minute the BioCompute Object was created: "))
    sec = int(input("(int) Enter the second the BioCompute Object was created: "))
    secFrac = float(input("(decimal) Enter the second fraction the BioCompute Object was created: "))
    timeZone = int(input("(int) Enter the time zone offset (0 for Eastern Time): "))

    newCreated = DateTime(year, month, day, hr, min, sec, secFrac, timeZone)
    dateVal = newCreated.validate(year, month, day, hr, min, sec, secFrac, timeZone)
    if dateVal:
        return newCreated
    else:
        print("Invalid Date. All fields of the DateTime class are required")
        makeCreated()


def makeModified():
    year = int(input("(int) Enter the year the BioCompute Object was modified: "))
    month = int(input("(int) Enter the month the BioCompute Object was modified: "))
    day = int(input("(int) Enter the day the BioCompute Object was modified: "))
    hr = int(input("(int) Enter the hour the BioCompute Object was modified: "))
    min = int(input("(int) Enter the minute the BioCompute Object was modified: "))
    sec = int(input("(int) Enter the second the BioCompute Object was modified: "))
    secFrac = float(input("(decimal) Enter the second fraction the BioCompute Object was modified: "))
    timeZone = int(input("(int) Enter the time zone offset (0 for Eastern Time): "))

    newModified = DateTime(year, month, day, hr, min, sec, secFrac, timeZone)
    dateVal = newModified.validate(year, month, day, hr, min, sec, secFrac, timeZone)

    if dateVal:
        return newModified
    else:
        print("Invalid Date. All fields of the DateTime class are required")
        makeModified()


def makeVersion():
    print("Semantic Versioning used (major. minor. patch)")
    major = int(input("(int) Enter the major: "))
    minor = int(input("(int) Enter the minor: "))
    patch = int(input("(int) Enter the patch: "))

    newVersion = SemanticVersion(major, minor, patch)
    valVers = newVersion.validate(major, minor, patch)
    if valVers:
        return newVersion
    else:
        print("Invalid Semantic Version")
        makeVersion()


def makeContributor():
    print("Contributor Information")
    contName = input("Enter the contributor's name: ")
    cont = input("Enter contribution ('createdBy', 'authoredBy', 'contributedBy', 'createdAt', 'createdWith', 'curatedBy') or 'None':  ")
    contAff = input("Enter contributor's affiliation (ex. Geroge Washington University) or 'None': ")
    contEmail = input("Enter contributor's email or 'None': ")
    contOrcid = input("Enter contributor's orcid or 'None': ")

    if contName == "None":
        contName = None
    if cont == "None":
        cont = None
    if contAff == "None":
        contAff = None
    if contEmail == "None":
        contEmail = None    
    if contOrcid == "None":
        contOrcid = None

    newContributor = Contributor(cont, contName, contAff, contEmail, contOrcid)
    valContr = newContributor.validate(cont, contName, contAff, contEmail, contOrcid)
    if valContr:
        return newContributor
    else:
        tryAgain = input("Invalid Contributor, would you like to try to build a valid Contributor object? (y/n)")
        if tryAgain == 'y':
            makeContributor()
        else:
            print("Exiting...'None' returned")
            return None


def makeReviewer():
    print("Reviewer Information")
    noDate = input("Is there a date with the review? (y/n): ")
    if noDate == 'n':
        revDate = None
    else:
        revYear = int(input("(int) Enter the year the BioCompute Object was created: "))
        revMonth = int(input("(int) Enter the month the BioCompute Object was created: "))
        revDay = int(input("(int) Enter the day the BioCompute Object was created: "))
        revHr = int(input("(int) Enter the hour the BioCompute Object was created: "))
        revMin = int(input("(int) Enter the minute the BioCompute Object was created: "))
        revSec = int(input("(int) Enter the second the BioCompute Object was created: "))
        revSecFrac = float(input("(decimal) Enter the second fraction the BioCompute Object was created: "))
        revTimeZone = int(input("(int) Enter the time zone offset (0 for Eastern Time): "))
        revDate = DateTime(revYear, revMonth, revDay, revHr, revMin, revSec, revSecFrac, revTimeZone)

    revContr = input("Enter reviewer contribution or 'None' if there is no contribution: ")
    if revContr == 'None':
        revContr = None
    
    revAff = input("Enter reviewer affiliation or 'None' if affiliation is not included: ")
    if revAff == 'None':
        revAff = None

    revEmail = input("Enter reviewer email or 'None' if email is not included: ")        
    if revEmail == 'None':
        revEmail = None
    
    revORCID = input("Enter reviewer ORCID or 'None' if ORCID is not included: ")
    if revORCID == 'None':
        revORCID = None
        
    revComm = input("Enter reviewer comment of 'None' if comment is not included: ")
    if revComm == 'None':
        revComm = None

    revName = input("Enter the name of the reviewer: ")
    revStatus = input("Enter reviewer status ('unreviewed', 'in-review', 'approved', 'rejected', 'suspended'): ")
    
    

    newRev = Review(revDate, revStatus, revName, revComm, revContr, revAff, revEmail, revORCID)
    val = newRev.validate(revDate, revStatus, revName, revComm, revContr, revAff, revEmail, revORCID)

    if val:
        return newRev
    else:
        tryAgain = input("Invalid Reviewer, would you like to try to build a valid Reviewer object? (y/n)")
        if tryAgain == 'y':
            makeReviewer()
        else:
            print("Exiting...'None' returned")
            return None

def makeEmbargo():
    print("Embargo Information")
    isNone = input("Enter 'None' if there is no embargo field: ")
    if isNone == 'None':
        return None

    styear = int(input("(int) Enter the start year: "))
    stmonth = int(input("(int) Enter the start month: "))
    stday = int(input("(int) Enter the start day: "))
    sthr = int(input("(int) Enter the start hour: "))
    stmin = int(input("(int) Enter the start minute: "))
    stsec = int(input("(int) Enter the start second: "))
    stsecFrac = float(input("(decimal) Enter the start second fraction: "))
    sttimeZone = int(input("(int) Enter the start time zone offset (0 for Eastern Time): "))

    startTime = DateTime(styear, stmonth, stday, sthr, stmin, stsec, stsecFrac, sttimeZone)
    startTime.validate(styear, stmonth, stday, sthr, stmin, stsec, stsecFrac, sttimeZone)

    EMyear = int(input("(int) Enter the end year: "))
    EMmonth = int(input("(int) Enter the end month: "))
    EMday = int(input("(int) Enter the end day: "))
    EMhr = int(input("(int) Enter the end hour: "))
    EMmin = int(input("(int) Enter the end minute: "))
    EMsec = int(input("(int) Enter the end second: "))
    EMsecFrac = float(input("(decimal) Enter the end second fraction: "))
    EMtimeZone = int(input("(int) Enter the end time zone offset (0 for Eastern Time): "))

    endTime = DateTime(EMyear, EMmonth, EMday, EMhr, EMmin, EMsec, EMsecFrac, EMtimeZone)
    endTime.validate(EMyear, EMmonth, EMday, EMhr, EMmin, EMsec, EMsecFrac, EMtimeZone)

    newEmbargo = Embargo(startTime, endTime)
    valEmb = newEmbargo.validate(startTime, endTime)
    if valEmb:
        return newEmbargo
    else:
        tryAgain = input("Invalid Embargo, would you like to try to build a valid Embargo object? (y/n)")
        if tryAgain == 'y':
            makeEmbargo()
        else:
            print("Exiting...'None' returned")
            return None


def makeObsoleteDate():
    isNone = input("Enter 'None' if there is no obsolete time field: ")
    if isNone == 'None':
        return None

    obyear = int(input("(int) Enter the obsolete year: "))
    obmonth = int(input("(int) Enter the obsolete month: "))
    obday = int(input("(int) Enter the obsolete day: "))
    obhr = int(input("(int) Enter the obsolete hour: "))
    obmin = int(input("(int) Enter the obsolete minute: "))
    obsec = int(input("(int) Enter the obsolete second: "))
    obsecFrac = float(input("(decimal) Enter the obsolete second fraction: "))
    obtimeZone = int(input("(int) Enter the obsolete time zone offset (0 for Eastern Time): "))

    obsoleteTime = DateTime(obyear, obmonth, obday, obhr, obmin, obsec, obsecFrac, obtimeZone)
    dateVal = obsoleteTime.validate(obyear, obmonth, obday, obhr, obmin, obsec, obsecFrac, obtimeZone)
    if dateVal:
        return obsoleteTime
    else:
        tryAgain = input("Invalid DateTime, would you like to try to build a valid DateTime object? (y/n)")
        if tryAgain == 'y':
            makeObsoleteDate()
        else:
            print("Exiting...'None' returned")
            return None

def makeDerivedID():
    parentID = input("Enter the parent BCO ID or 'None' if BCO is not derived from another object: ")
    if parentID == 'None':
        return None
    parentBCO_ID = ObjectID(parentID)
    return parentBCO_ID


def makeExDataEndPts():
    print("External Data Endpoints Information")
    fn = input("Enter the name of the external data endpoint: ")
    url = input("Enter the URL of the external data endpoint: ")
    dataEndPt = ExternalDataEndpoints(fn, url)

    return dataEndPt

def makeEnvironmentVars():
    print("Environment Variables Information")
    isNone = input("Enter 'None' if Environment Variables are not included in BCO, otherwise, enter any key: ")
    if isNone == 'None':
        return None
    envVarsList = []
    numVars = int(input("Enter the number of Environment Variables in the BCO: "))
    iterator = 0
    while iterator < numVars:
        varName = input("Enter the name of the Environment variable: ")
        variable = input("Enter the variable: ")
        tempEnvVar = EnvironmentVariable(varName, variable)
        envVarsList.append(tempEnvVar)
        iterator += 1

    return envVarsList


def makeExecution():
    print("EXECUTION DOMAIN")
    numExtPts = int(input("Enter the number of External Data Endpoints your BCO has: "))
    numPrereqs = int(input("Enter the number of Software Prerequisites your BCO has: "))
    numScripts = int(input("Enter the number of Scripts your BCO has: "))
    scriptDriver = input("Enter script driver: ")
    prereqsList = []
    pointsList = []
    scriptList = []

    x = y = z = 0
    while x < numExtPts:
        point = makeExDataEndPts()
        pointsList.append(point)
        x += 1
    
    while y < numPrereqs:
        prereq = makeSoftwarePrereqs()
        prereqsList.append(prereq)
        y += 1

    while z < numScripts:
        scpt = makeScript()
        scriptList.append(scpt)
        z += 1

    envVarList = makeEnvironmentVars()

    newExecution = ExecutionDomain(scriptList, scriptDriver, prereqsList, pointsList, envVarList)
    valEx = newExecution.validate(scriptList, scriptDriver, prereqsList, pointsList, envVarList)
    if valEx:
        return newExecution
    else:
        tryAgain = input("Invalid Execution Domain, would you like to try to build a valid Execution Domain object? (y/n)")
        if tryAgain == 'y':
            makeExecution()
        else:
            print("Exiting...'None' returned")
            return None

    
def makeScript():
    print("Script(s) Information")
    isAccess = input("Does your script have an access time? (y/n): ")
    if isAccess == 'n':
        accessTime = None
    else:
        accessTime = makeDateTime()

    filename = input("Enter 'None' if script does not have a filename, otherwise enter the filename: ")
    if filename == 'None':
        filename = None

    checkSum = input("Enter 'None' if there is no SHA1 Checksum for the script, otherwise enter it here: ")
    if checkSum == 'None':
        checkSum = None
    scptUri = input("Enter the script URI: ")
    sptURI = URI(scptUri)

    newScript = Script(filename, sptURI, accessTime, checkSum)
    valScript = newScript.validate(filename, sptURI, accessTime, checkSum)
    if valScript:
        return newScript
    else:
        tryAgain = input("Invalid Script, would you like to try to build a valid Script object? (y/n)")
        if tryAgain == 'y':
            makeScript()
        else:
            print("Exiting...'None' returned")
            return None


def makeDateTime():
    year = int(input("(int) Enter the year: "))
    month = int(input("(int) Enter the month: "))
    day = int(input("(int) Enter the day: "))
    hr = int(input("(int) Enter the hour: "))
    min = int(input("(int) Enter the minute: "))
    sec = int(input("(int) Enter the second: "))
    secFrac = float(input("(decimal) Enter the second fraction: "))
    timeZone = int(input("(int) Enter the time zone offset (0 for Eastern Time): "))

    dateTime = DateTime(year, month, day, hr, min, sec, secFrac, timeZone)
    dateVal = dateTime.validate(year, month, day, hr, min, sec, secFrac, timeZone)
    if dateVal:
        return dateTime
    else:
        tryAgain = input("Invalid DateTime, would you like to try to build a valid DateTime object? (y/n)")
        if tryAgain == 'y':
            makeDateTime()
        else:
            print("Exiting...'None' returned")
            return None

def makeURI():
    newUri = input("Enter uri: ")
    newURI = URI(newUri)
    return newURI

def makeSoftwarePrereqs():
    print("Software Prerequisite Information")
    tempName = input("Enter name of software prerequisite: ")
    tempFileName = input("Enter 'None' if there is no filename, otherwise enter the filename of sofetware prerequisite: ")
    if tempFileName == 'None':
        tempFileName = None
    tempURI = makeURI()
    tempVers = makeVersion()
    isAT = input("Is there an access time? Enter (y/n): ")
    if isAT == 'y':
        tempAT = makeDateTime()
    else:
        tempAT = None
    tempCheck = input("Enter 'None' if there is no Checksum, otherwise enter the SHA1 Checksum: ")
    if tempCheck == 'None':
        tempCheck = None

    newSoftwarePrereq = SoftwarePrerequisites(tempName, tempVers, tempURI, tempFileName, tempAT, tempCheck)
    valPrereq = newSoftwarePrereq.validate(tempName, tempVers, tempURI, tempFileName, tempAT, tempCheck)
    if valPrereq:
        return newSoftwarePrereq
    else:
        tryAgain = input("Invalid Software Prerequisite, would you like to try to build a valid Software Prerequisite object? (y/n)")
        if tryAgain == 'y':
            makeSoftwarePrereqs()
        else:
            print("Exiting...'None' returned")
            return None


def makeInputSubdomain():
    print("Input Subdomain Information")
    inAccessTime = input("Is there an access time? Enter (y/n): ")
    if inAccessTime == 'y':
        inAccessTime = makeDateTime()
    else:
        inAccessTime = None
    inFilename = input("Enter the filename: ")
    inURIstr = input("Enter the URI: ")
    inCheck = input("Enter 'None' if there is no SHA1 Checksum, otherwise enter the SHA1 Checksum: ")
    if inCheck == 'None':
        inCheck = None
    inURI = URI(inURIstr)

    newInSub = InputSubdomain(inURI, inFilename, inAccessTime, inCheck)
    valInSub = newInSub.validate(inURI, inFilename, inAccessTime, inCheck)
    if(valInSub):
        return newInSub
    else:
        tryAgain = input("Invalid Input Subdomain, would you like to try to build a valid Input Subdomain object? (y/n)")
        if tryAgain == 'y':
            makeInputSubdomain()
        else:
            print("Exiting...'None' returned")
            return None


def makeOutputSubdomain():
    print("Output Subdomain Information")
    outAccessTime = input("Is there an access time? Enter (y/n): ")
    if outAccessTime == 'y':
        outAccessTime = makeDateTime()
    else:
        outAccessTime = None
    outMediatype = input("Enter the output mediatype, enter 'None' if not included: ")

    if outMediatype == 'None':
        outAccessTime = None
    outFilename = input("Enter the filename: ")

    outURIstr = input("Enter the URI: ")
    outCheck = input("Enter 'None' if there is no SHA1 Checksum, otherwise enter the SHA1 Checksum: ")
    if outCheck == 'None':
        outCheck = None
    outURI = URI(outURIstr)

    newOutSub = OutputSubdomain(outURI, outFilename, outCheck, outMediatype, outAccessTime)
    valOutSub = newOutSub.validate(outURI, outFilename, outCheck, outMediatype, outAccessTime)
    if(valOutSub):
        return newOutSub
    else:
        tryAgain = input("Invalid Output Subdomain, would you like to try to build a valid Output Subdomain object? (y/n)")
        if tryAgain == 'y':
            makeOutputSubdomain()
        else:
            print("Exiting...'None' returned")
            return None


def makeIO():
    print("IO DOMAIN")
    numIns = int(input("Enter the number of inputs: "))
    numOuts = int(input("Enter the number of outputs: "))
    inputSubList = []
    outputSubList = []
    it = 0
    it2 = 0

    while it < numIns:
        tempIn = makeInputSubdomain()
        inputSubList.append(tempIn)
        it += 1

    while it2 < numOuts:
        tempOut = makeOutputSubdomain()
        outputSubList.append(tempOut)
        it2 += 1

    newIO = IODomain(inputSubList, outputSubList)
    valIO = newIO.validate(inputSubList, outputSubList)
    if valIO:
        return newIO
    else:
        tryAgain = input("Invalid IO Domain, would you like to try to build a valid IO Domain object? (y/n)")
        if tryAgain == 'y':
            makeIO()
        else:
            print("Exiting...'None' returned")
            return None


def makeDescription():
    print("DESCRIPTION DOMAIN")
    numSteps = int(input("Enter the number of pipeline steps you have: "))
    step = 0
    pipelineSteps = []
    while step < numSteps:
        tempStep = makePipelineSteps()
        pipelineSteps.append(tempStep)
        step += 1

    xRef = makeXRefs()
    keywords = makeKeywords()
    platforms = makePlatform()

    newDesc = DescriptionDomain(keywords, pipelineSteps, platforms, xRef)
    valDesc = newDesc.validate(keywords, pipelineSteps, platforms, xRef)
    if valDesc:
        return newDesc
    else:
        tryAgain = input("Invalid Description Domain, would you like to try to build a valid IO Domain object? (y/n)")
        if tryAgain == 'y':
            makeDescription()
        else:
            print("Exiting...'None' returned")
            return None

def makeXRefs():
    print("Xref Information")
    xrefList = []
    numXrefs = int(input("Enter the number of X Refs your BCO has: "))
    x = 0
    while x < numXrefs:
        x += 1

    return xrefList

def makeKeywords():
    keywordsList = []
    numWords = int(input("Enter the number of keywords your BCO has: "))
    k = 0
    while k < numWords:
        tempWord = input("Enter keyword: ")
        keywordsList.append(tempWord)
        k += 1

    return keywordsList


def makePipelineSteps():
    print("Pipeline Step Information")
    stepNum = int(input("(int) Enter the step number of the pipeline step: "))
    pipeName = input("Enter the name of the pipeline step: ")
    pipeDesc = input("Enter the description of the pipeline step: ")
    numIn = int(input("Enter the number of input files this step has: "))
    numOut = int(input("Enter the number of output files this step has: "))
    numPrereqs = int(input("Enter the number of prerequisites this step has: "))
    vers = input("Does this pipeline step have a version? (y/n): ")
    if vers == 'y':
        pipeVers = makeVersion()
    else:
        pipeVers = None
    x = y = z = 0
    inList = []
    outList = []
    prereqList = []

    while x < numIn:
        tempIn = makeInputList()
        inList.append(tempIn)
        x += 1

    while y < numOut:
        tempOut = makeOutputList()
        outList.append(tempOut)
        y += 1
    
    while z < numPrereqs:
        tempPre = makePrereqs()
        prereqList.append(tempPre)
        z += 1


    newPipeline = PipelineSteps(stepNum, pipeName, pipeDesc, inList, outList, pipeVers, prereqList)
    valPipe = newPipeline.validate(stepNum, pipeName, pipeDesc, inList, outList, pipeVers, prereqList)
    if valPipe:
        return newPipeline
    else:
        tryAgain = input("Invalid Pipeline Step, would you like to try to build a valid Pipeline Step object? (y/n)")
        if tryAgain == 'y':
            makePipelineSteps()
        else:
            print("Exiting...'None' returned")
            return None


# pipeline argument
def makePrereqs():
    print("Pipeline Step Prerequisites")
    prereqName = input("Enter 'None' if the name is not included, otherwise enter the name of the prerequisite: ")
    if prereqName == 'None':
        prereqName = None

    prereqFilename = input("Enter 'None' if the filename is not included, otherwise enter the filename of the prerequisite: ")
    if prereqFilename == 'None':
        prereqFilename = None

    prereqURI = input("Enter the URI of the prerequisite: ")
    prereqURI = URI(prereqURI)

    prereqAccessTime = input("Is there an access time? Enter (y/n): ")
    if prereqAccessTime == 'y':
        prereqAccessTime = makeDateTime()
    else:
        prereqAccessTime = None

    prereqCheck = input("Enter 'None' if the SHA1 Checksum is not included, otherwise enter the SHA1 Checksum: ")
    if prereqCheck == 'None':
        prereqCheck = None

    newPrereq = Input(prereqURI, prereqFilename, prereqAccessTime, prereqCheck)
    valPrereq = newPrereq.validate(prereqURI, prereqFilename, prereqAccessTime, prereqCheck)
    if valPrereq:
        return newPrereq
    else:
        tryAgain = input("Invalid Prerequisite, would you like to try to build a valid Prerequisite object? (y/n)")
        if tryAgain == 'y':
            makePrereqs()
        else:
            print("Exiting...'None' returned")
            return None

# pipeline argument
# make the actual list in the makePipeline() function
def makeInputList():
    print("Pipeline Step Inputs")
    inFilename = input("Enter 'None' if the filename is not included, otherwise enter the filename of the input file: ")
    if inFilename == 'None':
        inFilename = None

    inURI = input("Enter the URI of the input file: ")
    inputURI = URI(inURI)

    inputAccessTime = input("Is there an access time? Enter (y/n): ")
    if inputAccessTime == 'y':
        inputAccessTime = makeDateTime()
    else:
        inputAccessTime = None

    inCheck = input("Enter 'None' if the SHA1 Checksum is not included, otherwise enter the SHA1 Checksum: ")
    if inCheck == 'None':
        inCheck = None

    newInputFile = Input(inputURI, inFilename, inputAccessTime, inCheck)
    valIn = newInputFile.validate(inputURI, inFilename, inputAccessTime, inCheck)
    if valIn:
        return newInputFile
    else:
        tryAgain = input("Invalid Input List, would you like to try to build a valid valid Input List object? (y/n)")
        if tryAgain == 'y':
            makeInputList()
        else:
            print("Exiting...'None' returned")
            return None
    

# pipeline argument
def makeOutputList():
    print("Pipeline Step Outputs")
    outFilename = input("Enter 'None' if the filename is not included, otherwise enter the filename of the output file: ")
    if outFilename == 'None':
        outFilename = None

    outURI = input("Enter the URI of the output file: ")
    outputURI = URI(outURI)

    outputAccessTime = input("Is there an access time? Enter (y/n): ")
    if outputAccessTime == 'y':
        outputAccessTime = makeDateTime()
    else:
        outputAccessTime = None

    outCheck = input("Enter 'None' if the SHA1 Checksum is not included, otherwise enter the SHA1 Checksum: ")
    if outCheck == 'None':
        outCheck = None

    newOutputFile = Input(outputURI, outFilename, outputAccessTime, outCheck)
    valOut = newOutputFile.validate(outputURI, outFilename, outputAccessTime, outCheck)
    if valOut:
        return newOutputFile
    else:
        tryAgain = input("Invalid Output List, would you like to try to build a valid OutputList object? (y/n)")
        if tryAgain == 'y':
            makeOutputList()
        else:
            print("Exiting...'None' returned")
            return None


def makePlatform():
    print("Platform Information")
    platformsList = []
    numP = int(input("Enter the number of platforms your BCO has: "))
    p = 0
    while p < numP:
        tempPlat = input("Enter platform: ")
        platformsList.append(tempPlat)
        p += 1

    return platformsList

def makeXref():
    print("Xref Information")
    nameSpace = input("Enter the Namespace of the X Ref: ")
    xName = input("Enter the Name of the X Ref")
    xAccessTime = makeDateTime()
    xID = int(input("Enter the ID of the X Ref: "))

    newXRef = Xref(nameSpace, xName, xAccessTime, xID)
    valXR = newXRef.validate(nameSpace, xName, xAccessTime, xID)
    if valXR:
        return newXRef
    else:
        tryAgain = input("Invalid X Ref, would you like to try to build a valid X Ref object? (y/n)")
        if tryAgain == 'y':
            makeXref()
        else:
            print("Exiting...'None' returned")
            return None

def makeError():
    print("ERROR DOMAIN")
    numEmp = int(input("Enter the number of Empirical errors your BCO has: "))
    numAlg = int(input("Enter the number of Algorithmic errors your BCO has: "))
    empiricalList = []
    algorithmicList = []
    empIt = algIt = 0

    while empIt < numEmp:
        tempEmp = makeEmpiricalError()
        empiricalList.append(tempEmp)
        empIt += 1

    while algIt < numAlg:
        tempAlg = makeAlgorithmicError()
        algorithmicList.append(tempAlg)
        algIt += 1

    newError = ErrorDomain(empiricalList, algorithmicList)
    valErr = newError.validate(empiricalList, algorithmicList)
    if valErr:
        return newError
    else:
        tryAgain = input("Invalid Error Domain, would you like to try to build a valid Error Domain object? (y/n)")
        if tryAgain == 'y':
            makeError()
        else:
            print("Exiting...'None' returned")
            return None


def makeEmpiricalError():
    empirical = input("Enter empirical error: ")
    empError = EmpiricalError(empirical)
    return empError

def makeAlgorithmicError():
    algorithmic = input("Enter algorithmic error: ")
    algError = AlgorithmicError(algorithmic)
    return algError


def makeParametric():
    print("PARAMETRIC DOMAIN")
    numParams = int(input("How many Parameters does your BioCompute Object have? "))
    p = 0
    paramsList = []
    while p < numParams:
        step = input("Enter the step of the parameter: ")
        param = input("Enter the parameter: ")
        value = input("Enter the value of this parameter: ")
        newParam = Parametric(step, param, value)
        valParam = newParam.validate(step, param, value)
        if valParam:
            paramsList.append(newParam)
        else:
            print("This is an invalid Parameter Object and will be omitted from the list.")
            continue

    return paramsList


def makeBCO():
    newMeta = makeMeta()
    print("USABILITY DOMAIN")
    newUse = str(input("Enter the Usability: "))
    newProv = makeProv()
    newExn = makeExecution()
    newDesc = makeDescription()
    newErr = makeError()
    newIO = makeIO()
    newParam = makeParametric()

    newBCO3 = BioComputeObject(newMeta, newUse, newProv, newExn, None, newDesc, newErr, newIO, newParam)
    valBCO = newBCO3.validate(newMeta, newUse, newProv, newExn, None, newDesc, newErr, newIO, newParam)
    if valBCO:
        return newBCO3
    else:
        tryAgain = input("Invalid BioCompute Object, would you like to try to build a valid BCO? (y/n)")
        if tryAgain == 'y':
            makeBCO()
        else:
            print("Exiting...'None' returned")
            return None


# bcoObject = makeBCO()
# pprint(vars(bcoObject))
# pprint(bcoObject.meta)
# pprint(vars(bcoObject.provenance_Domain))
# pprint(vars(bcoObject.usability_Domain))
# pprint(vars(bcoObject.description_Domain))
# pprint(vars(bcoObject.description_Domain.pipeline_Step))
# pprint(vars(bcoObject.execution_Domain))
# pprint(vars(bcoObject.execution_Domain.software_Prerequisites))
# pprint(vars(bcoObject.io_Domain))
# pprint(vars(bcoObject.io_Domain.input_Subdomain))
# pprint(vars(bcoObject.io_Domain.output_Subdomain))
# pprint(vars(bcoObject.parametric_Domain))







# *************************************** JSON TO BCO CLASS OBJECT FUNCTION + HELPER FUNCTIONS *************************************************

# turns string to DateTime class object
def strToDateTime(dateStr):

    # separate numbers of the date string from formatting chars ('-', ':', 'T', '.', '+')
    # pass numbers in to make DateTime object
    # Handle different formats with ifs, try-catch and 'None'

    idx1 = dateStr.index("-")
    idx2 = dateStr.index("-", idx1+1)
    idx3 = dateStr.index("T")
    idx4 = dateStr.index(":")
    idx5 = dateStr.index(":", idx4+1)
    idx6 = dateStr.index(".")
    # idx6 = dateStr.index("-")
    idx7 = idx6+3
    
    yr = dateStr[:idx1]
    mth = dateStr[idx1+1:idx2]
    d = dateStr[idx2+1:idx3]
    hr = dateStr[idx3+1:idx4]
    min = dateStr[idx4+1:idx5]
    sec = dateStr[idx5+1:idx6]

    try:
        idx8 = dateStr.index("+")
    except ValueError:
        idx8 = None
    try:
        idx9 = dateStr.index("-", idx2+1)
    except ValueError:
        idx9 = None
    
    if not idx8 is None:
        secfrac = dateStr[idx6+1:idx8]
        tzOff = dateStr[idx8+1:]
    elif not idx9 is None:
        secfrac = dateStr[idx6+1:idx9]
        tzOff = dateStr[idx9+1:]
    elif idx8 is None and idx9 is None:
        secfrac = dateStr[idx6+1:idx7]
        tzOff = dateStr[idx6+3:]


    dtObj = DateTime(yr, mth, d, hr, min, sec, secfrac, tzOff)
    
    # print(yr)
    # print(mth)
    # print(d)
    # print(hr)
    # print(min)
    # print(sec)
    # print(secfrac)
    # print(tzOff)
     
    return dtObj

# strToDateTime("2019-08-12T19:11:18.36-21:00")

# takes in string and returns Version object
def strToVersion(strVers):

    # separate numbers of the version string from formatting chars ('.')
    # pass numbers in to make Version object
    # Handle different formats with ifs, try-catch and 'None' (Major.Minor.Patch) and (Major.Minor)

    try:
        dotIdx1 = strVers.index(".")
    except: #Used when a version does not have a .
        dotIdx1 = strVers
        newVersion = SemanticVersion(strVers, 0, None)
        return newVersion
    try: 
        dotIdx2 = strVers.index(".", dotIdx1+1)
        major = strVers[:dotIdx1]
        minor = strVers[dotIdx1+1:dotIdx2]
        patch = strVers[dotIdx2+1:]

    except ValueError:
        major = strVers[:dotIdx1]
        minor = strVers[dotIdx1+1:]
        patch = None

    try:
        majorInt = int(major)
        minorInt = int(minor)
        if not patch is None:
            patchInt = int(patch)
        else:
            patchInt = None
        newVersion = SemanticVersion(majorInt, minorInt, patchInt)
    except ValueError:
        newVersion = None

    return newVersion


# FIXME: Clean up and check durability (type check all objects and arguments, all nonrequired fields must be wrapped in try-except:KeyError block regardless of where the item lives/what level it is.)
# Download published BCOs from website and feed them through function
# Validation is embedded in each make function

#THIS IS NOT COMPLETE. STILL NEEDS A LOT OF WORK. AS OF NOW IT EXPORTS JSON JUST FINE. HOWEVER, IT IS VERY VERY HARD TO READ 
def exportJSON(BCOin):
    #Converts all Domains to a dictionary
    if isinstance(BCOin, BioComputeObject):
        Set = {
            str(BCOin.description_Domain), 
            str(BCOin.error_Domain),
            str(BCOin.execution_Domain),
            str(BCOin.extension_Domain),
            str(BCOin.io_Domain),
            str(BCOin.metaData),
            str(BCOin.parametric_Domain),
            str(BCOin.usability_Domain)
        }
        json_object = json.dumps(list(Set))
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(json_object, f, ensure_ascii=False)
    return None

def importJSON(filepath):
    try:
        outputBCO = JSONtoClass(filepath)
    except FileNotFoundError:
        print("Please enter a valid file path")
    return outputBCO

#read in JSON file, create bco class instance from json
def JSONtoClass(jsonFn):
    f = open(jsonFn, 'r')

    data = json.load(f)
    etag = data["etag"]
    try:
        object_id = data["object_id"]
    except KeyError:
        object_id = None
    spec_Version = data["spec_version"]
    jMeta = Meta(object_id, etag, spec_Version)
    jUseList = []
    Uses = data["usability_domain"]

    for use in Uses:
        jUseList.append(str(use))

    prov = data["provenance_domain"]

    try:
        embargo = prov["embargo"]
    except KeyError:
        embargo = None

    provEmbargo = None
    if not embargo is None:
        try:
            startTime = embargo["start_time"]
            startTimeObj = strToDateTime(startTime)
        except KeyError:
            startTimeObj = None
        try:
            endTime = embargo["end_time"]
            endTimeObj = strToDateTime(endTime)
        except KeyError:
            endTimeObj = None
        provEmbargo = Embargo(startTimeObj, endTimeObj)

    try:
        obsoleteDate = prov["obsolete_after"]
        provObsoleteDate = strToDateTime(obsoleteDate)
    except KeyError:
        provObsoleteDate = None        

    provName = prov["name"]
    provVers = prov["version"]
    provLicense = prov["license"]

    try:
        provDerived = prov["derived_from"]
    except KeyError:
        provDerived = None

    contributors = prov["contributors"]

    try:
        review = prov["review"]
    except KeyError:
        review = None

    contrList = []
    revList = []
    # loop through contributors
    for cont in contributors:
        # print(cont)
        name = cont["name"] # only required field of contributor
        contr = cont["contribution"]

        try:
            aff = cont["affiliation"]
        except KeyError:
            aff = None
        
        try:
            email = cont["email"]
        except KeyError:
            email = None
        
        try:
            orcid = cont["orcid"]
        except KeyError:
            orcid = None

        tempCont = Contributor(contr, name, aff, email, orcid)
        contrList.append(tempCont)

    #status and reviewer name are required for reviewer
    if not review is None:
        for rev in review:
            # print(rev)
            status = rev["status"]
            revName = rev["reviewer"]["name"]
            contr = rev["reviewer"]["contribution"]

            try:
                aff = rev["reviewer"]["affiliation"]
            except KeyError:
                aff = None
        
            try:
                email = rev["reviewer"]["email"]
            except KeyError:
                email = None
        
            try:
                orcid = rev["reviewer"]["orcid"]
            except KeyError:
                orcid = None

            try:
                comment = rev["reviewer_comment"]
            except KeyError:
                comment = None
        
            try:
                date = rev["date"]
            except KeyError:
                date = None

            tempRev = Review(date, status, revName, comment, contr, aff, email, orcid)
            revList.append(tempRev)
    
    # print(contrList)
    # print(revList)

    provCreated = prov["created"] 
    provModified = prov["modified"] 
    createdDate = strToDateTime(provCreated)
    modifiedDate = strToDateTime(provModified)

    jProv = ProvenanceDomain(provName, provLicense, provVers, createdDate, modifiedDate, contrList, revList, provEmbargo, provObsoleteDate, provDerived)

#Description Domain

    descript = data["description_domain"]
    try:
        kw = descript["keywords"]
    except KeyError:
        kw = None

    try:
        plat = descript["platform"]
    except KeyError:
        plat = None
        
    try: 
        xRef = descript["xref"]
    except KeyError:
        xRef = None

    pipeStp = descript["pipeline_steps"]
    # inputs = pipeStp["input_list"]
    # outputs = pipeStp["output_list"]
    # prereqSt = pipeStp["prerequisite"]
    # name, description, prereqs list, inputs list, outputs list all required
    # Use raw json view in builder page with dummy data for non required fields to see the string key (ex. "sha1_checksum")
    pipeSteps = []
    xRefList = []
    inputsLst = []
    outputsLst = []
    prereqsLst = []
    keywordsList = []
    platformsList = []

    for ps in pipeStp:
        stName = ps["name"]
        stDesc = ps["description"]
        stepNum = ps["step_number"]
        inputs = ps["input_list"]
        outputs = ps["output_list"]
        try:
            prereqSt = ps["prerequisite"]
        except KeyError:
            prereqSt = None
        try:
            stVers = ps["version"]
            stepVersion = strToVersion(stVers)
        except KeyError:
            stepVersion = None

        for inpt in inputs:
            inputsUri = inpt["uri"]
            inputsUriObj = URI(inputsUri)
            try:
                inputsAT = inpt["access_time"]
                inputsAtObj = strToDateTime(inputsAT)
            except KeyError:
                inputsAtObj = None
            
            try: 
                inputsFn = inpt["filename"]
            except KeyError:
                inputsFn = None
            try:
                inputsCheck = inpt["sha1_checksum"]
            except KeyError:
                inputsCheck = None
            
            tempIn = Input(inputsUriObj, inputsFn, inputsAtObj, inputsCheck)
            inputsLst.append(tempIn)

        for outpt in outputs:
            outputsUri = outpt["uri"]
            outputsUriObj = URI(outputsUri)
            try:
                outputsAT = outpt["access_time"]
                outputsAtObj = strToDateTime(outputsAT)
            except KeyError:
                outputsAtObj = None
            try:
                outputsFn = outpt["filename"]
            except KeyError:
                outputsFn = None
            try:
                outputsCheck = outpt["sha1_checksum"]
            except KeyError:
                outputsCheck = None

            tempOut = Output(outputsUriObj, outputsFn, outputsAtObj, outputsCheck)
            outputsLst.append(tempOut)

        for pre in prereqSt:
            prereqUri = pre["uri"]["uri"]
            prereqUriObj = URI(prereqUri)
            try:
                prereqName = pre["name"]
            except KeyError:
                prereqName = None

            try:
                prereqAT = pre["uri"]["access_time"]
                prereqAtObj = strToDateTime(prereqAT)
            except KeyError:
                prereqAtObj = None

            try:
                prereqFn = pre["uri"]["filename"]
            except KeyError:
                prereqFn = None
            try:
                prereqCheck = pre["uri"]["sha1_checksum"]
            except KeyError:
                prereqCheck = None
            
            tempPrereq = Prerequisite(prereqName, prereqUriObj, prereqFn, prereqAtObj, prereqCheck)
            prereqsLst.append(tempPrereq)

        pStep = PipelineSteps(stepNum, stName, stDesc, inputsLst, outputsLst, stepVersion, prereqsLst)
        pipeSteps.append(pStep)

    # build xrefs list
    if not xRef is None:
        for x in xRef:
            nameSpace = x["namespace"]
            xName = x["name"]
            Ids = x["ids"]
            xIds = ObjectID(Ids)
            accessTime = x["access_time"]
            xAccessTime = strToDateTime(accessTime)
            tempX = Xref(nameSpace, xName, xIds, xAccessTime)
            xRefList.append(tempX)

    if not kw is None:
        for word in kw:
            keywordsList.append(word)
    
    if not plat is None:
        for platform in plat:
            platformsList.append(platform)


    jDescription = DescriptionDomain(keywordsList, pipeSteps, platformsList, xRefList)


    # build Execution Domain
    execution = data["execution_domain"]
    externalPoints = execution["external_data_endpoints"]
    softwarePrereqs = execution["software_prerequisites"]
    scriptDriver = execution["script_driver"]
    script = execution["script"]
    externalPtsList = []
    softwarePrereqsList = []
    scriptList = []
    
    for sc in script:
        scURI = sc["uri"]["uri"]
        scURIObj = URI(scURI)
        try:
            scFilename = sc["uri"]["filename"]
        except KeyError:
            scFilename = None
        try:
            scAccessTime = sc["uri"]["access_time"]
            scAT = strToDateTime(scAccessTime)
        except KeyError:
            scAT = None
        try:
            scCheck = sc["uri"]["sha1_checksum"]
        except KeyError:
            scCheck = None

        tempScript = Script(scFilename, scURIObj, scAT, scCheck)
        scriptList.append(tempScript)

    for swpr in softwarePrereqs:
        preName = swpr["name"]
        preVers = swpr["version"]
        preVersion = strToVersion(preVers)
        preUri = swpr["uri"]["uri"]
        prerequisiteURI = URI(preUri)

        try:
            preFilename = swpr["uri"]["filename"]
        except KeyError:
            preFilename = None
        try:
            preAccessTime = swpr["uri"]["access_time"]
            prerequisiteAT = strToDateTime(preAccessTime)
        except KeyError:
            prerequisiteAT = None
        try:
            preCheck = swpr["uri"]["sha1_checksum"]
        except KeyError:
            preCheck = None

        tempPre = SoftwarePrerequisites(preName, preVersion, prerequisiteURI, preFilename, prerequisiteAT, preCheck)
        softwarePrereqsList.append(tempPre)

    for point in externalPoints:
        ptURL = point["url"]
        ptName = point["name"]
        tempPT = ExternalDataEndpoints(ptName, ptURL)
        externalPtsList.append(tempPT)



    try:
        environmentVars = execution["environment_variables"]
    except KeyError:
        environmentVars = None

    keyList = []
    envKeyList = []
    valueList = []
    envValList = []

    counter = 0
    if not environmentVars is None:
        for var in environmentVars: 
            if counter % 2:
                valueList.append(var)
            else:
                keyList.append(var)
            counter += 1

        for key in keyList:
            tempKey = environmentVars[key]
            envKeyList.append(tempKey)

        for val in valueList:
            tempVal = environmentVars[val]
            envValList.append(tempVal)

    EnvVars = EnvironmentVariable(envKeyList, envValList)


    jExecution = ExecutionDomain(scriptList, scriptDriver, softwarePrereqsList, externalPtsList, EnvVars)

    # build Extension Domain
    extension = data["extension_domain"]
    userData = []
    extensionSchema = []
    for schemaVals in extension:
        try:
            tempVal = schemaVals["extension_schema"]
            extensionSchema.append(tempVal)
        except KeyError:
             extensionSchema = None
    
    if not extensionSchema is None:
        for var in extension:
            try:
                tempData = var
                userData.append(tempData)
            except KeyError:
                break
    jExtension = None
    #print(extensionSchema)
    #print(userData)
    #jExtension = ExtensionDomain(extensionSchema, userData)


    io = data["io_domain"]
    inputsList = []
    outputsList = []
    try:
        inSub = io["input_subdomain"]
        outSub = io["output_subdomain"]
    except KeyError:
        inSub = None
        outSub = None

    for inpt in inSub:
        inputURI = inpt["uri"]["uri"]
        inURI = URI(inputURI)
        try:
            inputFilename = inpt["uri"]["filename"]
        except KeyError:
            inputFilename = None
        
        try:
            inputAT = inpt["uri"]["access_time"]
            inAT = strToDateTime(inputAT)
        except KeyError:
            inAT = None
        
        try:
            inputCheck = inpt["uri"]["sha1_checksum"]
        except KeyError:
            inputCheck = None

        tempInput = InputSubdomain(inURI, inputFilename, inAT, inputCheck)
        inputsList.append(tempInput)

    for outpt in outSub:
        outputURI = outpt["uri"]["uri"]
        outURI = URI(outputURI)

        # Wanted to see if we could replace all the try catches with ifs to reduce complexity/ make it cleaner 
        # but accessing a non-existant key throws Key Error, even if it is in the condition of the if statement
        # NOTE: Throws Key Error
        # outputFilename = outpt["uri"]["filename"]
        # if outpt["uri"]["filename"]:
        #     outputFilename = outpt["uri"]["filename"]
        # else:
        #     outputFilename = None

        # NOTE: Throws Key Error
        # outputFilename = outpt["uri"]["filename"]
        # if outputFilename:
        #     continue
        # else:
        #     outputFilename = None
        
        try:
            outputFilename = outpt["uri"]["filename"]
        except KeyError:
            outputFilename = None

        try:
            outputAT = outpt["uri"]["access_time"]
            outAT = strToDateTime(outputAT)
        except KeyError:
            outAT = None

        try:
            outputCheck = outpt["uri"]["sha1_checksum"]
        except KeyError:
            outputCheck = None

        try:
            media = outpt["mediatype"]
        except KeyError:
            media = None

        tempOutput = OutputSubdomain(outURI, outputFilename, outputCheck, media, outAT)
        outputsList.append(tempOutput)


    jIO = IODomain(inputsList, outputsList)

    #build Parametric Domain
    try:
        parametric = data["parametric_domain"]
    except:
        parametric = None
    jParamList = []
    
    if not parametric is None:
        for param in parametric:
            paramStep = param["step"]
            parameter = param["param"]
            paramValue = param["value"]
            
            tempParam = Parametric(paramStep, parameter, paramValue)
            jParamList.append(tempParam)


    # build Error Domain
    err = data["error_domain"]
    try:
        emp = str(err["empirical_error"])
        alg = str(err["algorithmic_error"])
    except KeyError:
        emp = None
        alg = None

    jError = ErrorDomain(emp, alg)


    # BUILD BCO CLASS OBJECT 
    BCO_Class_Obj = BioComputeObject(jMeta, jUseList, jProv, jExecution, jExtension, jDescription, jError, jIO, jParamList)
    # pprint(vars(BCO_Class_Obj))
    # pprint(BCO_Class_Obj.meta)
    # pprint(vars(BCO_Class_Obj.provenance_Domain))
    # pprint(BCO_Class_Obj.usability_Domain)
    # pprint(vars(BCO_Class_Obj.description_Domain))
    # pprint(vars(BCO_Class_Obj.description_Domain.pipeline_Step))
    # pprint(vars(BCO_Class_Obj.execution_Domain))
    # pprint(vars(BCO_Class_Obj.execution_Domain.software_Prerequisites))
    # pprint(vars(BCO_Class_Obj.io_Domain))
    # pprint(vars(BCO_Class_Obj.io_Domain.input_Subdomain))
    # pprint(vars(BCO_Class_Obj.io_Domain.output_Subdomain))
    # pprint(vars(BCO_Class_Obj.parametric_Domain))
    exportJSON(BCO_Class_Obj)

    # BCO_Class_Obj.validate(jMeta, jUseList, jProv, jExecution, jExtension, jDescription, jError, jIO, jParamList)

    return BCO_Class_Obj

# newBCO1 = JSONtoClass("/Users/Panig/Desktop/extensionDomanText.json")
# newBCO2 = JSONtoClass("/Users/seanc/Desktop/CopyNumberCounterBCO.json")
newBCO3 = JSONtoClass("/Users/seanc/Desktop/TEST_BCO.json") # Modified pipeline to test areToolsRegistered() and alignSteps()









# *************************************************** COMPARISON STRUCTURE + SIMPLE COMPARISONS + HELPER FUNCTIONS *******************************************************

# sets BCO inputted to None. Needs more. Can be done once a container is made, a way to save out the BCO. 
def deleteBCO(BCOin):
    
    BCOin = None
    return BCOin

# returns true if the two BCOs are the same BCO 
def isSameBCO(BCO1, BCO2):

    if isinstance(BCO1, BioComputeObject):
        meta1 = BCO1.meta
    if isinstance(BCO2, BioComputeObject):
        meta2 = BCO2.meta

    if isinstance(meta1, Meta):
        etag1 = meta1.etag
    if isinstance(meta2, Meta):
        etag2 = meta2.etag

    if etag1 == etag2:
        return True
    return False


# print(isSameBCO(BCO_000139, newBCO3))

# returns true if one BCO is derived from the other
def isParentBCO(BCO1, BCO2):

    if isinstance(BCO1, BioComputeObject):
        meta1 = BCO1.meta
        prov1 = BCO1.provenance_Domain
    if isinstance(BCO2, BioComputeObject):
        meta2 = BCO2.meta
        prov2 = BCO2.provenance_Domain

    if isinstance(meta1, Meta):
        objID1 = meta1.bco_Id
    if isinstance(prov1, ProvenanceDomain):
        derived1 = prov1.derived_From        
    if isinstance(meta2, Meta):
        objID2 = meta2.bco_Id
    if isinstance(prov2, ProvenanceDomain):
        derived2 = prov2.derived_From

    if objID1 == derived2:
        print("In the order they were entered, BioCompute Object 1 is the parent BCO of BioCompute Object 2")
        return True
    elif objID2 == derived1:
        print("In the order they were entered, BioCompute Object 1 was derived from BioCompute Object 2")
        return True
    return False


def test2(BCO1, BCO2):
    if isinstance(BCO1, BioComputeObject):
        execution1 = BCO1.execution_Domain
    if isinstance(execution1, ExecutionDomain):
        softwarePres1 = execution1.software_Prerequisites
    if isinstance(BCO2, BioComputeObject):
        execution2 = BCO2.execution_Domain
    if isinstance(execution2, ExecutionDomain):
        softwarePres2 = execution2.software_Prerequisites



    # should just be comapring names, name, uri, version are the required fields.
    commonSwList = []
    swList1 = []
    swList2 = []
    for sw1 in softwarePres1:
        swList1.append(sw1.name)
    for sw2 in softwarePres2:
        swList2.append(sw2.name)

    for swp1 in softwarePres1:
        for swp2 in softwarePres2:
            if swp1 == swp2:
                commonSwList.append(swp1.name)
                swList1.remove(swp1.name)
                swList2.remove(swp2.name)

    if len(commonSwList) == 0:
        print("There are no common software prerequisites")
    else:    
        print("Common software prerequisites: ")
        pprint(commonSwList)

    if len(swList1) == 0 and len(swList2) == 0:
        print("There are no differences in software prerequisites")
    else:
        print("Different software prerequisites: ")
        pprint(swList1)
        pprint(swList2)
    return False

# test2(BCO_000139, newBCO3)

# compares the prerequisites, script driver, and external data endpoints needed to run each pipeline
def comparePrereqs(BCO1, BCO2):
    if isinstance(BCO1, BioComputeObject):
        execution1 = BCO1.execution_Domain
    if isinstance(execution1, ExecutionDomain):
        scriptDriver1 = execution1.script_Driver
        softwarePres1 = execution1.software_Prerequisites
        external1 = execution1.external_Data_Endpoints
    if isinstance(BCO2, BioComputeObject):
        execution2 = BCO2.execution_Domain
    if isinstance(execution2, ExecutionDomain):
        scriptDriver2 = execution2.script_Driver
        softwarePres2 = execution2.software_Prerequisites
        external2 = execution2.external_Data_Endpoints
    if isinstance(softwarePres1, SoftwarePrerequisites):
        swpName1 = softwarePres1.name
        swpURI1 = softwarePres1.uri
        swpVersion1 = softwarePres1.version
    if isinstance(softwarePres2, SoftwarePrerequisites):
        swpName2 = softwarePres1.name
        swpURI2 = softwarePres1.uri
        swpVersion2 = softwarePres1.version


    # should just be comapring names, name, uri, version are the required fields.
    commonSwList = []
    swList1 = []
    swList2 = []
    for sw1 in softwarePres1:
        swList1.append(sw1)
    for sw2 in softwarePres2:
        swList2.append(sw2)

    for swp1 in softwarePres1:
        for swp2 in softwarePres2:
            if swp1.name is swp2.name:
                commonSwList.append(swp1.name)
                swList1.remove(swp1.name)
                swList2.remove(swp2.name)

    if len(commonSwList) == 0:
        print("There are no common software prerequisites")
    else:    
        print("Common software prerequisites: ")
        pprint(commonSwList)

    if len(swList1) == 0 and len(swList2) == 0:
        print("There are no differences in software prerequisites")
    else:
        print("Different software prerequisites: ")
        pprint(swList1)
        pprint(swList2)

    if scriptDriver1 == scriptDriver2:
        print("Script Drivers are the same")
    else: 
        print("Script Drivers are different: ")
        pprint(scriptDriver1)
        pprint(scriptDriver2)

    # compare external data endpoints same way as software prerequisites
    
    return False

def getToolType(toolName):
    # query toolType database in git and return string type
    targetFile = 'https://raw.github.com/biocompute-objects/-Tool-Type-Dictionary/main/toolsDictionary.json'
    req = requests.get(targetFile)
    typeDict = json.loads(req.text)

    toolType = None
    for type in typeDict:
        if typeDict[type] == toolName:
            toolType = type

    # print(toolType)
    return toolType

def alignLogic():
    wfl1 = ["Alignment", "Variant Calling", "Annotation", "Enrichment"]
    wfl2 = ["Alignment", "Variant Calling", "Filtering", "Annotation"]
    overlap = []

    if len(wfl1) > len(wfl2):
        diff = len(wfl1) -len(wfl2)
    else:
        diff = len(wfl2) - len(wfl1)

    for i in range(len(wfl1)):
        for j in range(len(wfl2)):
            # print(i, wfl1[i], j, wfl2[j])
            if i == j and wfl1[i] == wfl2[j]:
                overlap.append(wfl1[i])
            if i < len(wfl1) and j < len(wfl2):
                if wfl1[i] == wfl2[j] and i == j+1:
                    overlap.append(None)
                    wfl2.insert(i-1, None)
                    print(wfl1)
                    print(wfl2)
                elif wfl1[i] == wfl2[j] and i+1 == j:
                    overlap.append(None)
                    wfl1.insert(j-1, None)
                    print(wfl1)
                    print(wfl2)
    if wfl1[len(wfl1)-1] != wfl2[len(wfl2)-1]:
                overlap.append(None) 

    while diff > 0:
        overlap.append(None)
        diff -= 1

    print(overlap)

    return None

# alignLogic()

def alignSteps(BCO1, BCO2):
    # NOTE: can assume tools are registered in toolType dictionary 

    if isinstance(BCO1, BioComputeObject):
        desc_BCO1 = BCO1.description_Domain
    if isinstance(BCO2, BioComputeObject):
        desc_BCO2 = BCO2.description_Domain
    if isinstance(desc_BCO1, DescriptionDomain):
        workflow1 = desc_BCO1.pipeline_Step
    if isinstance(desc_BCO2, DescriptionDomain):
        workflow2 = desc_BCO2.pipeline_Step

    # Make list to represent workflows with just the tooltype. (Loop through steps, call getTooltype, add it to list)
    # Need to be able to modify the lists, can't work with actual pipelinesteps list

    PipelineToolTypes1 = []
    PipelineToolTypes2 = []
    overlapList = []
    
    for step1 in workflow1:
        tempType1 = getToolType(step1.name)
        PipelineToolTypes1.append(tempType1)

    for step2 in workflow2:
        tempType2 = getToolType(step2.name)
        PipelineToolTypes2.append(tempType2)

    # print(PipelineToolTypes1)
    # print(PipelineToolTypes2)

    if len(PipelineToolTypes1) > len(PipelineToolTypes2):
        diff = len(PipelineToolTypes1) - len(PipelineToolTypes2)
    else:
        diff = len(PipelineToolTypes2) > len(PipelineToolTypes1)

    for i in range(len(PipelineToolTypes1)):
        for j in range(len(PipelineToolTypes2)):
            if i == j and PipelineToolTypes1[i] == PipelineToolTypes2[j]:
                overlapList.append(PipelineToolTypes1[i])
            if i < len(PipelineToolTypes1) and j < len(PipelineToolTypes2):
                if PipelineToolTypes1[i] == PipelineToolTypes2[j] and i == j+1:
                    overlapList.append("-------")
                    PipelineToolTypes2.insert(i-1, "-------")
                elif PipelineToolTypes1[i] == PipelineToolTypes2[j] and i+1 == j:
                    overlapList.append("-------")
                    PipelineToolTypes1.insert(j-1, "-------")
    if PipelineToolTypes1[len(PipelineToolTypes1)-1] != PipelineToolTypes2[len(PipelineToolTypes2)-1]:
        overlapList.append("-------")

    while diff > 0:
        overlapList.append("-------")
        diff -= 1

    
    outputList = [overlapList, PipelineToolTypes1, PipelineToolTypes2] # Helps with command line output 
    
    # print(overlapList)

    return outputList

# alignSteps(BCO_000139, newBCO3)

def alignedOutput():
    lists = alignSteps(BCO_000139, newBCO3)
    print('\n')
    print('{:50} {:50} {:50}'.format("Workflow Overlap", "BCO 1", "BCO 2"))
    print('\n')
    for x, y, z in zip(*lists):
        print('{:50} {:50} {:50}'.format(x, y, z))

alignedOutput()


# Loops through pipeline steps for both BCOs and checks if the tool used in each step is registered in the toolType repo
# Retruns true if tools of ALL steps of BOTH bcos are registered, false otherwise
def areToolsRegistered(BCO1, BCO2):
    # targetFile2 = 'https://raw.github.com/skeeney01/-Tool-Type-Dictionary/main/toolsDictionary.json'
    targetFile = 'https://raw.github.com/biocompute-objects/-Tool-Type-Dictionary/main/toolsDictionary.json'
    req = requests.get(targetFile)
    typeDict = json.loads(req.text)

    # Make dummy pipelines that are registered to check logic:

    input_0_URI_TEST = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/1_download.sh")
    output_0_URI_TEST = URI("https://github.com/dpastling/plethora/blob/master/data/1000Genomes_samples.txt")
    input_0_TEST = Input(input_0_URI_TEST, None, None, None)
    output_0_TEST = Output(output_0_URI_TEST, None, None, None)
    inputArr0_TEST = [input_0_TEST]
    outputArr0_TEST = [output_0_TEST]
    prereqURI0_TEST = URI("https://github.com")
    prereq0_TEST = Prerequisite("Prerequisite 0", prereqURI0_TEST, None, None, None)
    prereqList0_TEST = [prereq0_TEST]
    pipelineStp0_TEST = PipelineSteps(0, "Bowtie2", "self script downloads the fastq files for each sample from the 1000 Genomes site as specified in a sample_index file", inputArr0_TEST, outputArr0_TEST, None, prereqList0_TEST)

    input_1_URI_TEST = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/2_trim.sh")
    output_1_URI_TEST = URI("https://github.com/dpastling/plethora/blob/master/logs/trim_stats.txt")
    input_1_TEST = Input(input_1_URI_TEST, None, None, None)
    output_1_TEST = Output(output_1_URI_TEST, None, None, None)
    inputArr1_TEST = [input_1_TEST] 
    outputArr1_TEST = [output_1_TEST]
    prereqURI1_TEST = URI("https://github.com/dpastling/plethora/blob/master")
    prereq1_TEST = Prerequisite("Prerequisite 1", prereqURI1_TEST, None, None, None)
    prereqList1_TEST = [prereq1_TEST]
    pipelineStp1_TEST = PipelineSteps(1, "Heptagon", "self script automates the task of trimming low quality bases from the 3' ends of the reads and removes any that are shorter than 80 bp.", inputArr1_TEST, outputArr1_TEST, None, prereqList1_TEST)

    input_2_URI_TEST = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/3_batch_bowtie.sh")
    output_2_URI_TEST = URI("https://github.com/dpastling/plethora/blob/master/align_report.txt")
    input_2_TEST = Input(input_2_URI_TEST, None, None, None)
    output_2_TEST = Output(output_2_URI_TEST, None, None, None)
    inputArr2_TEST = [input_2_TEST]
    outputArr2_TEST = [output_2_TEST]
    prereqURI2_TEST = URI("https://github.com/dpastling/plethora/blob/master/code")
    prereq2_TEST = Prerequisite("Prerequisite 2", prereqURI2_TEST, None, None, None)
    prereqList2_TEST = [prereq2_TEST]
    pipelineStp2_TEST = PipelineSteps(2, "metaseqR", "self script aligns reads to the genome with Bowtie2.", inputArr2_TEST, outputArr2_TEST, None, prereqList2_TEST)

    input_3_URI_TEST = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/5_batch_make_bed.sh")
    output_3_URI_TEST = URI("https://github.com/dpastling/plethora/blob/master/results/test_read_depth.bed")
    input_3_TEST = Input(input_3_URI_TEST, None, None, None)
    output_3_TEST = Output(output_3_URI_TEST, None, None, None)
    inputArr3_TEST = [input_3_TEST]
    outputArr3_TEST = [output_3_TEST]
    prereqURI3_TEST = URI("https://github.com/dpastling/plethora/blob/master/code")
    prereq3_TEST = Prerequisite("Prerequisite 3", prereqURI3_TEST, None, None, None)
    prereqList3_TEST = [prereq3_TEST]
    pipelineStp3_TEST = PipelineSteps(3, "dbSNP", "self script: Coverts the .bam alignment file into bed format. Parses the reads Calls the merge_pairs.pl script (described below) to combined proper pairs into a single fragment. Finds overlaps with the reference bed file containing the regions of interest (e.g. DUF1220). Calculates the average coverage for each region: (number of bases that overlap) / (domain length)", inputArr3_TEST, outputArr3_TEST, None, prereqList3_TEST)

    pipelineSteps_TEST = [pipelineStp0_TEST, pipelineStp1_TEST, pipelineStp2_TEST, pipelineStp3_TEST]



    input_0_URI_TEST2 = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/1_download.sh")
    output_0_URI_TEST2 = URI("https://github.com/dpastling/plethora/blob/master/data/1000Genomes_samples.txt")
    input_0_TEST2 = Input(input_0_URI_TEST2, None, None, None)
    output_0_TEST2 = Output(output_0_URI_TEST2, None, None, None)
    inputArr0_TEST2 = [input_0_TEST2]
    outputArr0_TEST2 = [output_0_TEST2]
    prereqURI0_TEST2 = URI("https://github.com")
    prereq0_TEST2 = Prerequisite("Prerequisite 0", prereqURI0_TEST2, None, None, None)
    prereqList0_TEST2 = [prereq0_TEST2]
    pipelineStp0_TEST2 = PipelineSteps(0, "Bowtie2", "self script downloads the fastq files for each sample from the 1000 Genomes site as specified in a sample_index file", inputArr0_TEST2, outputArr0_TEST2, None, prereqList0_TEST2)

    input_1_URI_TEST2 = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/2_trim.sh")
    output_1_URI_TEST2 = URI("https://github.com/dpastling/plethora/blob/master/logs/trim_stats.txt")
    input_1_TEST2 = Input(input_1_URI_TEST2, None, None, None)
    output_1_TEST2 = Output(output_1_URI_TEST2, None, None, None)
    inputArr1_TEST2 = [input_1_TEST2] 
    outputArr1_TEST2 = [output_1_TEST2]
    prereqURI1_TEST2 = URI("https://github.com/dpastling/plethora/blob/master")
    prereq1_TEST2 = Prerequisite("Prerequisite 1", prereqURI1_TEST2, None, None, None)
    prereqList1_TEST2 = [prereq1_TEST2]
    pipelineStp1_TEST2 = PipelineSteps(1, "Heptagon", "self script automates the task of trimming low quality bases from the 3' ends of the reads and removes any that are shorter than 80 bp.", inputArr1_TEST2, outputArr1_TEST2, None, prereqList1_TEST2)

    input_2_URI_TEST2 = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/3_batch_bowtie.sh")
    output_2_URI_TEST2 = URI("https://github.com/dpastling/plethora/blob/master/align_report.txt")
    input_2_TEST2 = Input(input_2_URI_TEST2, None, None, None)
    output_2_TEST2 = Output(output_2_URI_TEST2, None, None, None)
    inputArr2_TEST2 = [input_2_TEST2]
    outputArr2_TEST2 = [output_2_TEST2]
    prereqURI2_TEST2 = URI("https://github.com/dpastling/plethora/blob/master/code")
    prereq2_TEST2 = Prerequisite("Prerequisite 2", prereqURI2_TEST2, None, None, None)
    prereqList2_TEST2 = [prereq2_TEST2]
    pipelineStp2_TEST2 = PipelineSteps(2, "metaseqR", "self script aligns reads to the genome with Bowtie2.", inputArr2_TEST2, outputArr2_TEST2, None, prereqList2_TEST2)

    input_3_URI_TEST2 = URI("https://github.com/dpastling/plethora/blob/master/code/1000genomes/5_batch_make_bed.sh")
    output_3_URI_TEST2 = URI("https://github.com/dpastling/plethora/blob/master/results/test_read_depth.bed")
    input_3_TEST2 = Input(input_3_URI_TEST2, None, None, None)
    output_3_TEST2 = Output(output_3_URI_TEST2, None, None, None)
    inputArr3_TEST2 = [input_3_TEST2]
    outputArr3_TEST2 = [output_3_TEST2]
    prereqURI3_TEST2 = URI("https://github.com/dpastling/plethora/blob/master/code")
    prereq3_TEST2 = Prerequisite("Prerequisite 3", prereqURI3_TEST2, None, None, None)
    prereqList3_TEST2 = [prereq3_TEST2]
    pipelineStp3_TEST2 = PipelineSteps(3, "badName", "self script: Coverts the .bam alignment file into bed format. Parses the reads Calls the merge_pairs.pl script (described below) to combined proper pairs into a single fragment. Finds overlaps with the reference bed file containing the regions of interest (e.g. DUF1220). Calculates the average coverage for each region: (number of bases that overlap) / (domain length)", inputArr3_TEST2, outputArr3_TEST2, None, prereqList3_TEST2)

    pipelineSteps_TEST2 = [pipelineStp0_TEST2, pipelineStp1_TEST2, pipelineStp2_TEST2, pipelineStp3_TEST2]

    if isinstance(BCO1, BioComputeObject):
        desc_BCO1 = BCO1.description_Domain
    if isinstance(BCO2, BioComputeObject):
        desc_BCO2 = BCO2.description_Domain
    if isinstance(desc_BCO1, DescriptionDomain):
        workflow1 = desc_BCO1.pipeline_Step
    if isinstance(desc_BCO2, DescriptionDomain):
        workflow2 = desc_BCO2.pipeline_Step

    # loop through pipeline steps, search toolType dictionary 
    # keep track of how many matches there are and compare that to the length of the pipeline steps list. 
    toolRegistered = False
    matchCount1 = 0
    for w1 in pipelineSteps_TEST:
        for idx in typeDict:
            # print(w1.name, typeDict[idx])
            if w1.name == typeDict[idx]:
                matchCount1 += 1

    matchCount2 = 0
    for w2 in pipelineSteps_TEST2:
        for idx2 in typeDict:
            if w2.name == typeDict[idx2]:
                matchCount2 += 1
    
    if matchCount1 == len(pipelineSteps_TEST) and matchCount2 == len(pipelineSteps_TEST2):
        toolRegistered = True
    else:
        toolRegistered = False

    print(toolRegistered)
    return toolRegistered

# areToolsRegistered(BCO_000139, newBCO3)

# outputs simple side by side comparison of bco workflows if either one contains a tool not registered in the toolType Dictionary
# Shows the step number and name
def sideBySideWorkflows(BCO1, BCO2):
    if isinstance(BCO1, BioComputeObject):
        desc_BCO1 = BCO1.description_Domain
    if isinstance(BCO2, BioComputeObject):
        desc_BCO2 = BCO2.description_Domain
    if isinstance(desc_BCO1, DescriptionDomain):
        workflow1 = desc_BCO1.pipeline_Step
    if isinstance(desc_BCO2, DescriptionDomain):
        workflow2 = desc_BCO2.pipeline_Step

    print("\n")
    print(" High Level View of each Workflow")
    print("\n")
    print('{:50} {:50}'.format("Pipeline 1", "Pipeline 2"))
    print("\n")
    for i, j in list(itertools.zip_longest(workflow1, workflow2, fillvalue= None)):
        try:
            # print("Step %s: %s \t \t \t \t|\t \t Step %s: %s \n" %(i.step_Number, i.name,i.step_Number, j.name))
            print('{} {:50} {} {:50}'.format(i.step_Number, i.name, j.step_Number, j.name))
        except AttributeError:
            if not i is None:
                # print("Step ", i.step_Number, i.name, "\t \t \t |")
                print('{:50} {:50}'.format(i.step_Number, i.name))
            elif not j is None:
                # print(" \t \t ------------- \t \t \t \t \t| \t \t \t ", "Step ", j.step_Number, ": ", j.name)
                print('{:50} {:50}'.format(j.step_Number, j.name))
            else:
                continue

    # expand = input("Would you like to print all parts of each pipeline step, for both pipelines? (y/n): ")
    # if expand == 'y':
    #     for i, j in list(itertools.zip_longest(workflow1, workflow2, fillvalue= None)):
    #         print("\n %s \n %s \n" %(i, j))
    return None

# sideBySideWorkflows(BCO_000139, newBCO3)


# compares software prereqs, checks if two BCOs are the same or if one is derived from the other
# can take in BCO class object and json (any combination of the two)
def simpleStats(BCO1, BCO2):
    if isinstance(BCO1, BioComputeObject) and isinstance(BCO2, BioComputeObject):
        if isSameBCO(BCO1, BCO2):
            print("These two BioCompute Class Objects are the same")
            return None
        else:
            comparePrereqs(BCO1, BCO2)
            isParentBCO(BCO1, BCO2)
    elif isinstance(BCO1, BioComputeObject) and isinstance(BCO2, json):
        classObj2 = JSONtoClass(BCO2)
        if isSameBCO(BCO1, classObj2):
            print("These two BioCompute Class Objects are the same")
            return None
        else:
            comparePrereqs(BCO1, classObj2)
            isParentBCO(BCO1, classObj2)
    elif isinstance(BCO1, json) and isinstance(BCO2, BioComputeObject):
        classObj1 = JSONtoClass(BCO1)
        if isSameBCO(classObj1, BCO2):
            print("These two BioCompute Class Objects are the same")
            return None
        else:
            comparePrereqs(classObj1, BCO2)
            isParentBCO(classObj1, BCO2)    
    elif isinstance(BCO1, json) and isinstance(BCO2, json):
        classObj1 = JSONtoClass(BCO1)
        classObj2 = JSONtoClass(BCO2)
        if isSameBCO(classObj1, classObj2):
            print("These two BioCompute Class Objects are the same")
            return None
        else:
            comparePrereqs(classObj1, classObj2)
            isParentBCO(classObj1, classObj2)
    else:
        print("Invalid BCOs Entered. (Must be BioCompute Object Class instance or JSON)")
        return None


# output graphic function? -Torcivia 
    # Workflow overlap graphic:
        # loop through overlapList, if not None, print box with tooltype, else output grey filler box

    # individual BCO workflow graphics:
        # loop through both pipelines ->
        # check if tool types are the same
        # check if tools themselves are the same
        # check if versions are the same 
        # check if parameters are the same
        # output boxes and red text/lines/dots where there are differences



# Compare function takes in two BCOs in either class object or json (any combination)
# checks if tools are registered in type tool repo
# If tools are registered, the steps of pipelines are aligned
# will output graphic of aligned steps + workflow overlap 
# otherwise command line side by side of workflows is output
def compare(BCO1, BCO2):

    if isinstance(BCO1, BioComputeObject) and isinstance(BCO2, BioComputeObject):
        if areToolsRegistered(BCO1, BCO2):
            alignSteps(BCO1, BCO2)
            # output graphic here
        else: 
            sideBySideWorkflows(BCO1, BCO2)
    elif isinstance(BCO1, BioComputeObject) and isinstance(BCO2, json):
        classObj2 = JSONtoClass(BCO2)
        if areToolsRegistered(BCO1, classObj2):
            alignSteps(BCO1, classObj2)
            # output graphic here
        else: 
            sideBySideWorkflows(BCO1, classObj2)
    elif isinstance(BCO1, json) and isinstance(BCO2, BioComputeObject):
        classObj1 = JSONtoClass(BCO1)
        if areToolsRegistered(classObj1, BCO2):
            alignSteps(classObj1, BCO2)
            # output graphic here
        else: 
            sideBySideWorkflows(classObj1, BCO2)  
    elif isinstance(BCO1, json) and isinstance(BCO2, json):
        classObj1 = JSONtoClass(BCO1)
        classObj2 = JSONtoClass(BCO2)
        if areToolsRegistered(classObj1, classObj2):
            alignSteps(classObj1, classObj2)
            # output graphic here
        else: 
            sideBySideWorkflows(classObj1, classObj2)
    else:
        print("Invalid BCOs Entered. (Must be BioCompute Object Class instance or JSON)")


    return None
    

# more simple comparison made by user specified domain

def compareByDomain(BCO1, BCO2):
    if not (isinstance(BCO1, BioComputeObject) and isinstance(BCO2, BioComputeObject)):
        print("Error please make sure inputs are of type BioComputeObject or json")
        return 0
    userIn = str.lower(input(print("Please enter which domains you would like to compare. Enter 'Help' for keywords: ")))
    match userIn:
        case 'help':
            print("With this command you can compare two areas of a domain. The domains being Meta, Provenace, Execution, Description, Inputs, Outputs, Error and Parameters. Extension is not supported as the Extension domain is a user defined type.  To compare two domains type the name of the domain. For example, to compare two Parameter domains type 'Parameter'. To exit type 'EXIT'")
            compareByDomain(BCO1, BCO2)
        case 'exit':
            print("Exiting method. Returning a value of 0")
            return 0
        case 'meta':
            print("Comparing Meta Domains: ")
            compareMeta(BCO1, BCO2)
        case 'provenance': 
            print("Comparing Provenance Domains: ")
            compareProvenance(BCO1, BCO2)
        case 'execution':
            print("Comparing Execution Domains: ")
            compareExecution(BCO1, BCO2)
        case 'description': 
            print("Comparing Description Domains: ")
            compareDescription(BCO1, BCO2)
        case 'inputs': 
            print("Comparing Description Domains: ")
            compareInputs(BCO1, BCO2)
        case 'outputs': 
            print("Comparing Description Domains: ")
            compareOutputs(BCO1, BCO2)   
        case 'error': 
            print("Comparing Error Domains: ")
            compareError(BCO1, BCO2)   
        case 'parameter': 
            print("Comparing Parameter Domains: ")
            compareParameters(BCO1, BCO2) 
        case other:
            print("Please check your spelling you entered the wrong domain. If you would like to exit type 'EXIT'")
            compareByDomain(BCO1, BCO2)
def compareMeta(BCO1, BCO2):
    userIn = str.lower(input(print("What parts of the meta data would you like to view? Type 'Help' for keywords: ")))
    match userIn:
        case 'help':
            print("You can view both BCOs Etags, BCOid, SpecVersions by typing their respective names. For example, if you wanted to view BCOids type 'BCOid'. To view all of them by typing 'ALL'. ")
            compareMeta(BCO1, BCO2)
        case 'exit':
            print("Exiting method. Returning a value of 0")
            return 0
        case 'all':
            print("BCO 1: ", BCO1.meta)
            print("BCO 2: ", BCO2.meta)
        case 'etag':
            print("BCO 1: ", BCO1.metaData.e_tag)
            print("BCO 2: ", BCO2.metaData.e_tag)
        case 'bcoid':
            print("BCO 1: ", BCO1.metaData.bcoId)
            print("BCO 2: ", BCO2.metaData.bcoId)
        case 'specversion':
            print("BCO 1: ", BCO1.metaData.version)
            print("BCO 2: ", BCO2.metaData.version)
        case other:
            print("Please check your spelling. To exit type 'EXIT'")
            compareMeta(BCO1, BCO2)
    return None

def compareProvenance(BCO1, BCO2):
     userIn = str.lower(input(print("What parts of the Provenance data would you like to view? Type 'Help' for keywords: ")))
     match userIn:
        case 'help':
            print("You can view Name, License, Version, Created, Modified, Contributors, Review, Embargo, Obsolete, Derived_From by typing their respective names. For example, if you wanted to view name type 'Name'. To view all of them by typing 'ALL'. ")
            compareProvenance(BCO1, BCO2)
        case 'exit':
            print("Exiting method. Returning a value of 0")
            return 0
        case 'all':
            print("BCO 1: ", BCO1.provenance)
            print("BCO 2: ", BCO2.provenance)
        case 'name':
            print("BCO 1: ", BCO1.provenance_Domain.provName)
            print("BCO 2: ", BCO1.provenance_Domain.provName)
        case 'license':
            print("BCO 1: ", BCO1.provenance_Domain.provLicense)
            print("BCO 2: ", BCO1.provenance_Domain.provLicense)
        case 'version':
            print("BCO 1: ", BCO1.provenance_Domain.provVersion)
            print("BCO 2: ", BCO1.provenance_Domain.provVersion)
        case 'created':
            print("BCO 1: ", BCO1.provenance_Domain.provCreated)
            print("BCO 2: ", BCO1.provenance_Domain.provCreated)
        case 'contributors':
            print("BCO 1: ", BCO1.provenance_Domain.provContributors)
            print("BCO 2: ", BCO1.provenance_Domain.provContributors)
        case 'modified':
            print("BCO 1: ", BCO1.provenance_Domain.provModified)
            print("BCO 2: ", BCO1.provenance_Domain.provModified)
        case 'review':
            print("BCO 1: ", BCO1.provenance_Domain.provReview)
            print("BCO 2: ", BCO1.provenance_Domain.provReview)
        case 'embargo':
            print("BCO 1: ", BCO1.provenance_Domain.provEmbargo)
            print("BCO 2: ", BCO1.provenance_Domain.provEmbargo)
        case 'obselete':
            print("BCO 1: ", BCO1.provenance_Domain.provObsolete)
            print("BCO 2: ", BCO1.provenance_Domain.provObsolete)
        case 'derived from':
            print("BCO 1: ", BCO1.provenance_Domain.provDerived)
            print("BCO 2: ", BCO1.provenance_Domain.provDerived)
        case other:
            print("Please check your spelling. To exit type 'EXIT'")
            compareProvenance(BCO1, BCO2)
def compareExecution(BCO1, BCO2):
    userIn = str.lower(input(print("What parts of the Execution data would you like to view? Type 'Help' for keywords: ")))
    match userIn:
        case 'all':
            print("BCO 1: ", BCO1.execution)
            print("BCO 2: ", BCO2.execution)
        case 'script':
            print("BCO 1: ", BCO1.execution_Domain.exScript)
            print("BCO 2: ", BCO2.execution_Domain.exScript)
        case 'scriptdriver': 
            print("BCO 1: ", BCO1.execution_Domain.scriptDr)
            print("BCO 2: ", BCO2.execution_Domain.scriptDr)
        case 'prerequisites':
            print("BCO 1: ", BCO1.execution_Domain.swPrereqs)
            print("BCO 2: ", BCO2.execution_Domain.swPrereqs)
        case 'enviornmentalvariable':
            print("BCO 1: ", BCO1.execution_Domain.envVars)
            print("BCO 2: ", BCO2.execution_Domain.envVars)
        case 'externaldata':
            print("BCO 1: ", BCO1.execution_Domain.extDataEP)
            print("BCO 2: ", BCO2.execution_Domain.extDataEP)
        case 'help':
             print("You can view script, scriptdriver, prerequisites, externaldata, and environmentalvariables. For example, to view Environmental Variables type 'enviornmentalvariables' in the command line. To view ALL data type 'all' ")
             compareExecution(BCO1, BCO2)
        case 'exit':
            print("Exiting method. Returning a value of 0")
            return 0
        case other:
            print("Please check your spelling. To exit type 'EXIT'")
            compareExecution(BCO1, BCO2)
    
def compareDescription(BCO1, BCO2):
    userIn = str.lower(input(print("What parts of the Description data would you like to view? Type 'Help' for keywords: ")))
    match userIn:
        case 'all':
            print("BCO 1: ", BCO1.description)
            print("BCO 2: ", BCO2.description)
        case 'help':
             print("You can view keywords, pipeline, and xref. For example, to view pipeline type 'pipeline' in the command line. To view ALL data type 'all' ")
             compareDescription(BCO1, BCO2)
        case 'exit':
            print("Exiting method. Returning a value of 0")
            return 0
        case 'keywords':
            print("BCO 1: ", BCO1.description_Domain.descKeyword)
            print("BCO 2: ", BCO2.description_Domain.descKeyword)
        case 'pipeline':
             print("BCO 1: ", BCO1.description_Domain.pipeLine)
             print("BCO 2: ", BCO2.description_Domain.pipeLine)
        case 'xref':
            print("BCO 1: ", BCO1.description_Domain.descXref)
            print("BCO 2: ", BCO2.description_Domain.descXref)
        case other:
            print("Please check your spelling. To exit type 'EXIT'")
            compareDescription(BCO1, BCO2)

def compareInputs(BCO1, BCO2):
    userIn = str.lower(input(print("What parts of the Inputs data would you like to view? Type 'Help' for keywords: ")))
    match userIn:
        case 'all':
            print("BCO 1: ", BCO1.io_Domain.input_Subdomain)
            print("BCO 2: ", BCO2.io_Domain.input_Subdomain)
        case 'help':
             print("You can view all of the input subdomain data. To do so type 'all'. To exit type exit. ")
             compareInputs(BCO1, BCO2)
        case 'exit':
            print("Exiting method. Returning a value of 0")
            return 0
        case other:
            print("Please check your spelling. To exit type 'EXIT'")
            compareInputs(BCO1, BCO2)
        

def compareOutputs(BCO1, BCO2):
    userIn = str.lower(input(print("What parts of the Outputs data would you like to view? Type 'Help' for keywords: ")))
    match userIn:
        case 'all':
            print("BCO 1: ", BCO1.io_Domain.output_Subdomain)
            print("BCO 2: ", BCO2.io_Domain.output_Subdomain)
        case 'help':
             print("You can view all of the input subdomain data. To do so type 'all'. To exit type exit. ")
             compareOutputs(BCO1, BCO2)
        case 'exit':
            print("Exiting method. Returning a value of 0")
            return 0
        case other:
            print("Please check your spelling. To exit type 'EXIT'")
            compareOutputs(BCO1, BCO2)
def compareError(BCO1, BCO2):
    userIn = str.lower(input(print("What parts of the Error data would you like to view? Type 'Help' for keywords: ")))
    match userIn:
        case 'all':
            print("BCO 1: ", BCO1.error_Domain)
            print("BCO 2: ", BCO2.error_Domain)
        case 'help':
             print("You can view empricial error and algorithmic error. When typing out please forgo spaces To view all data type all.  To exit type exit. ")
             compareError(BCO1, BCO2)
        case 'exit':
            print("Exiting method. Returning a value of 0")
            return 0
        case 'empiricalerror':
            print("BCO 1: ", BCO1.error_Domain.empErr)
            print("BCO 2: ", BCO2.error_Domain.empErr)
        case 'algorithmicerror':
            print("BCO 1: ", BCO1.error_Domain.algErr)
            print("BCO 2: ", BCO2.error_Domain.algErr)
        case other:
            print("Please check your spelling. To exit type 'EXIT'")
            compareOutputs(BCO1, BCO2)

def compareParameters(BCO1, BCO2):
    userIn = str.lower(input(print("What parts of the Error data would you like to view? Type 'Help' for keywords: ")))
    match userIn:
        case 'all':
            print("BCO 1: ", BCO1.parametric_Domain)
            print("BCO 2: ", BCO2.parametric_Domain)
        case 'help':
             print("You can view steps, parameters and values. When typing out please forgo spaces To view all data type all.  To exit type exit. ")
             compareParameters(BCO1, BCO2)
        case 'exit':
            print("Exiting method. Returning a value of 0")
            return 0 
#EndChange
# returns true if two BCOs are compatible for concatenation
def ConcatCheck():
    return False

compareByDomain(BCO_000139, newBCO3)

# returns true if two BCOs are compatible for concatenation
def ConcatCheck():
    return False






# ****************************************************************** TASKS + NOTES ******************************************************************

# TODO: 
# Try with several BCOs and start to find out how robust the functions are. Check in with Rohan to see how many BCOs he fed into the functions he tested.
# Make commandline output for side by side and aligned workflows, output in matrix that can be made into graphic
# more thorough testing of make functions
# more thorough testing of JSON to BCO Class object function
# Usability Domain should be a list of strings
# Fill in domain comparison functions
# Implement Extention Domain, makeExtentionDomain function, add extension section to json translation function
# use getter/setter methods to make a modify existing BCO function
# make container for SAVED BCOs
# make function to save out BCO class objects
# more functionality: Derive/update from existing BCO, Save draft, Publish BCO
# Make delete BCO function 
# Serialize or something to save out published BOCS
# Function that qureies databse and checks that your environment is conforment
# graphical illustration for workflow




# NOTE:
# simplest case, for the alignment function, list limitations of the tool. 
# JSON to class instance made, need to go back and clear/improve durability
# versioning for an object for greater than less than 
# version mismatch checks? 

# compare should highlight differences in pipelines 
# start with just comparing two BCOS for now
# performance comparison ^^^^
# could implement tabular comparison by domain
# graphical representation of pipelines? <-- I think John Torcivia is tackling this
# compare tool type of each step: (aligner/variant calling/filter/annotation), next level step tool, then next level tool parameters of same steps

# Read into how to override characters like '<', '.', '=', '+'
# BCO1 < BCO2 which is the later version
# BCO1 = BCO2 are they the same BCO
# BCO1 + BCO2 Concatenate two BCOs. Hadley put a pin in this idea

# compare prerequisites to see if two pipelines can be run in the same environment 
# check for concatenation? 
# what is completely unified vs everything else is a difference. 
# need to align workflows to be able to compare piplines
# compare function dependent on best practices, tool type field and alignment of pipelines
# tool name, convert to all lowercase, look for if thats in the list of all other steps. Could have two different alignmets. Find in list and order in that list 
# search description domain, list of subdomains based on step name
# align by tool? 

# users populate BCO create, modify, delete by calling function instance of function
# focus on usability of semi-techincal users
# BCO here is a representation of real BCOs that can have functionality that maybe shouldn't be done on a draft or published bco
# BCO story vs API definition
# UPDATE bcotool readme

# All domain level validate() functions have been tested except for Extension Schema
# Most lower level validate() functions have been tested
# validate() functions are lebeled denoting their test status (tested or not)
# Type checking lists of obejcts is odd, lists can hold different types so just checked that that an argument is of type 'list'
# lists are not hashable, they cannot be the key in a map, so they had to be checked separatey because either a list object was the key or 
# 'list' python object was the key and both are unhashable. 

# writing out json equivalent. serialized version, essentially a binary smaller saved boject structure to recinstitute it. Look for save out objects in python
# saving out in json or binary json could be the only way that makes sense. Some way to save them out, user should 
# look into serialization, if serialized, only people in library can read it. 
# json: exporting/importing, then comparisons higher priority than cat. Use semvar library?
# graphical rep (dont worry about being stuck) OR concatenation,  arguments for the funcitons are added domains, default can be description or IO. 
# put this stuff in README (-) inbetween 
# Hold off on concatenation.

# maybe dont need saving right now vs 
# Regulatory package for specific roles, formats a report with usability, list of steps, not inputs poutputs, maybe not params either. Concsie report 
# uml diagram style workflow next to it. 
# Include parameters
# graphic workflow
# overriding/overloading equlaity greater than less than sings for versions of BCOs, newer or older versions can be functions too. do this for comparisons. BCO versioning isnt semantic

# concatenation BCOs and concatenates, validating that fields are compatible domians, and takes work flwo steps and add them into workflow of first step list and outputs new BCO
# concatentation, what needs to be the same to concatenate. Domains need to be compatible, identical vs not. iterative function override the plus, function that takes argumetns one required BCO, order matters.
# graph theory libraries, graph object, visulaize this, library for visualization compnent. Nodes and edges. 
# UML might work but can try to find something better. 
# serial workflow
# align nodes that are the same
