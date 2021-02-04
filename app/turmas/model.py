from ..extensions import db
from ..association import association_table


#### Horario
#### Tabela para especificar um horário durante a semana para uma turma
# id -> identificação
# dia_da_semana -> string que indica o dia da semana em questão
# horario_inicio -> string no formato "00:00:00" indicando o horário de inicio da aula nesse dia da semana
# horario_final -> string no formato "00:00:00" indicando o horário de término da aula nesse dia da semana
# turma_id -> indica a turma específica que esse horário se refere
class Horario(db.Model):
    __tablename__ = 'horarios'
    id = db.Column(db.Integer, primary_key = True)
    dia_da_semana = db.Column(db.String(20), nullable=False)
    horario_inicio = db.Column(db.String(8), nullable=False)
    horario_final = db.Column(db.String(8), nullable=False)

    # Horário(Many) <-> Turma(One)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'))


#### Turmas
#### 
# id -> identificação
# sala_de_aula -> string com a identificação da sala de aula da turma
# horario -> relação com cada horário de realização das aulas
# materia_id - > relação com a matéria específica dessa turma
# alunos -> relação com os alunos inscritos na matéria
# professor -> relação com o professor que dará aula nessa turma
class Turmas(db.Model):
    __tablename__ = 'turmas'
    id = db.Column(db.Integer, primary_key = True)
    sala_de_aula = db.Column(db.String(10), nullable = False)

    # Horário(Many) <-> Turma(One)
    horario = db.relationship('Horario', backref = 'horario')

    # materia(one) <-> turma(many)
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'))

    # alunos(many) <-> turma(many)
    alunos = db.relationship('Alunos', secondary=association_table , backref='aluno')

    # professor(one) <-> turma(many)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))
