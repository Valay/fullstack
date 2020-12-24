from flask import Flask, render_template, request, jsonify, abort, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__, static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://valashah@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
    completed = db.Column(db.Boolean(), nullable=False, default=False)

    def __repr__(self):
        return f'<Todo Item: {self.id} {self.description}>'

@app.route('/todos/deleted', methods=['DELETE'])
def onDelete():
    body = {}
    error = False
    try:
        delete_id = request.get_json()['id']
        Todo.query.filter_by(id=delete_id).delete()
        db.session.commit()
        body['success'] = True
    except:
        print("Unexpected Error occurred:", sys.exec_info()[0])
        db.session.rollback()
        error = True
        body['success'] = False
    finally:
        db.session.close()
    if error:
        abort(400)
    return jsonify(body)

@app.route('/todos/completed', methods=['POST'])
def onCompleteCheck():
    body = {}
    error = False
    try:
        completed = request.get_json()['completed']
        id = request.get_json()['id']
        todoItem = Todo.query.get(id)
        todoItem.completed = completed
        db.session.commit()
        body['completed'] = completed
    except:
        print("Unexpected Error occurred:", sys.exec_info()[0])
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        abort(400)
    return jsonify(body)

@app.route('/todos/create', methods=['POST'])
def create():
    body = {}
    error = False
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
        body['id'] = todo.id
    except:
        print("Unexpected Error occurred:", sys.exec_info()[0])
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    if error:
        abort(400)
    return jsonify(body)

@app.route('/')
def index():
    data = Todo.query.order_by('id').all()
    return render_template('index.html', data=data)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

app.run('127.0.0.1', debug=True)