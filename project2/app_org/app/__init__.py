from flask import Flask
from app.config import Config
from app.blueprints.main.routes import main
from app.blueprints.auth.routes import auth
from app.blueprints.products.routes import products
from app.blueprints.profile.routes import profile
from app.blueprints.orders.routes import orders
from app.blueprints.cart.routes import cart
from app.blueprints.wishlists.routes import wishlist
from app.blueprints.checkout.routes import checkout
from app.blueprints.reviews.routes import reviews
from app.blueprints.admin.routes import admin_bp
from app.blueprints.errors.routes import errors

def create_app():
    app = Flask(__name__)
    
    # Outros blueprints aqui
    
    app.register_blueprint(errors)

    return app

from app.extensions import db,migrate, csrf

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar as extensões flask aqui
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(products)
    app.register_blueprint(profile)
    app.register_blueprint(orders)
    app.register_blueprint(cart)
    app.register_blueprint(wishlist)
    app.register_blueprint(checkout)
    app.register_blueprint(reviews)
    app.register_blueprint(admin_bp)
    app.register_blueprint(errors)
    
    with app.app_context():
        from app.blueprints.auth.models import User, Role
        from app.blueprints.cart.models import Cart, CartItem
        from app.blueprints.products.models import Product, Category
        from app.blueprints.orders.models import Order, OrderItem
        from app.blueprints.reviews.models import Review
        from app.blueprints.wishlists.models import Wishlist, WishlistItem
    
    

    return app

