import os
import requests
import base64
import json


lockfilepath=(os.path.join("\\",(os.getenv('LOCALAPPDATA')),r'Riot Games\Riot Client\Config\lockfile'))

def get_lockfile():
    if os.path.exists(os.path.join("\\",(os.getenv('LOCALAPPDATA')),r'Riot Games\Riot Client\Config\lockfile')):
        with open(lockfilepath) as lf:
            x=lf.read().split(":")
            keys=['name', 'PID', 'port', 'password', 'protocol']
            return(dict(zip(keys,x)))

    else:
        print("E1")


fin=get_lockfile()
print(fin)
headers = {}


def get_puuid():

    headers['Authorization'] = 'Basic ' + base64.b64encode(('riot:' + fin['password']).encode()).decode()
    response = requests.get("https://127.0.0.1:{port}/chat/v1/session".format(port=fin['port']), headers=headers, verify=False)
    return(response.json()['puuid'])

def getpresence():
    headers['Authorization'] = 'Basic ' + base64.b64encode(('riot:' + fin['password']).encode()).decode()
    response = requests.get("https://127.0.0.1:{port}/chat/v4/presences".format(port=fin['port']), headers=headers, verify=False)
    presences = response.json()
    for presence in presences['presences']:
        if presence['puuid'] == get_puuid():
            payload = (json.loads(base64.b64decode(presence['private'])))
            return payload
    
