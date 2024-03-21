from dash import html
import dash_mantine_components as dmc
import logging

from utils import sub_title, create_breakpoint_two_cols, convert_kilo_to_giga
from .components import percentage_component
from services import get_request



def render_utilisation_system(args):

    memories_values, memories_labels, memories_colors = [], [], []
    disk_values, disk_labels, disk_colors = [], [], []

    mem_api_response = get_request(args.API_SYSTEM_MEMORY)
    disk_api_response = get_request(args.API_SYSTEM_DISK)

    # Test si la reponse de la memoire n'est pas None
    if mem_api_response is not None:
        available = mem_api_response["response"]["available"]
        free = mem_api_response["response"]["free"]
        percent = mem_api_response["response"]["percent"]
        total = mem_api_response["response"]["total"]

        # memories_values = [convert_kilo_to_giga(
        #     float(available)), convert_kilo_to_giga(float(free))] # TODO: Decommenter
        memories_labels = ["Libre", "Occupé"]
        memories_colors = ["#005B41", "#008170"]

    # Test si la reponse du disque n'est pas None
    if disk_api_response is not None:
        disque = disk_api_response["response"]["/dev/mapper/ubuntu--vg-ubuntu--lv"]
        free = disque['free']
        total = disque['total']
        used = disque['used']

        disk_values = [convert_kilo_to_giga(
            float(free)), convert_kilo_to_giga(float(used))]
        disk_labels = ["Libre", "Utilisé"]
        disk_colors = ["#0F0F0F", "#232D3F"]
    
    else: 
        memories_values = [10, 30] # TODO: Supprimer
        memories_labels = ["Libre", "Occupé"] # TODO: Supprimer
        memories_colors = ["#005B41", "#008170"] # TODO: Supprimer

        disk_values = [10, 0.4] # TODO: Supprimer
        disk_labels = ["Libre", "Utilisé"] # TODO: Supprimer
        disk_colors = ["#0F0F0F", "#232D3F"] # TODO: Supprimer
        logging.error(f"Erreur lors du chargement des routes {args.API_SYSTEM_MEMORY} et {args.API_SYSTEM_DISK}")

    return html.Div(
        children=[
            sub_title("Utilisation système"),
            dmc.SimpleGrid(
                cols=2,
                spacing="lg",
                breakpoints=create_breakpoint_two_cols,
                children=[
                    percentage_component(title="Utilisation de la mémoire", colors=memories_colors,
                                         labels=memories_labels, values=memories_values, value_prefix="GO"),
                    percentage_component(title="Utilisation du disque dur", colors=disk_colors,
                                         labels=disk_labels, values=disk_values, value_prefix="GO"),
                ]
            )
        ]
    )
