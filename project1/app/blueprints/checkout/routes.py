from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from app.extensions import db
from app.blueprints.cart.models import Cart, CartItem
from app.blueprints.orders.models import Order, OrderItem
from app.blueprints.products.models import Product
from app.utils import get_user_by_id, login_required

checkout = Blueprint('checkout', __name__)

def calculate_totals(cart_items):
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    tax = subtotal * 0.1  
    shipping = 10.00 if subtotal < 100 else 0  
    total = subtotal + tax + shipping
    return subtotal, tax, shipping, total

@checkout.route('/checkout')
@login_required
def checkout_page():
    user_id = session['user_id']
    
    try:
        user = get_user_by_id(user_id)
    except:
        user = None
    cart = Cart.query.filter_by(user_id=user_id).first()
    
    if not cart or not cart.items:
        flash('Your cart is empty!', 'error')
        return redirect(url_for('products.products_page'))

    cart_items = cart.items
    for item in cart.items:
        if item.product.quantity < item.quantity or  not item.product.is_in_stock():
            flash(f"Product {item.product.name} does not have enough stock. Only {item.product.quantity} in stock", 'error')
            return redirect(url_for('cart.cart_page'))
    
    db.session.commit()

    subtotal, tax, shipping, total = calculate_totals(cart_items)
    
    
    return render_template('checkout.html', 
                           cart_items=cart_items, 
                           subtotal=subtotal, 
                           tax=tax, 
                           shipping=shipping, 
                           total=total, user = user)

@checkout.route('/checkout/process', methods=['POST'])
@login_required
def process_checkout():
    user_id = session['user_id']
    cart = Cart.query.filter_by(user_id=user_id).first()
    
    if not cart or not cart.items:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('products.products_page'))

    full_name = request.form.get('full_name')
    address = request.form.get('address')
    city = request.form.get('city')
    zip_code = request.form.get('zip_code')
    country = request.form.get('country')
    card_number = request.form.get('card_number')
    card_expiry = request.form.get('card_expiry')
    card_cvc = request.form.get('card_cvc')

    subtotal, tax, shipping, total = calculate_totals(cart.items)
    #Implementar posteriormente um serviço de pagamentos

    order = Order(
        user_id=user_id, 
        total_amount=total, 
        shipping_address=address, 
        billing_address=address,  
        status='processed'
    )
    
    db.session.add(order)
    db.session.commit()
    for item in cart.items:
        if item.product.quantity >= item.quantity and item.product.is_in_stock():
            item.product.quantity -= item.quantity
            if item.product.quantity == 0:
                item.product.set_out_of_stock()
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity
            )
            db.session.add(order_item)
            db.session.delete(item)
        else:
            flash(f"Product {item.product.name} does not have enough stock.Please remove!", 'error')
            db.session.delete(order)
            db.session.commit()
            return redirect(url_for('cart.cart_page'))
    
    db.session.commit()

    flash('Your order has been placed successfully!', 'success')
    return redirect(url_for('orders.order_confirmation', order_id=order.id))

