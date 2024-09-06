from flask import Blueprint, redirect, render_template, flash, request, url_for
errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@errors.app_errorhandler(413)
def file_too_large(e):
    if request.endpoint == 'profile.upload_profile_picture':
        flash("File size must be less than 1 MB", 'error')
        return redirect(url_for('profile.profile_page'))
    elif request.endpoint == 'auth.register':
        flash("File size must be less than 1 MB", 'error')
        return redirect(url_for('auth.register'))
    
    return "File too large", 413  