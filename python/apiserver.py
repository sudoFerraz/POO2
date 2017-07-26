from flask import Flask, render_template
from flask import jsonify
from flask import request
import json
import dbmodel
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from dbmodel import User
from dbmodel import School
from dbmodel import Course
from dbmodel import Discipline
from dbmodel import Review
from dbmodel import Content
from dbmodel import Text
from dbmodel import Subscribe
from dbmodel import Notification
from dbmodel import Archive
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, \
    logout_user, current_user, request, redirect
from matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import BaseView, expose
from jinja2 import Markup
from flask import url_for
from flask_admin import form
import os
from dbmodel import Image
import jinja2

basedir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(basedir, 'static')
