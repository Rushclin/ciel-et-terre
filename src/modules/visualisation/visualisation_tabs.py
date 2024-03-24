from dash import html
import dash_mantine_components as dmc
from modules.visualisation.components import build_visualisation_table, build_visualisation_graph
from utils import convert_microsecond_in_frequency


def render_visualisation_tabs(args):
    return html.Div(
        [
            dmc.Tabs(
                [
                    dmc.TabsList(
                        [
                            dmc.Tab("Capteur 1",
                                    value="stream_accel_1"),
                            dmc.Tab("Capteur 2",
                                    value="stream_accel_2"),
                        ]
                    ),
                    dmc.TabsPanel(
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        build_visualisation_table(x_min=1, x_max=1,
                                                                  y_max=1, y_min=1, frequence=convert_microsecond_in_frequency(float(10)))
                                    ],
                                    id="recapitulatif-acc-1"
                                ),
                                dmc.Tabs(
                                    [
                                        dmc.TabsList(
                                            [
                                                dmc.Tab(
                                                    "Axe X", value="axe_x"),
                                                dmc.Tab(
                                                    "Axe Y", value="axe_y"),
                                            ]
                                        ),
                                        html.Div(                                                 build_visualisation_graph(
                                                     id="graphe-acceleremoter-1", title="Visualiser sur l'accéléromètre 1"),
                                                 style={"paddingTop": 10}
                                                 ),

                                    ],
                                    value="axe_x",
                                    id="current-accelemeter-1-axe",
                                    # variant="outline"
                                )
                            ]
                        ),
                        value="stream_accel_1"
                    ),
                    dmc.TabsPanel(
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        build_visualisation_table(x_min=1, x_max=1,
                                                                  y_max=1, y_min=1, frequence=convert_microsecond_in_frequency(float(1)))
                                    ],
                                    id="recapitulatif-acc-2"
                                ),
                                dmc.Tabs(
                                    [
                                        dmc.TabsList(
                                            [
                                                dmc.Tab(
                                                    "Axe X", value="axe_x"),
                                                dmc.Tab(
                                                    "Axe Y", value="axe_y"),
                                            ]
                                        ),
                                        html.Div(
                                            build_visualisation_graph(id="graphe-acceleremoter-2", title="Visualiser sur l'accéléromètre 2"), style={"paddingTop": 10}
                                        ),
                                    ],
                                    value="axe_x",
                                    id="current-accelemeter-2-axe",
                                )
                            ]
                        ),
                        value="stream_accel_2"
                    ),
                ],
                id="current-accelemeter",
                value="stream_accel_1",
            ),
        ]
    )
