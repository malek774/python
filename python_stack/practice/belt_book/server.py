from flask_app import app
# ! DON'T Forget to import ALL Controllers Here
from flask_app.controllers import users,books

if __name__ == '__main__':
    app.run(debug =True)