import json

def read_json_animal(X):
    with open('info/file.json', 'r') as f:
        obj = json.load(f)
    for val in obj['animals']:
        if val['id'] == X:
            return val

def read_json_family(X):
    with open('info/file.json', 'r') as f:
        obj = json.load(f)
    answer = []
    for val in obj['animals']:
        if val['family'] == X:
            answer.append(val['name'])
    return answer
