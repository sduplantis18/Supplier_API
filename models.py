import os
from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_migrate import Migrate
import json

database_name = "seated"
database_path = f'postgresql://sdupl:Baller24@localhost:5432/{database_name}'

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
    id = db.Column(Integer, primary_key = True)
    name = db.Column(String)
    address = db.Column(String)
    restaurant = relationship('Restaurant', backref='restaurant', lazy=True)
    runner = relationship('Runner', backref='runner', lazy=True)

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

    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'adress': self.address,
        }

'''
Define Restaurant Class
'''
class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(Integer, primary_key = True)
    name = db.Column(String)
    address = db.Column(String)
    arena_id = db.Column(Integer, db.ForeignKey('arenas.id'), nullable = False)
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
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'adress': self.address,
            'arena_id':self.arena_id,
            'menu':self.menu,
            'customer':self.customer
            }
    
'''
Define menu class
'''

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(Integer, primary_key = True)
    restaurant_id = db.Column(Integer, db.ForeignKey('restaurants.id'), nullable = False)
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
    id = db.Column(Integer, primary_key = True)
    name = db.Column(String)
    menu_id = db.Column(Integer, db.ForeignKey('menus.id'), nullable = False)

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
    id = db.Column(Integer, primary_key = True)
    name = db.Column(String)
    phone_number = db.Column(String(15))
    restaurant_id = db.Column(Integer, db.ForeignKey('restaurants.id'), nullable = False)
    order = relationship('Order', backref='order_id', lazy = True)

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
    id = db.Column(Integer, primary_key = True)
    arena_id = db.Column(Integer, db.ForeignKey('arenas.id'), nullable = False)
    shipment = relationship('Shipment', backref='shipment_id', lazy = True)

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
    id = db.Column(Integer, primary_key=True)
    order_date = db.Column(DateTime)
    order_type = db.Column(String)
    customer_id = db.Column(Integer, db.ForeignKey('customers.id'), nullable = False)
    restaurant_id = db.Column(Integer, db.ForeignKey('restaurants.id'), nullable =False)
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
    id = db.Column(Integer, primary_key = True)
    shipment_date = db.Column(DateTime)
    order_id = db.Column(Integer, db.ForeignKey('orders.id'), nullable = False)
    runner_id = db.Column(Integer, db.ForeignKey('runners.id'), nullable = False)

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




