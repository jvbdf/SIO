from app.extensions import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    products = db.relationship('Product', backref='category', lazy=True)
    
    def __repr__(self):
        return f"<Category {self.name}>"

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer)
    image_url = db.Column(db.String(200))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    rating = db.Column(db.Float)
    cart_items = db.relationship('CartItem', backref='product', lazy=True)
    order_items = db.relationship('OrderItem', backref='product', lazy=True)
    in_stock = db.Column(db.Boolean, default=True)
    
    # wishlist_items = db.relationship('WishlistItem', backref='product', lazy=True)
    # wishlist_items = db.relationship('WishlistItem', backref='product_assoc', lazy=True)
    wishlist_items = db.relationship('WishlistItem', back_populates='product', lazy=True)

    reviews = db.relationship('Review', backref='product', lazy=True)
    
    def check_in_stock(self):
        if self.quantity > 0:
            self.set_in_stock()
        else:
            self.set_out_of_stock()
    
    def set_in_stock(self):
        self.in_stock = True
        db.session.commit()
    
    def set_out_of_stock(self):
        self.in_stock = False
        db.session.commit()
        
    def is_in_stock(self):
        return self.in_stock
    
    
    def __repr__(self):
        return f"<Product {self.name} (Category: {self.category.name}, Price: {self.price}), Quantity: {self.quantity}>"
