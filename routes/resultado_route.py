from flask import jsonify, request, Blueprint
from controllers.resultado_controller import ResultadoController

resultado_module = Blueprint('resultados', __name__)
controller = ResultadoController()

@resultado_module.get('/')
def get():
    return jsonify(controller.get()), 201
    
@resultado_module.post('/mesa/<string:mesa_id>/candidato/<string:candidato_id>')
def create(mesa_id, candidato_id):
    return jsonify(controller.create(request.get_json(),mesa_id, candidato_id)), 201
    
@resultado_module.get('/<string:id>')
def show(id):
    return jsonify(controller.get_by_id(id))
    
@resultado_module.put('/<string:id>')
def update(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@resultado_module.delete('/<string:id>')
def delete(id):
    controller.delete(id)
    return jsonify({}), 204