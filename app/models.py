from app import db

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(255))
  created_at = db.Column(db.DateTime)

  def __init__(self, name=None, email=None, password=None, created_at=None):
    self.name = name
    self.email = email
    self.password = password
    self.created_at = created_at


class Note(db.Model):
  __tablename__ = 'notes'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  body = db.Column(db.Text)

  def __init__(self, title=None, body=None):
    self.title = title
    self.body = body