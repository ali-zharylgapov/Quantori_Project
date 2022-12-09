from app import db


class DNA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base = db.Column(db.String(1))
    rna = db.relationship('RNA', back_populates='dna')

    def __repr__(self):
        return f'DNA base is: {self.base}'


class RNA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base = db.Column(db.String(1))
    dna_base = db.Column(db.Integer, db.ForeignKey('dna.id'))
    dna = db.relationship('DNA', back_populates='rna')

    def __repr__(self):
        return f'RNA base is: {self.base}'


class Amino(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amino_acid = db.Column(db.String(1))
    codon = db.relationship('Codons', backref='amino')

    def __repr__(self):
        return f'Amino Acid is: {self.amino_acid}'


class Codons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codon = db.Column(db.String(3))
    amino_acid_id = db.Column(db.Integer, db.ForeignKey('amino.id'))

    def __repr__(self):
        return f'Codon is: {self.codon}'