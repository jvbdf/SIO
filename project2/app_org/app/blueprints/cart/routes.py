from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from app.extensions import db
from app.blueprints.cart.models import Cart, CartItem
from app.blueprints.products.models import Product
from app.utils import get_user_by_id ,login_required


cart = Blueprint('cart', __name__)

def calculate_totals(cart_items):
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    tax = subtotal * 0.1  # Exemplo de 10% de imposto
    shipping = 10.00 if subtotal < 100 else 0  # Frete grátis para pedidos acima de 100
    total = subtotal + tax + shipping
    return subtotal, tax, shipping, total


@cart.route('/cart')
@login_required
def cart_page():
    user_id = session['user_id']
    
    try:
        user = get_user_by_id(user_id)
    except:
        user = None
        
    cart = Cart.query.filter_by(user_id=user_id).first()

    cart_items = cart.items
    subtotal, tax, shipping, total = calculate_totals(cart_items)
    
    return render_template('cart.html', 
                           cart_items=cart_items, 
                           subtotal=subtotal, 
                           tax=tax, 
                           shipping=shipping, 
                           total=total, user = user)
    
@cart.route('/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    user_id = session['user_id']
    product = Product.query.get_or_404(product_id)
    quantity = request.form.get('quantity', type=int)
    
    if not quantity:
        quantity = 1
    
    cart = Cart.query.filter_by(user_id=user_id).first()
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    
    db.session.commit()
    flash(f'{product.name} added to cart.', 'success')
    
    return redirect(url_for('cart.cart_page'))

@cart.route('/cart/remove/<int:item_id>', methods=['POST'])
@login_required
def remove_item(item_id):
    user_id = session['user_id']
    cart = Cart.query.filter_by(user_id=user_id).first()
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=item_id).first()

    if not cart_item:
        flash("Item not found in cart.", "error")
        return redirect(url_for('cart.cart_page'))

    db.session.delete(cart_item)
    db.session.commit()
    
    flash(f'Item removed from cart.', 'success')
    return redirect(url_for('cart.cart_page'))

@cart.route('/cart/update', methods=['POST'])
@login_required
def update_cart():
    try:
        user_id = session['user_id']
        cart = Cart.query.filter_by(user_id=user_id).first()

        # Itera sobre os itens no formulário
        for key, value in request.form.items():
            if key.startswith('quantity_'):
                product_id = int(key.split('_')[1])
                quantity = int(value)
                
                if quantity > 0:
                    # Atualiza a quantidade do item no carrinho
                    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
                    if cart_item:
                        cart_item.quantity = quantity
                else:
                    flash(f'Invalid quantity for product ID {product_id}', 'error')
        
        db.session.commit()
        flash('Cart updated successfully.', 'success')
        
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating cart: {str(e)}', 'error')

    return redirect(url_for('cart.cart_page'))
