from app.extensions import db

class Wishlist(db.Model):
    __tablename__ = 'wishlists'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    items = db.relationship('WishlistItem', backref='wishlist', lazy=True)
    
    def __repr__(self):
        return f"<Wishlist {self.name} (User: {self.user_id})>"

class WishlistItem(db.Model):
    __tablename__ = 'wishlist_items'
    
    id = db.Column(db.Integer, primary_key=True)
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlists.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    # product = db.relationship('Product', backref='wishlist_assoc')
    product = db.relationship('Product', back_populates='wishlist_items')
    def __repr__(self):
        return f"<WishlistItem {self.id} (Product: {self.product_id}, Quantity: {self.quantity})>"