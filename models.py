#!/usr/bin/env python
# Copyright (c) 2018 Usharerose. All rights reserved.
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


DB_URI = "mysql://appannie:appannie@localhost:3306/blog"
Base = declarative_base()
engine = create_engine(DB_URI)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    users = relationship('User', backref='role')

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)


'''
class User(Base):
    __tablename__ = 'live_user'

    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    speaker_id = Column(String(40), index=True, unique=True)
    name = Column(String(40), index=True, nullable=False)
    gender = Column(SmallInteger, default=2)
    headline = Column(String(200))
    avatar_url = Column(String(100), nullable=False)
    bio = Column(String(200))
    description = Column(String(256))

    @classmethod
    def add(cls, **kwargs):
        speaker_id = kwargs.get('speaker_id', None)
        if speaker_id is not None:
            r = session.query(cls).filter_by(speaker_id=speaker_id).first()
            if r:
                return r
        try:
            r = cls(**kwargs)
            session.add(r)
            session.commit()
        except:
            session.rollback()
            raise
        else:
            return r
'''


Base.metadata.create_all(engine)
