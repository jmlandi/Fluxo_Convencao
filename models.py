from database import db

#Criando colunas banco de dados SQLITE
class Cadastro(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  number = db.Column(db.String())
  name = db.Column(db.String())
  fluxo = db.Column(db.String())
  datetime = db.Column(db.String())