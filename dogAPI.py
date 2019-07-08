import json
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

DB_FILENAME='dogs.json'
app = Flask(__name__)
api = Api(app)

#Read function
def load_data(f=DB_FILENAME):
    """
    Opens local json file and returns db
    """
    try:
        with open(f, 'r') as f:
            try:
                db = json.load(f)
            except ValueError:
                return None
        return db
    except FileNotFoundError:
        abort(501, message="Server error.")

#Write function
def write_data(db, f=DB_FILENAME):
    """
    Opens local json file and writes db back
    """
    try:
        with open(f, 'w') as f:
                json.dump(db, f)
    except FileNotFoundError:
        abort(501, message="Server error.")

#Set up keys
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('owner')
parser.add_argument('notes')

#Handle route with id
class OneDog(Resource):
    def get(self, dog_id):
        db = load_data()
        if dog_id not in db:
            abort(404, message="Dog {} doesn't exist".format(dog_id))
        return db[dog_id]

    def delete(self, dog_id):
        db = load_data()
        if dog_id not in db:
            abort(404, message="Dog {} doesn't exist".format(dog_id))
        del db[dog_id]
        write_data(db)
        return '', 204

    def put(self, dog_id):
        args = parser.parse_args()
        db = load_data()
        if dog_id not in db:
            abort(404, message="Dog {} doesn't exist".format(dog_id))
        dog = db[dog_id]
        dog['name'] = args['name'] if args['name'] is not None else dog['name']
        dog['owner'] = args['owner'] if args['owner'] is not None else dog['owner']
        dog['notes'] = args['notes'] if args['notes'] is not None else dog['notes']
        db[dog_id] = dog
        write_data(db)
        return db[dog_id], 201

#Handle route without id
class AllDogs(Resource):
    def get(self):
        return load_data()

    def post(self):
        args = parser.parse_args()
        db = load_data()
        if db is not None:
            dog_id = 'dog_' + str(int(max(db.keys()).lstrip('dog_')) + 1)
        else:
            dog_id = 'dog_1'
            db = {}
        db[dog_id] = {'name': args['name'],
               'owner': args['owner'],
               'notes': args['notes']}
        write_data(db)
        return db[dog_id], 201

#API Routing
api.add_resource(AllDogs, '/dogs')
api.add_resource(OneDog, '/dogs/<dog_id>')


if __name__ == '__main__':
    app.run(debug=True)
