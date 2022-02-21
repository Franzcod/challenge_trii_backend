from flask import Flask

app = Flask(__name__)

api = 'https://rickandmortyapi.com/api/character/2'


@app.route('/')
def resp():
    import requests
    import json
    r = requests.get(api)
    data = r.json()
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
    

