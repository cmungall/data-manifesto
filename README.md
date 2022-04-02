# Data Manifesto: Data Manifest Objects

PRE-ALPHA

This repo contains a schema and code for working with semantic representation data manifests.


 - a LinkML schema
     * source: [src/linkml](src/linkml)
     * docs: [cmungall.github.io/data-manifesto](https://cmungall.github.io/data-manifesto/)
 - simple utility code
     * introspect a folder
     * apply customizable rules to infer semantic properties
     * render as linkml data / rdf / json

## Inference from file systems

See tests

given a folder structure like [tests/input/PersonSchema](tests/input/PersonSchema)

```yaml
name: file:test-manifesto
resources:
- name: file:test-manifesto/input/PersonSchema/personinfo.yaml
  created_by: cjm
  created_on: '2022-03-21T16:39:39.508942'
  path: input/PersonSchema/personinfo.yaml
  format: YAML
  bytes: 5368
  sha256: a9e1b95e90a1b2cfaf03902ed4ee92aa73bc8a14fe0f15ebb16357f0da42f8f4
- name: file:test-manifesto/input/PersonSchema/personinfo.json
  created_by: cjm
  created_on: '2022-03-21T16:39:39.510421'
  path: input/PersonSchema/personinfo.json
  format: JSON
  bytes: 8025
  sha256: aee37e2c6634a2f2ffc417dd1bb07135c4c3352d5552110a0d9ac0e4e490d3be
- name: file:test-manifesto/input/PersonSchema/Makefile
  created_by: cjm
  created_on: '2022-03-21T16:39:39.511144'
  path: input/PersonSchema/Makefile
  bytes: 1020
  sha256: a17642804c880da49088e16645ed35d1d92bd473ab16ca7b0db69d489b3eb90d
```

or the equivalent:

```turtle
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://purl.org/pav/> .
@prefix ns2: <https://w3id.org/linkml/manifesto/> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///test-manifesto> a void:Dataset ;
    dcat:distribution <file:///test-manifesto/input/PersonSchema/Makefile>,
        <file:///test-manifesto/input/PersonSchema/README.md>,
        <file:///test-manifesto/input/PersonSchema/build/example_personinfo_data.json>,
        <file:///test-manifesto/input/PersonSchema/build/example_personinfo_data.tsv>,
        <file:///test-manifesto/input/PersonSchema/build/example_personinfo_data.tsv.old>,
        <file:///test-manifesto/input/PersonSchema/build/example_personinfo_data.ttl>,
        <file:///test-manifesto/input/PersonSchema/codesets/vital_status_codeset.yaml>,
        <file:///test-manifesto/input/PersonSchema/data/example_personinfo_data.yaml>,
        <file:///test-manifesto/input/PersonSchema/data/z.yaml>,
        <file:///test-manifesto/input/PersonSchema/personinfo.json>,
        <file:///test-manifesto/input/PersonSchema/personinfo.png>,
        <file:///test-manifesto/input/PersonSchema/personinfo.yaml>,
        <file:///test-manifesto/input/PersonSchema/personinfo/Pipfile>,
        <file:///test-manifesto/input/PersonSchema/personinfo/excel/personinfo.xlsx>,
        <file:///test-manifesto/input/PersonSchema/personinfo/graphql/personinfo.graphql>,
        <file:///test-manifesto/input/PersonSchema/personinfo/java/personinfo.sql>,
        <file:///test-manifesto/input/PersonSchema/personinfo/jsonld/personinfo.context.jsonld>,
        <file:///test-manifesto/input/PersonSchema/personinfo/jsonld/personinfo.jsonld>,
        <file:///test-manifesto/input/PersonSchema/personinfo/jsonschema/personinfo.schema.json>,
        <file:///test-manifesto/input/PersonSchema/personinfo/owl/README.md>,
        <file:///test-manifesto/input/PersonSchema/personinfo/owl/personinfo.owl.ttl.gz>,
        <file:///test-manifesto/input/PersonSchema/personinfo/personinfo.py>,
        <file:///test-manifesto/input/PersonSchema/personinfo/personinfo_sqla.py>,
        <file:///test-manifesto/input/PersonSchema/personinfo/prefixmap/personinfo.json>,
        <file:///test-manifesto/input/PersonSchema/personinfo/prefixmap/personinfo.tsv>,
        <file:///test-manifesto/input/PersonSchema/personinfo/prefixmap/personinfo.yaml>,
        <file:///test-manifesto/input/PersonSchema/personinfo/protobuf/personinfo.proto>,
        <file:///test-manifesto/input/PersonSchema/personinfo/shacl/personinfo.shacl.ttl>,
        <file:///test-manifesto/input/PersonSchema/personinfo/shex/personinfo.shex>,
        <file:///test-manifesto/input/PersonSchema/personinfo/shex/personinfo.shexj>,
        <file:///test-manifesto/input/PersonSchema/personinfo/sqlschema/personinfo.sql>,
        <file:///test-manifesto/input/PersonSchema/personinfo_pydantic.py> .

<file:///test-manifesto/input/PersonSchema/Makefile> a dcat:Distribution ;
    ns1:createdBy "cjm"^^xsd:anyURI ;
    ns1:createdOn "2022-03-21T16:39:39.511144"^^xsd:dateTime ;
    dcat:byteSize 1020 ;
    ns2:path "input/PersonSchema/Makefile" ;
    ns2:sha256 "a17642804c880da49088e16645ed35d1d92bd473ab16ca7b0db69d489b3eb90d" .

<file:///test-manifesto/input/PersonSchema/README.md> a dcat:Distribution ;
    ns1:createdBy "cjm"^^xsd:anyURI ;
    ns1:createdOn "2022-03-21T16:39:39.513991"^^xsd:dateTime ;
    dcat:byteSize 619 ;
    ns2:path "input/PersonSchema/README.md" ;
    ns2:sha256 "56e144d94c660ff5e32aea964e1b13232bce95c5f9ef1e8053e8335ffcef23fb" .

<file:///test-manifesto/input/PersonSchema/build/example_personinfo_data.json> a dcat:Distribution ;
    dcterms:format "JSON" ;
    ns1:createdBy "cjm"^^xsd:anyURI ;
    ns1:createdOn "2022-03-21T16:39:39.562493"^^xsd:dateTime ;
    dcat:byteSize 1088 ;
    ns2:path "input/PersonSchema/build/example_personinfo_data.json" ;
    ns2:sha256 "d944d8ae8f653160164d5eadaeb6b324264a2e58ab023266eca6c0dc24744e20" .

<file:///test-manifesto/input/PersonSchema/build/example_personinfo_data.tsv> a dcat:Distribution ;
    ns1:createdBy "cjm"^^xsd:anyURI ;
    ns1:createdOn "2022-03-21T16:39:39.563553"^^xsd:dateTime ;
    dcat:byteSize 809 ;
    ns2:path "input/PersonSchema/build/example_personinfo_data.tsv" ;
    ns2:sha256 "fcd9fcfdcf69a8151759a69966b93533eca4921ac2f2f505d8a141c3ed0316fd" .
```
