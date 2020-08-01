from flaskr.db import get_db


class Curso:
    @staticmethod
    def cria_curso(dados_curso: dict) ->dict:
        db = get_db()
        nome_curso = dados_curso.get('nome')
        descricao_curso = dados_curso.get('descricao')

        db.execute(
            'INSERT INTO Curso (nome, descricao) VALUES (?, ?)',
            (nome_curso, descricao_curso)
        )
        db.commit()

        return dados_curso

    @staticmethod
    def pega_curso_id(curso_id: int):
        db = get_db()
        curso = db.execute(
            'SELECT * FROM Curso WHERE id = ?', (curso_id,)
        ).fetchone()

        return curso

    def atualiza_curso(self, curso_id, dados_curso):
        db = get_db()
        nome_curso = dados_curso.get('nome')
        descricao_curso = dados_curso.get('descricao')

        db.execute(
            'UPDATE Curso set nome = ?, descricao = ? WHERE id = ?',
            (nome_curso, descricao_curso, curso_id)
        )
        db.commit()
        curso_atualizado = self.pega_curso_id(curso_id)

        return curso_atualizado

    def deleta_curso(self, curso_id):
        db = get_db()
        db.execute('DELETE FROM Curso WHERE id = ?', (curso_id,))
        db.commit()

        return 'Curso deletado'

    @staticmethod
    def lista_cursos(limit, offset):
        db = get_db()
        lista_cursos = db.execute(
            f'SELECT * FROM Curso LIMIT {offset}, {limit}'
        ).fetchall()
        
        return lista_cursos
