from dash import html
import dash_mantine_components as dmc
from utils import create_breadcrumbs, title
from modules.sauvegardes import render_sauvegarde_form


def page_sauvegardes(args):
    return html.Div(
        [
            dmc.Container(
                size="lg",
                mt=5,
                children=[
                    create_breadcrumbs(steep_1="Application", link_steep_1="/application",
                                       steep_2="Sauvegardes", link_steep_2="/application/sauvegardes"),
                    title("Sauvegardes des données"),
                    render_sauvegarde_form(args),
                ]
            )
        ]
    )
