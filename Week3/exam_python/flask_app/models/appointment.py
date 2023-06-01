from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE


class Appointment:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id'] #! Must Have
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def create_appointment(cls, data):
        query = """
            INSERT INTO appointments (user_id,task, date, status)
            VALUES (%(user_id)s,%(task)s,%(date)s,%(status)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # - GET ALL
    # @classmethod
    # def get_all_parties(cls):
    #     query = """
    #         SELECT * FROM partie LEFT JOIN users ON partie.user_id = users.id;; 
    #     """
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     print(results)
    #     parties = []
    #     for row in results:
    #         party = cls(row)
    #         party.poster = f"{row['first_name']} {row['last_name']}"
    #         parties.append(party)
    #     return parties
    
    
    @classmethod
    def get_by_id(cls,data):
        query = """
                select * from appointments
                where id =%(id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)< 1 :
            return []
        return cls(results[0])
    
    @classmethod
    def get_user_appointments(cls,data):
        query = """
                select * from appointments
                where user_id =%(user_id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query,data)
        appointments = []
        for row in results:
            appointment = cls(row)
            appointments.append(appointment)
        return appointments
    
    @classmethod
    def update_appointment(cls, data):
        query = """
            UPDATE appointments SET task =%(task)s,date =%(date)s,status =%(status)s
            WHERE id = %(id)s ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def delete_appointment(cls, data):
        query = """
           delete from appointments where id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    
    @staticmethod
    def validate_appointment(data):
        is_valid = True
        if len(data['task']) < 6:
            flash("Task must be at  least 6 characters !")
            is_valid = False
        if data['date'] == "":
            is_valid = False
            flash("Date is required")
            
        
        return is_valid