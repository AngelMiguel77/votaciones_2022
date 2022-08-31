from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
from routes.candidato_route import candidato_module
from routes.partido_route import partido_module
from routes.mesa_route import mesa_module

config = dotenv_values('.env')
app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(candidato_module, url_prefix="/candidatos")
app.register_blueprint(partido_module, url_prefix="/partidos")
app.register_blueprint(mesa_module, url_prefix="/mesas")

@app.route('/')
def hello_world():
    dictToReturn = {'message': 'Hola mundo'}
    return jsonify(dictToReturn)

if __name__ == '__main__':
    app.run(host='localhost', port=config["PORT"], debug=False)