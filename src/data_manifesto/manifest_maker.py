from datetime import datetime
import hashlib
from pathlib import Path, PurePath
from pwd import getpwuid
from typing import Union, List

from data_manifesto.datamodel.data_manifesto import DataPackage, DataResource, Rule, RulePrecondition, \
    RulePostcondition, FormatEnum
from linkml_runtime.dumpers import yaml_dumper


def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()


class ManifestMaker:
    rules: List[Rule] = None

    def create_package_from_directory(self, path: Union[str, Path], name: str = None) -> DataPackage:
        if isinstance(path, str):
            path = PurePath(path)
        if name is None:
            name = self._name_from_path(path)
        resources = []
        for x in Path(path).glob('**/*'):
            if x.is_file():
                resources.append(self.create_resource_from_file(x, parent=name))
        package = DataPackage(name=name,
                              resources=resources)
        return package


    def create_resource_from_file(self, path: Union[str, Path], parent: str = None) -> DataResource:
        if isinstance(path, str):
            path = PurePath(path)
        if parent is None:
            name = self._name_from_path(path)
        else:
            name = f'{parent}/{str(path)}'
        st = path.stat()
        resource = DataResource(name=name,
                                path=str(path),
                                bytes=st.st_size,
                                created_by=getpwuid(st.st_uid).pw_name,
                                created_on=datetime.fromtimestamp(st.st_ctime),
                                sha256=sha256sum(str(path))
                                )
        for rule in self._rules():
            if all(self.matches_precondition(pre, resource) for pre in rule.preconditions):
                for post in rule.postconditions:
                    self.apply_postcondition(post, resource)
        return resource

    def _name_from_path(self, path: Path):
        return f'file:{str(path)}'

    def _rules(self):
        return self._get_default_rules()

    def _get_default_rules(self) -> List[Rule]:
        rules = []
        for suffix, fmt in [('json', 'JSON'), ('yaml', 'YAML')]:
            rules.append(Rule(preconditions=[RulePrecondition(has_suffix=suffix)],
                              postconditions=[RulePostcondition(format=fmt)]))
        #for suffix, cmp in [('gz', 'GZIP'), ('zip', 'ZIP')]:
        #    rules.append(Rule(preconditions=[RulePrecondition(final_suffix=suffix)],
        #                      postconditions=[RulePostcondition(compression=cmp)]))
        return rules

    def matches_precondition(self, pre: RulePrecondition, resource: DataResource) -> bool:
        toks = [t.lower() for t in resource.path.split('.')]
        if pre.final_suffix:
            if toks[-1] != pre.final_suffix:
                return False
        if pre.has_suffix:
            if not any(t == pre.has_suffix for t in toks):
                return False
        return True

    def apply_postcondition(self, post: RulePostcondition, resource: DataResource) -> bool:
        for k, v in vars(post).items():
            #print(f'SETTING {k} = {v} // {type(v)}')
            setattr(resource, k, v)
            #print(f'  SET { yaml_dumper.dumps(resource)}')

