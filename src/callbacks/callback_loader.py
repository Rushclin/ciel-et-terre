from callbacks.layout_callback import LayoutCallback
from callbacks.auth_callback import AuthCallback
from callbacks.parametre_callback import ParametreCallback
from callbacks.sauvegarde_callback import SauvegardeCallback


def load_callbacks(app, args) -> None:
    """
    La fonction qui doit chager tous les callbacks de l'application.
    """

    LayoutCallback(app, args).register_callback()
    AuthCallback(app, args).register_callback()
    ParametreCallback(app, args).register_callback()
    
    # Je register tous les callbacks pour actionner le loader lors du clique sur les bouttons 
    SauvegardeCallback(app, args).register_clientside_callback("save_download_csv")
    SauvegardeCallback(app, args).register_clientside_callback("save_download_txt")
    SauvegardeCallback(app, args).register_clientside_callback("save_download_json")
