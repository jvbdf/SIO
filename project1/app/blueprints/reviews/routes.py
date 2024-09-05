from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.extensions import db
from app.blueprints.reviews.models import Review
from app.utils import get_user_by_id, login_required
from datetime import datetime

reviews = Blueprint('reviews', __name__)

@reviews.route('/product/<int:product_id>/review', methods=['POST'])
@login_required
def add_review(product_id):
    user_id = session.get('user_id')
    

    rating = request.form.get('rating')
    comment = request.form.get('comment')
    
    if not rating or not comment:
        flash('Please fill out all fields.', 'error')
        return redirect(url_for('products.view', id=product_id))
    
    review = Review(
        product_id=product_id,
        user_id=user_id,
        rating=int(rating),
        comment=comment,
        date=datetime.utcnow()
    )
    
    db.session.add(review)
    db.session.commit()
    
    flash('Your review has been submitted!', 'success')
    return redirect(url_for('products.view', id=product_id))

@reviews.route('/reviews')
@login_required
def review():
    user_id = session['user_id']
    user = get_user_by_id(user_id)

    reviews = Review.query.filter_by(user_id=user_id).all()

    return render_template('reviews.html', user=user, reviews=reviews)
