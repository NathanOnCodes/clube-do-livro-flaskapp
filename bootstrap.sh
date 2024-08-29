#/bin/bash
flask db init
flask db migrate -m "init db"
flask db upgrade