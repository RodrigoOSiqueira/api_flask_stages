from flask import Blueprint, request

from flaskr.models import Curso
from flaskr.serializers import CursoSerializer

bp_curso = Blueprint('curso', __name__, url_prefix='/curso')


@bp_curso.route('/<int:curso_id>/', methods=['GET'])
def pega_curso(curso_id):
    curso = Curso.pega_curso_id(curso_id)
    if not curso:
        return '', 204

    return CursoSerializer.serialize_curso(curso)

@bp_curso.route('/criar/', methods=['POST'])
def cria_curso():
    dados = request.json

    if not dados.get('nome') or not dados.get('descricao'):
        return 'Dados incompletos', 400

    novo_curso = Curso.cria_curso(dados)

    return novo_curso

@bp_curso.route('/<int:curso_id>', methods=['PUT'])
def atualiza_curso(curso_id):
    dados = request.json

    if not Curso().pega_curso_id(curso_id):
        return 'Curso não existente', 404

    if not dados.get('nome') and not dados.get('descricao'):
        return 'Dados incompletos', 400

    curso_atualizado = Curso().atualiza_curso(curso_id, dados)

    return CursoSerializer.serialize_curso(curso_atualizado)

@bp_curso.route('/<int:curso_id>', methods=['DELETE'])
def deleta_curso(curso_id):
    if not Curso().pega_curso_id(curso_id):
        return 'Curso não existente', 404

    return Curso().deleta_curso(curso_id), 200

@bp_curso.route('/', methods=['GET'])
def lista_cursos():
    cursos = Turma.lista_cursos()

    return CursoSerializer().serialize(cursos)
