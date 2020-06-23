from flask import jsonify, request
from flask_restful import reqparse, abort, fields, marshal_with, Resource, Api
from app import db, create_app
from app.models import Store
import os

config_name = os.getenv('APP_ENV')
app = create_app(config_name)
api = Api(app)


def get_store_or_abort_if_not_found(store_id):
    store_result = Store.query.get(store_id)
    if store_result is None:
        abort(404, message='Store {} does not exist'.format(store_id))
    return store_result


# Request arguments
parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('address', type=str)
parser.add_argument('country', type=str)

# Marshall model for response
store_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'address': fields.String,
    'country': fields.String,
}


class StoreListResource(Resource):
    @marshal_with(store_fields)
    def get(self):
        stores_list = Store.query.all()
        return stores_list

    def post(self):
        request.get_json(force=True)
        args = parser.parse_args()
        new_store = Store(name=args['name'],
                          address=args['address'],
                          country=args['country'])
        db.session.add(new_store)
        db.session.commit()
        return get_store_or_abort_if_not_found(new_store.id).serialize(), 201


class StoreResource(Resource):
    @marshal_with(store_fields)
    def get(self, store_id):
        return get_store_or_abort_if_not_found(store_id)

    def delete(self, store_id):
        get_store_or_abort_if_not_found(store_id)
        Store.query.filter_by(id=store_id).delete()
        db.session.commit()
        return '', 204

    def put(self, store_id):
        request.get_json(force=True)
        args = parser.parse_args()
        update_store = get_store_or_abort_if_not_found(store_id)
        update_store.name = args['name']
        update_store.address = args['address']
        update_store.country = args['country']
        db.session.commit()
        return update_store.serialize(), 201


# Health-check endpoint
@app.route('/', methods=['GET'])
@app.route('/health', methods=['GET'])
def health_check():
    health = {
        'service': 'Store',
        'status': 'healthy'
    }
    return jsonify(health)


# Add api resource routing
api.add_resource(StoreListResource, '/store')
api.add_resource(StoreResource, '/store/<int:store_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
