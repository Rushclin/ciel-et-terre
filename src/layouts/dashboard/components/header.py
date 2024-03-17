import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html, dcc, clientside_callback, Input, Output, callback
from flask_login import logout_user


def create_header_link(icon, href, size=22, color="indigo"):
    """
    create_header_link 

    =================== 

    This function take in input : \n 
    1. icon name in type Str \n
    2. href for location Str \n
    3. size, default 22px in type int\n 
    4. color, default indigo in str \n 

    And return a type Anchor provide by dash mantine
    """
    return dmc.Anchor(
        dmc.ThemeIcon(
            DashIconify(
                icon=icon,
                width=size,
            ),
            variant="outline",
            radius=30,
            size=36,
            color=color,
        ),
        href=href,
        target="_blank",
    )


def create_home_link(label):
    """create_home_link est le composant utilisé dans le sidebar pour créer la navigation"""
    return dmc.Anchor(
        label,
        size="xl",
        href="/application",
        underline=False,
    )


def create_header(args):
    """HEADER FOR APP"""

    return dmc.Header(
        height=70,
        fixed=True,
        px=25,
        children=[
            dmc.Stack(
                justify="center",
                style={"height": 70},
                children=dmc.Grid(
                    children=[
                        dmc.Col(
                            [
                                dmc.MediaQuery(
                                    create_home_link(args.APP_NAME),
                                    smallerThan="lg",
                                    styles={"display": "none"},
                                ),
                                dmc.MediaQuery(
                                    create_home_link(args.APP_NAME),
                                    largerThan="lg",
                                    styles={"display": "none"},
                                ),
                            ],
                            span="content",
                            pt=12,
                        ),
                        dmc.Col(
                            span="auto",
                            children=dmc.Group(
                                position="right",
                                spacing="xl",
                                children=[
                                    create_header_link(
                                        "radix-icons:github-logo",
                                        "https://github.com/Rushclin/",
                                    ),
                                    create_header_link(
                                        "material-symbols:mail-outline",
                                        "mailto:takamrushclin@gmail.com",
                                    ),
                                    create_header_link(
                                        "mdi:telephone-in-talk-outline",
                                        "tel:+237690139627",
                                    ),
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="mingcute:exit-line", width=22
                                        ),
                                        variant="outline",
                                        radius=30,
                                        size=36,
                                        color="yellow",
                                        id="exit-btn",
                                    ),
                                    dmc.MediaQuery(
                                        dmc.ActionIcon(
                                            DashIconify(
                                                icon="radix-icons:hamburger-menu",
                                                width=18,
                                            ),
                                            id="drawer-hamburger-button",
                                            variant="outline",
                                            size=36,
                                        ),
                                        largerThan="lg",
                                        styles={"display": "none"},
                                    ),
                                ],
                            ),
                        ),
                    ]
                ),
            )
        ],
    )


def create_nav_item(
    path: str,
    title: str,
    icon="home",
):
    return html.Li(
        [
            dcc.Link(
                [
                    html.Span(
                        icon,
                        className="material-symbols-outlined icon",
                    ),
                    html.Span(
                        title,
                        className="text",
                    ),
                ],
                href=path,
                className="nav-link",
            ),
        ],
        className="nav-item",
    )


def create_main_nav_link(icon, label, href):
    return dmc.Anchor(
        dmc.Group(
            [
                DashIconify(
                    icon=icon,
                    width=23,
                    color=dmc.theme.DEFAULT_COLORS["indigo"][5],
                ),
                dmc.Text(label, size="sm"),
            ]
        ),
        href=href,
        variant="text",
        mb=5,
        style={"fontSize": "20px"},
    )


def create_side_nav_content():
    main_links = dmc.Stack(
        mt=20,
        children=[
            html.Ul(
                html.Li(
                    create_nav_item(
                        path="/application",
                        title="Accueil",
                    ),
                    className="nav-item",
                )
            ),
            dmc.Divider(),
            html.Ul(
                html.Li(
                    create_nav_item(path="/application/visualisation",
                                    title="Visualisation", icon="map"),
                    className="nav-item",
                )
            ),
            dmc.Divider(),
            html.Ul(
                [
                    html.Li(
                        create_nav_item(
                            path="/application/parametres", title="Paramètres", icon="settings"
                        ),
                        className="nav-item",
                        style={"marginBottom": 20},
                    ),
                    html.Li(
                        create_nav_item(
                            path="/application/sauvegardes", title="Sauvegardes", icon="save"
                        ),
                        className="nav-item",
                        style={"marginBottom": 20},
                    ),
                    html.Li(
                        create_nav_item(
                            path="/application/systeme", title="Système", icon="sensor_door"
                        ),
                        className="nav-item",
                    ),
                ]
            ),
            dmc.Divider(),
            html.Ul(
                html.Li(
                    create_nav_item(
                        path="/application/notifications",
                        title="Notifications",
                        icon="notifications",
                    ),
                    className="nav-item",
                ),
            ),
            dmc.Divider(),
            html.Ul(
                html.Li(
                    create_nav_item(
                        path="/application/about", title="A propos de nous", icon="partner_exchange"
                    ),
                    className="nav-item",
                ),
            ),
        ],
        style={"marging": 0},
    )
    return dmc.Stack(
        spacing=0,
        children=[
            main_links,
        ],
        px=25,
    )


def create_side_navbar(args):
    """SIDEBAR FOR THE APP"""

    return dmc.Navbar(
        fixed=True,
        id="components-navbar",
        position={"top": 70},
        width={"base": 300},
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                children=create_side_nav_content(),
            )
        ],
    )


def create_navbar_drawer():
    """DRAWER FOR APP"""
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayOpacity=0.55,
        overlayBlur=3,
        zIndex=9,
        size=300,
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                style={"height": "100vh"},
                pt=20,
                children=create_side_nav_content(),
            )
        ],
    )


def create_aside(description: str, title="Une description de la section"):
    """ASIDE FOR APP, A utiliser pour afficher une description. Lorsque l'ecran est large, il est affiché"""
    return dmc.Aside(
        position={"top": 140, "right": 0},
        fixed=True,
        id="toc-navbar",
        width={"base": 300},
        zIndex=10,
        children=[
            dmc.Text(
                title,
                align="center",
                my=10,
                weight="bold",
            ),
            dmc.Text(
                description,
                align="center",
                my=10,
                mx=0,
            ),
        ],
        withBorder=True,
    )


def create_navbar_drawer(args):
    """DRAWER FOR APP"""
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayOpacity=0.55,
        overlayBlur=3,
        zIndex=9,
        size=300,
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                style={"height": "100vh"},
                pt=20,
                children=create_side_nav_content(),
            )
        ],
    )


clientside_callback(
    """function(n_clicks) { return true }""",
    Output("components-navbar-drawer", "opened"),
    Input("drawer-hamburger-button", "n_clicks"),
    prevent_initial_call=True,
)

clientside_callback(
    """function(n_clicks) { return "/" }""",
    Output("url", "pathname"),
    Input("exit-btn", "n_clicks"),
    prevent_initial_call=True,
)
