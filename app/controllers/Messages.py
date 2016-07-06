from system.core.controller import *
import re

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)
        self.load_model('Message')
        self.db = self._app.db

    def create(self):
        self.models['Message'].create_message(request.form, session['user']['id'])
        return redirect('/users'.format(request.form['user_id']))

"""
        self.models['WelcomeModel'].add_message()
        messages = self.models['WelcomeModel'].grab_messages()
        user = self.models['WelcomeModel'].get_user()
        return self.load_view('index.html', messages=messages, user=user)
        """
