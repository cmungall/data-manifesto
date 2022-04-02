# Auto generated from data_manifesto.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-04-01T17:40:20
# Schema: datasets
#
# id: https://w3id.org/linkml/data-manifesto
# description: A datamodel for datasets
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
BALD = CurieNamespace('bald', 'https://www.opengis.net/def/binary-array-ld/')
BIBO = CurieNamespace('bibo', 'http://purl.org/ontology/bibo/')
CSVW = CurieNamespace('csvw', 'http://www.w3.org/ns/csvw#')
DATASETS = CurieNamespace('datasets', 'https://w3id.org/linkml/manifesto/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EDAM = CurieNamespace('edam', 'http://edamontology.org/')
FILE = CurieNamespace('file', 'file:///')
FORMATS = CurieNamespace('formats', 'http://www.w3.org/ns/formats/')
FRICTIONLESS = CurieNamespace('frictionless', 'https://specs.frictionlessdata.io/')
ISO19115 = CurieNamespace('iso19115', 'http://def.isotc211.org/iso19115/-1/2014/CitationAndResponsiblePartyInformation/code/CI_RoleCode/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MEDIATYPES = CurieNamespace('mediatypes', 'https://www.iana.org/assignments/media-types/')
OSLC = CurieNamespace('oslc', 'http://open-services.net/ns/core#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SH = CurieNamespace('sh', 'https://w3id.org/shacl/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
UPCORE = CurieNamespace('upcore', 'https://www.uniprot.org/core/')
VOID = CurieNamespace('void', 'http://rdfs.org/ns/void#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DATASETS


# Types

# Class references
class InformationName(extended_str):
    pass


class DataPackageName(InformationName):
    pass


class DataResourceName(InformationName):
    pass


@dataclass
class Information(YAMLRoot):
    """
    Grouping for datasets and data files
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASETS.Information
    class_class_curie: ClassVar[str] = "datasets:Information"
    class_name: ClassVar[str] = "Information"
    class_model_uri: ClassVar[URIRef] = DATASETS.Information

    name: Union[str, InformationName] = None
    download_url: Optional[Union[str, URI]] = None
    license: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    conforms_to: Optional[Union[str, URIorCURIE]] = None
    conforms_to_schema: Optional[Union[str, URIorCURIE]] = None
    conforms_to_class: Optional[Union[str, URIorCURIE]] = None
    version: Optional[str] = None
    language: Optional[str] = None
    publisher: Optional[Union[str, URIorCURIE]] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    issued: Optional[Union[str, XSDDateTime]] = None
    created_by: Optional[Union[str, URIorCURIE]] = None
    created_on: Optional[Union[str, XSDDateTime]] = None
    status: Optional[Union[str, URIorCURIE]] = None
    deprecated: Optional[Union[bool, Bool]] = None
    compression: Optional[Union[str, "CompressionTypeEnum"]] = None
    was_derived_from: Optional[str] = None
    page: Optional[str] = None
    test_roles: Optional[Union[Union[str, "TestRole"], List[Union[str, "TestRole"]]]] = empty_list()
    parent: Optional[Union[str, InformationName]] = None
    alternate_parents: Optional[Union[Union[str, InformationName], List[Union[str, InformationName]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, InformationName):
            self.name = InformationName(self.name)

        if self.download_url is not None and not isinstance(self.download_url, URI):
            self.download_url = URI(self.download_url)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.conforms_to is not None and not isinstance(self.conforms_to, URIorCURIE):
            self.conforms_to = URIorCURIE(self.conforms_to)

        if self.conforms_to_schema is not None and not isinstance(self.conforms_to_schema, URIorCURIE):
            self.conforms_to_schema = URIorCURIE(self.conforms_to_schema)

        if self.conforms_to_class is not None and not isinstance(self.conforms_to_class, URIorCURIE):
            self.conforms_to_class = URIorCURIE(self.conforms_to_class)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.publisher is not None and not isinstance(self.publisher, URIorCURIE):
            self.publisher = URIorCURIE(self.publisher)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self.issued is not None and not isinstance(self.issued, XSDDateTime):
            self.issued = XSDDateTime(self.issued)

        if self.created_by is not None and not isinstance(self.created_by, URIorCURIE):
            self.created_by = URIorCURIE(self.created_by)

        if self.created_on is not None and not isinstance(self.created_on, XSDDateTime):
            self.created_on = XSDDateTime(self.created_on)

        if self.status is not None and not isinstance(self.status, URIorCURIE):
            self.status = URIorCURIE(self.status)

        if self.deprecated is not None and not isinstance(self.deprecated, Bool):
            self.deprecated = Bool(self.deprecated)

        if self.compression is not None and not isinstance(self.compression, CompressionTypeEnum):
            self.compression = CompressionTypeEnum(self.compression)

        if self.was_derived_from is not None and not isinstance(self.was_derived_from, str):
            self.was_derived_from = str(self.was_derived_from)

        if self.page is not None and not isinstance(self.page, str):
            self.page = str(self.page)

        if not isinstance(self.test_roles, list):
            self.test_roles = [self.test_roles] if self.test_roles is not None else []
        self.test_roles = [v if isinstance(v, TestRole) else TestRole(v) for v in self.test_roles]

        if self.parent is not None and not isinstance(self.parent, InformationName):
            self.parent = InformationName(self.parent)

        if not isinstance(self.alternate_parents, list):
            self.alternate_parents = [self.alternate_parents] if self.alternate_parents is not None else []
        self.alternate_parents = [v if isinstance(v, InformationName) else InformationName(v) for v in self.alternate_parents]

        super().__post_init__(**kwargs)


@dataclass
class DataPackage(Information):
    """
    A collection of data resources
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VOID.Dataset
    class_class_curie: ClassVar[str] = "void:Dataset"
    class_name: ClassVar[str] = "DataPackage"
    class_model_uri: ClassVar[URIRef] = DATASETS.DataPackage

    name: Union[str, DataPackageName] = None
    resources: Optional[Union[Dict[Union[str, DataResourceName], Union[dict, "DataResource"]], List[Union[dict, "DataResource"]]]] = empty_dict()
    rules: Optional[Union[Union[dict, "Rule"], List[Union[dict, "Rule"]]]] = empty_list()
    parent: Optional[Union[str, DataPackageName]] = None
    alternate_parents: Optional[Union[Union[str, DataPackageName], List[Union[str, DataPackageName]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DataPackageName):
            self.name = DataPackageName(self.name)

        self._normalize_inlined_as_list(slot_name="resources", slot_type=DataResource, key_name="name", keyed=True)

        if not isinstance(self.rules, list):
            self.rules = [self.rules] if self.rules is not None else []
        self.rules = [v if isinstance(v, Rule) else Rule(**as_dict(v)) for v in self.rules]

        if self.parent is not None and not isinstance(self.parent, DataPackageName):
            self.parent = DataPackageName(self.parent)

        if not isinstance(self.alternate_parents, list):
            self.alternate_parents = [self.alternate_parents] if self.alternate_parents is not None else []
        self.alternate_parents = [v if isinstance(v, DataPackageName) else DataPackageName(v) for v in self.alternate_parents]

        super().__post_init__(**kwargs)


@dataclass
class DataResource(Information):
    """
    An individual file or table
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Distribution
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "DataResource"
    class_model_uri: ClassVar[URIRef] = DATASETS.DataResource

    name: Union[str, DataResourceName] = None
    path: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None
    media_type: Optional[str] = None
    encoding: Optional[str] = None
    bytes: Optional[int] = None
    hash: Optional[str] = None
    md5: Optional[str] = None
    sha256: Optional[str] = None
    dialect: Optional[str] = None
    parent: Optional[Union[str, DataResourceName]] = None
    alternate_parents: Optional[Union[Union[str, DataResourceName], List[Union[str, DataResourceName]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DataResourceName):
            self.name = DataResourceName(self.name)

        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.media_type is not None and not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        if self.encoding is not None and not isinstance(self.encoding, str):
            self.encoding = str(self.encoding)

        if self.bytes is not None and not isinstance(self.bytes, int):
            self.bytes = int(self.bytes)

        if self.hash is not None and not isinstance(self.hash, str):
            self.hash = str(self.hash)

        if self.md5 is not None and not isinstance(self.md5, str):
            self.md5 = str(self.md5)

        if self.sha256 is not None and not isinstance(self.sha256, str):
            self.sha256 = str(self.sha256)

        if self.dialect is not None and not isinstance(self.dialect, str):
            self.dialect = str(self.dialect)

        if self.parent is not None and not isinstance(self.parent, DataResourceName):
            self.parent = DataResourceName(self.parent)

        if not isinstance(self.alternate_parents, list):
            self.alternate_parents = [self.alternate_parents] if self.alternate_parents is not None else []
        self.alternate_parents = [v if isinstance(v, DataResourceName) else DataResourceName(v) for v in self.alternate_parents]

        super().__post_init__(**kwargs)


@dataclass
class FormatDialect(YAMLRoot):
    """
    Additional format information for a file
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASETS.FormatDialect
    class_class_curie: ClassVar[str] = "datasets:FormatDialect"
    class_name: ClassVar[str] = "FormatDialect"
    class_model_uri: ClassVar[URIRef] = DATASETS.FormatDialect

    comment_prefix: Optional[str] = None
    delimiter: Optional[str] = None
    double_quote: Optional[str] = None
    header: Optional[str] = None
    quote_char: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.comment_prefix is not None and not isinstance(self.comment_prefix, str):
            self.comment_prefix = str(self.comment_prefix)

        if self.delimiter is not None and not isinstance(self.delimiter, str):
            self.delimiter = str(self.delimiter)

        if self.double_quote is not None and not isinstance(self.double_quote, str):
            self.double_quote = str(self.double_quote)

        if self.header is not None and not isinstance(self.header, str):
            self.header = str(self.header)

        if self.quote_char is not None and not isinstance(self.quote_char, str):
            self.quote_char = str(self.quote_char)

        super().__post_init__(**kwargs)


@dataclass
class RulePostcondition(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASETS.RulePostcondition
    class_class_curie: ClassVar[str] = "datasets:RulePostcondition"
    class_name: ClassVar[str] = "RulePostcondition"
    class_model_uri: ClassVar[URIRef] = DATASETS.RulePostcondition

    format: Optional[str] = None
    conforms_to: Optional[Union[str, URIorCURIE]] = None
    compression: Optional[Union[str, "CompressionTypeEnum"]] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.conforms_to is not None and not isinstance(self.conforms_to, URIorCURIE):
            self.conforms_to = URIorCURIE(self.conforms_to)

        if self.compression is not None and not isinstance(self.compression, CompressionTypeEnum):
            self.compression = CompressionTypeEnum(self.compression)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        super().__post_init__(**kwargs)


@dataclass
class RulePrecondition(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASETS.RulePrecondition
    class_class_curie: ClassVar[str] = "datasets:RulePrecondition"
    class_name: ClassVar[str] = "RulePrecondition"
    class_model_uri: ClassVar[URIRef] = DATASETS.RulePrecondition

    basename_regexp: Optional[str] = None
    dirname_regexp: Optional[str] = None
    path_regexp: Optional[str] = None
    final_suffix: Optional[str] = None
    has_suffix: Optional[str] = None
    has_content: Optional[Union[dict, "ContentCheck"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.basename_regexp is not None and not isinstance(self.basename_regexp, str):
            self.basename_regexp = str(self.basename_regexp)

        if self.dirname_regexp is not None and not isinstance(self.dirname_regexp, str):
            self.dirname_regexp = str(self.dirname_regexp)

        if self.path_regexp is not None and not isinstance(self.path_regexp, str):
            self.path_regexp = str(self.path_regexp)

        if self.final_suffix is not None and not isinstance(self.final_suffix, str):
            self.final_suffix = str(self.final_suffix)

        if self.has_suffix is not None and not isinstance(self.has_suffix, str):
            self.has_suffix = str(self.has_suffix)

        if self.has_content is not None and not isinstance(self.has_content, ContentCheck):
            self.has_content = ContentCheck(**as_dict(self.has_content))

        super().__post_init__(**kwargs)


@dataclass
class Rule(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASETS.Rule
    class_class_curie: ClassVar[str] = "datasets:Rule"
    class_name: ClassVar[str] = "Rule"
    class_model_uri: ClassVar[URIRef] = DATASETS.Rule

    preconditions: Optional[Union[Union[dict, RulePrecondition], List[Union[dict, RulePrecondition]]]] = empty_list()
    postconditions: Optional[Union[Union[dict, RulePostcondition], List[Union[dict, RulePostcondition]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.preconditions, list):
            self.preconditions = [self.preconditions] if self.preconditions is not None else []
        self.preconditions = [v if isinstance(v, RulePrecondition) else RulePrecondition(**as_dict(v)) for v in self.preconditions]

        if not isinstance(self.postconditions, list):
            self.postconditions = [self.postconditions] if self.postconditions is not None else []
        self.postconditions = [v if isinstance(v, RulePostcondition) else RulePostcondition(**as_dict(v)) for v in self.postconditions]

        super().__post_init__(**kwargs)


@dataclass
class ContentCheck(YAMLRoot):
    """
    an object describing conditions that apply to the contents of a file
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASETS.ContentCheck
    class_class_curie: ClassVar[str] = "datasets:ContentCheck"
    class_name: ClassVar[str] = "ContentCheck"
    class_model_uri: ClassVar[URIRef] = DATASETS.ContentCheck

    contains_regexp: Optional[str] = None
    minimum_line_number: Optional[int] = None
    maximum_line_number: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contains_regexp is not None and not isinstance(self.contains_regexp, str):
            self.contains_regexp = str(self.contains_regexp)

        if self.minimum_line_number is not None and not isinstance(self.minimum_line_number, int):
            self.minimum_line_number = int(self.minimum_line_number)

        if self.maximum_line_number is not None and not isinstance(self.maximum_line_number, int):
            self.maximum_line_number = int(self.maximum_line_number)

        super().__post_init__(**kwargs)


# Enumerations
class DistributionLevel(EnumDefinitionImpl):

    LatestVersion = PermissibleValue(text="LatestVersion")
    SpecificVersion = PermissibleValue(text="SpecificVersion")

    _defn = EnumDefinition(
        name="DistributionLevel",
    )

class TestRole(EnumDefinitionImpl):
    """
    describes the role an artefact plays for system testing or for informing humans
    """
    Example = PermissibleValue(text="Example",
                                     description="intended as an informative example that shows an agent how to do something, and may be used in automated test suites")
    CounterExample = PermissibleValue(text="CounterExample",
                                                   description="intended as an informative example that shows an agent how NOT to do something, and may be used in automated test suites as negative data")
    PerformanceTest = PermissibleValue(text="PerformanceTest",
                                                     description="intended to be used for benchmarking or carrying out performance tests, for example, time and memory to process a resource")

    _defn = EnumDefinition(
        name="TestRole",
        description="describes the role an artefact plays for system testing or for informing humans",
    )

class MediaTypeEnum(EnumDefinitionImpl):

    csv = PermissibleValue(text="csv",
                             meaning=MEDIATYPES["text/csv"])

    _defn = EnumDefinition(
        name="MediaTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "rdf-xml",
                PermissibleValue(text="rdf-xml",
                                 meaning=MEDIATYPES["application/rdf+xml"]) )

class CompressionTypeEnum(EnumDefinitionImpl):

    GZIP = PermissibleValue(text="GZIP")
    ZIP = PermissibleValue(text="ZIP")
    BGZIP = PermissibleValue(text="BGZIP")

    _defn = EnumDefinition(
        name="CompressionTypeEnum",
    )

class FormatEnum(EnumDefinitionImpl):

    N3 = PermissibleValue(text="N3",
                           meaning=FORMATS.N3)
    Microdata = PermissibleValue(text="Microdata",
                                         meaning=FORMATS.microdata)
    POWDER = PermissibleValue(text="POWDER",
                                   meaning=FORMATS.POWDER)
    RDFa = PermissibleValue(text="RDFa",
                               meaning=FORMATS.RDFa)
    Turtle = PermissibleValue(text="Turtle",
                                   meaning=FORMATS.Turtle)
    TriG = PermissibleValue(text="TriG",
                               meaning=FORMATS.TriG)
    YAML = PermissibleValue(text="YAML")
    JSON = PermissibleValue(text="JSON")
    Markdown = PermissibleValue(text="Markdown")

    _defn = EnumDefinition(
        name="FormatEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "JSON-LD",
                PermissibleValue(text="JSON-LD",
                                 meaning=FORMATS["JSON-LD"]) )
        setattr(cls, "N-Triples",
                PermissibleValue(text="N-Triples",
                                 meaning=FORMATS["N-Triples"]) )
        setattr(cls, "N-Quads",
                PermissibleValue(text="N-Quads",
                                 meaning=FORMATS["N-Quads"]) )
        setattr(cls, "LD Patch",
                PermissibleValue(text="LD Patch",
                                 meaning=FORMATS.LD_Patch) )
        setattr(cls, "OWL XML Serialization",
                PermissibleValue(text="OWL XML Serialization",
                                 meaning=FORMATS.OWL_XML) )
        setattr(cls, "OWL Functional Syntax",
                PermissibleValue(text="OWL Functional Syntax",
                                 meaning=FORMATS.OWL_Functional) )
        setattr(cls, "OWL Manchester Syntax",
                PermissibleValue(text="OWL Manchester Syntax",
                                 meaning=FORMATS.OWL_Manchester) )
        setattr(cls, "POWDER-S",
                PermissibleValue(text="POWDER-S",
                                 meaning=FORMATS["POWDER-S"]) )
        setattr(cls, "PROV-N",
                PermissibleValue(text="PROV-N",
                                 meaning=FORMATS["PROV-N"]) )
        setattr(cls, "PROV-XML",
                PermissibleValue(text="PROV-XML",
                                 meaning=FORMATS["PROV-XML"]) )
        setattr(cls, "RDF/JSON",
                PermissibleValue(text="RDF/JSON",
                                 meaning=FORMATS.RDF_JSON) )
        setattr(cls, "RDF/XML",
                PermissibleValue(text="RDF/XML",
                                 meaning=FORMATS.RDF_XML) )
        setattr(cls, "RIF XML Syntax",
                PermissibleValue(text="RIF XML Syntax",
                                 meaning=FORMATS.RIF_XML) )
        setattr(cls, "SPARQL Results in XML",
                PermissibleValue(text="SPARQL Results in XML",
                                 meaning=FORMATS.SPARQL_Results_XML) )
        setattr(cls, "SPARQL Results in JSON",
                PermissibleValue(text="SPARQL Results in JSON",
                                 meaning=FORMATS.SPARQL_Results_JSON) )
        setattr(cls, "SPARQL Results in CSV",
                PermissibleValue(text="SPARQL Results in CSV",
                                 meaning=FORMATS.SPARQL_Results_CSV) )
        setattr(cls, "SPARQL Results in TSV",
                PermissibleValue(text="SPARQL Results in TSV",
                                 meaning=FORMATS.SPARQL_Results_TSV) )

# Slots
class slots:
    pass

slots.name = Slot(uri=DCTERMS.identifier, name="name", curie=DCTERMS.curie('identifier'),
                   model_uri=DATASETS.name, domain=None, range=URIRef)

slots.identifier = Slot(uri=SCHEMA.identifier, name="identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=DATASETS.identifier, domain=None, range=Optional[Union[str, List[str]]])

slots.sameAs = Slot(uri=SCHEMA.sameAs, name="sameAs", curie=SCHEMA.curie('sameAs'),
                   model_uri=DATASETS.sameAs, domain=None, range=Optional[str])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=DATASETS.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=DATASETS.description, domain=None, range=Optional[str])

slots.language = Slot(uri=SCHEMA.inLanguage, name="language", curie=SCHEMA.curie('inLanguage'),
                   model_uri=DATASETS.language, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DCTERMS.publisher, name="publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=DATASETS.publisher, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.issued = Slot(uri=DCTERMS.issued, name="issued", curie=DCTERMS.curie('issued'),
                   model_uri=DATASETS.issued, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.page = Slot(uri=DCAT.landingPage, name="page", curie=DCAT.curie('landingPage'),
                   model_uri=DATASETS.page, domain=None, range=Optional[str])

slots.dialect = Slot(uri=CSVW.dialect, name="dialect", curie=CSVW.curie('dialect'),
                   model_uri=DATASETS.dialect, domain=None, range=Optional[str])

slots.bytes = Slot(uri=DCAT.byteSize, name="bytes", curie=DCAT.curie('byteSize'),
                   model_uri=DATASETS.bytes, domain=None, range=Optional[int])

slots.path = Slot(uri=DATASETS.path, name="path", curie=DATASETS.curie('path'),
                   model_uri=DATASETS.path, domain=None, range=Optional[str])

slots.isAccessibleForFree = Slot(uri=SCHEMA.isAccessibleForFree, name="isAccessibleForFree", curie=SCHEMA.curie('isAccessibleForFree'),
                   model_uri=DATASETS.isAccessibleForFree, domain=None, range=Optional[Union[bool, Bool]])

slots.download_url = Slot(uri=DCAT.downloadURL, name="download_url", curie=DCAT.curie('downloadURL'),
                   model_uri=DATASETS.download_url, domain=None, range=Optional[Union[str, URI]])

slots.format = Slot(uri=DCTERMS.format, name="format", curie=DCTERMS.curie('format'),
                   model_uri=DATASETS.format, domain=None, range=Optional[str])

slots.compression = Slot(uri=DATASETS.compression, name="compression", curie=DATASETS.curie('compression'),
                   model_uri=DATASETS.compression, domain=None, range=Optional[Union[str, "CompressionTypeEnum"]])

slots.encoding = Slot(uri=DATASETS.encoding, name="encoding", curie=DATASETS.curie('encoding'),
                   model_uri=DATASETS.encoding, domain=None, range=Optional[str])

slots.hash = Slot(uri=DATASETS.hash, name="hash", curie=DATASETS.curie('hash'),
                   model_uri=DATASETS.hash, domain=None, range=Optional[str])

slots.sha256 = Slot(uri=DATASETS.sha256, name="sha256", curie=DATASETS.curie('sha256'),
                   model_uri=DATASETS.sha256, domain=None, range=Optional[str])

slots.md5 = Slot(uri=DATASETS.md5, name="md5", curie=DATASETS.curie('md5'),
                   model_uri=DATASETS.md5, domain=None, range=Optional[str])

slots.media_type = Slot(uri=DCAT.mediaType, name="media_type", curie=DCAT.curie('mediaType'),
                   model_uri=DATASETS.media_type, domain=None, range=Optional[str])

slots.conforms_to = Slot(uri=DCTERMS.conformsTo, name="conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=DATASETS.conforms_to, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.conforms_to_schema = Slot(uri=DATASETS.conforms_to_schema, name="conforms_to_schema", curie=DATASETS.curie('conforms_to_schema'),
                   model_uri=DATASETS.conforms_to_schema, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.conforms_to_class = Slot(uri=DATASETS.conforms_to_class, name="conforms_to_class", curie=DATASETS.curie('conforms_to_class'),
                   model_uri=DATASETS.conforms_to_class, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.profile = Slot(uri=DATASETS.profile, name="profile", curie=DATASETS.curie('profile'),
                   model_uri=DATASETS.profile, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.funder = Slot(uri=SCHEMA.funder, name="funder", curie=SCHEMA.curie('funder'),
                   model_uri=DATASETS.funder, domain=None, range=Optional[str])

slots.includedInDataCatalog = Slot(uri=SCHEMA.includedInDataCatalog, name="includedInDataCatalog", curie=SCHEMA.curie('includedInDataCatalog'),
                   model_uri=DATASETS.includedInDataCatalog, domain=None, range=Optional[str])

slots.temporalCoverage = Slot(uri=SCHEMA.temporalCoverage, name="temporalCoverage", curie=SCHEMA.curie('temporalCoverage'),
                   model_uri=DATASETS.temporalCoverage, domain=None, range=Optional[str])

slots.spatialCoverage = Slot(uri=SCHEMA.spatialCoverage, name="spatialCoverage", curie=SCHEMA.curie('spatialCoverage'),
                   model_uri=DATASETS.spatialCoverage, domain=None, range=Optional[str])

slots.keywords = Slot(uri=DCAT.keyword, name="keywords", curie=DCAT.curie('keyword'),
                   model_uri=DATASETS.keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.themes = Slot(uri=DCAT.theme, name="themes", curie=DCAT.curie('theme'),
                   model_uri=DATASETS.themes, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.parent = Slot(uri=DATASETS.parent, name="parent", curie=DATASETS.curie('parent'),
                   model_uri=DATASETS.parent, domain=None, range=Optional[Union[str, InformationName]])

slots.alternate_parents = Slot(uri=DATASETS.alternate_parents, name="alternate_parents", curie=DATASETS.curie('alternate_parents'),
                   model_uri=DATASETS.alternate_parents, domain=None, range=Optional[Union[Union[str, InformationName], List[Union[str, InformationName]]]])

slots.resources = Slot(uri=DCAT.distribution, name="resources", curie=DCAT.curie('distribution'),
                   model_uri=DATASETS.resources, domain=None, range=Optional[Union[Dict[Union[str, DataResourceName], Union[dict, DataResource]], List[Union[dict, DataResource]]]])

slots.hasPart = Slot(uri=SCHEMA.hasPart, name="hasPart", curie=SCHEMA.curie('hasPart'),
                   model_uri=DATASETS.hasPart, domain=None, range=Optional[Union[str, DataPackageName]])

slots.test_roles = Slot(uri=DATASETS.test_roles, name="test_roles", curie=DATASETS.curie('test_roles'),
                   model_uri=DATASETS.test_roles, domain=None, range=Optional[Union[Union[str, "TestRole"], List[Union[str, "TestRole"]]]])

slots.created_by = Slot(uri=PAV.createdBy, name="created_by", curie=PAV.curie('createdBy'),
                   model_uri=DATASETS.created_by, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.created_on = Slot(uri=PAV.createdOn, name="created_on", curie=PAV.curie('createdOn'),
                   model_uri=DATASETS.created_on, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.last_updated_on = Slot(uri=PAV.lastUpdatedOn, name="last_updated_on", curie=PAV.curie('lastUpdatedOn'),
                   model_uri=DATASETS.last_updated_on, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.modified_by = Slot(uri=OSLC.modifiedBy, name="modified_by", curie=OSLC.curie('modifiedBy'),
                   model_uri=DATASETS.modified_by, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.status = Slot(uri=BIBO.status, name="status", curie=BIBO.curie('status'),
                   model_uri=DATASETS.status, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.deprecated = Slot(uri=OWL.deprecated, name="deprecated", curie=OWL.curie('deprecated'),
                   model_uri=DATASETS.deprecated, domain=None, range=Optional[Union[bool, Bool]])

slots.license = Slot(uri=DCTERMS.license, name="license", curie=DCTERMS.curie('license'),
                   model_uri=DATASETS.license, domain=None, range=Optional[str])

slots.version = Slot(uri=PAV.version, name="version", curie=PAV.curie('version'),
                   model_uri=DATASETS.version, domain=None, range=Optional[str])

slots.was_derived_from = Slot(uri=PROV.wasDerivedFrom, name="was_derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=DATASETS.was_derived_from, domain=None, range=Optional[str])

slots.rules = Slot(uri=DATASETS.rules, name="rules", curie=DATASETS.curie('rules'),
                   model_uri=DATASETS.rules, domain=None, range=Optional[Union[Union[dict, Rule], List[Union[dict, Rule]]]])

slots.formatDialect__comment_prefix = Slot(uri=DATASETS.comment_prefix, name="formatDialect__comment_prefix", curie=DATASETS.curie('comment_prefix'),
                   model_uri=DATASETS.formatDialect__comment_prefix, domain=None, range=Optional[str])

slots.formatDialect__delimiter = Slot(uri=DATASETS.delimiter, name="formatDialect__delimiter", curie=DATASETS.curie('delimiter'),
                   model_uri=DATASETS.formatDialect__delimiter, domain=None, range=Optional[str])

slots.formatDialect__double_quote = Slot(uri=DATASETS.double_quote, name="formatDialect__double_quote", curie=DATASETS.curie('double_quote'),
                   model_uri=DATASETS.formatDialect__double_quote, domain=None, range=Optional[str])

slots.formatDialect__header = Slot(uri=DATASETS.header, name="formatDialect__header", curie=DATASETS.curie('header'),
                   model_uri=DATASETS.formatDialect__header, domain=None, range=Optional[str])

slots.formatDialect__quote_char = Slot(uri=DATASETS.quote_char, name="formatDialect__quote_char", curie=DATASETS.curie('quote_char'),
                   model_uri=DATASETS.formatDialect__quote_char, domain=None, range=Optional[str])

slots.rulePrecondition__basename_regexp = Slot(uri=DATASETS.basename_regexp, name="rulePrecondition__basename_regexp", curie=DATASETS.curie('basename_regexp'),
                   model_uri=DATASETS.rulePrecondition__basename_regexp, domain=None, range=Optional[str])

slots.rulePrecondition__dirname_regexp = Slot(uri=DATASETS.dirname_regexp, name="rulePrecondition__dirname_regexp", curie=DATASETS.curie('dirname_regexp'),
                   model_uri=DATASETS.rulePrecondition__dirname_regexp, domain=None, range=Optional[str])

slots.rulePrecondition__path_regexp = Slot(uri=DATASETS.path_regexp, name="rulePrecondition__path_regexp", curie=DATASETS.curie('path_regexp'),
                   model_uri=DATASETS.rulePrecondition__path_regexp, domain=None, range=Optional[str])

slots.rulePrecondition__final_suffix = Slot(uri=DATASETS.final_suffix, name="rulePrecondition__final_suffix", curie=DATASETS.curie('final_suffix'),
                   model_uri=DATASETS.rulePrecondition__final_suffix, domain=None, range=Optional[str])

slots.rulePrecondition__has_suffix = Slot(uri=DATASETS.has_suffix, name="rulePrecondition__has_suffix", curie=DATASETS.curie('has_suffix'),
                   model_uri=DATASETS.rulePrecondition__has_suffix, domain=None, range=Optional[str])

slots.rulePrecondition__has_content = Slot(uri=DATASETS.has_content, name="rulePrecondition__has_content", curie=DATASETS.curie('has_content'),
                   model_uri=DATASETS.rulePrecondition__has_content, domain=None, range=Optional[Union[dict, ContentCheck]])

slots.rule__preconditions = Slot(uri=DATASETS.preconditions, name="rule__preconditions", curie=DATASETS.curie('preconditions'),
                   model_uri=DATASETS.rule__preconditions, domain=None, range=Optional[Union[Union[dict, RulePrecondition], List[Union[dict, RulePrecondition]]]])

slots.rule__postconditions = Slot(uri=DATASETS.postconditions, name="rule__postconditions", curie=DATASETS.curie('postconditions'),
                   model_uri=DATASETS.rule__postconditions, domain=None, range=Optional[Union[Union[dict, RulePostcondition], List[Union[dict, RulePostcondition]]]])

slots.contentCheck__contains_regexp = Slot(uri=DATASETS.contains_regexp, name="contentCheck__contains_regexp", curie=DATASETS.curie('contains_regexp'),
                   model_uri=DATASETS.contentCheck__contains_regexp, domain=None, range=Optional[str])

slots.contentCheck__minimum_line_number = Slot(uri=DATASETS.minimum_line_number, name="contentCheck__minimum_line_number", curie=DATASETS.curie('minimum_line_number'),
                   model_uri=DATASETS.contentCheck__minimum_line_number, domain=None, range=Optional[int])

slots.contentCheck__maximum_line_number = Slot(uri=DATASETS.maximum_line_number, name="contentCheck__maximum_line_number", curie=DATASETS.curie('maximum_line_number'),
                   model_uri=DATASETS.contentCheck__maximum_line_number, domain=None, range=Optional[int])

slots.DataPackage_parent = Slot(uri=DATASETS.parent, name="DataPackage_parent", curie=DATASETS.curie('parent'),
                   model_uri=DATASETS.DataPackage_parent, domain=DataPackage, range=Optional[Union[str, DataPackageName]])

slots.DataPackage_alternate_parents = Slot(uri=DATASETS.alternate_parents, name="DataPackage_alternate_parents", curie=DATASETS.curie('alternate_parents'),
                   model_uri=DATASETS.DataPackage_alternate_parents, domain=DataPackage, range=Optional[Union[Union[str, DataPackageName], List[Union[str, DataPackageName]]]])

slots.DataResource_parent = Slot(uri=DATASETS.parent, name="DataResource_parent", curie=DATASETS.curie('parent'),
                   model_uri=DATASETS.DataResource_parent, domain=DataResource, range=Optional[Union[str, DataResourceName]])

slots.DataResource_alternate_parents = Slot(uri=DATASETS.alternate_parents, name="DataResource_alternate_parents", curie=DATASETS.curie('alternate_parents'),
                   model_uri=DATASETS.DataResource_alternate_parents, domain=DataResource, range=Optional[Union[Union[str, DataResourceName], List[Union[str, DataResourceName]]]])