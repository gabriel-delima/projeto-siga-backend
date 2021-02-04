from .extensions import db

association_table = db.Table('association',db.Model.metadata,
                    db.Column('alunos',db.Integer, db.ForeignKey('alunos.id')),
                    db.Column('turmas',db.Integer,db.ForeignKey('turmas.id')))

