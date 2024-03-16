import dash_mantine_components as dmc
from dash import html, dcc
from layouts.dashboard.components.header import create_header, create_side_navbar, create_navbar_drawer


class DashboardLayout:
    def get_layout(self, page, args):
        layout = dmc.MantineProvider(
            dmc.MantineProvider(
                theme={

                    """Example of app configuration"""

                    "fontFamily": "'Poppins', sans-serif",
                    "primaryColor": "indigo",
                    "components": {
                        "Button": {"styles": {"root": {"fontWeight": 400}}},
                        "Alert": {"styles": {"title": {"fontWeight": 500}}},
                        "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                    },
                },

                children=[
                    dcc.Location(id="url-dashboard", refresh="callback-nav"),
                    html.Div(id="notify-container"),

                    dmc.NotificationsProvider(
                        [
                            create_header(args),
                            create_side_navbar(args),
                            create_navbar_drawer(args),
                            html.Div(
                                dmc.Container(
                                    size="lg",
                                    pt=90,
                                    children=page(args)
                                ),
                                id="wrapper",
                            ),
                        ]
                    ),
                ]
            ),
            theme={"colorScheme": "light"},
            id="theme-provider",
            withGlobalStyles=True,
            withNormalizeCSS=True,
        )
        return layout
