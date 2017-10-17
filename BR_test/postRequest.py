import json
import sys
import requests
import time

url = 'http://localhost:5555/datawriter'
# url = 'https://brainrider.herokuapp.com/datawriter'

i = 0
while True:
    i += 1

    data = {
        "id": i,
        "data": "hello_a"
    }

    req = requests.post(url, json = data)

    time.sleep(15)
