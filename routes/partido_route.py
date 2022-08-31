from flask import jsonify, request, Blueprint
from controllers.partido_controller import PartidoController

partido_module = Blueprint('partidos', __name__)
controller = PartidoController()

@partido_module.get('/')
def get():
    return jsonify(controller.get()), 201
    
@partido_module.post('/')
def create():
    return jsonify(controller.create(request.get_json())), 201
    
@partido_module.get('/<string:id>')
def show(id):
    return jsonify(controller.get_by_id(id))
    
@partido_module.put('/<string:id>')
def update(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@partido_module.delete('/<string:id>')
def delete(id):
    controller.delete(id)
    return jsonify({}), 204