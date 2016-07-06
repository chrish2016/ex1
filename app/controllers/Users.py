from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Message')
        self.load_model('Friend')
        self.db = self._app.db

    def index(self):
        users = self.models['User'].fetch_all_users(session['user']['id'])
        return self.load_view('/users/index.html', users=users)

    def logout(self):
        session.clear()
        return redirect('/')

    def edit(self, id):
        user = self.models['User'].fetch_user_by_id(id)
        print "Edit method in Users Controller received {}".format(user)
        return self.load_view('users/edit.html', user=user)

    def delete(self, id):
        result = self.models['User'].delete_user_by_id(id)
        return redirect('/users')

    def show(self, id):
        user = self.models['User'].fetch_user_by_id(id)
        messages = self.models['Message'].fetch_messages_by_user_id(id)
        friends = self.models['Friend'].fetch_all_friends(id)
        return self.load_view('users/show.html', user=user, friends=friends, messages=messages)

    def remove(self, id):
        result = self.models['User'].remove_friend_by_id(id)
        return redirect('/users')

    def add(self, id):
        friend = self.models['Friend'].add_friend_by_id(id)
        return redirect('/users', friend=friend)


"""
        self.models['WelcomeModel'].add_message()
        messages = self.models['WelcomeModel'].grab_messages()
        user = self.models['WelcomeModel'].get_user()
        return self.load_view('index.html', messages=messages, user=user)
        """
