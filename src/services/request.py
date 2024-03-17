import requests
from requests.exceptions import HTTPError


def get_request(route: str):
    """Fonction qui doit éffectuer les requêtes en GET à l'API"""
    try:
        response = requests.get(route)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    except HTTPError as http_err:
        print(f"HTTP ERROR: {http_err}")
    except Exception as err:
        print(f"ERROR : {err}")


def post_request(route: str, data: any):
    """Fonction qui doit éffectuer les requêtes API en POST"""
    try:
        response = requests.post(route, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except Exception as err:
        print(f"Error: {err}")
