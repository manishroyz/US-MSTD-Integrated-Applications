from flask import Flask

# Flask app name used by the my_app.py
app = Flask(__name__)

from app import routes