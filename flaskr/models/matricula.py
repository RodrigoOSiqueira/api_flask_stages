from flaskr.db import get_db


class Matricula:
    @staticmethod
    def cria_matricula(turma_id: int, nome_aluno: str):
        db = get_db()

        db.execute(
            'INSERT INTO Matricula (nome_aluno, turma_id) VALUES (?, ?)',
            (nome_aluno, turma_id)
        )
        db.commit()

        return {
            "nome_aluno": nome_aluno,
            "turma_id": turma_id
        }
