from flask import Blueprint, flash, redirect, render_template, session, url_for
from app.extensions import db
from app.blueprints.products.models import Product
from app.blueprints.wishlists.models import Wishlist, WishlistItem
from app.utils import get_user_by_id, login_required

wishlist = Blueprint('wishlists', __name__)

@wishlist.route('/wishlist')
@login_required
def view_wishlist():
    user_id = session['user_id']
    
    try:
        user = get_user_by_id(user_id)
    except:
        user = None
    if not user_id:
        flash('You need to be logged in to view your wishlist.', 'error')
        return redirect(url_for('auth.login'))

    wishlist = Wishlist.query.filter_by(user_id=user_id).first()

    if not wishlist:
        flash('Your wishlist is empty.', 'info')
        wishlist_items = None
    else:
        wishlist_items = wishlist.items  
    return render_template('wishlist.html', wishlist_items=wishlist_items, user = user)


@wishlist.route('/wishlist/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_wishlist(product_id):
    user_id = session.get('user_id')
    product = Product.query.get_or_404(product_id)
    wishlist = Wishlist.query.filter_by(user_id=user_id).first()

    if not wishlist:
        wishlist = Wishlist(user_id=user_id, name="My Wishlist")
        db.session.add(wishlist)
        db.session.commit()

    wishlist_item = WishlistItem.query.filter_by(wishlist_id=wishlist.id, product_id=product_id).first()

    if wishlist_item:
        flash(f'{product.name} is already in your wishlist.', 'error')
    else:
        wishlist_item = WishlistItem(wishlist_id=wishlist.id, product_id=product_id)
        db.session.add(wishlist_item)
        db.session.commit()
        flash(f'{product.name} added to your wishlist.', 'success')
    
    return redirect(url_for('products.view', id=product_id))


@wishlist.route('/wishlist/remove/<int:product_id>', methods=['POST'])
@login_required
def remove_from_wishlist(product_id):
    user_id = session.get('user_id')
    wishlist = Wishlist.query.filter_by(user_id=user_id).first()

    if not wishlist:
        flash('Wishlist not found.', 'error')
        return redirect(url_for('wishlists.view_wishlist'))

    wishlist_item = WishlistItem.query.filter_by(wishlist_id=wishlist.id, product_id=product_id).first()

    if wishlist_item:
        db.session.delete(wishlist_item)
        db.session.commit()
        flash(f'Item removed from your wishlist.', 'success')
    else:
        flash('Item not found in your wishlist.', 'error')

    return redirect(url_for('wishlists.view_wishlist'))
