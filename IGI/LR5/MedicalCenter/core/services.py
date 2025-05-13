import requests
from django.conf import settings

def fetch_external_services():
    try:
        response = requests.get('https://api.example.com/medical-services')
        return response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        return []