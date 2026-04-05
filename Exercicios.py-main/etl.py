#Repositorio da API
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

import pandas as pd #importando id dos clientes

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

import requests #importando bibiliotecas
import json

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None #verifica se get trouxe algo que seja valido

users = [user for id in user_ids if (user := get_user(id)) is not None] #percorre cada id e ignora os id none
print(json.dumps(users, indent=2))