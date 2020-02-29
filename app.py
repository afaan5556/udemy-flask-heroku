from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
import os

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') # tell app that the db lives in the root folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQL alchemy tracks every change regardless of saving to db by default which takes resrouces. This turns that off
app.secret_key = 'Bummiesjelly310'
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates /auth endpoint

api.add_resource(UserRegister, '/register')
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')

if __name__ == '__main__': # Make sure app is run when file is run but not if file is imported
	db.init_app(app)
	app.run(port=5000, debug=True)