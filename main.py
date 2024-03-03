import pandas as pd
import requests


base_url = 'https://api.tronalddump.io/'
q_string = 'search/quote?query='
### query = input('what do you want to query?')

url = base_url+q_string+'test'

responses = requests.get(url)
responses = responses.json()
responses = responses['_embedded']['quotes']

all_data = []

for response in responses:
    data = {'appeared_at': response['appeared_at'],
            'created_at': response['created_at'],
            'quote': response['value']}
    all_data.append(data)

df = pd.DataFrame(all_data)
print(df)
