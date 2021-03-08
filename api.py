from flask import Flask, request
from flask_restful import Api, Resource

import socket

app = Flask(__name__)
api = Api(app)

class Servidor(Resource):
    def post(self):
        info_servidor = request.data
        ip_servidor = socket.gethostbyname(socket.gethostname())


nombre_archivo = ip_servidor + "_" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + ".csv"


api.add_resource(Servidor, '/infosistema')


if __name__ == '__main__':
    app.run(debug=True)
