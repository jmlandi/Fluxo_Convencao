from flask import Flask
from database import db
from controllers import Controller

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qEChL7wqsafR3SpF72cEA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def index():
    return Controller.index()

@app.route('/saida')
def saida():
  return Controller.saida()
    

@app.route('/create', methods=['POST'])
def create():
  return Controller.create()

@app.route('/cadastros')
def cadastros():
  return Controller.cadastros()

@app.route('/delete/<int:id>')
def delete(id):
  return Controller.delete(id)

with app.app_context():
  db.create_all()

app.run(host='0.0.0.0', port=81)
