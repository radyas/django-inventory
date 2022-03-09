from rest_framework.utils import json


def format_response_data(data):
    return json.loads(data)
