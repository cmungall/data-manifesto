import pkgutil
import unittest
import os
from pathlib import Path

import yaml
import json

from data_manifesto.datamodel.data_manifesto import *
from data_manifesto.manifest_maker import ManifestMaker
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper, rdflib_dumper
from linkml_runtime.utils.introspection import package_schemaview
from rdflib import Graph

from tests import OUTPUT_DIR, ROOT, SCHEMA_DIR


class TestManifesto(unittest.TestCase):
    """tests datamodel """

    def test_manifesto(self):
        sv = SchemaView(str(SCHEMA_DIR / 'data_manifesto.yaml'))
        mm = ManifestMaker()
        pkg = mm.create_package_from_directory('input/PersonSchema', name='file:test-manifesto')
        assert any(r.format == 'YAML' for r in pkg.resources)
        assert any(r.format == 'JSON' for r in pkg.resources)
        #assert any(r.compression == 'GZIP' for r in pkg.resources)
        ys = yaml_dumper.dumps(pkg)
        print(ys)
        rdfstr = rdflib_dumper.dumps(pkg, schemaview=sv)
        print(rdfstr)
