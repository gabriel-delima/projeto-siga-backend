from ..extensions import db


#### Professores
#### 
# id -> identificação
# nome -> string indicando o nome do professor
# cpf -> inteiro indicando o cpf do professor
# formacao -> string indicando a formacao do professor
# turma -> relação com as turmas que o professor dará aula
class Professores(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30), nullable = False)
    cpf = db.Column(db.Integer, unique = True)
    formacao = db.Column(db.String(30), nullable = False)

    # professor(one) <-> turma(many)
    turma = db.relationship('Turmas', backref = 'owner')