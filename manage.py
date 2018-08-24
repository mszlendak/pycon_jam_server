from flask import Flask
from flask_restplus import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


@api.route('/userinfo')
class UserInfo(Resource):
    def get(self):
        return {
	       'login': 'testStrig',
	       'points': 213213,
	       'stats': {
		    'strength': 54,
		    'dexterity': 54,
		    'stamina': 54,
		    'initiative': 47
		    },
		'items': list(),
		'process_ogoing': list(),
		'process_available': list()
    }



if __name__ == '__main__':
    app.run()
