import sys
import requests
import random
import json
import time

# url = 'http://localhost:5555/datawriter'
url = 'https://brainrider.herokuapp.com/datawriter'

i = 0
while True:
    i += 1
    course = random.choice(["Forward", "Backward", "Left", "Right"])
    data = {
        "id": i,
        "data": course
    }

    req = requests.post(url, json=data)

    time.sleep(15)
