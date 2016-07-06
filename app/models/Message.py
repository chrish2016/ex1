from system.core.model import Model

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()
        self.queries = {
            'create_message': "INSERT INTO messages (user_id, author_id, message, created_at, updated_at) values (:user_id, :author_id, :message, NOW(), NOW())",
            'fetch_messages_by_user_id': "SELECT * FROM messages WHERE user_id = :id"
        }

    def create_message(self, form_data, author_id):
        query = self.queries['create_message']
        data = {
            'user_id' : form_data['user_id'],
            'author_id' : author_id,
            'message' : form_data['message']
        }
        result = self.db.query_db(query, data)
        return result

    def fetch_messages_by_user_id(self, id):
        query = self.queries['fetch_messages_by_user_id']
        data = {
            'id' : id
        }
        result = self.db.query_db(query, data)
        return result



    # def grab_messages(self, id):
    #     query = "SELECT * from messages where users_id = :user_id"
    #     data = {'user_id':1}
    #     return self.db.query_db(query, data)
