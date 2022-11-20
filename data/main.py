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
    codon = db.relationship('Codons', backref='codon_name')

    def __repr__(self):
        return f'Amino Acid is: {self.amino_acid}'


class Codons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codon = db.Column(db.String(3))
    amino_acid_id = db.Column(db.String, db.ForeignKey('amino.id'))

    def __repr__(self):
        return f'Codon is: {self.codon}'


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

    amino_acid_s = Amino(amino_acid='S')
    amino_acid_l = Amino(amino_acid='L')
    amino_acid_c = Amino(amino_acid='C')
    amino_acid_w = Amino(amino_acid='W')
    amino_acid_e = Amino(amino_acid='E')
    amino_acid_d = Amino(amino_acid='D')
    amino_acid_p = Amino(amino_acid='P')
    amino_acid_v = Amino(amino_acid='V')
    amino_acid_n = Amino(amino_acid='N')
    amino_acid_m = Amino(amino_acid='M')
    amino_acid_k = Amino(amino_acid='K')
    amino_acid_y = Amino(amino_acid='Y')
    amino_acid_i = Amino(amino_acid='I')
    amino_acid_q = Amino(amino_acid='Q')
    amino_acid_f = Amino(amino_acid='F')
    amino_acid_r = Amino(amino_acid='R')
    amino_acid_t = Amino(amino_acid='T')
    amino_acid_end = Amino(amino_acid='.')
    amino_acid_a = Amino(amino_acid='A')
    amino_acid_g = Amino(amino_acid='G')
    amino_acid_h = Amino(amino_acid='H')

    codon_1 = Codons(codon='UCU', amino_acid_id='S')
    codon_2 = Codons(codon='UCC', amino_acid_id='S')
    codon_3 = Codons(codon='UCA', amino_acid_id='S')
    codon_4 = Codons(codon='UCG', amino_acid_id='S')
    codon_5 = Codons(codon='AGU', amino_acid_id='S')
    codon_6 = Codons(codon='AGC', amino_acid_id='S')
    codon_7 = Codons(codon='UUA', amino_acid_id='L')
    codon_8 = Codons(codon='UUG', amino_acid_id='L')
    codon_9 = Codons(codon='CUU', amino_acid_id='L')
    codon_10 = Codons(codon='CUC', amino_acid_id='L')
    codon_11 = Codons(codon='CUA', amino_acid_id='L')
    codon_12 = Codons(codon='CUG', amino_acid_id='L')
    codon_13 = Codons(codon='UGU', amino_acid_id='C')
    codon_14 = Codons(codon='UGC', amino_acid_id='C')
    codon_15 = Codons(codon='UGG', amino_acid_id='W')
    codon_16 = Codons(codon='GAA', amino_acid_id='E')
    codon_17 = Codons(codon='GAG', amino_acid_id='E')
    codon_18 = Codons(codon='GAU', amino_acid_id='D')
    codon_19 = Codons(codon='GAC', amino_acid_id='D')
    codon_20 = Codons(codon='CCU', amino_acid_id='P')
    codon_21 = Codons(codon='CCC', amino_acid_id='P')
    codon_22 = Codons(codon='CCA', amino_acid_id='P')
    codon_23 = Codons(codon='CCG', amino_acid_id='P')
    codon_24 = Codons(codon='GUU', amino_acid_id='V')
    codon_25 = Codons(codon='GUC', amino_acid_id='V')
    codon_26 = Codons(codon='GUA', amino_acid_id='V')
    codon_27 = Codons(codon='GUG', amino_acid_id='V')
    codon_28 = Codons(codon='AAU', amino_acid_id='N')
    codon_29 = Codons(codon='AAC', amino_acid_id='N')
    codon_30 = Codons(codon='AUG', amino_acid_id='M')
    codon_31 = Codons(codon='AAA', amino_acid_id='K')
    codon_32 = Codons(codon='AAG', amino_acid_id='K')
    codon_33 = Codons(codon='UAU', amino_acid_id='Y')
    codon_34 = Codons(codon='UAC', amino_acid_id='Y')
    codon_35 = Codons(codon='AUU', amino_acid_id='I')
    codon_36 = Codons(codon='AUC', amino_acid_id='I')
    codon_37 = Codons(codon='AUA', amino_acid_id='I')
    codon_38 = Codons(codon='CAA', amino_acid_id='Q')
    codon_39 = Codons(codon='CAG', amino_acid_id='Q')
    codon_40 = Codons(codon='UUU', amino_acid_id='F')
    codon_41 = Codons(codon='UUC', amino_acid_id='F')
    codon_42 = Codons(codon='CGU', amino_acid_id='R')
    codon_43 = Codons(codon='CGC', amino_acid_id='R')
    codon_44 = Codons(codon='CGA', amino_acid_id='R')
    codon_45 = Codons(codon='CGG', amino_acid_id='R')
    codon_46 = Codons(codon='AGA', amino_acid_id='R')
    codon_47 = Codons(codon='AGG', amino_acid_id='R')
    codon_48 = Codons(codon='ACU', amino_acid_id='T')
    codon_49 = Codons(codon='ACC', amino_acid_id='T')
    codon_50 = Codons(codon='ACA', amino_acid_id='T')
    codon_51 = Codons(codon='ACG', amino_acid_id='T')
    codon_52 = Codons(codon='UAA', amino_acid_id='.')
    codon_53 = Codons(codon='UAG', amino_acid_id='.')
    codon_54 = Codons(codon='UGA', amino_acid_id='.')
    codon_55 = Codons(codon='GCU', amino_acid_id='A')
    codon_56 = Codons(codon='GCC', amino_acid_id='A')
    codon_57 = Codons(codon='GCA', amino_acid_id='A')
    codon_58 = Codons(codon='GCG', amino_acid_id='A')
    codon_59 = Codons(codon='GGU', amino_acid_id='G')
    codon_60 = Codons(codon='GGC', amino_acid_id='G')
    codon_61 = Codons(codon='GGA', amino_acid_id='G')
    codon_62 = Codons(codon='GGG', amino_acid_id='G')
    codon_63 = Codons(codon='CAU', amino_acid_id='H')
    codon_64 = Codons(codon='CAC', amino_acid_id='H')

    db.session.add_all([amino_acid_h, amino_acid_g, amino_acid_a, amino_acid_end, amino_acid_t, amino_acid_s, amino_acid_f, amino_acid_r, amino_acid_q, amino_acid_i, amino_acid_m, amino_acid_n, amino_acid_k, amino_acid_y, amino_acid_p, amino_acid_v, amino_acid_w, amino_acid_d, amino_acid_c, amino_acid_e, amino_acid_l])

    db.session.add_all([codon_1, codon_2, codon_3, codon_4, codon_5, codon_6, codon_7, codon_8, codon_9, codon_10, codon_11, codon_12, codon_13, codon_14, codon_15, codon_16, codon_17, codon_18, codon_19, codon_20, codon_21, codon_22, codon_23, codon_24, codon_25, codon_26, codon_27, codon_28, codon_29, codon_30, codon_31, codon_32, codon_33, codon_34, codon_35, codon_36, codon_37, codon_38, codon_39, codon_40, codon_41, codon_42, codon_43, codon_44, codon_45, codon_46, codon_47, codon_48, codon_49, codon_50, codon_51, codon_52, codon_53, codon_54, codon_55, codon_56, codon_57, codon_58, codon_59, codon_60, codon_61, codon_62, codon_63, codon_64])

    # db.session.commit()
