from dash import Output, Input, State
from flask_login import login_user
from callbacks.base import BaseCallback
from models.UserModel import User

from layouts.auth.auth_loader import AuthLoader


class AuthCallback(BaseCallback):
    def __init__(self, app, args) -> None:
        super().__init__(app, args)
        self.auth_loader = AuthLoader()

    def register_callback(self):
        @self.app.callback(
            Output('url', 'pathname'),
            Input('login-button', 'n_clicks'),
            [
                State('input-username', 'value'),
                State('input-password', 'value')
            ]
        )
        def render_auth_callback(n_clicks, username: str, password: str):
            if n_clicks is not None and n_clicks > 0 and self.auth_loader.authenticate(username, password):
                login_user(User(username))
                return '/application'
            return '/'
