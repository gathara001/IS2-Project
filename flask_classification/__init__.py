import os
from flask import Flask
from routes import main_blueprint
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func 
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


db = SQLAlchemy()

def create_app():
    #Flask instance
    app = Flask(__name__)
    #Secret Key
    app.config['SECRET_KEY'] = '764528ab1b10cd0c349dfde280ba735'
    #Add Database - MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask_app'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)

    bcrypt = Bcrypt(app)

    app.register_blueprint(main_blueprint)

    return app
