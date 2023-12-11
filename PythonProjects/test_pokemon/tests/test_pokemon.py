import requests
import pytest

def test_ger_trainers():
    response = requests.get(url='https://api.pokemonbattle.me:9104/trainers', 
     headers={'Content-Type': 'application/json', 'trainer_token': 'ca766358c7ff98cf39e17376aab76e77'},
     timeout=5, params={'trainer_id':3531})
    print(f'Code: {response.status_code}. Message: {response.text}')
    assert response.status_code == 200