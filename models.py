import os
from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "suppliers"
database_path = f'postgresql://sdupl:Baller24@localhost:5432/{database_name}'

db = SQLAlchemy()

#bind the flask app to a SQLAlchmey service
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"]=database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Define arena class
'''
class Arena(db.Model):
    __tablename__ = 'arenas'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    address = Column(String)

'''
Define Restaurant Class
'''
class Restuarant(db.Model):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    address = Column(String)

'''
Define menu class
'''
class Menu(db.Model):
    __tablename__ = 'menus'
    id = Column(Integer, primary_key = True)

'''
Define menu item class
'''
class Menu_Item(db.Model):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key = True)
    name = Column(String)

'''
Define Customer class
'''
class Customer(db.Model):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    phone_number = Column(String(15))

'''
Define runner class
'''
class Runner(db.Model):
    __tablename__ = 'runners'
    id = Column(Integer, primary_key = True)

'''
Define Order class
'''
class Order(db.Model):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime)
    order_type = Column(String)

'''
Define shipment class
'''
class Shipment(db.Model):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key = True)
    shipment_date = Column(DateTime)




