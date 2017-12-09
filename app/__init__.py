from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.auths.views import mod as authsModule
from app.notes.views import mod as notesModule
app.register_blueprint(authsModule)
app.register_blueprint(notesModule)