from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
        
    @classmethod
    def create(cls,data):
        query = """
                insert into users (first_name,last_name,email,password)
                values (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_by_email(cls,data):
        query = """
                select * from users
                where email =%(email)s;
                """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)< 1 :
            return []
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = """
                select * from users
                where id =%(id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)< 1 :
            return []
        return cls(results[0])
    
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash("First Name must be at  least 2 characters !","reg")
            is_valid = False
        
        if len(data['last_name']) < 2:
            flash("Last Name must be at  least 2 characters !" ,"reg")
            is_valid = False
        if len(data['email']) < 1:
            flash("Email is required !","reg")
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!" ,"reg")
            is_valid = False
        else:
            email_dic = {
                'email' : data['email']
            }
            potential_user = User.get_by_email(email_dic)
            if potential_user:
                flash("Email is already taken, hopefully by you !" ,"reg")
                is_valid = False
        if len (data["password"]) <8 :
            flash("Password must be at  least 8 characters !" ,"reg")
            is_valid = False
        elif not data["password"] == data["confirm_password"]:
            flash("Passwords don't match !" ,"reg")
            is_valid = False
            
        
        return is_valid
    
