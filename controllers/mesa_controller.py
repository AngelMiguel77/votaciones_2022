from models.mesa_model import MesaModel
from db.mesa_repository import MesaRepository

class MesaController():

    def __init__(self) -> None:
        self.repo = MesaRepository()

    def get(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data):
        mesa = MesaModel(data)
        return {"id": self.repo.save(mesa)}

    def update(self, id, data):
        mesa = MesaModel(data)
        self.repo.update(id, mesa)

    def delete(self, id):
        self.repo.delete(id)