'''
Author: Joel Rubio
Date: 5-july-2022
'''

from employees import EmployeeFile
from httpRequests import sendPostRequest

def main():
    
    url     = 'http://localhost:8080/apiv1/empleados/add'
    headers = {'Content-Type': 'application/json'}

    for payload in EmployeeFile().getEmployees():
        print(f'Payload: {payload.serialize()}')
        response = sendPostRequest(url, headers, payload.serialize())
        print(f'Response code: {response.status}\n')


if __name__ == "__main__":
    main()