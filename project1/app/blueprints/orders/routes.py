from datetime import datetime
from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from app.blueprints.cart.models import Cart, CartItem
from app.blueprints.orders.models import Order, OrderItem
from app.blueprints.products.models import Product
from app.utils import get_user_by_id, login_required
from app.extensions import db

orders = Blueprint('orders', __name__)

def calculate_totals(order_items):
    subtotal = sum(item.product.price * item.quantity for item in order_items)
    tax = subtotal * 0.1
    shipping = 10.00 if subtotal < 100 else 0
    total = subtotal + tax + shipping
    return subtotal, tax, shipping, total

@orders.route('/order/history')
@login_required
def order_history():
    user_id = session.get('user_id')

    user = get_user_by_id(user_id)
    orders = Order.query.filter_by(user_id=user_id).order_by(Order.date.desc()).all()
    return render_template('order_history.html', orders=orders, user=user)

@orders.route('/order/confirmation/<int:order_id>')
@login_required
def order_confirmation(order_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))  # Redireciona para login se não estiver autenticado

    user = get_user_by_id(user_id)
    order = Order.query.get_or_404(order_id)
    order_items = order.items

    subtotal, tax, shipping, total = calculate_totals(order_items)

    return render_template('order_confirmation.html',
                           order=order,
                           order_items=order_items,
                           subtotal=subtotal,
                           tax=tax,
                           shipping=shipping,
                           total=total,
                           user=user)

# @orders.route('/order/repeat/<int:order_id>')
# def repeat_order(order_id):
#     user_id = session.get('user_id')
    
#     user = get_user_by_id(user_id)
#     order = Order.query.get_or_404(order_id)
#     order_items = order.items

    
#     subtotal, tax, shipping, total = calculate_totals(order_items)

#     new_order = Order(
#         user_id=user_id,
#         total_amount=total,  
#         shipping_address=order.shipping_address,
#         billing_address=order.billing_address,
#         status='processed',  
#         date=datetime.utcnow()  
#     )
#     db.session.add(new_order)
#     db.session.commit()
    
    

#     for item in order_items:
#         new_order_item = OrderItem(
#             order_id=new_order.id,
#             product_id=item.product_id,
#             quantity=item.quantity
#         )
#         db.session.add(new_order_item)

#     db.session.commit()

#     flash('Your order has been repeated successfully!', 'success')
#     return redirect(url_for('orders.order_confirmation', order_id=new_order.id))


@orders.route('/order/repeat/<int:order_id>')
@login_required
def repeat_order(order_id):
    user_id = session.get('user_id')
    order = Order.query.get_or_404(order_id)
    order_items = order.items

    cart = Cart.query.filter_by(user_id=user_id).first()
    
    for item in order_items:
        existing_cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=item.product_id).first()
        
        if existing_cart_item:
            existing_cart_item.quantity += item.quantity
        else:
            new_cart_item = CartItem(
                cart_id=cart.id,
                product_id=item.product_id,
                quantity=item.quantity
            )
            db.session.add(new_cart_item)
    
    db.session.commit()

    return redirect(url_for('cart.cart_page'))
