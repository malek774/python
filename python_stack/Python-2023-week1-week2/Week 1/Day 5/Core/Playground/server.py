from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/play')
def init_box():
    return render_template('index.html')

@app.route('/play/<int:times>')
def times_box(times):
    return render_template('index.html' , times = times)

@app.route('/play/<int:times>/<color>')
def color_box(times,color):
    return render_template('index.html' , times = times, color=color)

if __name__ == "__main__":
    app.run(debug=True)
