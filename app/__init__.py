from flask import Flask
from .config import Config
from .extensions import db

from .alunos.model import Alunos
from .boletim.model import Boletins, Resultados, Periodos
from .materias.model import Materias
from .professores.model import Professores
from .turmas.model import Turmas, Horario
from .association import association_table

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    return app

