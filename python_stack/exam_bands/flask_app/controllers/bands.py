from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.band import Band

@app.route('/bands/new')
def new_band():
    if 'user_id' in session:
        return render_template("new_band.html")
    return redirect('/')



@app.route('/bands/create', methods=['POST'])
def create_band():
    print("REQUEST FORM********",request.form)
    if(Band.validate(request.form)):
        data = {
            **request.form,'user_id':session['user_id']
        }
        Band.add_band(data)
        return redirect('/dashboard')
    return redirect('/bands/new')

@app.route('/bands/<band_id>/destroy')
def delete_band(band_id):
    if 'user_id' in session:
        Band.delete({'id':band_id})
    return redirect('/dashboard')

@app.route('/bands/<band_id>/edit')
def edit_band(band_id):
    if 'user_id' in session:
        one_band=Band.get_by_id({'id':band_id})
        return render_template("edit_band.html", band=one_band)
    return redirect('/')

@app.route('/bands/edit', methods=['POST'])
def update():
    if(Band.validate(request.form)):
        print(request.form)
        Band.update_band(request.form)
        return redirect('/dashboard')
    return redirect('/bands/'+str(request.form['id'])+'/edit')


#::::::::::::::::::::::::::#


@app.route('/bands/<int:band_id>')
def one_band(band_id):
    if 'user_id' in session:
        user = User.get_by_id({'id':session['user_id']})
        one_band= Band.get_by_id({'id':band_id})
        return render_template('one.html',band=one_band,user=user)
    return redirect('/')

@app.route('/my_bands')
def my_bands():
    if 'user_id' in session:
        user = User.get_by_id({'id':session['user_id']})
        bands = Band.get_all_by_user_id({'user_id': session['user_id']})
        return render_template('one.html', bands = bands, user = user)
    return redirect('/')



