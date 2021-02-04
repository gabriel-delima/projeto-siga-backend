from ..extensions import db
from ..association import association_table

#### Alunos
# id -> identificação
# nome -> string indicando o nome do aluno
# cpf -> inteiro indicando o cpf do aluno
# nascimento -> data do seu nascimento
# sexo -> string indicando o sexo do aluno
# período -> string indicando o período de ingresso do aluno no formato "xxxx.x", ex: 2020.1
# curso -> string indicando o curso da ufrj
# turma -> relação com as turmas em que o aluno está inscrito
# boletim_id -> relação com seu boletim específico.
class Alunos(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30), nullable = False)
    cpf = db.Column(db.Integer, unique = True, nullable = False)
    nascimento = db.Column(db.Date, nullable = False)
    sexo = db.Column(db.String(10), nullable = False)
    período = db.Column(db.String(6), nullable = False)
    curso = db.Column(db.String(30), nullable = False)
    
    # alunos(many) <-> turma(many)
    turmas = db.relationship('Turmas', secondary=association_table , backref='turma')

    # Boletim(one) <-> Aluno(one)
    boletim_id = db.Column(db.Integer, db.ForeignKey('boletins.id'))