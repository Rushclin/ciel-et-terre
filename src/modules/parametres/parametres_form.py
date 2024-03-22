import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html, Output, Input, callback, callback_context as ctx, no_update, clientside_callback, dcc, State

from utils import create_breakpoint_two_cols, create_breakpoint_tree_cols, sub_title, convert_frequency_in_microsecond, convert_microsecond_in_frequency
from services import post_request

format_parametres = [
    {"value": "R", "label": "Raw ADC Codes"},
    {"value": "V", "label": "Voltage"},
    {"value": "G", "label": "Convertir en [g]"},
    {"value": "M", "label": "Mettre par seconde"},
]


def render_parametre_form(args):
    """Le composant qui doit rendre le paramétrage des Sensors """

    # Transormation du type
    sensors_list = []
    for data in args.SENSORS:
        sensors_list.append(dict(data))

    return html.Div(
        children=[
            dmc.SimpleGrid(
                cols=1,
                spacing="lg",
                mt=20,
                breakpoints=create_breakpoint_two_cols,
                children=[
                    dmc.Select(
                        data=sensors_list,
                        style={"width": '100%'},
                        label="Selectionnez un capteur",
                        id="select-sensor",
                        rightSection=DashIconify(
                            icon="radix-icons:chevron-down"),
                        placeholder="Selectionnez un capteur",
                        searchable=True,
                        nothingFound="Aucune option trouvée",
                    ),
                ],
            ),
            html.Div(id="show-sensor-container"),
        ]
    )

@callback(
    Output("show-sensor-container", "children"),
    Input("select--sensor", "data")
)
def render(data):
    print(data)
    return str(data)



# ========= Callack pour afficher le fornulaire en fonction du choix du client ============



    # if ctx.triggered_id is not None:
    #     if value != "":
    #         save = {"value": value}
    #         title = "Accéleromètre 1 " if value == "measurement_accel_1" else "Accéleromètre 2"

    #         params = {
    #             "section": "accel_1" if value == "measurement_accel_1" else "accel_2"
    #         }

    #         result = post_request(route="get_config",
    #                               data=params)  # TODO: Change

    #         if result is not None:
    #             value = result["value"]

    #             x_min = value["x_min"]
    #             x_max = value["x_max"]

    #             y_min = value["y_min"]
    #             y_max = value["y_max"]

    #             z_min = value["z_min"]
    #             z_max = value["z_max"]

    #             data_format = value["data_format"]
    #             stream = value["stream"]
    #             rate = value["rate"]
    #             period = value["period"]
    #             sample_size = value['sample_size']

    #             format_frequence = convert_microsecond_in_frequency(
    #                 float(rate))

    #             return render_accelerometer_form_after_selecte(
    #                 value,
    #                 title,
    #                 echantillonage=sample_size,
    #                 rate=format_frequence,
    #                 period=period,
    #                 data_format=data_format,
    #                 x_min=x_min,
    #                 x_max=x_max,
    #                 y_max=y_max,
    #                 y_min=y_min,
    #                 z_max=z_max,
    #                 z_min=z_min)
    #         else:
    #             print("Le resultat est None")
    #             return no_update
    #     else:
    #         no_update
    # else:
    #     return no_update


# ========== Recuperation des valeurs et sauvegarde du formulaire. C'est ici qu'on effectue l'appel API ============

# @callback(
#     Output("notify-container", "children", allow_duplicate=True),
#     Output("show-accelerometer-container", "children", allow_duplicate=True),
#     Input("save-form", "n_clicks"),
#     [
#         State("echantillonage", "value"),
#         State("duree_detection", "value"),
#         State("format_parametrage", "value"),
#         State("minimale_x", "value"),
#         State("maximale_x", "value"),
#         State("minimale_y", "value"),
#         State("maximale_y", "value"),
#         State("minimale_z", "value"),
#         State("maximale_z", "value"),
#         State("frequence", "value"),
#         State("selected-accelerometer", "data"),
#     ],
#     prevent_initial_call=True,
# )
# def save_submit_form(
#     n_clicks,
#     echantillonage,
#     duree_detection,
#     format_parametrage,
#     minimale_x,
#     maximale_x,
#     minimale_y,
#     maximale_y,
#     minimale_z,
#     maximale_z,
#     frequence,
#     selected_accelerometer
# ):

#     selected_accel_stream = selected_accelerometer.get('value', '')
#     message = "Les données ont bien été chargées"

#     selected_acc = "accel_1" if selected_accel_stream == "measurement_accel_1" else "accel_2"

#     # Je recupere d'abord le contexte pour me rassurer que l'action vient du boutton avant de faire des traitements

#     if "save-form" in ctx.triggered_id and n_clicks > 0:

#         # On effectue la requete API ici, le print ne sert a rien ...

#         convert_frequence = convert_frequency_in_microsecond(float(frequence))

#         params = {
#             "section": selected_acc.__str__(),
#             "x_min": minimale_x.__str__(),
#             "x_max": maximale_x.__str__(),
#             "y_min": minimale_y.__str__(),
#             "y_max": maximale_y.__str__(),
#             "z_min": minimale_z.__str__(),
#             "z_max": maximale_z.__str__(),
#             "data_format": format_parametrage.__str__(),
#             "rate": convert_frequence.__str__(),
#             "sample_size": echantillonage.__str__(),
#         }

#         result = post_request(route="set_config", data=params)  # TODO: Change

#         if result is not None:
#             return dmc.Notification(
#                 id="my-notification",
#                 title="Chargement de vos paramètres",
#                 message="Le processus de chargement a commencé, veuillez patienter.",
#                 color="green",
#                 action="show",
#                 autoClose=True,
#                 icon=DashIconify(icon="akar-icons:circle-check"),
#             ), dmc.Alert(message, title="Modification terminée", color="blue", mt=20),
#         else:
#             return no_update
#     else:
#         return no_update
