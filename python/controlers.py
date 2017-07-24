from sqlalchemy.orm import sessionmaker
from datacontrol import User, School, Notification, Content
from prettytable import PrettyTable
import dbmodel
from sqlalchemy import inspect
import hashlib
import paramiko
import os



class ostools(object):
    def __init__(self):
        self.os = ""
        self.user = ""
        self.ip = ""

    def sshconnection(self, ip, port, username, password):
        ssh = paramiko.SSHClient()
        ssh.connect(ip, port, username, password)
        return ssh

    def dbconnection(self):
        enfine = create_engine('postgresql://postgres:postgres@localhost/postgres')
        Session = scoped_session(sessionmaker())
        Session.configure(bind=engine)
        session = Session
        return session

class user_handler(object):
    """Funcoes auxiliares para manejamento da tabela USER"""
    def __init__(self):
        self.user = ""
        self.logged = False

    def criauser(self,session,newemail,newpass,newname,newschool,newbirth):
        newuser = datacontrol.User(name=newname, email=newemail, \
                                   password=newpassword, school=newschool, \
                                   dnascimento=newbirth, usertype=0)
        session.add(newuser)
        session.commit()
        session.flush()
        self.user = newuser.email
        return newuser

    def getuser(self, session, searchemail):
        founduser = session.query(User).filter_by(email=searchemail).first()
        if not founduser:
            return False
        if founduser.email == searchemail:
            return founduser
        else:
            return False

    def updatetype(self, session, useremail):
        founduser = session.query(User).filter_by(email=useremail).first()
        if not founduser:
            return False
        if founduser.usertype == 0:
            founduser.usertype = 1
        if founduser.usertype == 1:
            founduser.usertype = 0
        session.commit()
        session.flush()
        return userfound

    def updatepass(self, session, usernewpass, useremail):
        founduser = session.query(User).filter_by(email=useremail).first()
        if not founduser:
            return False
        founduser.password = usernewpass
        session.commit()
        session.flush()
        return founduser

    def delete(self, session, useremail):
        founduser = session.query(User).filter_by(email=useremail).delete()
        session.commit()
        session.flush()

class school_handler(object):
    """Classe para manipulação na tabela schools"""

    def __init__(self):
        self.schoolid = ""
        self.schooname = ""

    def delete(self, schoolid):
        foundschool = session.query(School).filter_by(id=schoolid).delete()
        session.commit()
        session.flush()


