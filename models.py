from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

db = SQLAlchemy()
login = LoginManager()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(128), unique=True)
    user_email = db.Column(db.String(128))
    user_pass = db.Column(db.String())

    def set_password(self, password):
        self.user_pass = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_pass, password)

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.authenticated

    def get_id(self):
        return self.user_id

    def is_anonymous(self):
        return False


class Blocks(db.Model):
    __tablename__ = 'blocks'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    reason = db.Column(db.String)


class Screenshots(db.Model):
    __tablename__ = 'screenshots'
    id = db.Column(db.Integer, primary_key=True)
    block = db.Column(db.Integer, db.ForeignKey('blocks.id'))
    path = db.Column(db.String)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
