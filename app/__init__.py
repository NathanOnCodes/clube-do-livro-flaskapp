from flask import Flask
from flask_restx import Api
from .extensions import db
from .extensions import migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app, version='1.0', title='Book Ranking API', description='API para ranking de livros')

    from .resources.book import api as book_ns
    api.add_namespace(book_ns, path='/books')
    return app

