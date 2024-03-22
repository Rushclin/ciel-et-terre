from dash import html, dcc
from dash_iconify import DashIconify
import dash_mantine_components as dmc
from utils import create_breakpoint_tree_cols

input_event = {"event": "change"}


def create_sauvegardes_table(args):
    return dmc.Table(
        striped=True,
        highlightOnHover=True,
        withBorder=True,
        withColumnBorders=True,
        my=30,
        id="preview_save_data",
        children=[

        ]
    )


def render_sauvegarde_form(args):
    return html.Div(
        children=[
            create_sauvegarde_form(args),
            dmc.Text("Téléchargez pour prévisualiser les données ici.",
                     weight=500, my=20),
            create_sauvegardes_table(args),
        ]
    )


def create_sauvegarde_form(args):

    # Transormation du type
    sensors_list = []
    for data in args.SENSORS:
        sensors_list.append(dict(data))

    return html.Div(
        children=[
            html.Div(children=[], id="alert-errors"),
            dmc.SimpleGrid(
                cols=3,
                spacing="lg",
                mt=20,
                breakpoints=create_breakpoint_tree_cols,
                children=[
                    dmc.Select(
                        label="Choisir le capteur",
                        placeholder="Choisir le capteur",
                        value="ai_1",
                        data=sensors_list,
                        style={"width": "100%", "marginBottom": 10},
                        id="sensor_choice",
                        searchable=True
                    ),
                    html.Div(
                        children=[
                            dmc.Text("Date de début", size="sm"),
                            dcc.Input(type="datetime-local", step="1",
                                      id="date-begin", className="custom-datetime-input"),
                        ]
                    ),
                    html.Div(
                        children=[
                            dmc.Text("Date de fin", size="sm"),
                            dcc.Input(type="datetime-local", step="1",
                                      id="date-end", className="custom-datetime-input"),
                        ]
                    )
                ],
            ),
            dcc.Download(id="download"),
            dmc.SimpleGrid(
                cols=3,
                spacing="lg",
                mt=20,
                breakpoints=create_breakpoint_tree_cols,
                children=[
                    dmc.Button(
                        "Télécharger en CSV",
                        leftIcon=DashIconify(
                            icon="ph:file-csv-thin",
                        ),
                        id="save_download_csv",
                        variant="outline",
                    ),
                    dmc.Button(
                        "Télécharger en TXT",
                        leftIcon=DashIconify(
                            icon="bxs:file-txt",
                        ),
                        id="save_download_txt",
                        variant="outline",
                    ),
                    dmc.Button(
                        "Télécharger en JSON",
                        leftIcon=DashIconify(
                            icon="bxs:file-json",
                        ),
                        id="save_download_json",
                        variant="outline",
                    ),
                ],
            ),
        ]
    )
