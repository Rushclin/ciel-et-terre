import dash_mantine_components as dmc
from utils import create_breakpoint_tree_cols
from dash import html
from services import get_request
import logging


def Tile(heading, description):
    return dmc.Card(
        radius="md",
        p="xl",
        withBorder=True,
        m=5,
        children=[
            dmc.Text(heading, size="lg", mt="md"),
            dmc.Divider(
                style={"width": 50},
                size="sm",
                color=dmc.theme.DEFAULT_COLORS["indigo"][5],
                my=10,
            ),
            dmc.Text(description, size="sm", color="dimmed", mt="sm"),
        ],
    )


def render_system_infos(args):

    elements = []
    has_error = False
    response = get_request(args.API_SYSTEM)

    if response is not None:
        has_error = False
        architecture = response['response']['cpu_arch']
        name = response['response']['PRETTY_NAME']
        os_type = response['response']['os_type']

        elements.append(
            html.Div(
                Tile(description=architecture, heading="Architecture")
            )
        )

        elements.append(
            html.Div(
                Tile(description=name, heading="Système d'exploitation")
            )
        )

        elements.append(
            html.Div(
                Tile(description=os_type, heading="Noyau")
            )
        )

    else:
        has_error = True
        logging.error(
            f"La réponse de la route {args.API_SYSTEM} est {response}")

    return dmc.SimpleGrid(
        cols=3,
        mt=50,
        breakpoints=create_breakpoint_tree_cols,
        id="infos-du-systeme",
        children=elements
    ) if not has_error else dmc.Alert(
        "Impossible de charger les données, veuillez vérifier votre connexion internet.",
        title="Chargement impossible !",
        color="red"
    )
