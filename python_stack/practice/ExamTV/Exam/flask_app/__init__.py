from flask import Flask
from flask_bcrypt import bcrypt

app = Flask(__name__)
app.secret_key = "the_key_of_h"