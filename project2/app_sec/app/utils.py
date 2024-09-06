


from functools import wraps
from flask import flash, redirect, session, url_for
from app.blueprints.auth.models import User
from app.blueprints.products.models import Product
from app.config import Config
import re
import requests



def login_user(user: User):
    if user!= None:
        session['user_id'] = user.id
        session['username'] = user.username
        session['name'] = user.name
    
def logout_user():
    session.clear()
    
    
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You must be logged in to access this page', 'error')
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return decorated_function

def get_product(id:int):
    product = Product.query.filter_by(id=id).first()  
    return product

def get_user_by_id(id:int):
    user = User.query.filter_by(id=id).first()
    return user

def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not User.query.filter_by(id= session['user_id']).first().is_admin() :
            flash('You must be an Admin to access this page', 'error')
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return decorated_function

def validate_password(password, confirm_password):
    
    if password != confirm_password:
        flash('Passwords do not match. Please try again.', 'error')
        return False
    
    normalized_password = re.sub(r'\s+', ' ', password).strip()
    
    if len(normalized_password) < 12:
        flash("Password must be at least 12 characters long after combining multiple spaces.", "error")
        return False
    
    if len(normalized_password) > 128:
        flash("Password cannot be more than 128 characters long.", "error")
        return False
    
    if not all(character.isprintable() for character in password):
        flash("Password contains non-printable characters.", "error")
        return False
    
    return True
    

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        flash('Invalid email format.', 'error')
        return False
    return True

def validate_phone(phone):
    phone_regex = r'^\+?[0-9]{7,15}$'
    if not re.match(phone_regex, phone):
        flash('Invalid phone number format.', 'error')
        return False
    return True

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_captcha(captcha_response):
    payload = {
        'secret': Config.RECAPTCHA_SECRET_KEY ,
        'response': captcha_response
    }
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
    result = response.json()
    return result.get('success', False)
