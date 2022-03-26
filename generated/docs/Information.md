
# Class: Information


Grouping for datasets and data files

URI: [datasets:Information](https://w3id.org/linkml/manifesto/Information)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Information&#124;name:string;download_url:uri%20%3F;license:string%20%3F;title:string%20%3F;description:string%20%3F;conforms_to:uriorcurie%20%3F;conforms_to_schema:uriorcurie%20%3F;conforms_to_class:uriorcurie%20%3F;version:string%20%3F;language:string%20%3F;publisher:uriorcurie%20%3F;keywords:string%20*;issued:datetime%20%3F;created_by:uriorcurie%20%3F;created_on:datetime%20%3F;compression:CompressionTypeEnum%20%3F;was_derived_from:string%20%3F;page:string%20%3F;test_roles:TestRole%20*]^-[DataResource],[Information]^-[DataPackage],[DataResource],[DataPackage])](https://yuml.me/diagram/nofunky;dir:TB/class/[Information&#124;name:string;download_url:uri%20%3F;license:string%20%3F;title:string%20%3F;description:string%20%3F;conforms_to:uriorcurie%20%3F;conforms_to_schema:uriorcurie%20%3F;conforms_to_class:uriorcurie%20%3F;version:string%20%3F;language:string%20%3F;publisher:uriorcurie%20%3F;keywords:string%20*;issued:datetime%20%3F;created_by:uriorcurie%20%3F;created_on:datetime%20%3F;compression:CompressionTypeEnum%20%3F;was_derived_from:string%20%3F;page:string%20%3F;test_roles:TestRole%20*]^-[DataResource],[Information]^-[DataPackage],[DataResource],[DataPackage])

## Children

 * [DataPackage](DataPackage.md) - A collection of data resources
 * [DataResource](DataResource.md) - An individual file or table

## Referenced by Class


## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Description: the unique name of the dataset
     * Range: [String](types/String.md)
 * [download_url](download_url.md)  <sub>0..1</sub>
     * Range: [Uri](types/Uri.md)
 * [license](license.md)  <sub>0..1</sub>
     * Description: license for the data
     * Range: [String](types/String.md)
 * [title](title.md)  <sub>0..1</sub>
     * Description: the official title of the element
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: human readable description of the information
     * Range: [String](types/String.md)
 * [conforms_to](conforms_to.md)  <sub>0..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [conforms_to_schema](conforms_to_schema.md)  <sub>0..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [conforms_to_class](conforms_to_class.md)  <sub>0..1</sub>
     * Description: class in schema which the data object instantiates
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [version](version.md)  <sub>0..1</sub>
     * Description: particular version of schema
     * Range: [String](types/String.md)
 * [language](language.md)  <sub>0..1</sub>
     * Description: language in which the information is expressed
     * Range: [String](types/String.md)
 * [publisher](publisher.md)  <sub>0..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [keywords](keywords.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [issued](issued.md)  <sub>0..1</sub>
     * Range: [Datetime](types/Datetime.md)
 * [created_by](created_by.md)  <sub>0..1</sub>
     * Description: agent that created the element
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [created_on](created_on.md)  <sub>0..1</sub>
     * Description: time at which the element was created
     * Range: [Datetime](types/Datetime.md)
 * [compression](compression.md)  <sub>0..1</sub>
     * Range: [CompressionTypeEnum](CompressionTypeEnum.md)
 * [was_derived_from](was_derived_from.md)  <sub>0..1</sub>
     * Description: A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en
     * Range: [String](types/String.md)
 * [page](page.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [test_roles](test_roles.md)  <sub>0..\*</sub>
     * Range: [TestRole](TestRole.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Close Mappings:** | | schema:CreativeWork |
|  | | bald:Resource |

