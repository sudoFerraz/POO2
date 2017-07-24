import os
import sqlalchemy
import sys
import paramiko
import hashlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from prettytable import PrettyTable
from sqlalchemy import inspect

def dbconnection(self):
    engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
    Session = scoped_session(sessionmaker())
    Session.configure(bind=engine)
    session = Session
    return session

