from app.blueprints.products.models import Product
from app.extensions import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    shipping_address = db.Column(db.String(200), nullable=False)
    billing_address = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='processed')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  

    items = db.relationship('OrderItem', backref='order', lazy=True)
    
            
    def __repr__(self):
        return f"<Order {self.id} (User: {self.user_id}, Status: {self.status}, Date: {self.date})>"


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    
        
    def __repr__(self):
        return f"<OrderItem {self.id} (Order: {self.order_id}, Product: {self.product_id}, Quantity: {self.quantity})>"
