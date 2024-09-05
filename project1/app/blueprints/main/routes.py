from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main',__name__)



@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/')
def index():
    return redirect(url_for('main.home'))