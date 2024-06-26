import pytz
import logging
import datetime
from dash import html
from datetime import datetime
from dateutil import parser, tz
from tzlocal import get_localzone
import dash_mantine_components as dmc


def create_breadcrumbs(
    steep_1: str, steep_2: str, link_steep_1="", link_steep_2=""
):
    """
    create_breadcrumbs

    ==================

    Component to render BreadCrump component

    """
    return dmc.Breadcrumbs(
        separator="→",
        children=[
            dmc.Anchor(steep_1, href=link_steep_1, underline=False),
            dmc.Anchor(steep_2, href=link_steep_2, underline=False),
        ],
        mb=20,
    )


def title(title: str):
    """Composant qui doit afficher un titre de niveau avec une taille de 30px"""

    return dmc.Title(align="center", children=title, my=20, order=2, className="color-primary", style={'color': '#232D3F'})


def sub_title(sub_title: str):
    return dmc.Title(align="center", children=sub_title, my=30, order=4, className="color-primary")


def create_preview_header(df):
    columns = df.columns.tolist()
    return html.Thead(html.Tr([html.Th(col) for col in columns]))


def create_preview_body(df):
    values = df.values
    return html.Tbody([html.Tr([html.Td(cell) for cell in row]) for row in values])


create_breakpoint_two_cols = [
    {"maxWidth": 980, "cols": 2, "spacing": "md"},
    {"maxWidth": 755, "cols": 1, "spacing": "sm"},
    {"maxWidth": 600, "cols": 1, "spacing": "sm"},
]


create_breakpoint_tree_cols = [
    {"maxWidth": 980, "cols": 3, "spacing": "md"},
    {"maxWidth": 755, "cols": 3, "spacing": "sm"},
    {"maxWidth": 600, "cols": 1, "spacing": "sm"},
]

create_breakpoint_four_cols = [
    {"maxWidth": 980, "cols": 4, "spacing": "md"},
    {"maxWidth": 755, "cols": 4, "spacing": "sm"},
    {"maxWidth": 600, "cols": 1, "spacing": "sm"},
]


def create_accordion_label(label, image, description):
    return dmc.AccordionControl(
        dmc.Group(
            [
                dmc.Avatar(src=image, radius="xl", size="lg"),
                html.Div(
                    [
                        dmc.Text(label),
                        dmc.Text(description, size="sm",
                                 weight=400, color="dimmed"),
                    ]
                ),
            ]
        )
    )


def create_accordion_content(content):
    return dmc.AccordionPanel(dmc.Text(content, size="sm"))


def convert_frequency_in_microsecond(value):
    # Assurer que la valeur est dans la plage spécifiée
    value = max(16, min(4880, value))
    # Effectuer la conversion en utilisant une règle de trois
    converted_value = (1 / value) * 1e6

    return round(converted_value)


def convert_microsecond_in_frequency(value):
    # Effectuer la conversion en utilisant une règle de trois
    converted_value = 1 / (value * 1e-6)
    return round(converted_value)


def format_quering(data, champ='time'):
    """
    Function to format query string to get data from Mongo DB
    """
    query = {}

    if data == "nan":
        pass
    else:
        query = {champ: {'$gte': datetime.fromisoformat(
            data['time_start']), '$lte': datetime.fromisoformat(data['time_stop'])}}

    return query


def convert_kilo_to_giga(kilo_value):
    """
    Fonction qui doit convertir de KO à GO
    """

    giga_value = round(kilo_value / 1073741824, 2)
    return giga_value


def convert_time(time_str):
    try:
        time_obj = parser.parse(time_str)

        local_time = time_obj.astimezone(tz.tzlocal())

        return local_time.strftime("%Y-%m-%d %H:%M:%S.%f")
    except Exception as e:
        logging.error(e)
        return None


def convert_utc_to_local_time(utc_time):
    try:
        utc_date = datetime.datetime.fromisoformat(utc_time)

        local_timezone = get_localzone()

        fuseau_local = pytz.timezone(str(local_timezone))

        utc_date = pytz.utc.localize(utc_date)

        local_date = utc_date.astimezone(fuseau_local)

        return local_date.isoformat(sep=" ")
    except Exception as e:
        logging.error(e)
        return None


def convert_local_time_to_utc(local_time):

    local_timezone = get_localzone()
    local_date = datetime.datetime.fromisoformat(local_time)

    local_tz = pytz.timezone(local_timezone.__str__())

    local_date = local_tz.localize(local_date)

    utc_date = local_date.astimezone(pytz.utc)

    return utc_date.isoformat()
