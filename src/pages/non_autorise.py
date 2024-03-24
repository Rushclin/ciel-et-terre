from dash import html, dcc
import dash_mantine_components as dmc
from utils import title, sub_title
from dash_extensions import Lottie


def page_non_autorisee(args):
    return html.Div(
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'height': '100vh',  # Pour occuper toute la hauteur de la fenêtre visible
            'text-align': 'center'
        },
        children=[
            dmc.Container(
                children=[
                    title(args.APP_NAME),
                    sub_title(args.APP_DESCRIPTION),
                     Lottie(
                options=dict(
                    loop=True,
                    autoplay=True,
                ),
                isClickToPauseDisabled=True,
                url="https://lottie.host/017a30ca-a051-490e-a5c0-ddaeecaa6f25/ZqjZdCckwC.json",
                width="40%",
            ),
                    dmc.Text(
                        "Vous n'êtes pas autorisé à voir cette page, veuillez vous connecter",
                        align='center'  # Pour aligner le texte au centre
                    ),
                   
                    dmc.Anchor(
                        "Connectez-vous ici",
                        href="/",
                        underline=False,
                        mt=10
                    ),
                ]
            )
        ]
    )
