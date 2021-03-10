from flask import Flask
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)

names = {"Lucas":{"age":26,"gender":male}}
class HelloWorld(Resource):
    def get(self, name):
        return{"data": name}
    def post(self):
        return{"data": "postado"}
api.add_resource(HelloWorld, "/helloword<string:name>")
if __name__ == "__main__":
    app.run(debug=True)