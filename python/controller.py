import sqlalchemy
import model

sessionmaker = model.ostools()
session = sessionmaker.dbconnection()

userhandler = model.user_handler()
schoolhandler = model.school_handler()
coursehandler = model.course_handler()
disciplinehandler = model.discipline_handler()
contenthandler = model.content_handler()
texthandler = model.text_handler()
archivehandler = model.archive_handler()


class Logged_normal(object, useremail):
    pass

class Logged_super(object, useremail):

class Not_Logged(object):
    """Nao logado no servidor ainda"""
    def __init__(self):
        self.user = ""

    def login(self, loginuser, loginpwd):

