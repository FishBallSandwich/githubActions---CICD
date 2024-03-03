import pytest
import requests



@pytest.fixture
def base_url():
    base_url = 'https://api.tronalddump.io/'
    q_string = 'search/quote?query='
    endpoint = base_url + q_string
    return endpoint


def fetch_quotes(base_url, query):

    url = base_url + query

    try:
        response = requests.get(url)

    except requests.RequestException as e:
        print("Error fetching data:", e)
        response = []

    return response

def test_fetch_quotes(base_url):
    response = fetch_quotes(base_url,'America')
    if response:
        response = response.json()['_embedded']['quotes']
        assert len(response) > 0

def test_status(base_url):
    response = fetch_quotes(base_url, 'Taco Bell')
    assert response.status_code == 200