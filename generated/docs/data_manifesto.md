
# datasets


**metamodel version:** 1.7.0

**version:** None


A datamodel for datasets


### Classes

 * [FormatDialect](FormatDialect.md) - Additional format information for a file
 * [Information](Information.md) - Grouping for datasets and data files
     * [DataPackage](DataPackage.md) - A collection of data resources
     * [DataResource](DataResource.md) - An individual file or table
 * [Rule](Rule.md)
 * [RulePostcondition](RulePostcondition.md)
 * [RulePrecondition](RulePrecondition.md)

### Mixins


### Slots

 * [bytes](bytes.md)
 * [compression](compression.md)
 * [conforms_to](conforms_to.md)
     * [conforms_to_class](conforms_to_class.md) - class in schema which the data object instantiates
     * [conforms_to_schema](conforms_to_schema.md)
 * [created_by](created_by.md) - agent that created the element
 * [created_on](created_on.md) - time at which the element was created
 * [description](description.md) - human readable description of the information
 * [dialect](dialect.md)
 * [download_url](download_url.md)
 * [encoding](encoding.md)
 * [format](format.md)
 * [➞comment_prefix](formatDialect__comment_prefix.md)
 * [➞delimiter](formatDialect__delimiter.md)
 * [➞double_quote](formatDialect__double_quote.md)
 * [➞header](formatDialect__header.md)
 * [➞quote_char](formatDialect__quote_char.md)
 * [hash](hash.md)
     * [md5](md5.md)
     * [sha256](sha256.md)
 * [issued](issued.md)
 * [keywords](keywords.md)
 * [language](language.md) - language in which the information is expressed
 * [last_updated_on](last_updated_on.md) - time at which the element was last updated
 * [license](license.md) - license for the data
 * [media_type](media_type.md)
 * [modified_by](modified_by.md) - agent that modified the element
 * [name](name.md) - the unique name of the dataset
 * [page](page.md)
 * [path](path.md)
 * [profile](profile.md)
 * [publisher](publisher.md)
 * [resources](resources.md)
 * [➞basename_regexp](rulePrecondition__basename_regexp.md)
 * [➞dirname_regexp](rulePrecondition__dirname_regexp.md)
 * [➞final_suffix](rulePrecondition__final_suffix.md)
 * [➞has_suffix](rulePrecondition__has_suffix.md)
 * [➞path_regexp](rulePrecondition__path_regexp.md)
 * [➞postconditions](rule__postconditions.md)
 * [➞preconditions](rule__preconditions.md)
 * [rules](rules.md)
 * [status](status.md) - status of the element
 * [test_roles](test_roles.md)
 * [themes](themes.md)
 * [title](title.md) - the official title of the element
 * [version](version.md) - particular version of schema
 * [was_derived_from](was_derived_from.md) - A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en

### Enums

 * [CompressionTypeEnum](CompressionTypeEnum.md)
 * [DistributionLevel](DistributionLevel.md)
 * [FormatEnum](FormatEnum.md)
 * [MediaTypeEnum](MediaTypeEnum.md)
 * [TestRole](TestRole.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
