from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields, reqparse


app = Flask(__name__)
api = Api(app, version='1.0', title='hello world!', description='hello')
ns  = api.namespace('hello', description='hello') #namespace


parser = reqparse.RequestParser()
parser.add_argument('sentence', type=str, required=True, help='hello sentence')

@ns.route('/argparse')
class ArgparseExample(Resource):
    
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        sentence_input = args['sentence']
        return jsonify({'return': sentence_input + ' hello world!'})


api_input = api.model('sentence', {
    'sentence': fields.String(required=True, description='sentence', example='hello')
})

@ns.route('/api')
class ApiExample(Resource):
    
    @api.expect(api_input)
    def post(self):
        sentence_input = request.json['sentence']
        return jsonify({'return': sentence_input + ' hello world!'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2431, threaded=False)
