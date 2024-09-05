


from functools import wraps
from flask import flash, redirect, session, url_for
from app.blueprints.auth.models import User
from app.blueprints.products.models import Product


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