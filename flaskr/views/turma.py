from flask import Blueprint, request

from flaskr.models import Turma, Curso, Matricula
from flaskr.serializers import TurmaSerializer, MatriculaSerializer

bp_turma = Blueprint('turma', __name__, url_prefix='/turma')


@bp_turma.route('/criar/', methods=['POST'])
def cria_turma():
    dados = request.json

    if not dados.get('nome') or not dados.get('curso_id'):
        return 'Dados incompletos', 400

    if not Curso().pega_curso_id(dados.get('curso_id')):
        return 'Curso não cadastrado', 400
    
    nova_turma = Turma.cria_turma(dados)

    return nova_turma

@bp_turma.route('/<int:turma_id>', methods=['GET'])
def pega_turma(turma_id):
    turma = Turma.pega_turma_id(turma_id)
    print(turma)
    if not turma:
        return '', 204

    return TurmaSerializer.serialize_turma(turma)

@bp_turma.route('/<int:turma_id>', methods=['PUT'])
def atualiza_turma(turma_id):
    dados = request.json

    if not dados.get('nome'):
        return 'Dados incompletos', 400

    if not Turma.pega_turma_id(turma_id):
        return 'Turma não existente', 404

    turma_atualizada = Turma().atualiza_turma(turma_id, dados)

    return TurmaSerializer.serialize_turma(turma_atualizada)

@bp_turma.route('/<int:turma_id>', methods=['DELETE'])
def deleta_turma(turma_id):
    if not Turma.pega_turma_id(turma_id):
        return 'Turma não existe!', 404

    return Turma().deleta_turma(turma_id)

@bp_turma.route('/<int:turma_id>/matricula/criar', methods=['POST'])
def cria_matricula(turma_id):
    dados = request.json

    if not dados.get('nome'):
        return 'Dados incompletos', 400

    if not Turma().pega_turma_id(turma_id):
        return 'Turma não existe!', 404

    matricula = Matricula.cria_matricula(turma_id, dados.get('nome'))

    return matricula

@bp_turma.route('/<int:turma_id>/matriculas', methods=['GET'])
def matriculas_turma(turma_id):
    matriculas = Matricula.matriculas_turma(turma_id)

    return MatriculaSerializer().serialize(matriculas)
