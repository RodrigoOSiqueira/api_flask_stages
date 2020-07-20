from flaskr.db import get_db


class Matricula:
    @staticmethod
    def cria_matricula(turma_id: int, nome: str):
        db = get_db()

        db.execute(
            'INSERT INTO Matricula (nome, turma_id) VALUES (?, ?)',
            (nome, turma_id)
        )
        db.commit()

        return {
            "nome": nome,
            "turma_id": turma_id
        }

    @staticmethod
    def matriculas_turma(turma_id):
        db = get_db()
        list_matriculas = db.execute(
            'SELECT * FROM Matricula m JOIN'
            ' Turma t ON m.turma_id = t.id'
            ' WHERE t.id = ?',
            (turma_id,)
        ).fetchall()

        return list_matriculas
