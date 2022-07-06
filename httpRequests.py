'''
Author: Joel Rubio
Date: 5-july-2022
'''

import urllib3
import json


def sendPostRequest(url, headers, payload):

    http = urllib3.PoolManager()

    encoded_data = json.dumps(payload).encode('utf-8')

    return http.request('POST', url, headers = headers, body = encoded_data)