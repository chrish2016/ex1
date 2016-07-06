from system.core.controller import *

class Friends(Controller):
    def __init__(self, action):
        super(Friends, self).__init__(action)
        self.load_model('User')
        self.load_model('Message')
        self.load_model('Friend')
        self.db = self._app.db

    def remove(self, id):
        result = self.models['Friend'].remove_friend_by_id(id)
        return redirect('/users')

    def add(self, id):
        result = self.models['Friend'].add_friend_by_id(session['user']['id'])
        return redirect('/users/show')


"""
        self.models['WelcomeModel'].add_message()
        messages = self.models['WelcomeModel'].grab_messages()
        user = self.models['WelcomeModel'].get_user()
        return self.load_view('index.html', messages=messages, user=user)
        """
