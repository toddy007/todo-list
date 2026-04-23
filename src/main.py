from flask import Flask
from tinydb import TinyDB
from utils.load_routes import load_routes

app = Flask(__name__)
db = TinyDB('src/database/database.json', create_dirs=True)

load_routes(app, db)

app.run(debug=True, port=8080)