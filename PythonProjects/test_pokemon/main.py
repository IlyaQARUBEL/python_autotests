import requests
response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
              json={
                     "pokemon_id": "21567"
                   },
               headers={'Content-Type': 'application/json', 'trainer_token': 'ca766358c7ff98cf39e17376aab76e77'},
               timeout=5)
print(f'Code: {response.status_code}. Message: {response.text}')
response.status_code ==400