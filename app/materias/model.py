from ..extensions import db

class Materias(db.Model):
    __tablename__ = 'materias'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30), nullable = False)
    codigo = db.Column(db.String(10), nullable = False, unique=True)
    creditos = db.Column(db.Integer)

    # materia(one) <-> turma(many)
    turma = db.relationship('Turmas', backref = 'owner')

    # Resultados(Many) <-> Materia(one)    obs.: O aluno pode fazer a mesma matéria várias vezes
    resultado = db.relationship('Resultados', backref = 'resultado')

