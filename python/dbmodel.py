import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from sqlalchemy import LargeBinary
from sqlalchemy import ForeignKey
from sqlalchemy.types import LargeBinary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from jinja2 import Markup
import os
from flask.ext.admin import Admin
from flask_admin.contrib.sqla import ModelView

basedir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(basedir, 'static')
Base = declarative_base()

class Notification(Base):
    __tablename__ = "Notifications"
    id = Column(Integer, primary_key=True)
    evento = Column(String)
    source = Column(String)
    tempo = Column(DateTime, server_default=func.now())

class Image(Base):
    __tablename__= "image"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    path = Column(String, unique=True)

    def __repr__(self):
        return self.name

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    usertype = Column(Boolean)
    school = Column(String)
    dnascimento = Column(String)


    def __repr__(self):
                 return ("<User(name='%s', usertype='%s' )>" %self.name, \
                 self.password, self.usertype)

class School(Base):
    __tablename__ = "Schools"
    id = Column(Integer, primary_key = True)
    name = Column(String)

class Course(Base):
    __tablename__ = "Courses"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    schoolid = (Integer, ForeignKey('School.id'))

class Discipline(Base):
    __tablename__ = "Disciplines"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    courseid = Column(Integer, ForeignKey('Courses.id'))

class Content(Base):
    __tablename__ = "Contents"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    disciplineid = Column(Integer, ForeignKey('Disciplines.id'))

class Archive(Base):
    __tablename__ = "Archives"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    contentid = Column(Integer, ForeignKey('Contents.id'))
    extension = Column(String)
    archive = Column(LargeBinary)

class Text(Base):
    __tablename__ = "Texts"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    contentid = Column(Integer, ForeignKey('Contents.id'))
    text = Column(String)

engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


