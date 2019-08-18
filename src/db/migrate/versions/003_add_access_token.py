# -*- encoding:utf-8 -*-
import sqlalchemy
from sqlalchemy import *
from migrate import *
from migrate.changeset.constraint import ForeignKeyConstraint
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
  'access_token' , meta ,
  Column('user_id', String(255), ForeignKey('user.user_id' , onupdate='CASCADE' , ondelete='CASCADE') , nullable = False),
  Column('access_token', String(255),unique = True , nullable = False),
  Column('timestamp' , DATETIME , nullable=False , server_default=sqlalchemy.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ')),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = sqlalchemy.Table('user', meta, autoload=True)
    table.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    _t = sqlalchemy.Table('user', meta, autoload=True)
    table.drop()

