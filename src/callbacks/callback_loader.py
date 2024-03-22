from callbacks.layout_callback import LayoutCallback
from callbacks.auth_callback import AuthCallback
from callbacks.parametre_callback import ParametreCallback


def load_callbacks(app, args) -> None:
    """
    La fonction qui doit chager tous les callbacks de l'application.
    """

    LayoutCallback(app, args).register_callback()
    AuthCallback(app, args).register_callback()
    ParametreCallback(app, args).register_callback()
