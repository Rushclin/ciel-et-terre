from dash import html
import dash_mantine_components as dmc 

from utils import title
from modules.acceuil import render_system_infos

def page_acceuil (args):
    return html.Div(
        [
            dmc.Container(
                size="large",
                mt=5,
                children=[
                    title(args.APP_NAME),
                    render_system_infos(args),
                ]
            )
        ]
    )