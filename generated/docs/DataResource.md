
# Class: DataResource


An individual file or table

URI: [datasets:DataResource](https://w3id.org/linkml/manifesto/DataResource)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Information],[DataPackage]++-%20resources%200..*>[DataResource&#124;path:string%20%3F;format:string%20%3F;media_type:string%20%3F;encoding:string%20%3F;bytes:integer%20%3F;hash:string%20%3F;md5:string%20%3F;sha256:string%20%3F;dialect:string%20%3F;name(i):string;download_url(i):uri%20%3F;license(i):string%20%3F;title(i):string%20%3F;description(i):string%20%3F;conforms_to(i):uriorcurie%20%3F;conforms_to_schema(i):uriorcurie%20%3F;conforms_to_class(i):uriorcurie%20%3F;version(i):string%20%3F;language(i):string%20%3F;publisher(i):uriorcurie%20%3F;keywords(i):string%20*;issued(i):datetime%20%3F;created_by(i):uriorcurie%20%3F;created_on(i):datetime%20%3F;compression(i):CompressionTypeEnum%20%3F;was_derived_from(i):string%20%3F;page(i):string%20%3F;test_roles(i):TestRole%20*],[Information]^-[DataResource],[DataPackage])](https://yuml.me/diagram/nofunky;dir:TB/class/[Information],[DataPackage]++-%20resources%200..*>[DataResource&#124;path:string%20%3F;format:string%20%3F;media_type:string%20%3F;encoding:string%20%3F;bytes:integer%20%3F;hash:string%20%3F;md5:string%20%3F;sha256:string%20%3F;dialect:string%20%3F;name(i):string;download_url(i):uri%20%3F;license(i):string%20%3F;title(i):string%20%3F;description(i):string%20%3F;conforms_to(i):uriorcurie%20%3F;conforms_to_schema(i):uriorcurie%20%3F;conforms_to_class(i):uriorcurie%20%3F;version(i):string%20%3F;language(i):string%20%3F;publisher(i):uriorcurie%20%3F;keywords(i):string%20*;issued(i):datetime%20%3F;created_by(i):uriorcurie%20%3F;created_on(i):datetime%20%3F;compression(i):CompressionTypeEnum%20%3F;was_derived_from(i):string%20%3F;page(i):string%20%3F;test_roles(i):TestRole%20*],[Information]^-[DataResource],[DataPackage])

## Parents

 *  is_a: [Information](Information.md) - Grouping for datasets and data files

## Referenced by Class

 *  **None** *[resources](resources.md)*  <sub>0..\*</sub>  **[DataResource](DataResource.md)**

## Attributes


### Own

 * [path](path.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [title](title.md)  <sub>0..1</sub>
     * Description: the official title of the element
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: human readable description of the information
     * Range: [String](types/String.md)
 * [format](format.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [media_type](media_type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: text/csv None
     * Example: application/json None
 * [encoding](encoding.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [bytes](bytes.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [hash](hash.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [md5](md5.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [sha256](sha256.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [dialect](dialect.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

### Inherited from Information:

 * [name](name.md)  <sub>1..1</sub>
     * Description: the unique name of the dataset
     * Range: [String](types/String.md)
 * [download_url](download_url.md)  <sub>0..1</sub>
     * Range: [Uri](types/Uri.md)
 * [license](license.md)  <sub>0..1</sub>
     * Description: license for the data
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
| **Mappings:** | | dcat:Distribution |
| **See also:** | | [https://specs.frictionlessdata.io/data-resource](https://specs.frictionlessdata.io/data-resource) |
| **Exact Mappings:** | | schema:DataDownload |

