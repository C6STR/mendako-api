# -*- encoding:utf-8 -*-
from sqlalchemy import *
from migrate import *
import enum
from sqlalchemy import (Column, String, Text, ForeignKey, \
                create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index)
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import (sessionmaker, relationship, scoped_session)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER as Integer
from datetime import datetime

meta = MetaData()

table = Table(
    'test-task', meta,
    Column('task-id', Integer, primary_key=True),
    Column('task-name', String(255), nullable=False),
    Column('types',Integer, nullable=False),
    Column('priority',Integer , nullable=False),
    Column('status',Integer , nullable=False),
    Column('start-daytime' , DATETIME , nullable=False),
    Column('end-daytime' , DATETIME , nullable=False),
)
    

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    table.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    table.drop()
