from flask import Flask, request, jsonify, g
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)

class Hello(Resource):
    def get(self):
        return jsonify({'message':'hello world'})

    def post(self):
        f=open("2022-02-2209.02.02full.csv","r");
        # data=request.get_json()
        # return jsonify({'data: data'})

class Square(Resource):
    def get(self):

        input_json = request.get_json(force=True) 

        c = {
            'sum' : int(input_json['num'])**2 
        }
        
        f=open("sample.txt","w")
        #square=Square()
        f.write(str(c['sum']))
        f.close()
        return jsonify(c)

api.add_resource(Hello,'/')
api.add_resource(Square, '/square/')

if __name__=='__main__':
    app.run(debug=True)