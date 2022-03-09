from datetime import datetime

import requests
from rest_framework.utils import json


def format_response_data(data):
    return json.loads(data)


def get_list_data(url):
    response = requests.get(url)

    # set data if the response is successful
    if response.status_code == 200:
        return format_response_data(response.json())
    else:
        return []


def get_detail_data(url):
    response = requests.get(url)

    # set data if the response is successful
    if response.status_code == 200:
        data = format_response_data(response.json())
        data['added_at'] = datetime.fromisoformat(data['added_at'])
        return data

    else:
        return None
