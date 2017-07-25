from sqlalchemy.orm import sessionmaker
from dbmodel import User, School, Notification, Content
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
    """Classe para manipulacao na tabela schools"""

    def __init__(self):
        self.schoolid = ""
        self.schooname = ""

    def delete(self, schoolid, session):
        foundschool = session.query(School).filter_by(id=schoolid).delete()
        session.commit()
        session.flush()

    def get_school_id(self, schoolname, session):
        foundschool = session.query(School).filter_by(name=schoolname).first()
        if not foundschool:
            return False
        return foundschool.id

    def get_all_schools(self, session):
        foundschools = session.query(School).order_by(School.id)
        return foundschools

    def cria_school(self, newnome, session):
        newschool = datacontrol.School(name=newnome)
        session.add(newschool)
        session.commit()
        session.flush()
        return newschool

    def update_schoolname(self, newnome, schoolid, session):
        foundschool = session.query(School).filter_by(id=schoolid).first()
        if not foundschool:
            return False
        foundschool.name = newnome
        session.commit()
        session.flush()
        return foundschool

class course_handler(object):
    """Classe para manipulacao de cursos"""
    def __init__(self):
        self.courseid = ""
        self.schoolid = ""

    def getcourse(self, session, courseid):
        foundcourse = session.query(Course).filter_by(id=courseid).first()
        if not foundschool:
            return False
        return foundcourse

    def getcourseid(self, session, coursename):
        foundcourse = session.query(Course).filter_by(name=coursename).first()
        if not foundcourse:
            return False
        return foundcourse.id

    def criacourse(self, session, coursename, courseschool):
        newcourse = datacontrol.Course(name=coursename, schoolid=courseschool)
        session.add(newcourse)
        session.commit()
        session.flush()
        return newcourse

    def deletecourse(self, courseid):
        foundcourse = session.query(Course).filter_by(id=courseid).delete()
        session.commit()
        session.flush()

    def updatecourse(self, courseid, newname):
        foundcourse = session.query(Course).filter_by(id=courseid).first()
        if not foundcourse:
            return False
        foundcourse.name = newname
        session.commit()
        session.flush()
        return foundcourse

    def get_all_school_courses(self, idschool):
        """Retorna uma lista de cursos de uma escola"""
        foundcourses = session.query(Course).filter_by(schoolid=idschool)
        if not foundcourses:
            return False
        return foundcourses

class discipline_handler(object):
    """Classe para manipulacao de disciplinas"""
    def __init__(self):
        self.discipline = ""
        self.course = ""

    def getdiscipline(self, session, disciplineid):
        founddiscipline = session.query(Discipline).filter_by(id=disciplineid)\
            .first()
        if not founddiscipline:
            return False
        return founddisciple

    def getdisciplineid(self, session, disciplinename):
        founddiscipline = session.query(Discipline).filter_by\
            (name=disciplinename).first()
        if not founddiscipline:
            return False
        return founddiscipline.id

    def deletediscipline(self, session, disciplineid):
        founddiscipline = session.query(Discipline).filter_by(id=disciplineid)\
            .delete()
        session.commit()
        session.flush()

    def get_all_course_disciplines(self, session, idcourse):
        """Retorna lista de disciplinas de um curso"""
        founddisciplines = session.query(Discipline).filter_by\
            (courseid=idcourse)
        if not founddisciplines:
            return False
        else:
            return founddisciplines

    def createdisciplines(self, disciplinename, session, disciplinecourse):
        newdiscipline = datacontrol.Discipline(name=disciplinename, courseid=\
                                               disciplinecourse)
        session.add(newdiscipline)
        session.commit()
        session.flush()
        return newdiscipline

    def updatediscipline(self, newname, session, disciplineid):
        founddiscipline = session.query(Discipline).filter_by(id=disciplineid)\
            .first()
        if not founddiscipline:
            return False
        founddiscipline.name = newname
        session.commit()
        session.flush()
        return founddiscipline


class content_handler(object):
    """Classe para manipulacao dos contents"""
    def __init__(self):
        self.content = ""
        self.discipline = ""

    def getcontent(self, session, contentid):
        foundcontent = session.query(Content).filter_by(id=contentid).first()
        if not foundcontent:
            return False
        else:
            return foundcontent

    def getcontentbyname(self, session, contentname):
        foundcontent = session.query(Content).filter_by(name=contentname).\
            first()
        if not foundcontent:
            return False
        else:
            return foundcontent

    def deletecontent(self, session, contentid):
        foundcontent = session.query(Content).filter_by(id=contentid).delete()
        session.commit()
        session.flush()

    def get_all_content_by_discipline(self, session, iddiscipline):
        """Retorna uma lista de todos os conteudos de uma disciplina"""
        foundcontents = session.query(Content).filter_by\
            (disciplineid=iddiscipline)
        if not foundcontents:
            return False
        else:
            return foundcontents


    def criacontent(self, session, contentname, discipline):
        newcontent = datacontrol.Content(name=contentname, \
                                         disciplineid=discipline)
        session.add(newcontent)
        session.commit()
        session.flush()

    def update_content(self, session, contentname, contentid):
        foundcontent = session.query(Content).filter_by(id=contentid)
        if not foundcontent:
            return False
        else:
            foundcontent.name = contentname
        session.commit()
        session.flush()
        return foundcontent

class text_handler(object):
    """Classe para manipulacao de textos de conteudo"""
    def __init__(self):
        self.text = ""
        self.content = ""

    def deletetext(self, session, textid):
        foundtext = session.query(Text).filter_by(id=textid).delete()
        session.commit()
        session.flush()

    def gettext(self, session, textid):
        foundtext = session.query(Text).filter_by(id=textid).first()
        if not foundtext:
            return False
        else:
            return foundtext

    def gettextid(self, session, textname):
        foundtext = session.query(Text).filter_by(name=textname).first()
        if not foundtext:
            return False
        else:
            return foundtext.id

    def criatext(self, session, textname, newtext, idcontent):
        newtext = datacontrol.Text(name=textname, contentid=idcontent, \
                                   text=newtext)
        session.add(newtext)
        session.commit()
        session.flush()
        return newtext

    def get_all_content_texts(self, session, idcontent):
        """Retorna uma lista de todos os textos de uma content"""
        foundtexts = session.query(Text).filter_by(contentid=idcontent)
        if not foundtexts:
            return False
        else:
            return foundtexts

class archive_handler(object):
    """Classe para manipulacao de arquivos das disciplines"""
    def __init__(self):
        self.archive = ""
        self.discipline = ""


