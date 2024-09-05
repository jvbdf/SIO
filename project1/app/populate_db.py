from app.extensions import db
from app.blueprints.auth.models import User, Role
from app.blueprints.cart.models import Cart, CartItem
from app.blueprints.wishlists.models import  Wishlist, WishlistItem
from app.blueprints.products.models import Product, Category
from app.blueprints.orders.models import Order, OrderItem
from app.blueprints.reviews.models import Review
from app.extensions import db



def create_roles():
    admin_role = Role(name='admin')
    user_role = Role(name='user')
    
    db.session.add(admin_role)
    db.session.add(user_role)
    print('Roles created')
    db.session.commit()

def create_users():
    admin_role = Role.query.filter_by(name='admin').first()
    user_role = Role.query.filter_by(name='user').first()
    
    user1 = User(name='Admin User', email='admin@example.com', username='admin', password='adminpass', role=admin_role)
    user2 = User(name='Regular User', email='user@example.com', username='user', password='userpass', role=user_role)
    
    user1.set_password('adminpass')
    user2.set_password('userpass')
    
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print(f'User \'{user1.name}\' created ')
    print(f'User \'{user2.name}\' created ')

def create_categories():
    category1 = Category(name='Caps')
    category2 = Category(name='Hoodies')
    category3 = Category(name='Keychains')
    category4 = Category(name='Mousepads')
    category5 = Category(name='Mugs')
    category6 = Category(name='Notebooks')
    category7 = Category(name='Pins')
    category8 = Category(name='Stickers')
    category9 = Category(name='T-Shirts')
    
    db.session.add(category1)
    db.session.add(category2)
    db.session.add(category3)
    db.session.add(category4)
    db.session.add(category5)
    db.session.add(category6)
    db.session.add(category7)
    db.session.add(category8)
    db.session.add(category9)
    db.session.commit()
    
    print('Categories created')

def create_products():
    # Supondo que as categorias já foram criadas
    caps = Category.query.filter_by(name='Caps').first()
    hoodies = Category.query.filter_by(name='Hoodies').first()
    keychains = Category.query.filter_by(name='Keychains').first()
    mousepads = Category.query.filter_by(name='Mousepads').first()
    mugs = Category.query.filter_by(name='Mugs').first()
    notebooks = Category.query.filter_by(name='Notebooks').first()
    pins = Category.query.filter_by(name='Pins').first()
    stickers = Category.query.filter_by(name='Stickers').first()
    tshirts = Category.query.filter_by(name='T-Shirts').first()

    products = [
        # Caps 
        Product(name='Cap 1', description='Stylish cap for everyday use.', price=24.99, quantity=25, category=caps, image_url='static/img/cap/cap_1.png'),
        Product(name='Cap 2', description='Another stylish cap.', price=26.99, quantity=15, category=caps, image_url='static/img/cap/cap_2.png'),
        
        # Hoodies 
        Product(name='Hoodie 1', description='Comfortable hoodie for everyday wear.', price=49.99, quantity=10, category=hoodies, image_url='static/img/hoodie/hoodie_1.png'),
        Product(name='Hoodie 2', description='Stylish hoodie with a unique design.', price=52.99, quantity=10, category=hoodies, image_url='static/img/hoodie/hoodie_2.png'),
        Product(name='Hoodie 3', description='Warm and cozy hoodie for chilly days.', price=54.99, quantity=10, category=hoodies, image_url='static/img/hoodie/hoodie_3.png'),
        Product(name='Hoodie 4', description='Lightweight hoodie for any occasion.', price=46.99, quantity=10, category=hoodies, image_url='static/img/hoodie/hoodie_4.png'),
        Product(name='Hoodie 5', description='Classic hoodie with a comfortable fit.', price=58.99, quantity=10, category=hoodies, image_url='static/img/hoodie/hoodie_5.png'),
        Product(name='Hoodie 6', description='Trendy hoodie with modern aesthetics.', price=59.99, quantity=10, category=hoodies, image_url='static/img/hoodie/hoodie_6.png'),

        # Keychains
        Product(name='Keychain 1', description='Durable keychain with a sleek design.', price=4.99, quantity=100, category=keychains, image_url='static/img/keychain/keychain_1.png'),
        Product(name='Keychain 2', description='Compact keychain with a stylish look.', price=5.49, quantity=100, category=keychains, image_url='static/img/keychain/keychain_2.png'),
        Product(name='Keychain 3', description='Keychain with a modern twist.', price=5.99, quantity=80, category=keychains, image_url='static/img/keychain/keychain_3.png'),
        Product(name='Keychain 4', description='Unique keychain design.', price=6.99, quantity=60, category=keychains, image_url='static/img/keychain/keychain_4.png'),

        # Mousepads 
        Product(name='Mousepad 1', description='Smooth surface for precise mouse control.', price=12.99, quantity=50, category=mousepads, image_url='static/img/mousepad/mousepad_1.png'),
        Product(name='Mousepad 2', description='Ergonomic mousepad for comfortable use.', price=14.99, quantity=40, category=mousepads, image_url='static/img/mousepad/mousepad_2.png'),

        # Mugs 
        Product(name='Mug 1', description='High-quality ceramic mug.', price=9.99, quantity=50, category=mugs, image_url='static/img/mug/mug_1.png'),
        Product(name='Mug 2', description='Elegant mug for your favorite beverage.', price=11.99, quantity=40, category=mugs, image_url='static/img/mug/mug_2.png'),
        Product(name='Mug 3', description='Classic mug with a unique design.', price=10.99, quantity=45, category=mugs, image_url='static/img/mug/mug_3.png'),
        Product(name='Mug 4', description='Large mug for a big coffee fix.', price=12.99, quantity=30, category=mugs, image_url='static/img/mug/mug_4.png'),
        Product(name='Mug 5', description='Perfect mug for any occasion.', price=9.49, quantity=55, category=mugs, image_url='static/img/mug/mug_5.png'),
        Product(name='Mug 6', description='Durable mug with a stylish design.', price=10.49, quantity=50, category=mugs, image_url='static/img/mug/mug_6.png'),

        # Notebooks
        Product(name='Notebook 1', description='Perfect notebook for jotting down notes.', price=9.99, quantity=60, category=notebooks, image_url='static/img/notebook/notebook_1.png'),
        Product(name='Notebook 2', description='Stylish notebook for daily use.', price=8.99, quantity=70, category=notebooks, image_url='static/img/notebook/notebook_2.png'),

        # Pins 
        Product(name='Pin 1', description='Unique pin for your collection.', price=2.99, quantity=200, category=pins, image_url='static/img/pin/pin_1.png'),
        Product(name='Pin 2', description='Decorative pin with a modern design.', price=3.49, quantity=180, category=pins, image_url='static/img/pin/pin_2.png'),
        Product(name='Pin 3', description='Classic pin with a stylish look.', price=2.49, quantity=220, category=pins, image_url='static/img/pin/pin_3.png'),

        # Stickers 
        Product(name='Sticker 1', description='High-quality sticker for your laptop or phone.', price=1.99, quantity=500, category=stickers, image_url='static/img/sticker/sticker_1.png'),
        Product(name='Sticker 2', description='Durable sticker with a unique design.', price=2.49, quantity=450, category=stickers, image_url='static/img/sticker/sticker_2.png'),

        # T-Shirts 
        Product(name='T-Shirt 1', description='Comfortable t-shirt with a modern design.', price=19.99, quantity=30, category=tshirts, image_url='static/img/t_shirt/t_shirt_1.png'),
        Product(name='T-Shirt 2', description='Classic t-shirt for everyday wear.', price=18.99, quantity=35, category=tshirts, image_url='static/img/t_shirt/t_shirt_2.png'),
        Product(name='T-Shirt 3', description='Stylish t-shirt with unique graphics.', price=20.99, quantity=25, category=tshirts, image_url='static/img/t_shirt/t_shirt_3.png'),
        Product(name='T-Shirt 4', description='Comfortable and durable t-shirt.', price=21.49, quantity=28, category=tshirts, image_url='static/img/t_shirt/t_shirt_4.png'),
        Product(name='T-Shirt 5', description='T-shirt with a trendy design.', price=22.99, quantity=22, category=tshirts, image_url='static/img/t_shirt/t_shirt_5.png'),
        Product(name='T-Shirt 6', description='Soft t-shirt for everyday comfort.', price=23.49, quantity=30, category=tshirts, image_url='static/img/t_shirt/t_shirt_6.png'),
        Product(name='T-Shirt 7', description='Graphic t-shirt with a modern look.', price=24.99, quantity=20, category=tshirts, image_url='static/img/t_shirt/t_shirt_7.png')
    ]

    db.session.add_all(products)
    db.session.commit()
    
    print('Products created')

def create_carts_and_items():
    user = User.query.filter_by(username='user').first()
    cart = Cart(user_id=user.id)
    db.session.add(cart)
    db.session.commit()
    
    print(f'Cart for user \'{user.name}\' created')
    
    product1 = Product.query.filter_by(name='Hoodie 1').first()
    product2 = Product.query.filter_by(name='Mug 1').first()
    
    cart_item1 = CartItem(cart_id=cart.id, product_id=product1.id, quantity=1)
    cart_item2 = CartItem(cart_id=cart.id, product_id=product2.id, quantity=2)
    
    db.session.add(cart_item1)
    db.session.add(cart_item2)
    db.session.commit()
    
    print(f'CartItem for product \'{product1.name}\' with quantity {cart_item1.quantity} created')
    print(f'CartItem for product \'{product2.name}\' with quantity {cart_item2.quantity} created')

def create_orders_and_items():
    user = User.query.filter_by(username='user').first()
    order = Order(user_id=user.id, total_amount=79.97, shipping_address='123 Street, City', billing_address='123 Street, City', status='completed')
    db.session.add(order)
    db.session.commit()
    
    print(f'Order for user \'{user.name}\' created')
    
    product1 = Product.query.filter_by(name='Hoodie 1').first()
    product2 = Product.query.filter_by(name='Mug 1').first()
    
    order_item1 = OrderItem(order_id=order.id, product_id=product1.id, quantity=1)
    order_item2 = OrderItem(order_id=order.id, product_id=product2.id, quantity=2)
    
    db.session.add(order_item1)
    db.session.add(order_item2)
    db.session.commit()
    
    print(f'OrderItem for product \'{product1.name}\' with quantity {order_item1.quantity} created')
    print(f'OrderItem for product \'{product2.name}\' with quantity {order_item2.quantity} created')

def create_reviews():
    user = User.query.filter_by(username='user').first()

    reviews = [
        # Caps Reviews
        Review(user_id=user.id, product_id=1, rating=5, comment='Great cap! Fits perfectly and looks stylish.'),
        Review(user_id=user.id, product_id=2, rating=4, comment='Nice cap, but could be a little bigger.'),

        # Hoodies Reviews
        Review(user_id=user.id, product_id=3, rating=5, comment='Absolutely love this hoodie! So comfortable.'),
        Review(user_id=user.id, product_id=4, rating=4, comment='Good quality, but the color faded a bit after washing.'),
        Review(user_id=user.id, product_id=5, rating=5, comment='Warm and cozy, perfect for cold weather.'),
        Review(user_id=user.id, product_id=6, rating=5, comment='Lightweight and breathable, great for spring.'),
        Review(user_id=user.id, product_id=7, rating=4, comment='Nice fit, but the sleeves are a little short.'),
        Review(user_id=user.id, product_id=8, rating=5, comment='Trendy design, got a lot of compliments!'),

        # Keychains Reviews
        Review(user_id=user.id, product_id=9, rating=5, comment='Durable and looks great on my keys.'),
        Review(user_id=user.id, product_id=10, rating=4, comment='Nice design, but a bit pricey for a keychain.'),
        Review(user_id=user.id, product_id=11, rating=5, comment='Perfect size, easy to find in my bag.'),
        Review(user_id=user.id, product_id=12, rating=5, comment='Unique design, really stands out.'),

        # Mousepads Reviews
        Review(user_id=user.id, product_id=13, rating=5, comment='Smooth surface, my mouse glides perfectly.'),
        Review(user_id=user.id, product_id=14, rating=4, comment='Good mousepad, but could be a little thicker.'),

        # Mugs Reviews
        Review(user_id=user.id, product_id=15, rating=5, comment='Great mug, perfect size for my morning coffee.'),
        Review(user_id=user.id, product_id=16, rating=4, comment='Elegant design, but a bit fragile.'),
        Review(user_id=user.id, product_id=17, rating=5, comment='Love the design, and it keeps my coffee warm.'),
        Review(user_id=user.id, product_id=18, rating=5, comment='Big enough for a large coffee, just what I needed.'),
        Review(user_id=user.id, product_id=19, rating=4, comment='Nice mug, but the handle is a bit small.'),
        Review(user_id=user.id, product_id=20, rating=5, comment='Stylish and durable, my favorite mug now.'),

        # Notebooks Reviews
        Review(user_id=user.id, product_id=21, rating=5, comment='Perfect notebook for notes, good paper quality.'),
        Review(user_id=user.id, product_id=22, rating=4, comment='Nice notebook, but the cover could be sturdier.'),

        # Pins Reviews
        Review(user_id=user.id, product_id=23, rating=5, comment='Cute pin, looks great on my backpack.'),
        Review(user_id=user.id, product_id=24, rating=4, comment='Good quality, but a bit expensive for a pin.'),
        Review(user_id=user.id, product_id=25, rating=5, comment='Unique design, really adds a nice touch.'),

        # Stickers Reviews
        Review(user_id=user.id, product_id=26, rating=5, comment='Great sticker, sticks well and looks cool.'),
        Review(user_id=user.id, product_id=27, rating=4, comment='Nice sticker, but it faded a bit in the sun.'),

        # T-Shirts Reviews
        Review(user_id=user.id, product_id=28, rating=5, comment='Comfortable t-shirt, fits perfectly.'),
        Review(user_id=user.id, product_id=29, rating=4, comment='Nice t-shirt, but the color faded after a few washes.'),
        Review(user_id=user.id, product_id=30, rating=5, comment='Great graphics, really stands out.'),
        Review(user_id=user.id, product_id=31, rating=4, comment='Good quality, but the sizing is a bit off.'),
        Review(user_id=user.id, product_id=32, rating=5, comment='Super comfortable, my new favorite t-shirt.'),
        Review(user_id=user.id, product_id=33, rating=5, comment='Love the design, and it fits well.'),
        Review(user_id=user.id, product_id=34, rating=4, comment='Nice t-shirt, but the fabric is a bit thin.')
    ]

    db.session.add_all(reviews)
    db.session.commit()
    
    print('Reviews created')

def create_all():
    create_roles()
    create_users()
    create_categories()
    create_products()
    create_carts_and_items()
    create_orders_and_items()
    create_reviews()
    
