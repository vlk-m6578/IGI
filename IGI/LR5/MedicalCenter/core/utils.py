import requests
from django.conf import settings

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OWM_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def fetch_doctor_schedule(doctor_id):
    """Пример использования API для получения расписания"""
    try:
        response = requests.get(
            f"{settings.API_BASE_URL}/doctors/{doctor_id}/schedule",
            headers={"Authorization": f"Bearer {settings.API_KEY}"}
        )
        return response.json() if response.status_code == 200 else None
    except requests.exceptions.RequestException:
        return None