from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models.user import User

class Band :
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.bandname = data['bandname']
        self.musicgenre = data['musicgenre']
        self.homecity = data['homecity']
        self.poster = ""

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM bands;
                """
        results = connectToMySQL(DATABASE).query_db(query)
        band = []
        for row in results:
            band.append(cls(row))
        return band

    @classmethod
    def get_all_by_user_id(cls, data):
        query = """
                SELECT * FROM bands WHERE user_id = %(user_id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query,data)
        band = []
        for row in results:
            band.append(cls(row))
        return band
    
    @classmethod
    def add_band(cls, data):
        query = """
        INSERT INTO bands (user_id, bandname, musicgenre,homecity) 
        VALUES (%(user_id)s,%(bandname)s,%(musicgenre)s, %(homecity)s);
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        print("QUERY RESULT",result)
        return result
    
    @classmethod
    def update_band(cls,data):
        query="""UPDATE bands SET bandname = %(bandname)s,
        musicgenre=%(musicgenre)s, homecity=%(homecity)s
        WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete(cls, data):
        query = """
        delete from bands where id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def edit_band(cls, data):
        query = """UPDATE bands SET name = %(bandname)s, musicgenre  = %(musicgenre )s, homecity = %(homecity )s 
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM bands WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['bandname'])< 2:
            flash("Band Name must be at least 3")
            is_valid = False
        if len(data['musicgenre'])< 10:
            flash("Music Genre too short")
            is_valid = False
        if len(data["homecity"]) < 2:
            flash("Home City must be at least 3")
            is_valid = False
        return is_valid 