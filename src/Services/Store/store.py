from flask import Flask, jsonify
from werkzeug.exceptions import NotFound

app = Flask(__name__)

stores = [
    {
        'id': 1,
        'name': 'flagship-SG',
        'address': 'Woodlands',
        'country': 'Singapore'
    },
    {
        'id': 2,
        'name': 'J-Square',
        'address': 'MacPherson',
        'country': 'Singapore'
    },
    {
        'id': 3,
        'name': 'Causeway Mall',
        'address': 'Johore Bahru',
        'country': 'Malaysia'
    }
]

@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores, 'total': len(stores)})


@app.route('/store/<id>', methods=['GET'])
def get_store(id):
    id = int(id)
    total_stores = len(stores)
    print(total_stores)
    if id - 1 not in range(total_stores):
        raise NotFound
    result = stores[id - 1] # temp hardcode by list index
    return jsonify({'store': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

