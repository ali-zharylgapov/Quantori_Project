import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class DNA(db.Model):
    base = db.Column(db.String(1), primary_key=True)
    rna = db.relationship('RNA', back_populates='dna')

    def __repr__(self):
        return f'DNA base is: {self.base}'


class RNA(db.Model):
    base = db.Column(db.String(1), primary_key=True)
    dna_base = db.Column(db.Integer, db.ForeignKey('dna.base'))
    dna = db.relationship('DNA', back_populates='rna')

    def __repr__(self):
        return f'RNA base is: {self.base}'


with app.app_context():
    db.create_all()

    dna_A = DNA(base='A')
    dna_C = DNA(base='C')
    dna_G = DNA(base='G')
    dna_T = DNA(base='T')

    rna_A = RNA(base='A', dna_base='A')
    rna_C = RNA(base='C', dna_base='C')
    rna_G = RNA(base='G', dna_base='G')
    rna_U = RNA(base='U', dna_base='T')

    db.session.add_all([dna_A, dna_C, dna_G, dna_T])
    db.session.add_all([rna_A, rna_C, rna_G, rna_U])

    db.session.commit()
