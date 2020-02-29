from app import app
from db import db

db.init_app(app)

@app.before_first_request # Run method below once before the first request into this app
def create_tables():
	db.create_all() # Creates the 'sqlite:///data.db' with all tables in it