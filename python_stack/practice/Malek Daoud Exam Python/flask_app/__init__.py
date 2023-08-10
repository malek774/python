from flask import Flask, session, redirect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = "the_key_of_happiness_is_having_dreams"