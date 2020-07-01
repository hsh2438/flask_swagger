import json
import requests


address = 'http://127.0.0.1:2431/hello'


def argparse(sentence):
    headers = {'accept': 'application/json'}
    response = requests.get(address+'/argparse?sentence=' + sentence, headers=headers)
    return json.loads(str(response.content, 'utf-8'))


def api(sentence):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data = {'sentence': sentence}
    response = requests.post(address+'/api', headers=headers, data=json.dumps(data))
    return json.loads(str(response.content, 'utf-8'))


if __name__ == '__main__':
    print(argparse('argparse'))
    print(api('api'))
