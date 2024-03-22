from dash import Output, Input, State, no_update
from callbacks.base import BaseCallback


class SauvegardeCallback(BaseCallback):
    def __init__(self, app, args) -> None:
        super().__init__(app, args)

    def register_callback(self, input: str, format_type: str):
        @self.app.callback(
            Output("download", "data", allow_duplicate=True),
            Output(input, "loading"),
            Output("preview_save_data", "children", allow_duplicate=True),
            # Ce output doit s'afficher en cas d'erreur
            Output("alert-errors", "children", allow_duplicate=True),
            Input(input, "n_clicks"),
            State('date-begin', 'value'),
            State('date-end', 'value'),
            State("acc_choice", "value"),
        )
        def _d(n,
               s_date_begin,
               s_date_fin,
               acc_choice
               ):

            return no_update, no_update, no_update, no_update

    def register_clientside_callback(self, input):
        self.app.clientside_callback(
            """
            function updateLoadingState(n_clicks) {
                return true
            }
            """,
            Output(input, "loading", allow_duplicate=True),
            Input(input, "n_clicks"),
            prevent_initial_call=True,
        )
