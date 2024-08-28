from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # type: ignore

db = SQLAlchemy()
migrate = Migrate() 