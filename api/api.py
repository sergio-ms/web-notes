from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
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
    content = db.Column(db.String(500), unique=True)

    def __init__(self, name, content):
        self.name = name
        self.content = content


class NoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'content')


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)


# Create some test data for our catalog in the form of a list of dictionaries.
notes = [
    {'id': 1,
     'name': 'A Fire Upon the Deep',
     'content': 'Vernor Vinge'
     },
    {'id': 2,
     'name': 'The Ones Who Walk Away From Omelas',
     'content': 'Ursula K. Le Guin'
     },
    {'id': 3,
     'name': 'Dhalgren',
     'content': 'Samuel R. Delany'
     }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/notes', methods=['GET'])
def api_all():
    return jsonify(notes)


@app.route('/api/v1/notes', methods=['POST'])
def add_note():
    # name = request.json['name']  # a multidict containing POST data
    # notes.append(data)
    # print(request)
    return jsonify(notes)


if __name__ == '__main__':
    app.run()
