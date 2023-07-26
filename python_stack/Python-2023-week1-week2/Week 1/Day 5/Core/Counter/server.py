from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    if 'counter' in session:
        session['counter'] += 0
    else:
        session['counter'] = 0
    return render_template('index.html', counter=session['counter'])

@app.route('/increment', methods=['POST'])
def increment():
    session['counter'] += 2
    return redirect(url_for('home'))

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
