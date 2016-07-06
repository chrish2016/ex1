from system.core.model import Model
import re

EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

class Friend(Model):
    def __init__(self):
        super(Friend, self).__init__()
        self.queries = {
            'create_user' : "INSERT INTO users (first_name, last_name, alias, email, pw_hash, created_at, updated_at) VALUES( :first_name, :last_name, :alias, :email, :password, NOW(), NOW())",
            'get_user' : "SELECT id, first_name, last_name, alias, email, friends, admin, created_at, updated_at FROM users WHERE id = :id",
            'get_user_by_email' : "SELECT * FROM users WHERE email = :email LIMIT 1",
            'fetch_all_users' : "SELECT id, first_name, last_name, alias, email, friends, admin, created_at, updated_at FROM users WHERE id != :id",
            'fetch_user_by_id' : "SELECT id, first_name, last_name, alias, email, friends, admin, created_at, updated_at FROM users WHERE id = :id",
            'update_user' : "UPDATE users SET first_name=:first_name, last_name=:last_name, alias=:alias, email=:email, pw_hash=:password WHERE id = :id",
            'delete_user' : "DELETE FROM users WHERE id = :id",
            'fetch_all_friends' :  "SELECT id, friend, created_at, updated_at FROM friends WHERE id != :id",
            'add_friend_by_id' : "INSERT INTO friends (friend) VALUES(:friend)"
        }
    def add_friend_by_id(self, id):
        query = self.queries['add_friend_by_id']
        data = {
            'id': id,
            'friend': friend
        }
        result = self.db.query_db(query, data)
        return result

    def fetch_all_friends(self, id):
        query = self.queries['fetch_all_friends']
        data = {
            'id': id
        }
        result = self.db.query_db(query, data)
        return result
    """
    Below is an example of a model method that queries the database for all users in a fictitious application

    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True

    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
