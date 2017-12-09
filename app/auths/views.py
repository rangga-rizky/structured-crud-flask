from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.auths.forms import RegisterForm, LoginForm
from app.models import User
from app.auths.decorators import requires_login
import datetime

mod = Blueprint('auths', __name__, url_prefix=None)

@mod.route('/dashboard/')
@requires_login
def dashboard():
  return render_template("dashboard.html", user=g.user)

@mod.route('/')
def home():
  return render_template("home.html")

@mod.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])

@mod.route('/login/', methods=['GET', 'POST'])
def login():
  form = LoginForm(request.form)
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and check_password_hash(user.password, form.password.data):
      session['user_id'] = user.id
      flash('Welcome %s' % user.email)
      return redirect(url_for('auths.dashboard'))    
    return redirect(url_for('.home'))
    flash('Wrong email or password', 'error-message')
  return render_template("auths/login.html", form=form)

@mod.route('/register/', methods=['POST','GET'])
def register():
  form = RegisterForm(request.form)
  if form.validate_on_submit():
    user = User(email=form.email.data, \
      password=generate_password_hash(form.password.data),created_at=datetime.datetime.now() )
    db.session.add(user)
    db.session.commit()
    session['user_id'] = user.id
    flash('Thanks for registering')
    return redirect(url_for('auths.dashboard'))    
  return render_template("auths/register.html", form=form)

@mod.route("/logout")
def logout():
    session.pop('user_id', None)
    return home()