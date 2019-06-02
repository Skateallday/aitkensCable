import sqlite3
from flask import Flask, g

app = Flask(__name__)

def get_db()
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect('static/user_db.db')
        g.db = db
    return db