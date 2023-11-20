import os
from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func 


#Flask instance
app = Flask(__name__)

#Secret Key
app.config['SECRET_KEY'] = '764528ab1b10cd0c349dfde280ba735'
#Add Database - MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy()
