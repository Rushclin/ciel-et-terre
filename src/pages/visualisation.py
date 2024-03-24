from dash import html
import dash_mantine_components as dmc 
from modules.visualisation import render_visualisation_tabs
from utils import create_breadcrumbs, title, sub_title


def page_visualisation(args):
    return html.Div(
        dmc.Container(
             size="lg", 
                mt=5, 
                children=[
                    create_breadcrumbs(steep_1="Application", steep_2="Visualisation", link_steep_1="/application", link_steep_2="/application/visualisation"),
                    title("Visualisation des données"), 
                    sub_title("Veuillez choisir un capteur à visualiser"),
                    render_visualisation_tabs(args),
                ]
        )
    )
