from flask import jsonify, request, Blueprint
from controllers.mesa_controller import MesaController

mesa_module = Blueprint('mesas', __name__)
controller = MesaController()

@mesa_module.get('/')
def get_candidato():
    return jsonify(controller.get()), 201
    
@mesa_module.post('/')
def create_candidato():
    return jsonify(controller.create(request.get_json())), 201
    
@mesa_module.get('/<string:id>')
def show_candidato(id):
    return jsonify(controller.get_by_id(id))
    
@mesa_module.put('/<string:id>')
def update_candidato(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@mesa_module.delete('/<string:id>')
def delete_candidato(id):
    controller.delete(id)
    return jsonify({}), 204