from models.candidato_model import CandidatoModel
from models.partido_model import PartidoModel
from db.candidato_repository import CandidatoRepository
from db.partido_repository import PartidoRepository

class CandidatoController():

    def __init__(self) -> None:
        self.repo = CandidatoRepository()
        self.repo_partido = PartidoRepository()

    def get(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data, partido_id):
        candidato = CandidatoModel(data)
        partido = self.repo_partido.get_by_id(partido_id)
        candidato.partido = PartidoModel(partido)
        return {"id": self.repo.save(candidato)}

    def update(self, id, data):
         candidato = CandidatoModel(data)
         self.repo.update(id, candidato)

    def delete(self, id):
        self.repo.delete(id)
