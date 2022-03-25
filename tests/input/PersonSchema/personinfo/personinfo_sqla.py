
from dataclasses import dataclass
from dataclasses import field
from typing import List

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_registry = registry()
metadata = MetaData()

from personinfo import *


tbl_Address = Table('Address', metadata, 
    Column('street', Text, primary_key=True),
    Column('city', Text, primary_key=True),
    Column('postal_code', Text, primary_key=True),
)
tbl_Concept = Table('Concept', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('description', Text),
    Column('image', Text),
)
tbl_Container = Table('Container', metadata, 
    Column('persons', Text, primary_key=True),
    Column('organizations', Text, primary_key=True),
)
tbl_DiagnosisConcept = Table('DiagnosisConcept', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('description', Text),
    Column('image', Text),
)
tbl_EmploymentEvent = Table('EmploymentEvent', metadata, 
    Column('started_at_time', Text, primary_key=True),
    Column('ended_at_time', Text, primary_key=True),
    Column('duration', Text, primary_key=True),
    Column('is_current', Text, primary_key=True),
    Column('employed_at', Text, ForeignKey('Organization.id'), primary_key=True),
    Column('Person_id', Text, ForeignKey('Person.id'), primary_key=True),
)
tbl_Event = Table('Event', metadata, 
    Column('started_at_time', Text, primary_key=True),
    Column('ended_at_time', Text, primary_key=True),
    Column('duration', Text, primary_key=True),
    Column('is_current', Text, primary_key=True),
)
tbl_FamilialRelationship = Table('FamilialRelationship', metadata, 
    Column('started_at_time', Text, primary_key=True),
    Column('ended_at_time', Text, primary_key=True),
    Column('related_to', Text, ForeignKey('Person.id'), primary_key=True),
    Column('type', Text, primary_key=True),
    Column('Person_id', Text, ForeignKey('Person.id'), primary_key=True),
)
tbl_MedicalEvent = Table('MedicalEvent', metadata, 
    Column('started_at_time', Text, primary_key=True),
    Column('ended_at_time', Text, primary_key=True),
    Column('duration', Text, primary_key=True),
    Column('is_current', Text, primary_key=True),
    Column('in_location', Text, ForeignKey('Place.id'), primary_key=True),
    Column('diagnosis', Text, ForeignKey('DiagnosisConcept.id'), primary_key=True),
    Column('procedure', Text, ForeignKey('ProcedureConcept.id'), primary_key=True),
    Column('Person_id', Text, ForeignKey('Person.id'), primary_key=True),
)
tbl_NamedThing = Table('NamedThing', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('description', Text),
    Column('image', Text),
)
tbl_Organization = Table('Organization', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('description', Text),
    Column('image', Text),
    Column('mission_statement', Text),
    Column('founding_date', Text),
    Column('founding_location', Text, ForeignKey('Place.id')),
)
tbl_Person = Table('Person', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('description', Text),
    Column('image', Text),
    Column('primary_email', Text),
    Column('birth_date', Text),
    Column('age_in_years', Text),
    Column('gender', Text),
    Column('current_address', Text),
)
tbl_Place = Table('Place', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
)
tbl_ProcedureConcept = Table('ProcedureConcept', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('description', Text),
    Column('image', Text),
)
tbl_Relationship = Table('Relationship', metadata, 
    Column('started_at_time', Text, primary_key=True),
    Column('ended_at_time', Text, primary_key=True),
    Column('related_to', Text, primary_key=True),
    Column('type', Text, primary_key=True),
)
tbl_Organization_aliases = Table('Organization_aliases', metadata, 
    Column('backref_id', Text, ForeignKey('Organization.id'), primary_key=True),
    Column('aliases', Text, primary_key=True),
)
tbl_Person_aliases = Table('Person_aliases', metadata, 
    Column('backref_id', Text, ForeignKey('Person.id'), primary_key=True),
    Column('aliases', Text, primary_key=True),
)
tbl_Place_aliases = Table('Place_aliases', metadata, 
    Column('backref_id', Text, ForeignKey('Place.id'), primary_key=True),
    Column('aliases', Text, primary_key=True),
)
mapper_registry.map_imperatively(Address, tbl_Address, properties={
})
mapper_registry.map_imperatively(Concept, tbl_Concept, properties={
})
mapper_registry.map_imperatively(Container, tbl_Container, properties={
})
mapper_registry.map_imperatively(DiagnosisConcept, tbl_DiagnosisConcept, properties={
})
mapper_registry.map_imperatively(EmploymentEvent, tbl_EmploymentEvent, properties={
})
mapper_registry.map_imperatively(Event, tbl_Event, properties={
})
mapper_registry.map_imperatively(FamilialRelationship, tbl_FamilialRelationship, properties={
})
mapper_registry.map_imperatively(MedicalEvent, tbl_MedicalEvent, properties={
})
mapper_registry.map_imperatively(NamedThing, tbl_NamedThing, properties={
})
mapper_registry.map_imperatively(Organization, tbl_Organization, properties={
})
mapper_registry.map_imperatively(Person, tbl_Person, properties={

    'has_employment_history': 
        relationship(EmploymentEvent, 
                      foreign_keys=tbl_EmploymentEvent.columns["Person_id"],
                      backref='Person'),


    'has_familial_relationships': 
        relationship(FamilialRelationship, 
                      foreign_keys=tbl_FamilialRelationship.columns["Person_id"],
                      backref='Person'),


    'has_medical_history': 
        relationship(MedicalEvent, 
                      foreign_keys=tbl_MedicalEvent.columns["Person_id"],
                      backref='Person'),

})
mapper_registry.map_imperatively(Place, tbl_Place, properties={
})
mapper_registry.map_imperatively(ProcedureConcept, tbl_ProcedureConcept, properties={
})
mapper_registry.map_imperatively(Relationship, tbl_Relationship, properties={
})
