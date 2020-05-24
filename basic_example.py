from flask import Flask, request
from flask_restplus import Api, Resource, fields


app = Flask(__name__)
api = Api(app, version='1.0', title='hello world!', description='hello')
ns  = api.namespace('hello', description='hello') #namespace


resource_input = api.model('input', {
    'sentence': fields.String(required=True, description='sentence')
})


@ns.route('/')
class HelloWorld(Resource):
    
    def get(self):
        return 'hello world!'
    
    @api.expect(resource_input)
    def post(self):
        print(request.json['sentence'])
        return 'hello world! post'



if __name__ == '__main__':
    app.run(debug=True)