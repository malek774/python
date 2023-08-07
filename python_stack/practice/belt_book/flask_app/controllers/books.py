from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.book import Book


@app.route('/books/new')
def new_book():
    return render_template('new_book.html',)
@app.route('/books/create',methods=['POST'])
def add_book():
    if(Book.validate(request.form)):
        data={
            **request.form,
            'user_id':session['user_id']
        }
        Book.create_book(data)
        return redirect('/books')
    return redirect('/books/new')
@app.route('/books/<int:book_id>')
def show(book_id):
    book=Book.get_by_id({'id':book_id})
    return render_template('show_one.html',book=book)
@app.route('/books/<int:book_id>/edit')
def edit(book_id):
    book=Book.get_by_id({'id':book_id})
    return render_template('edit.html',book=book)

@app.route('/books/<int:book_id>/update',methods=['POST'])
def edit_book(book_id):
    if(Book.validate(request.form)):
        aaa = Book.edit_book(request.form)
        
        print(aaa)
        return redirect('/books')
    return redirect('/books/'+str(book_id)+'/edit')
