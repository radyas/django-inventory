from datetime import datetime

import requests


def get_list_data(url):
    response = requests.get(url)

    # set data if the response is successful
    if response.status_code == 200:
        return response.json()
    else:
        return []


def get_detail_data(url):
    response = requests.get(url)

    # set data if the response is successful
    if response.status_code == 200:
        data = response.json()
        data['added_at'] = datetime.fromisoformat(data['added_at'])
        return data

    else:
        return None
