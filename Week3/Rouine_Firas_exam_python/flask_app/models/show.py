from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash
from flask_app import DATABASE


class Show:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id'] 
        self.title = data['title']
        self.network = data['network']
        self.date = data['date']
        self.description = data['description']
        self.poster_fn= user.User.get_by_id({'id':self.user_id}).first_name
        self.poster_ln= user.User.get_by_id({'id':self.user_id}).last_name
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def create_show(cls, data):
        query = """
            INSERT INTO shows (user_id,title,network,date,description)
            VALUES (%(user_id)s,%(title)s,%(network)s,%(date)s,%(description)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
        # - GET ALL
    @classmethod
    def get_all_shows(cls):
        query = """
            SELECT * FROM shows LEFT JOIN users ON shows.user_id = users.id;; 
        """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        shows = []
        for row in results:
            show = cls(row)
            show.poster = f"{row['first_name']} {row['last_name']}"
            shows.append(show)
        return shows
    @classmethod
    def get_by_id(cls,data):
        query = """
                select * from shows
                where id =%(id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)< 1 :
            return []
        return cls(results[0])
    

    
    @classmethod
    def update_show(cls, data):
        query = """
            UPDATE shows SET title =%(title)s,network =%(network)s,date =%(date)s,description =%(description)s
            WHERE id = %(id)s ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def delete_show(cls, data):
        query = """
           delete from shows where id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    
    @staticmethod
    def validate_show(data):
        is_valid = True
        if len(data['title']) < 3:
            flash("Title must be at  least 3 characters !")
            is_valid = False
        if len(data['network']) < 3:
            flash("Network must be at  least 3 characters !")
            is_valid = False
        if data['date'] == "":
            is_valid = False
            flash("Date is required")
        if len(data['description']) < 3:
            flash("Description must be at  least 3 characters !")
            is_valid = False       

        return is_valid