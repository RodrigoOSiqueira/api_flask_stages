from flaskr.db import get_db


class Turma:
    @staticmethod
    def cria_turma(dados_turma: dict) -> dict:
        db = get_db()
        nome_turma = dados_turma.get('nome')
        curso_id = dados_turma.get('curso_id')

        db.execute(
            'INSERT INTO Turma (nome, curso_id) VALUES (?, ?)',
            (nome_turma, curso_id)
        )
        db.commit()

        return dados_turma

    @staticmethod
    def pega_turma_id(turma_id: int):
        db = get_db()
        turma = db.execute(
            'SELECT * FROM Turma WHERE id = ?', (turma_id,)
        ).fetchone()

        return turma
        
    def atualiza_turma(self, turma_id: id, dados_turma: dict):
        db = get_db()
        nome_turma = dados_turma.get('nome')

        db.execute(
            'UPDATE Turma set nome = ? WHERE id = ?',
            (nome_turma, turma_id)
        )
        db.commit()
        turma_atualizada = self.pega_turma_id(turma_id)

        return turma_atualizada
    
    def deleta_turma(self, turma_id):
        db = get_db()
        db.execute('DELETE FROM Turma WHERE id = ?', (turma_id,))
        db.commit()

        return 'Turma deletada'
