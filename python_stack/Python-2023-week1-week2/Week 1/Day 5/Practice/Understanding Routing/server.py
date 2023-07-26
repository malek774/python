from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def hello_dojo():
    return 'Dojo!'

@app.route('/say/<whatever>')
def function1(whatever):
    return 'Hi ' + whatever

@app.route('/repeat/<int:times>/<word>')
def repeat(times,word):
    return (word + ' ') * times


# @app.route('/repeat/<int:times>/<word>')
# def repeat2(times,word):
#         for i in range(times):
#             return (word + ' ')

    

if __name__ == "__main__":
    app.run(debug=True)
