from dash import Output, Input
import dash_mantine_components as dmc

from callbacks.base import BaseCallback
from modules.parametres.components import show_sensor_form


class ParametreCallback(BaseCallback):
    def __init__(self, app, args) -> None:
        super().__init__(app, args)

    def register_callback(self):
        @self.app.callback(
            Output("show-sensor-container", "children"),
            Input("select-sensor", "value")
        )
        def _d(value):

            if value is None:
                return dmc.Alert(
                    "Veuillez selectionner un capteur pour afficher le formulaire",
                    title="Selectionnez un capteur !",
                    color="red",
                    mt=10
                )
            return show_sensor_form(
                args=self.args,
                id=value,
                title=f"#{value}",
                echantillonage=10,
                period=0,
                rate=10,
                x_max=0,
                x_min=1,
                y_max=1,
                y_min=1,

            )
