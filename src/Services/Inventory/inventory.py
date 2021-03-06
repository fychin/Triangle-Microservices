from flask import Flask, jsonify
from werkzeug.exceptions import NotFound

app = Flask(__name__)

inventory = [
    {
        'id': 1,
        'name': 'Jeans',
        'quantity': 30
    },
    {
        'id': 2,
        'name': 'Polo Shirt',
        'quantity': 81
    },
    {
        'id': 3,
        'name': 'Hoodie',
        'quantity': 5
    }
]

@app.route('/', methods=['GET'])
@app.route('/health', methods=['GET'])
def health_check():
    health = {'status': 'healthy'}
    return jsonify(health)


@app.route('/inventory', methods=['GET'])
def get_inventory_list():
    return jsonify({'inventory': inventory, 'total': len(inventory)})


@app.route('/inventory/<id>', methods=['GET'])
def get_inventory(id):
    id = int(id)
    total_inventory = len(inventory)
    print(total_inventory)
    if id - 1 not in range(total_inventory):
        raise NotFound
    result = inventory[id - 1] # temp hardcode by list index
    return jsonify({'inventory': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

