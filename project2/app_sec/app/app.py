from flask import Flask
from app import create_app
from app.blueprints.auth.models import User, Role
from app.blueprints.products.models import Product, Category
from app.blueprints.cart.models import Cart, CartItem
from app.blueprints.orders.models import Order, OrderItem
from app.blueprints.reviews.models import Review

app = create_app()

if __name__ == '__main__':
    
    app.run()