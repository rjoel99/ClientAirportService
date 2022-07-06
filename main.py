'''
Author: Joel Rubio
Date: 5-july-2022
'''

import json
import requests
from employees import EmployeeFile

def main():
    
    url = 'http://localhost:8080/apiv1/empleados/add'

    for payload in EmployeeFile().getEmployees():
        print(f'Payload: {payload.serialize()}')
        response = requests.post(url, json = payload.serialize())
        print(f'Response code: {response.status_code}\n')

if __name__ == "__main__":
    main()