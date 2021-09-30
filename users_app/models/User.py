
from users_app.config.MySQLConnection import connectToMySQL
from users_app.models import User

class User:
    def __init__( self, first_name, last_name, email,created_at,updated_at):
        self.first_name = first_name
        self.last_name = last_name
        self.email= email
        self.created_at=created_at
        self.updated_at=updated_at
        
        
      
        


    @classmethod
    def get_all_users( cls ):
        query = "SELECT * FROM users;"
     
        
        results = connectToMySQL( "users" ).query_db( query )
        users = []
        for user in results:
            users.append( User( user['first_name'], user['last_name'], user['email'],user['created_at'],user['updated_at']))
        return users
    
    @classmethod
    def add_user( cls, newUser ):
        query = "INSERT INTO users(first_name,last_name,email,updated_at,created_at) VALUES(%(first_name)s, %(last_name)s,%(email)s,now(),now());"
        data = {
            "first_name" : newUser.first_name,
            "last_name" : newUser.last_name,
            "email": newUser.email,
            "created_at":newUser.created_at,
            "updated_at": newUser.updated_at
                }
        print(1)
        result = connectToMySQL( 'users' ).query_db( query, data )
        print(2)
        return result  