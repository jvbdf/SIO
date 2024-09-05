from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from sqlalchemy import text
from app.blueprints.cart.models import Cart, CartItem
from app.blueprints.products.models import Category, Product
from app.utils import get_product, get_user_by_id, login_required
from app.extensions import db

products = Blueprint('products',__name__)


#Colocar aqui um login_required para bloquear o acesso 
@products.route('/shop')
def products_page():
    try:
        user = get_user_by_id(session['user_id'])
    except:
        user = None
        
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('shop.html', user = user, products = products, categories = categories)

@products.route('/product/<id>')
@login_required
def view(id):
    user_id = session['user_id']
    
    try:
        user = get_user_by_id(user_id)
    except:
        user = None
    
    # try:
    #     product = Product.query.filter_by(id=id).first()
    # except:
    #     return redirect(url_for('products.products_page'))
    
    product = Product.query.filter_by(id=id).first_or_404()
    
    total_reviews = len(product.reviews)
    if total_reviews > 0:
        average_rating = sum([review.rating for review in product.reviews]) / total_reviews
    else:
        average_rating = 0
    
    products = Product.query.all()
    
    return render_template('product.html', 
                           product=product, 
                           products=products, 
                           user=user, 
                           average_rating=average_rating, 
                           total_reviews=total_reviews)




@products.route('/search')
def search():
    try:
        user_id = session['user_id']
        user = get_user_by_id(user_id)
    except:
        user = None
    query = request.args.get('query')
    if query:
        products = Product.query.filter(Product.name.ilike(f"%{query}%")).all()
    else:
        products = []
    return render_template('search_results.html', products=products, query=query, user=user)
