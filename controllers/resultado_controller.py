from db.resultado_repository import ResultadoRepository
from db.mesa_repository import MesaRepository
from db.candidato_repository import CandidatoRepository

from models.mesa_model import MesaModel
from models.resultado_model import ResultadoModel
from models.candidato_model import CandidatoModel

class ResultadoController():

    def __init__(self) -> None:
        self.repo = ResultadoRepository()
        self.repo_mesa = MesaRepository()
        self.repo_candidato = CandidatoRepository()

    def get(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        return self.repo.get_by_id(id)

    def create(self, data, mesa_id, candidato_id):
        resultado = ResultadoModel(data)
        mesa = self.repo_mesa.get_by_id(mesa_id)
        resultado.mesa = MesaModel(mesa)
        print (mesa_id)
        
        candidato = self.repo_candidato.get_by_id(candidato_id)
        print (candidato_id)
        resultado.candidato = CandidatoModel(candidato)
        
        return {
            "id": self.repo.save(resultado)
        }

    def update(self, id, data):
        resultado = ResultadoModel(data)
        self.repo.update(id, resultado)

    def delete(self, id):
        self.repo.delete(id)