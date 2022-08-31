from flask import jsonify, request, Blueprint
from controllers.mesa_controller import MesaController

mesa_module = Blueprint('mesas', __name__)
controller = MesaController()

@mesa_module.get('/')
def get():
    return jsonify(controller.get()), 201
    
@mesa_module.post('/')
def create():
    return jsonify(controller.create(request.get_json())), 201
    
@mesa_module.get('/<string:id>')
def show(id):
    return jsonify(controller.get_by_id(id))
    
@mesa_module.put('/<string:id>')
def update(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@mesa_module.delete('/<string:id>')
def delete(id):
    controller.delete(id)
    return jsonify({}), 204