import hydra

from dash import Dash, html, dcc
from flask import Flask
from omegaconf import DictConfig
from flask_login import LoginManager
from models.UserModel import User
from callbacks.callback_loader import load_callbacks


@hydra.main(config_path="./configurations", config_name="base", version_base=None)
def main(args: DictConfig):

    scripts = [
        "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
        "https://www.googletagmanager.com/gtag/js?id=G-4PJELX1C4W",
        "https://media.ethicalads.io/media/client/ethicalads.min.js",
        # "https://unpkg.com/dash.nprogress@latest/dist/dash.nprogress.js"
    ]

    server = Flask(__name__)

    app = Dash(
        __name__,
        suppress_callback_exceptions=True,
        external_scripts=scripts,
        title=args.APP_NAME,
        update_title="...",
        server=server,
        # use_pages=True
    )

    server.config.update(SECRET_KEY=args.APP_SECRET)

    login_manager = LoginManager()
    login_manager.init_app(server)
    login_manager.login_view = "/login"

    # Chargement des callbacks de l'application
    load_callbacks(app, args)

    @login_manager.user_loader
    def load_user(username):
        """This function loads the user by user id. Typically this looks up the user from a user database.
        We won't be registering or looking up users in this example, since we'll just login using LDAP server.
        So we'll simply return a User object with the passed in username.
        """
        return User(username)

    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

    # run the app
    app.run(debug=True)


if __name__ == "__main__":
    main()
