from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from flask_cors import CORS

# Init app
app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    content = db.Column(db.String(500))

    def __init__(self, name, content):
        self.name = name
        self.content = content


class NoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'content')


# Init schema
note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)


@app.route('/api/v1/notes', methods=['POST'])
def add_note():
    name = request.json['name']
    content = request.json['content']

    print(content)
    new_note = Note(name, content)

    db.session.add(new_note)
    db.session.commit()

    return note_schema.jsonify(new_note)


@app.route('/api/v1/notes', methods=['GET'])
def get_notes():
    all_notes = Note.query.all()
    result = notes_schema.dump(all_notes)
    return jsonify(result)


@app.route('/api/v1/note/<id>', methods=['GET'])
def get_note(id):
    note = Note.query.get(id)
    return note_schema.jsonify(note)


@app.route('/api/v1/note/<id>', methods=['PUT'])
def update_note(id):
    note = Note.query.get(id)
    name = request.json['name']
    content = request.json['content']

    note.name = name
    note.content = content
    db.session.commit()

    return note_schema.jsonify(note)


@app.route('/api/v1/note/<id>', methods=['DELETE'])
def delete_note(id):
    print(id)
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()

    return note_schema.jsonify(note)


# if __name__ == '__main__':
#    app.run()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=float(os.getenv('MY_PORT', '5000')))
