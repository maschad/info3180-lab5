from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID, COMMON_PROVIDERS
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = "this is a super secure key"
app.config['OPENID_PROVIDERS'] = COMMON_PROVIDERS
# remember to change to heroku's database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lab5:admin@localhost/lab5'
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://yzicurmnvkqqhp:Kpl-6hLvDaRcPCelsrxdmydSgi@ec2-23-21-219-209.compute-1.amazonaws.com:5432/de7vj5i2j9deb1"
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app,'/tmp')

from app import views
