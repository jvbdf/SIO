from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import asc, desc
from app.extensions import db
from app.blueprints.products.models import Product
from app.utils import login_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET'])
@login_required
def admin():
    return redirect(url_for('admin.inventory_management'))


@admin_bp.route('/admin/inventory', methods=['GET'])
@login_required
def inventory_management():
    query = Product.query
    
    # Filtros
    search_term = request.args.get('search', '')
    stock_filter = request.args.get('stock', 'all')
    sort_by = request.args.get('sort', 'name')
    order = request.args.get('order', 'asc')
    page = request.args.get('page', 1, type=int)
    
    if search_term:
        query = query.filter(Product.name.ilike(f'%{search_term}%'))

    if stock_filter == 'in_stock':
        query = query.filter(Product.in_stock.is_(True))
    elif stock_filter == 'out_of_stock':
        query = query.filter(Product.in_stock.is_(False))

    # Ordenação
    if sort_by == 'price':
        query = query.order_by(asc(Product.price) if order == 'asc' else desc(Product.price))
    elif sort_by == 'quantity':
        query = query.order_by(asc(Product.quantity) if order == 'asc' else desc(Product.quantity))
    else:
        query = query.order_by(asc(Product.name) if order == 'asc' else desc(Product.name))
    
    # Paginação
    products = query.paginate(page=page, per_page=10)
    
    return render_template('inventory.html', products=products, search_term=search_term, stock_filter=stock_filter, sort_by=sort_by, order=order)

@admin_bp.route('/admin/inventory/update/<int:product_id>', methods=['POST'])
@login_required
def update_inventory(product_id):
    product = Product.query.get_or_404(product_id)
    
    new_quantity = request.form.get('quantity')
    if new_quantity and new_quantity.isdigit():
        product.quantity = int(new_quantity)        
        if product.quantity > 0:
            product.in_stock = True
        else:
            product.in_stock = False
        
        db.session.commit()
        flash(f'Product "{product.name}" updated successfully!', 'success')
    else:
        flash('Invalid quantity.', 'error')
    
    return redirect(url_for('admin.inventory_management'))
