from flask import Flask
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return{"Olá mundo"}
api.add_resource(HelloWorld, "/helloword")
if __name__ == "__main__":
    app.run(debug=True)