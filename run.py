from app import create_app
from app import db
from flask.cli import with_appcontext
import click

app = create_app()

@click.command(name="create_tables")
@with_appcontext
def create_tables():
    db.create_all()


app.cli.add_command(create_tables)

if __name__ == "__main__":
    app.run(debug=True)
