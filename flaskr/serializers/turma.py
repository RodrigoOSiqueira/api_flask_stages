class TurmaSerializer:
    @staticmethod
    def serialize_turma(turma):
        return {
            "id": turma['id'],
            "nome": turma['nome'],
            "curso_id": turma['curso_id']
        }
