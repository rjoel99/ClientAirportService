'''
Author: Joel Rubio
Date: 5-july-2022
'''

import json
import requests
from clients import ClientFile

def main():
    
    url = 'http://localhost:8080/api/v1/clients'

    clients = ClientFile().getClients()

    for payload in clients:
        print(f'Payload: {payload.serialize()}')
        response = requests.post(url, json = payload.serialize())
        print(f'Response code: {response.status_code}\n')

if __name__ == "__main__":
    main()