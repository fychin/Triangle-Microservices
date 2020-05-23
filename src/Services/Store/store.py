from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Resource, Api
from werkzeug.exceptions import NotFound

app = Flask(__name__)
api = Api(app)

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

def abort_if_store_not_found(store_id):
    if store_id not in range(1, len(stores)+1):
        abort(404, message='Store {} does not exist'.format(store_id))

# Request arguments
parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('address', type=str)
parser.add_argument('country', type=str)

class StoreList(Resource):
    def get(self):
        return {'stores': stores, 'total': len(stores)}
    
    def post(self):
        request.get_json(force=True)
        args = parser.parse_args()
        new_store = {
            'id': len(stores)+1,
            'name': args['name'],
            'address': args['address'],
            'country': args['country'],
        }
        stores.append(new_store)
        return stores[len(stores)-1], 201


class Store(Resource):
    def get(self, store_id):
        abort_if_store_not_found(store_id)
        index = store_id - 1
        return stores[index]

    def delete(self, store_id):
        abort_if_store_not_found(store_id)
        index = store_id - 1
        del stores[index]
        return '', 204

    def put(self, store_id):
        request.get_json(force=True)
        args = parser.parse_args()
        updated_store = {
            'id': store_id,
            'name': args['name'],
            'address': args['address'],
            'country': args['country'],
        }
        index = store_id - 1
        stores[index] = updated_store
        return updated_store, 201


# Health-check endpoint
@app.route('/', methods=['GET'])
@app.route('/health', methods=['GET'])
def health_check():
    health = {'status': 'healthy'}
    return jsonify(health)


# Add api resource routing
api.add_resource(StoreList, '/store')
api.add_resource(Store, '/store/<int:store_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

