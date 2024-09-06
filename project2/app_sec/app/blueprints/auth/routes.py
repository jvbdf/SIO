import hashlib
import os
from flask import Blueprint, flash, redirect, render_template, request, session,url_for
from sqlalchemy import text
from app.blueprints.auth.models import Role, User
from app.blueprints.cart.models import Cart
from app.config import Config
from app.extensions import db
from app.utils import allowed_file, login_user, logout_user, validate_email, validate_password, validate_phone, login_required, validate_captcha
from werkzeug.utils import secure_filename
auth = Blueprint('auth', __name__)


    

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if session.get('user_id'):
        return redirect(url_for('products.products_page'))
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        captcha_response = request.form['g-recaptcha-response']
        
        if validate_captcha(captcha_response):
            user = User.query.filter_by(email=email).first()

            if user.check_password(password):
                login_user(user)
                return redirect(url_for('products.products_page'))
            else:
                flash('Login failed. Check your email and/or password.', 'error')
                return redirect(url_for('auth.login'))

    return render_template('login.html')





@auth.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user_id'):
        flash('You already have an account. Please logout if you want to create another account','error')
        return redirect(url_for('products.products_page'))
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']        
        confirm_password = request.form['confirm_password']
        phone = request.form['phone']
        file = request.files['profile_picture']
        
        
        
        if not validate_email(email):
            return redirect(url_for('auth.register'))
        
        if not validate_phone(phone):
            return redirect(url_for('auth.register'))
        
        
        if not validate_password(password,confirm_password):
            return redirect(url_for('auth.register'))

        if not validate_phone(phone):
            return redirect(url_for('auth.register'))
        
        
        
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        
        
        if existing_user:
            flash('Email or username already exists. Please choose another.', 'error')
            return redirect(url_for('auth.register'))
        
        if not file :
            file_path = os.path.join(Config.UPLOAD_FOLDER, 'default_user.jpg')
                      
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
            file.save(file_path)
        else:
            flash('Invalid file type. Please upload an image.', 'error')
            return redirect(url_for('auth.register'))
        
        captcha_response = request.form['g-recaptcha-response']
        
        if validate_captcha(captcha_response):
                
        
            user_role = Role.query.filter_by(name='user').first()
            
    
            new_user = User(
                name=name, 
                email=email, 
                username=username, 
                password= password, 
                phone=phone, 
                role_id= user_role.id,
                profile_picture= file_path.replace("\\", "/")
            )
            new_user.set_password(password)
            
            db.session.add(new_user)
            db.session.commit()
            
            cart = Cart(user_id=new_user.id)
            db.session.add(cart)
            
            db.session.commit()
            
            flash('Registration successful! You can now login.', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth.route('/forgot', methods =['GET', 'POST'])
def forgot():
    return render_template('forgot_password.html')

@auth.route('/logout')
@login_required
def logout():
    flash("Thanks for visiting our Shop! Bye!", "success")
    logout_user()
    return redirect(url_for('main.home'))
