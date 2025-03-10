import sqlite3
from flask import g

def get_db(app):
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    with app.app_context():
        db = get_db(app)
        # Check if the 'users' table already exists
        table_exists = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'").fetchone()
        if not table_exists:
            # Create the table if it doesn't exist
            with app.open_resource('../schema.sql', mode='r') as f:
                db.executescript(f.read())
            db.commit()