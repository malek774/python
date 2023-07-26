from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'secret_key'  # Set a secret key for session

def generate_random_number():
    return random.randint(1, 100)

def reset_game():
    session['random_number'] = generate_random_number()
    session['attempts'] = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'random_number' not in session:
        reset_game()
    
    if request.method == 'POST':
        guess = int(request.form['guess'])
        attempts = session['attempts']
        random_number = session['random_number']
        
        if guess < random_number:
            message = 'Too low!'
            attempts += 1
        elif guess > random_number:
            message = 'Too high!'
            attempts += 1
        else:
            message = f'Congratulations! You guessed it right in {attempts+1} attempts!'
            reset_game()
        
        session['attempts'] = attempts
        return render_template('index.html', message=message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
