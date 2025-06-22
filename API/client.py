import requests

# factive_url:
api_url = "https://api.example.com"


def get_all_stickers():
    response = requests.get(f"{api_url}/stickers")
    response.raise_for_status()
    return response.json()


def get_stickers_by_name(item_name):
    response = requests.get(f"{api_url}/stickers/{item_name}")
    response.raise_for_status()
    return response.json()


def get_names_stickers_by_model(model):
    response = requests.get(f"{api_url}/stickers/names/{model}")
    response.raise_for_status()
    return response.json()
