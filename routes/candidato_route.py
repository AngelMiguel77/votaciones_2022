from flask import jsonify, request, Blueprint
from controllers.candidato_controller import CandidatoController

candidato_module = Blueprint('candidatos', __name__)
controller = CandidatoController()

@candidato_module.get('/')
def get():
    return jsonify(controller.get()), 201
    
@candidato_module.post('/partido/<string:partido_id>')
def create(partido_id):
    return jsonify(controller.create(request.get_json(), partido_id)), 201
    
@candidato_module.get('/<string:id>')
def show(id):
    return jsonify(controller.get_by_id(id))
    
@candidato_module.put('/<string:id>')
def update(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@candidato_module.delete('/<string:id>')
def delete(id):
    controller.delete(id)
    return jsonify({}), 204