from dash import html
import dash_mantine_components as dmc
from utils import title


def head(text):
    return dmc.Text(text, align="center", my=10, mx=0)


def page_a_propos(args):
    return html.Div(
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'height': '70vh',  
            'text-align': 'center'
        },
        children=[
            dmc.Container(
                size="lg",
                mt=5,
                children=[
                    title(
                        args.APP_NAME,
                    ),
                    head(
                        "Nous conçevons des dashboards specifiques à votre demande. Des Dashboards pour la production. "
                    ),
                    head("Code - Build - Test - Release. "),
                ],
            )
        ]
    )
