from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user
class Book:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.author = data['author']
        self.thought = data['thought']
        self.owner = user.User.get_by_id({'id':self.user_id}).name
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_book(cls,data):
        query= """INSERT INTO books (title,user_id, author, thought) 
        VALUES (%(title)s,%(user_id)s,%(author)s,%(thought)s);
        """
        result=connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        return result
    @classmethod
    def get_all(cls):
        query=""" SELECT * FROM books;
        """
        results =  connectToMySQL(DATABASE).query_db(query)
        all_rec=[]
        for row in results:
            all_rec.append(cls(row))
        return all_rec
    @classmethod
    def get_by_id(cls,data):
            query=""" SELECT * FROM books WHERE id =%(id)s
            """
            result = connectToMySQL(DATABASE).query_db(query,data)
            if (result):
                return cls(result[0])
    @classmethod
    def edit_book(cls,data):
        query="""UPDATE books
                SET title=%(title)s,author=%(author)s,thought=%(thought)s
                WHERE id = %(id)s;
        """
        return  connectToMySQL(DATABASE).query_db(query,data)
    # @classmethod
    # def remove(cls,data):
    #     query="""DELETE FROM recipes WHERE id=%(id)s
    #     """
    #     return  connectToMySQL(DATABASE).query_db(query,data)


    # * validation
    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['title'])<2:
            flash("Invalid  title!")
            is_valid=False
        if len(data['author'])<2:
            flash("Invalid author!")
            is_valid=False
        if len(data['thought'])<2:
            flash("Invalid thought!")
            is_valid=False

        return is_valid


