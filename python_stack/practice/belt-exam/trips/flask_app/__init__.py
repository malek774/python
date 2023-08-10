# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "THE_KEY_TO_HAPPINESS_IS_HAVING_DREAMS"
DATABASE = "trips_db"