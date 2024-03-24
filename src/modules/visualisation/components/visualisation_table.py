from dash import html
import dash_mantine_components as dmc

def generate_metric_row_helper(id:str, name:str, val_min, val_max, frequence):

    return generate_visualisation_row_table(
        id,
        {
            "id": id + "_name",
            "children": dmc.Text(
                name
            ),
        },
        {"id": id + "_valeur_min", "children": val_min},
        {"id": id + "_valeur_max", "children": val_max},
        {"id": id + "_echantillonage", "children": frequence},
    )

def build_visualisation_table(x_min, x_max, y_min, y_max, frequence): 
    header = html.Thead(
        html.Tr(
            [
                html.Th("Axe"),
                html.Th("Valeur minimale"),
                html.Th("Valeur maximale"),
                html.Th("Fréquence (Hz)"),
            ]
        )
    )

    body = html.Tbody(
            [
                generate_metric_row_helper(id="row_x", name="X", val_min=x_min, val_max=x_max, frequence=frequence),
                generate_metric_row_helper(id="row_y", name="Y", val_min=y_min, val_max=y_max, frequence=frequence),
            ]
    )
    return html.Div(
        children=[
            html.Div(
                dmc.Table(
                    striped=True,
                    highlightOnHover=True,
                    withBorder=True,
                    withColumnBorders=True,
                    my=20,
                    style={"width": "100%"},
                    children=[
                        header, body
                    ]
                )
            )
        ]
    )


def generate_visualisation_row_table(id, col1, col2, col3, col4):
    return html.Tr(
        id=id,
        children=[
            html.Td(
                id=col1['id'],
                children=col1['children']
            ),
            html.Td(
                id=col2['id'],
                children=col2['children']
            ),
            html.Td(
                id=col3['id'],
                children=col3['children']
            ),
            html.Td(
                id=col4['id'],
                children=col4['children']
            ),
        ],
    )
