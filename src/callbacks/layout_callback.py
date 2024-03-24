from dash import Output, Input

from callbacks.base import BaseCallback
from layouts.auth.auth_layout import AuthLayout
from layouts.dashboard.dashboard_layout import DashboardLayout

from flask_login import logout_user, current_user

from pages import not_found_404, page_acceuil, page_parametres, page_a_propos, page_systemes, page_notifications, page_sauvegardes, page_visualisation, page_non_autorisee


class LayoutCallback(BaseCallback):
    """
    Ce callback doit se charger de manager tout le layout de l'application
    """

    def __init__(self, app, args) -> None:
        super().__init__(app, args)
        self.auth_layout = AuthLayout().get_layout(self.args)
        self.dashboard_layout = DashboardLayout()

    def register_callback(self):
        @self.app.callback(
            Output('page-content', 'children'),
            Input('url', 'pathname')
        )
        def render_app_layout(pathname: str):
            if pathname == "/":
                logout_user()
                return self.auth_layout
            if current_user.is_authenticated:
                if pathname == "/application":
                    return self.dashboard_layout.get_layout(page_acceuil, self.args)
                elif pathname == "/application/parametres":
                    return self.dashboard_layout.get_layout(page_parametres, self.args)
                elif pathname == "/application/about":
                    return self.dashboard_layout.get_layout(page_a_propos, self.args)
                elif pathname == "/application/systeme":
                    return self.dashboard_layout.get_layout(page_systemes, self.args)
                elif pathname == "/application/notifications":
                    return self.dashboard_layout.get_layout(page_notifications, self.args)
                elif pathname == "/application/sauvegardes":
                    return self.dashboard_layout.get_layout(page_sauvegardes, self.args)
                elif pathname == "/application/visualisation":
                    return self.dashboard_layout.get_layout(page_visualisation, self.args)
                else:
                    return self.dashboard_layout.get_layout(not_found_404, self.args)
            else:
                return page_non_autorisee(self.args)
