from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.trips import Trip

@app.route('/trips/new')
def new_trip():
    if 'user_id' in session:
        return render_template("new_trip.html")
    return redirect('/')

@app.route('/trips/create', methods=['POST'])
def create_trip():
    if(Trip.validate(request.form)):
        data = {
            **request.form,'user_id':session['user_id']
        }
        Trip.add_trip(data)
        return redirect('/dashboard')
    return redirect('/trips/new')

@app.route('/trips/<trip_id>/destroy')
def delete_trip(trip_id):
    if 'user_id' in session:
        Trip.delete({'id':trip_id})
    return redirect('/dashboard')

@app.route('/trips/<trip_id>/edit')
def edit_trip(trip_id):
    if 'user_id' in session:
        one_trip=Trip.get_by_id({'id':trip_id})
        return render_template("edit_trip.html", trip=one_trip)
    return redirect('/')

@app.route('/trips/edit', methods=['POST'])
def update():
    if(Trip.validate(request.form)):
        print(request.form)
        Trip.update_trip(request.form)
        return redirect('/dashboard')
    return redirect('/trips/'+str(request.form['id'])+'/edit')


#::::::::::::::::::::::::::#


@app.route('/trips/<int:trip_id>')
def one_trip(trip_id):
    if 'user_id' in session:
        user = User.get_by_id({'id':session['user_id']})
        one_trip= Trip.get_by_id({'id':trip_id})
        return render_template('one.html',trip=one_trip,user=user)
    return redirect('/')



