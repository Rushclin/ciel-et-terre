import dash_mantine_components as dmc
from dash import html
from utils import create_breakpoint_two_cols, sub_title, create_breakpoint_tree_cols
from dash_iconify import DashIconify


def show_sensor_form(args, id: str, title: str, echantillonage, period, rate, x_min, x_max, y_min, y_max):
    return html.Div(
        children=[
            sub_title(title),
            dmc.SimpleGrid(
                cols=3,
                spacing="lg",
                mt=10,
                breakpoints=create_breakpoint_tree_cols,
                children=[
                    dmc.NumberInput(
                        label="Echantillonage",
                        style={"width": "100%"},
                        error="",
                        id="echantillonage",
                        type="number",
                        value=float(echantillonage),
                        placeholder="Entrez l'echantillonage de l'accéléromètre",
                        precision=2,
                        step=0.05,
                    ),
                    dmc.NumberInput(
                        label="Durée de détection",
                        style={"width": "100%"},
                        id="duree_detection",
                        value=float(period),
                        type="number",
                        placeholder="Entrez la durée de détection",
                        precision=2,
                        step=0.05,
                    ),
                    dmc.NumberInput(
                        label="Fréquence (Entre 16 et 4880 Hz)",
                        style={"width": "100%"},
                        error="",
                        id="frequence",
                        value=float(rate),
                        type="number",
                        placeholder="Entrez la durée de fréquence",
                        precision=2,
                        step=0.05,
                        min=16,
                        max=4880
                    ),
                ],
            ),
            sub_title("Paramètres de l'axe X"),
            dmc.SimpleGrid(
                cols=2,
                spacing="lg",
                mt=20,
                breakpoints=create_breakpoint_two_cols,
                children=[
                    dmc.NumberInput(
                        label="Valeur minimale",
                        style={"width": "100%"},
                        error="",
                        id="minimale_x",
                        value=float(x_min),
                        type="number",
                        placeholder="Valeur minimale de X",
                        precision=2,
                        step=0.05,
                    ),
                    dmc.NumberInput(
                        label="Valeur maximale",
                        style={"width": "100%"},
                        error="",
                        id="maximale_x",
                        value=float(x_max),
                        type="number",
                        placeholder="Valeur maximale de X",
                        precision=2,
                        step=0.05,
                    ),
                ],
            ),

            sub_title("Paramètres de l'axe Y"),
            dmc.SimpleGrid(
                cols=2,
                spacing="lg",
                mt=20,
                breakpoints=create_breakpoint_two_cols,
                children=[
                    dmc.NumberInput(
                        label="Valeur minimale",
                        style={"width": "100%"},
                        error="",
                        id="minimale_y",
                        value=float(y_min),
                        type="number",
                        placeholder="Valeur minimale de Y",
                        precision=2,
                        step=0.05,
                    ),
                    dmc.NumberInput(
                        label="Valeur maximale",
                        style={"width": "100%"},
                        error="",
                        id="maximale_y",
                        value=float(y_max),
                        type="number",
                        placeholder="Valeur maximale de Y",
                        precision=2,
                        step=0.05,
                    ),
                ],
            ),

            dmc.SimpleGrid(
                cols=3,
                spacing="lg",
                mt=20,
                breakpoints=create_breakpoint_tree_cols,
                children=[
                    dmc.Button(
                        "Valider",
                        variant="outline",
                        leftIcon=DashIconify(
                            icon="fluent:settings-32-regular"),
                        id="save-form",
                        mb=10,
                        n_clicks=0
                    ),
                ],
            ),
        ]
    )
