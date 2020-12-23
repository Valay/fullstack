from flask import Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://valashah@localhost:5432/todos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person id: {self.id}, name: {self.name}>'

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo Item: {self.id} {self.description}>'

db.create_all()

@app.route('/todos/create', methods=['POST'])
def create():
    body = {}
    error = False
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body[description] = todo.description
    except:
        print("Unexpected Error occcurred:", sys.exec_info()[0])
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        abort(400)
    return jsonify(body)

@app.route('/')
def index():
    data = Todo.query.all()
    return render_template('index.html', data=data)

app.run('127.0.0.1', debug=True)