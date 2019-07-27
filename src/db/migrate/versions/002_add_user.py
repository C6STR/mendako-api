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
    'user', meta,
    Column('user_id', String(255), primary_key=True),
    Column('mail_address', String(255), unique = True , nullable = False),
    Column('user_name', String(255), nullable = False),
    Column('password', String(255), nullable = False),
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
