import requests
import pytest

def test_creat_pokemon():
    response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
              "name": "generate",
              "photo": "generate"
               }, 
               headers={'Content-Type': 'application/json', 'trainer_token': 'ca766358c7ff98cf39e17376aab76e77'},
               timeout=5)
    print(f'Code: {response.status_code}. Message: {response.text}')
    assert response.status_code == 400
  
def test_rename_pokemon():
    response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
                     "pokemon_id": "21567",
                     "name": "pupatson",
               },
               headers={'Content-Type': 'application/json', 'trainer_token': 'ca766358c7ff98cf39e17376aab76e77'},
               timeout=5)
    print(f'Code: {response.status_code}. Message: {response.text}')
    assert response.status_code == 200
    
def test_pokemon_add_pokeball():
    response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
              json={
                     "pokemon_id": "21567"
                   },
               headers={'Content-Type': 'application/json', 'trainer_token': 'ca766358c7ff98cf39e17376aab76e77'},
               timeout=5)
    print(f'Code: {response.status_code}. Message: {response.text}')
    response.status_code == 400