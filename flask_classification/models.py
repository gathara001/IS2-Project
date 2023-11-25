from datetime import datetime
from flask_classification import db

# #Flask instance
# app = Flask(__name__)
#
# #Secret Key
# app.config['SECRET_KEY'] = '764528ab1b10cd0c349dfde280ba735'
# #Add Database - MySQL
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask_app'
#
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
#
# db = SQLAlchemy()



class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='User', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

