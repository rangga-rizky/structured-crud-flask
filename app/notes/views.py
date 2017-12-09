from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.models import Note,User
from app.notes.forms import NotesForm
from app.auths.decorators import requires_login

mod = Blueprint('notes', __name__, url_prefix='/notes')

@mod.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])

@mod.route('/', methods=['GET'])
@requires_login
def index():
  notes = Note.query.all()
  return render_template("notes/index.html",user=g.user,notes=notes)


@mod.route('/create/', methods=['GET','POST'])
@requires_login
def create():
  form = NotesForm(request.form)
  if form.validate_on_submit():
    note = Note(title=form.title.data,body=form.body.data  )
    db.session.add(note)
    db.session.commit()
    flash('Note Success created')
    return redirect(url_for('notes.index'))    
  return render_template("notes/create_notes.html", user=g.user ,form=form)

@mod.route('/edit', methods=['GET'])
@requires_login
def edit():
  form = NotesForm(request.form)   
  note = Note.query.filter_by(id=request.args.get('id')).first()
  return render_template("notes/edit_notes.html", user=g.user ,form=form,note=note)


@mod.route('/edit', methods=['POST'])
@requires_login
def update():
  form = NotesForm(request.form)   
  note = Note.query.filter_by(id=request.form.get('id')).first()
  if form.validate_on_submit():
    note.title = form.title.data
    note.body = form.body.data 
    db.session.commit()
    flash('Note Success created')
    return redirect(url_for('notes.index'))    
  return render_template("notes/edit_notes.html", user=g.user ,form=form,note=note)

@mod.route('/delete/', methods=['POST'])
@requires_login
def delete():
  note = Note.query.filter_by(id=request.form.get('id')).first()
  db.session.delete(note)
  db.session.commit()
  return redirect(url_for('notes.index')) 