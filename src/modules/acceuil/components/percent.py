import dash_mantine_components as dmc
from dash import html, dcc
import plotly.graph_objects as go


def percentage_component(title: str, labels: [], values: [], colors: [], value_prefix: str = ""):  # type: ignore

    labeled_labels = [
        f"{label} ({value} {value_prefix})" for label, value in zip(labels, values)]

    figure = go.Figure(
        data=[
            go.Pie(
                labels=labeled_labels,
                values=values,
                hole=0.2,
                scalegroup="one",
                textinfo="percent",
                textposition="inside",
                hoverinfo="label+percent",
                textfont=dict(
                    color="white",
                ),
                marker=dict(
                    colors=colors
                ),
            )
        ],
        layout={
            "margin": {"l": 50, "r": 50, "t": 50, "b": 50},
            "plot_bgcolor": "rgba(0, 0, 0, 0)",
        },
    )
    figure.update_traces(textposition='inside')
    figure.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

    return dmc.Card(
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
                    figure=figure,
                    config={
                        "displayModeBar": False,
                        "scrollZoom": False,
                        "responsive": True,
                    }
                ),
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": "100%"},
    )
