class CursoSerializer:
    @staticmethod
    def serialize_curso(curso):
        return {
            "id": curso['id'],
            "nome": curso['nome'],
            "descricao": curso['descricao']
        }
