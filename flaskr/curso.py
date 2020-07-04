from flask import Blueprint, request

bp_curso = Blueprint('curso', __name__)
cursos = {
    "data": [
        {   
            "id": 1,
            "nome": "API Flask",
            "descricao": "Um curso sobre Flask"
        },
        {   
            "id": 2,
            "nome": "Python3",
            "descricao": "Um curso sobre Python3"
        },
        {   
            "id": 3,
            "nome": "pipenv",
            "descricao": "Um curso sobre pipenv"
        }
    ]
}


@bp_curso.route('/curso/lista', methods=['GET'])
def lista_curos():
    return cursos
