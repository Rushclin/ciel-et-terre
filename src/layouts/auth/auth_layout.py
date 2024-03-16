import dash_mantine_components as dmc
from dash_extensions import EventListener
from dash_iconify import DashIconify
from components.input_field import InputField


class AuthLayout:
    def get_layout(self):

        input_event = {"event": "change"}

        username_input = InputField(
            label="Nom d'utilisateur",
            placeholder="Nom d'utilisateur",
            icon=DashIconify(icon="radix-icons:person"),
        ).get_input("input-username")

        password_input = InputField(
            label="Mot de passe",
            placeholder="Votre mot de passe",
            icon=DashIconify(icon="radix-icons:lock-closed"),
            input_type="password",
        ).get_input("input-password")

        layout = dmc.Container(
            children=[
                dmc.Card(
                    children=[
                        dmc.LoadingOverlay(
                            dmc.Stack(
                                id="loading-form",
                                children=[
                                    dmc.Title(
                                        "Data Logger.",
                                        my=10,
                                        align="center"
                                    ),

                                    EventListener(username_input, events=[
                                        input_event], logging=True, id="username"),
                                    EventListener(password_input, events=[
                                        input_event], logging=True, id="password"),

                                    dmc.Checkbox(
                                        label="Se souvenir de moi !",
                                        checked=True,
                                    ),
                                    dmc.Button(
                                        "Se connecter", id="login-button", variant="outline", fullWidth=True,
                                        n_clicks=0
                                    ),
                                ],
                            )
                        )
                    ],
                    withBorder=True,
                    shadow="sm",
                    radius="md",
                    style={"width": 500, "marginInline": "auto"},
                )
            ]
        )
        return layout
