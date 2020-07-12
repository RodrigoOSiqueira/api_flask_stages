from flask import jsonify


class CursoSerializer:
    @staticmethod
    def serialize_curso(curso):
        return {
            "id": curso['id'],
            "nome": curso['nome'],
            "descricao": curso['descricao']
        }
    
    @staticmethod
    def serialize_lista_cursos(cursos):
        return jsonify(list(map(
            lambda curso: {
                "id": curso['id'],
                "nome": curso['nome'],
                "descricao": curso['descricao']
            }, cursos
        )))

    def serialize(self, cursos):
        if isinstance(cursos, list):
            return self.serialize_lista_cursos(cursos)
        else:
            return self.serialize_curso(cursos)
