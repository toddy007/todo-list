from flask import Flask
from utils.load_routes import load_routes

app = Flask(__name__)

load_routes(app)

app.run(debug=True, port=8080)