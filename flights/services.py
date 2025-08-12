import requests

from amopromo_test.settings import MOCK_API_BASE_URL, MOCK_API_KEY, MOCK_AUTH_USER, MOCK_AUTH_USER_SENHA
from flights.mock_flights import get_mock_flights

MOCK_AUTH = (MOCK_AUTH_USER, MOCK_AUTH_USER_SENHA)


def get_flights_from_mock_airline(origin, destination, date):
    url = f"{MOCK_API_BASE_URL}/{MOCK_API_KEY}/{origin}/{destination}/{date}"
    try:
        response = requests.get(url, auth=(), timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[AVISO] Erro ao consultar API real ({e}). Usando mock local...")
        return get_mock_flights(origin, destination, date)
