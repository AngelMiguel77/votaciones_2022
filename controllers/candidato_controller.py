from models.candidato_model import CandidatoModel
from db.candidato_repository import CandidatoRepository

class CandidatoController():

    def __init__(self) -> None:
        self.repo = CandidatoRepository()

    def get(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data):
        candidato = CandidatoModel(data)
        return {"id": self.repo.save(candidato)}

    def update(self, id, data):
         candidato = CandidatoModel(data)
         self.repo.update(id, candidato)

    def delete(self, id):
        self.repo.delete(id)
