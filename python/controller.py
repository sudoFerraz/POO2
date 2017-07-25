import sqlalchemy
import model
import hashlib


sessionmaker = model.ostools()
session = sessionmaker.dbconnection()

userhandler = model.user_handler()
schoolhandler = model.school_handler()
coursehandler = model.course_handler()
disciplinehandler = model.discipline_handler()
contenthandler = model.content_handler()
texthandler = model.text_handler()
archivehandler = model.archive_handler()


class Logged_normal(object, userlogged):
    def __init__(self, userlogged):
        self.user = userlogged

    def subscribe(self, iddiscipline):
        pass


class Logged_super(object, userlogged):
    def __init__(self, userlogged):
        self.user = userlogged

    def subscribe(self, iddiscpline):
        pass

class Not_Logged(object):
    """Nao logado no servidor ainda"""
    def __init__(self):
        self.user = ""

    def login(self, loginemail, loginpwd):
        user = userhandler.getuser(session, loginemail)
        if not user:
            return False
        md5 = hashlib.md5(loginpwd).hexdigest()
        if user.password == md5:
            if user.usertype == 0:
                return Logged_normal(user)
            if user.usertype == 1:
                return Logged_super(user)
        else:
            return False

    def register(self, loginemail, loginpwd, username, userschool, userbirth):
        user = userhandler.criauser(loginemail, loginpwd, username, userschool,\
                                    userbirth)
        if not user:
            return False
        else:
            return Not_Logged()


    def searcharchives():
        pass

