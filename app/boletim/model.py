from ..extensions import db

#### Resultados
#### tabela com o resultado obtido em uma matéria específica
# id -> identificação
# grau -> nota recebida pelo aluno
# aprovacao -> indica se o aluno foi aprovado. True:Aprovado , False:Reprovado
# materia_id -> relação com a matéria específica que o aluno obteve esse resultado
# periodo_id -> relação com o período específico de realização da matéria
class Resultados(db.Model):
    __tablename__ = 'resultado'
    id = db.Column(db.Integer, primary_key = True)
    grau = db.Column(db.Integer, nullable = False)
    aprovacao = db.Column(db.Boolean, nullable = False) 

    # Resultados(Many) <-> Materia(one)    obs.: O aluno pode fazer a mesma matéria várias vezes
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'))

    # Resultados(Many) <-> Período(One) 
    periodo_id = db.Column(db.Integer, db.ForeignKey('periodos.id'))


#### Periodos
#### Tabela para dividir o boletim em grupos de períodos
# id -> identificação
# periodo_indicacao -> indicacao do período em questão como uma string no formato "xxxx.x", ex.: 2020.1
# resultados -> relação com os resultados obtidos nesse período específico
class Periodos(db.Model):
    __tablename__ = 'periodos'
    id = db.Column(db.Integer, primary_key = True)
    periodo_indicacao = db.Column(db.String(6), nullable = False)

    # Resultados(Many) <-> Período(One) 
    horario = db.relationship('Horario', backref = 'owner')

    # Boletim(one) <-> Períodos(many)
    boletim_id = db.Column(db.Integer, db.ForeignKey('boletins.id'))


#### Boletins
# id -> identificação
# periodo -> relação com cada período já cursado pelo aluno com seus respectivos resultados
# aluno_id -> relação com seu aluno específico
class Boletins(db.Model):
    __tablename__ = 'boletins'
    id = db.Column(db.Integer, primary_key = True)

    # Boletim(one) <-> Períodos(many)
    periodo = db.relationship('Periodos', backref = 'owner')

    # Boletim(one) <-> Aluno(one)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'))
