import os
from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import json

database_name = "suppliers"
database_path = f'postgresql://sdupl:#####@localhost:5432/{database_name}'

db = SQLAlchemy()

#bind the flask app to a SQLAlchmey service
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"]=database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

#method to wipe the db and start fresh
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

'''
Define arena class
'''
class Arena(db.Model):
    __tablename__ = 'arenas'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    address = Column(String)
    restaurant = relationship('Restaurant', backref='arena', lazy=True)
    runner = relationship('Runner', backref='runner', Lazy=True)

    #inserts a new model into the db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    #deletes model form db (if the model exists)
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #updates a model in the db
    def update(self):
        db.session.update(self)
        db.session.commit()

'''
Define Restaurant Class
'''
class Restuarant(db.Model):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    address = Column(String)
    arena_id = Column(Integer, ForeignKey('Arena.id'), nullable = False)
    menu = relationship('Menu', backref='menu', lazy = True)
    customer = relationship('Customer', backref='customer', lazy = True)
    order = relationship('Order', backref='order', lazy = True)

    #inserts a new model into the db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    #deletes model form db (if the model exists)
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #updates a model in the db
    def update(self):
        db.session.update(self)
        db.session.commit()
    
'''
Define menu class
'''
class Menu(db.Model):
    __tablename__ = 'menus'
    id = Column(Integer, primary_key = True)
    restaurant_id = Column(Integer, ForeignKey('Restuarant.id') nullable = False)
    menu_item = relationship('Menu_Item', backref='menu_item', lazy = True)

    #inserts a new model into the db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    #deletes model form db (if the model exists)
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #updates a model in the db
    def update(self):
        db.session.update(self)
        db.session.commit()

'''
Define menu item class
'''
class Menu_Item(db.Model):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    menu_id = Column(Integer, ForeignKey('Menu.id') nullable = False)

    #inserts a new model into the db
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    #deletes model form db (if the model exists)
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #updates a model in the db
    def update(self):
        db.session.update(self)
        db.session.commit()

'''
Define Customer class
'''
class Customer(db.Model):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    phone_number = Column(String(15))
    restaurant_id = Column(Integer, ForeignKey('Restuarant.id') nullable = False)
    order = relationship('Order', backref='order', lazy = True)

    #inserts a new model into the db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    #deletes model form db (if the model exists)
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #updates a model in the db
    def update(self):
        db.session.update(self)
        db.session.commit()

'''
Define runner class
'''
class Runner(db.Model):
    __tablename__ = 'runners'
    id = Column(Integer, primary_key = True)
    arena_id = Column(Integer, ForeignKey('Arena.id'), nullable = False)
    shipment = relationship('Shipment', backref='shipment', lazy = True)

    #inserts a new model into the db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    #deletes model form db (if the model exists)
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #updates a model in the db
    def update(self):
        db.session.update(self)
        db.session.commit()

'''
Define Order class
'''
class Order(db.Model):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime)
    order_type = Column(String)
    customer_id = Column(Integer, ForeignKey('Customer.id') nullable = False)
    restaurant_id = Column(Integer, ForiegnKey('Restaurant.id') nullable =False)
    shipment = relationship('Shipment', backref='shipment', lazy = True)

    #inserts a new model into the db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    #deletes model form db (if the model exists)
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #updates a model in the db
    def update(self):
        db.session.update(self)
        db.session.commit()

'''
Define shipment class
'''
class Shipment(db.Model):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key = True)
    shipment_date = Column(DateTime)
    order_id = Column(Integer, ForeignKey('Order.id') nullable = False)
    runner_id = Column(Integer, ForeignKey('Runner.id') nullable = False)

    #inserts a new model into the db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    #deletes model form db (if the model exists)
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #updates a model in the db
    def update(self):
        db.session.update(self)
        db.session.commit()




