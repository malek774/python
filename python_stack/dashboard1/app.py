from flask import Flask, render_template

app = Flask(__name__)

# Sample admin data
admins = [
    {"id": 1, "name": "Admin 1", "email": "admin1@example.com"},
    {"id": 2, "name": "Admin 2", "email": "admin2@example.com"},
    {"id": 3, "name": "Admin 3", "email": "admin3@example.com"},
    {"id": 4, "name": "Admin 4", "email": "admin4@example.com"},
    {"id": 5, "name": "Admin 5", "email": "admin5@example.com"},
]

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/users')
def render_users():
    return render_template('users.html')

@app.route('/admins')
def render_admins():
    return render_template('admins.html')

@app.route('/book_list')
def book_list():
    return render_template('book_list.html')

if __name__ == '__main__':
    app.run(debug=True)