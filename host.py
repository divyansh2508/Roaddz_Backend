from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)

@app.route('/')
def index():
    return '<h1>The website Page</h1>'

@app.route('/app')
def myapp():
    return '<h1>The app page</h1>'

class Hello(Resource):
    def get(self):
        return jsonify({'message':'hello world'})

    def post(self):
        data=request.get_json()
        return jsonify({'data: data'})

class Square(Resource):
    def get(self,num):
        return jsonify({'square: num**2'})

api.add_resource(Hello,'/')
api.add_resource(Square, '/square/<int:num>')
# @app.route('/api')
# def api():
#     return '<h1>The API Thing here</h1>'


# @app.route('/post', methods=["POST"])
# def testpost():
#      input_json = request.get_json(force=True) 
#      c = {'sum':int(input_json['a']) + int(input_json['b']) }
#      return jsonify(c)


if __name__=='__main__':
    app.run(debug=True)