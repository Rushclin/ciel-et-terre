from dash import html
import dash_mantine_components as dmc

from utils import create_breadcrumbs, title, sub_title
from modules.parametres import render_parametre_form


def page_parametres(args):
    return html.Div(
        [
            dmc.Container(
                size="lg",
                mt=5,
                children=[
                    create_breadcrumbs(steep_1="Application", steep_2="Paramètres",
                                       link_steep_1="/application", link_steep_2="application/parametres"),
                    title("Paramétrage des différents accéléromètres des capteurs."),
                    sub_title(
                        "Indiquez les differents paramètres que vous souhaitez."),
                        render_parametre_form(args)
                ]
            )
        ]
    )
