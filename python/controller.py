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
subscriptionhandler = model.subscription_handler()


class Logged_normal(object, userlogged):
    def __init__(self, userlogged):
        self.user = userlogged

    def subscribe(self, iddiscipline):
        newsubscription = subscriptionhandler.cria_subscription\
            (session, self.user.id, iddiscipline)
        if not newsubscription:
            return False
        else:
            return newsubscription

    def register_school(self, schoolname):
        newschool = schoolhandler.cria_school(schoolname, session)
        return newschool

    def register_courses(self, coursename, schoolname):
        schoolid = schoolhandler.get_school_id(schoolname, session)
        if not schoolid:
            return False
        else:
            newcourse = coursehandler.criacourse(session, coursename, schoolid)
            if not newcourse:
                return False
            else:
                return True

    def register_discipline(self, disciplinename, courseid):
        newdiscipline = disciplinehandler.creatediscipline(disciplinename, \
                                                           session, courseid)
        if not newdiscipline:
            return False
        else:
            return newdiscipline


    def review_content(self, contentid, userreview):
        newreview = reviewhandler.cria_review(session, contentid, self.user.id,\
                                               userreview)
        if not newreview:
            return False
        else:
            return newreview

    def search_discipline_by_course(self, courseid):
        disciplines = disciplinehandler.get_all_course_disciplines(session, \
                                                                   courseid)
        if not disciplines:
            return False
        else:
            return disciplines

    def search_content_by_discipline(self, disciplineid):
        contents = contenthandler.get_all_content_by_discipline(session, \
                                                                disciplineid)
        if not contents:
            return False
        else:
            return contents

    def search_courses_by_school(self, schoolid):
        courses = coursehandler.get_all_school_courses(session, schoolid)
        if not courses:
            return False
        else:
            return courses



    def register_text(self, contentname, disciplineid, newtext):
        newcontent = contenthandler.criacontent(session, contentname, disciplineid)
        if not newcontent:
            return False
        else:
            newtext = texthandler.criatext(session, newtext, newcontent.id)
            if not newtext:
                return False
            else:
                return newtext

class Logged_super(object, Logged_normal(), userlogged):
    def __init__(self, userlogged):
        self.user = userlogged

    def validate_school(schoolid, session):
        validatedschool = schoolhandler.validateschool(schoolid, session)
        if not validatedschool:
            return False
        else:
            return validatedschool

    def validate_content(contentid, session):
        validatedcontent = contenthandler.validate_content(session, contentid)
        if not validatedcontent:
            return False
        else:
            return validatedcontent


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

