from dash import html, callback, Input, Output, callback_context as ctx, no_update, dcc
import dash_mantine_components as dmc
from utils import create_breakpoint_tree_cols, sub_title
from dash_iconify import DashIconify
from time import sleep

def render_contoler_systeme(args): 
    return html.Div(
        [
            sub_title("Contôller le système"), 
            dmc.SimpleGrid(
                cols=3,
                spacing="lg",
                mt=20,
                breakpoints=create_breakpoint_tree_cols,
                children=[
                    dmc.Button(
                        "Reinitialiser l'alarme", 
                        leftIcon=DashIconify(icon="mdi:stopwatch-start"),
                        variant="outline",
                        id="btn-reinitialiser",
                        n_clicks=0
                    ),
                    dmc.Button(
                    "Redémarer l'ordinateur",
                        leftIcon=DashIconify(icon="mdi:car-engine-start"),
                        variant="outline",
                        id="btn-redemarrer",
                        n_clicks=0
                    ),
                    dmc.Button(
                    "Formater la clef",
                        leftIcon=DashIconify(icon="mdi:car-engine-start"),
                        variant="outline",
                        id="btn-formater",
                        n_clicks=0
                    ),
                    dcc.Store(id="btn-action")
                ]
            )
        ]
    )


# Les differents callbacks pour gerer les boutons 
# Ici c'est juste pour les notifications

@callback(
    Output('notify-container', 'children', allow_duplicate=True),
    Output("btn-action", "data"),
    Output("btn-formater", "loading", allow_duplicate=True),
    Output("btn-reinitialiser", "loading", allow_duplicate=True),
    Output("btn-redemarrer", "loading", allow_duplicate=True),

    Input("btn-formater", "n_clicks"),
    Input("btn-reinitialiser", "n_clicks"),
    Input("btn-redemarrer", "n_clicks"),
    prevent_initial_call=True
)
def save_action_to_execute(n_formater:int, n_reinitialiser:int, n_redemarrer:int): 
    # Je recupere le contexte d'execution et me rassure que c'est bien une action venant de l'un des bouttons avant de lancer l'execution
    action = {"action": ctx.triggered_id}

    # Je vais faire ainsi pour tous les trois boutons
    if "btn-formater" in ctx.triggered_id and n_formater > 0:
        return dmc.Notification(
                    id="my-notification",
                    title="Execution de l'opération de formatage de la clef en cours",
                    message="Veuillez patienter que le processus se complète.",
                    loading=True,
                    color="orange",
                    action="show",
                    autoClose=False,
                    disallowClose=True,
                ), action, True, False, False
    
    elif "btn-reinitialiser" in ctx.triggered_id and n_reinitialiser > 0:
        return dmc.Notification(
                    id="my-notification",
                    title="Execution de l'opération de reinitialisation de l'alarme en cours",
                    message="Veuillez patienter que le processus se complète.",
                    loading=True,
                    color="orange",
                    action="show",
                    autoClose=False,
                    disallowClose=True,
                ), action, False, True, False
    
    elif "btn-redemarrer" in ctx.triggered_id and n_redemarrer > 0:
        return dmc.Notification(
                    id="my-notification",
                    title="Execution de l'opération de redémarage de l'ordinateur en cours",
                    message="Veuillez patienter que le processus se complète.",
                    loading=True,
                    color="orange",
                    action="show",
                    autoClose=False,
                    disallowClose=True,
                ), action, False, False, True
    
    else: 
        return no_update, no_update, no_update, no_update, no_update
    

# Le callback qui doit executer l'action (ici l'appel API)

@callback(
    Output('notify-container', 'children', allow_duplicate=True),
    Output("btn-formater", "loading", allow_duplicate=True),
    Output("btn-reinitialiser", "loading", allow_duplicate=True),
    Output("btn-redemarrer", "loading", allow_duplicate=True),

    Input("btn-action", "data"),
    prevent_initial_call=True
)
def execute_action(data):
    # print(data)
    action = data.get('action', '')
    
    # TODO: Traiter l'opéraion en fonction de l'action. Implique ici l'envoie des requette API
    # Je vais donc faire des if pour chaque action, mais mainytenant c'est juste le test

    sleep(5) # Attendre 5 secondes avant de mettre a jour, TODO: On peut toujours retirer ou diminuer
    return dmc.Notification(
                id="my-notification",
                title="Fin de l'opération",
                message="Opération executée avec succès.",
                color="green",
                action="update",
                icon=DashIconify(icon="akar-icons:circle-check"),
            ), False, False, False