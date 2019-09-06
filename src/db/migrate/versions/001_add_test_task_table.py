# -*- encoding:utf-8 -*-
import sqlalchemy
from sqlalchemy import *
from migrate import *
import enum
from sqlalchemy import (Column, String, Text, ForeignKey, \
                create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index)
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import (sessionmaker, relationship, scoped_session)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER as Integer , BOOLEAN as Boolean
from datetime import datetime

meta = MetaData()

table = Table(
    'task', meta,
    Column('task_id', Integer, primary_key=True , autoincrement = True),
    Column('user_id' , String(255)),
    Column('task_name', String(255), nullable=False),
    Column('type',Integer, nullable=False),
    Column('priority',Integer , nullable=False),
    Column('status',Integer , nullable=False , server_default = "0"),
    Column('archived' , Boolean),
    Column('start_daytime' , DATETIME , nullable=False),
    Column('end_daytime' , DATETIME , nullable=False),
    Column('created_daytime' , DATETIME , nullable=True , server_default=sqlalchemy.text('CURRENT_TIMESTAMP')),
    Column('updated_daytime' , DATETIME , nullable=True , server_default=sqlalchemy.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ')),
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
