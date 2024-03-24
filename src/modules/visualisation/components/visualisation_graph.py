from dash import html, dcc
import dash_mantine_components as dmc
import plotly.graph_objects as go
from collections import deque

MAX_SIZE = 500

X = deque(maxlen=MAX_SIZE)
Yx = deque(maxlen=MAX_SIZE)
Yy = deque(maxlen=MAX_SIZE)
Yz = deque(maxlen=MAX_SIZE)
Y = deque(maxlen=MAX_SIZE)

# Je mets une queue pour gerer l'accelerometre 2

X_acc_2 = deque(maxlen=MAX_SIZE)
Yx_acc_2 = deque(maxlen=MAX_SIZE)
Yy_acc_2 = deque(maxlen=MAX_SIZE)
Yz_acc_2 = deque(maxlen=MAX_SIZE)
Y_acc_2 = deque(maxlen=MAX_SIZE)


def generate_graph_acc_1(name:str, data, min, max): 
    global X
    global Y
    global Yx
    global Yy
    global Yz
    global MAX_SIZE

    for entry in data:
        Yx.append(entry['x'])
        Yy.append(entry['y'])
        Yz.append(entry['z'])
        X.append(entry['time'])
    
    if name == "x":
        Y = Yx.copy()
    elif name == "y":
        Y = Yy.copy()
    else:
        Y = Yz.copy()

    out_of_control_trace = {
        "x": [],
        "y": [],
        "name": "Données hors de contrôle",
        "mode": "markers",
        "marker": dict(color="rgba(210, 77, 87, 0.7)", symbol="square", size=10),
    }

    # Pour tracer les points hors de contrôle 
    for index, data in enumerate(list(Y)):
        if float(data) >= max or float(data) <= min: 
            out_of_control_trace["x"].append(X[index])
            out_of_control_trace["y"].append(data)

    fig = {
        "data": [
            {
                "x": list(X), 
                "y": list(Y), 
                "mode": "lines+markers",
                "name": name,
                "line": {"color": "#008170"},
            }, 
            out_of_control_trace
        ]
    }

    fig["layout"] = dict(
        margin=dict(t=40),
        hovermode="closest",
        uirevision="Evolution temporelle",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend={"font": {"color": "darkgray"}, "orientation": "h", "x": 0, "y": 1.1},
        font={"color": "darkgray"},
        showlegend=True,
        xaxis={
            "zeroline": False,
            "showgrid": False,
            "title": "Evolution temporelle",
            "showline": False,
            "domain": [0, 1],
            "titlefont": {"color": "darkgray"},
        },
        yaxis={
            "title": "Axe "+name,
            "showgrid": False,
            "showline": False,
            "zeroline": False,
            "autorange": True,
            "titlefont": {"color": "darkgray"},
        },
        annotations=[],
        shapes=[]
    )

    return fig


def generate_graph_acc_2(name:str, data, min, max): 
    global X_acc_2
    global Yx_acc_2
    global Yx_acc_2
    global Yy_acc_2
    global Yz_acc_2
    global MAX_SIZE

    for entry in data:
        Yx_acc_2.append(entry['x'])
        Yy_acc_2.append(entry['y'])
        Yz_acc_2.append(entry['z'])
        X_acc_2.append(entry['time'])
    
    if name == "x":
        Y_acc_2 = Yx_acc_2.copy()
    elif name == "y":
        Y_acc_2 = Yy_acc_2.copy()
    else:
        Y_acc_2 = Yz_acc_2.copy()

    out_of_control_trace = {
        "x": [],
        "y": [],
        "name": "Données hors de contrôle",
        "mode": "markers",
        "marker": dict(color="rgba(210, 77, 87, 0.7)", symbol="square", size=10),
    }

    # Pour tracer les points hors de contrôle 
    for index, data in enumerate(list(Y_acc_2)):
        if float(data) >= max or float(data) <= min: 
            out_of_control_trace["x"].append(X_acc_2[index])
            out_of_control_trace["y"].append(data)

    fig = {
        "data": [
            {
                "x": list(X_acc_2), 
                "y": list(Y_acc_2), 
                "mode": "lines+markers",
                "name": name,
                "line": {"color": "#008170"},
            }, 
            out_of_control_trace
        ]
    }

    fig["layout"] = dict(
        margin=dict(t=40),
        hovermode="closest",
        uirevision="Evolution temporelle",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend={"font": {"color": "darkgray"}, "orientation": "h", "x": 0, "y": 1.1},
        font={"color": "darkgray"},
        showlegend=True,
        xaxis={
            "zeroline": False,
            "showgrid": False,
            "title": "Evolution temporelle",
            "showline": False,
            "domain": [0, 1],
            "titlefont": {"color": "darkgray"},
        },
        yaxis={
            "title": "Axe "+name,
            "showgrid": False,
            "showline": False,
            "zeroline": False,
            "autorange": True,
            "titlefont": {"color": "darkgray"},
        },
        annotations=[],
        shapes=[]
    )

    return fig



def build_visualisation_graph(title: str, id: str): 
    return html.Div(
        [
            dmc.Card(
                children=[
                    dmc.CardSection(
                        dmc.Group(
                            children=[
                                dmc.Text(title, weight=500),
                            ],
                            position="apart",
                        ),
                        withBorder=True,
                        inheritPadding=True,
                        py="xs",
                    ), 
                    html.Div(
                        dcc.Graph(
                            id=id,
                            figure=go.Figure(
                                { 
                                    "data": [
                                        {
                                            "y": [],
                                            "x": [],
                                            "mode": "lines+markers",
                                            "name": "x",
                                        }
                                    ],
                                   "layout": {
                                        "paper_bgcolor": "rgba(0,0,0,0)",
                                        "plot_bgcolor": "rgba(0,0,0,0)",
                                        "xaxis": dict(
                                            showline=False, showgrid=False, zeroline=False
                                        ),
                                        "yaxis": dict(
                                            showgrid=False, showline=False, zeroline=False
                                        ),
                                        "autosize": True,
                                    }, 
                                }
                            )
                        )
                    )
                ],
                withBorder=True,
                shadow="sm",
                radius="md",
                style={"width": "100%"},
                mt=10
            )
        ]
    )
