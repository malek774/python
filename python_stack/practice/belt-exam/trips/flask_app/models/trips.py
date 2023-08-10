from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models.user import User

class Trip :
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.destination = data['destination']
        self.start_date = data['start_date']
        self.end_date = data['end_date']
        self.plan = data['plan']
        self.poster = ""

    @classmethod
    def get_all(cls, data):
        query = """
        SELECT * FROM trips WHERE user_id = %(user_id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        trip = []
        for row in results:
            trip.append(cls(row))
        return trip

    @classmethod
    def add_trip(cls, data):
        query = """
        INSERT INTO trips (user_id, name, destination,start_date,end_date,plan) 
        VALUES (%(user_id)s,%(name)s,%(destination)s,%(start_date)s,%(end_date)s,%(plan)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update_trip(cls,data):
        query="""UPDATE trips SET name = %(name)s,
        destination=%(destination)s, start_date=%(start_date)s,end_date=%(end_date)s,plan=%(plan)s
        WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete(cls, data):
        query = """
        delete from trips where id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    # @classmethod
    # def edit_trip(cls, data):
    #     query = """UPDATE trips SET name = %(name)s, destination  = %(description )s, start_date = %(start_date )s , end_date = %(end_date)s, plan= %(plan)s
    #     WHERE id = %(id)s;
    #     """
    #     return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM trips WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name'])< 2:
            flash("Name must be at least 3", "edit")
            is_valid = False
        if len(data['destination'])< 10:
            flash("destination too short", "edit")
            is_valid = False
        if len(data['start_date'])== "":
            flash("Start Date is required", "edit")
            is_valid = False
        if data["end_date"] == "":
            flash("End Date is required", "edit")
            is_valid = False
        if len(data["plan"]) < 2:
            flash("Plan must be at least 3", "edit")
            is_valid = False
        return is_valid