from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def register(self):
        validation_result = self.models['WelcomeModel'].validate_reg_info(request.form)
        print validation_result
        if type(validation_result) == list:
            session['val_errors'] = validation_result
        if 'val_errors' in session:
            for error in session['val_errors']:
                flash(error)
            session.pop('val_errors')# clears flash messages
            return redirect('/')
        self.set_user_session(validation_result)
        return redirect('/users')

    def login(self):
        login_result = self.models['WelcomeModel'].login_user(request.form)
        print login_result
        if type(login_result) == list:
            session['login_errors'] = login_result
        if 'login_errors' in session:
            for error in session['login_errors']:
                flash(error)
            session.pop('login_errors')# clears flash messages
            return redirect('/')
        self.set_user_session(login_result)
        return redirect('/users')

    def set_user_session(self, validation_result):
        session['user'] = validation_result
        return

"""
        self.models['WelcomeModel'].add_message()
        messages = self.models['WelcomeModel'].grab_messages()
        user = self.models['WelcomeModel'].get_user()
        return self.load_view('index.html', messages=messages, user=user)
        """
