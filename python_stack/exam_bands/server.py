from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import bands


if __name__ == '__main__':
    app.run(debug =True)