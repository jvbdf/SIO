from app.extensions import db
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    
    def __repr__(self):
        return f"<Role {self.name}>"

class User(db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    
    address = db.Column(db.String(100))
    
    profile_picture = db.Column(db.String(200), nullable=True, default='static/img/profile_pics/default.jpg')

    
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy=True))
    carts = db.relationship('Cart', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)
    
    def is_admin(self):
        return self.role.name == 'admin'
    
    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return f"<User {self.username} (Role: {self.role.name})>"

