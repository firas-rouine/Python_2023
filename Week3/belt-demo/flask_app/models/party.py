from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models import user_model


class Party:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id'] #! Must Have
        self.title = data['title']
        self.location = data['location']
        self.description = data['description']
        self.date = data['date']
        self.all_ages = data['all_ages']
        self.user_fn = user_model.User.get_by_id({'id':self.user_id}).first_name 
        self.user_ln= user_model.User.get_by_id({'id':self.user_id}).last_name 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    def __repr__(self) -> str:
        return  self.first_name
    # - CREAT
    @classmethod
    def create_party(cls, data):
        query = """
            INSERT INTO partie (user_id,title, location, date, all_ages, description)
            VALUES (%(user_id)s,%(title)s,%(location)s,%(date)s,%(all_ages)s,%(description)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # - GET ALL
    @classmethod
    def get_all_parties(cls):
        query = """
            SELECT * FROM partie LEFT JOIN users ON partie.user_id = users.id;; 
        """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        parties = []
        for row in results:
            party = cls(row)
            party.poster = f"{row['first_name']} {row['last_name']}"
            parties.append(party)
        return parties
    
    
    @classmethod
    def get_by_id(cls,data):
        query = """
                select * from partie
                where id =%(id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)< 1 :
            return []
        return cls(results[0])
    
    @classmethod
    def get_user_parties(cls,data):
        query = """
                select * from partie
                where user_id =%(user_id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query,data)
        parties = []
        for row in results:
            party = cls(row)
            parties.append(party)
        return parties
    
    @classmethod
    def update_party(cls, data):
        query = """
            UPDATE partie SET title =%(title)s,location =%(location)s,date =%(date)s,all_ages =%(all_ages)s,
            description =%(description)s
            WHERE id = %(id)s ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def delete_party(cls, data):
        query = """
           delete from partie where id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    
    @staticmethod
    def validate_party(data):
        is_valid = True
        if len(data['title']) < 2:
            flash("Title must be at  least 2 characters !")
            is_valid = False
        
        if len(data['location']) < 2:
            flash("Location must be at  least 2 characters !" )
            is_valid = False
        if len(data['description'])<6:
            is_valid = False
            flash("Description greater than 6")
        if data['date'] == "":
            is_valid = False
            flash("Date is required")
            
        
        return is_valid