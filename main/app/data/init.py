import psycopg2
from flask.cli import FlaskGroup

from app import app, db
from models import DNA, RNA, Codons, Amino

cli = FlaskGroup(app)


@cli.command("create_seed_db")
def create_seed_db():

    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )

    conn.autocommit = True

    cursor = conn.cursor()

    sql = '''CREATE DATABASE test_1_db'''
    cursor.execute(sql)
    print('Database "test_1_db" created successfully')

    with app.app_context():
        db.create_all()

        dna_a = DNA(base='A')
        dna_c = DNA(base='C')
        dna_g = DNA(base='G')
        dna_t = DNA(base='T')

        rna_a = RNA(base='A', dna=dna_a)
        rna_c = RNA(base='C', dna=dna_c)
        rna_g = RNA(base='G', dna=dna_g)
        rna_t = RNA(base='U', dna=dna_t)

        db.session.add_all([dna_a, dna_c, dna_g, dna_t])
        db.session.add_all([rna_a, rna_c, rna_g, rna_t])

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

        codon_1 = Codons(codon='UCU', amino=amino_acid_s)
        codon_2 = Codons(codon='UCC', amino=amino_acid_s)
        codon_3 = Codons(codon='UCA', amino=amino_acid_s)
        codon_4 = Codons(codon='UCG', amino=amino_acid_s)
        codon_5 = Codons(codon='AGU', amino=amino_acid_s)
        codon_6 = Codons(codon='AGC', amino=amino_acid_s)
        codon_7 = Codons(codon='UUA', amino=amino_acid_l)
        codon_8 = Codons(codon='UUG', amino=amino_acid_l)
        codon_9 = Codons(codon='CUU', amino=amino_acid_l)
        codon_10 = Codons(codon='CUC', amino=amino_acid_l)
        codon_11 = Codons(codon='CUA', amino=amino_acid_l)
        codon_12 = Codons(codon='CUG', amino=amino_acid_l)
        codon_13 = Codons(codon='UGU', amino=amino_acid_c)
        codon_14 = Codons(codon='UGC', amino=amino_acid_c)
        codon_15 = Codons(codon='UGG', amino=amino_acid_w)
        codon_16 = Codons(codon='GAA', amino=amino_acid_e)
        codon_17 = Codons(codon='GAG', amino=amino_acid_e)
        codon_18 = Codons(codon='GAU', amino=amino_acid_d)
        codon_19 = Codons(codon='GAC', amino=amino_acid_d)
        codon_20 = Codons(codon='CCU', amino=amino_acid_p)
        codon_21 = Codons(codon='CCC', amino=amino_acid_p)
        codon_22 = Codons(codon='CCA', amino=amino_acid_p)
        codon_23 = Codons(codon='CCG', amino=amino_acid_p)
        codon_24 = Codons(codon='GUU', amino=amino_acid_v)
        codon_25 = Codons(codon='GUC', amino=amino_acid_v)
        codon_26 = Codons(codon='GUA', amino=amino_acid_v)
        codon_27 = Codons(codon='GUG', amino=amino_acid_v)
        codon_28 = Codons(codon='AAU', amino=amino_acid_n)
        codon_29 = Codons(codon='AAC', amino=amino_acid_n)
        codon_30 = Codons(codon='AUG', amino=amino_acid_m)
        codon_31 = Codons(codon='AAA', amino=amino_acid_k)
        codon_32 = Codons(codon='AAG', amino=amino_acid_k)
        codon_33 = Codons(codon='UAU', amino=amino_acid_y)
        codon_34 = Codons(codon='UAC', amino=amino_acid_y)
        codon_35 = Codons(codon='AUU', amino=amino_acid_i)
        codon_36 = Codons(codon='AUC', amino=amino_acid_i)
        codon_37 = Codons(codon='AUA', amino=amino_acid_i)
        codon_38 = Codons(codon='CAA', amino=amino_acid_q)
        codon_39 = Codons(codon='CAG', amino=amino_acid_q)
        codon_40 = Codons(codon='UUU', amino=amino_acid_f)
        codon_41 = Codons(codon='UUC', amino=amino_acid_f)
        codon_42 = Codons(codon='CGU', amino=amino_acid_r)
        codon_43 = Codons(codon='CGC', amino=amino_acid_r)
        codon_44 = Codons(codon='CGA', amino=amino_acid_r)
        codon_45 = Codons(codon='CGG', amino=amino_acid_r)
        codon_46 = Codons(codon='AGA', amino=amino_acid_r)
        codon_47 = Codons(codon='AGG', amino=amino_acid_r)
        codon_48 = Codons(codon='ACU', amino=amino_acid_t)
        codon_49 = Codons(codon='ACC', amino=amino_acid_t)
        codon_50 = Codons(codon='ACA', amino=amino_acid_t)
        codon_51 = Codons(codon='ACG', amino=amino_acid_t)
        codon_52 = Codons(codon='UAA', amino=amino_acid_end)
        codon_53 = Codons(codon='UAG', amino=amino_acid_end)
        codon_54 = Codons(codon='UGA', amino=amino_acid_end)
        codon_55 = Codons(codon='GCU', amino=amino_acid_a)
        codon_56 = Codons(codon='GCC', amino=amino_acid_a)
        codon_57 = Codons(codon='GCA', amino=amino_acid_a)
        codon_58 = Codons(codon='GCG', amino=amino_acid_a)
        codon_59 = Codons(codon='GGU', amino=amino_acid_g)
        codon_60 = Codons(codon='GGC', amino=amino_acid_g)
        codon_61 = Codons(codon='GGA', amino=amino_acid_g)
        codon_62 = Codons(codon='GGG', amino=amino_acid_g)
        codon_63 = Codons(codon='CAU', amino=amino_acid_h)
        codon_64 = Codons(codon='CAC', amino=amino_acid_h)

        db.session.add_all([amino_acid_h, amino_acid_g, amino_acid_a, amino_acid_end, amino_acid_t, amino_acid_s, amino_acid_f, amino_acid_r, amino_acid_q, amino_acid_i, amino_acid_m, amino_acid_n, amino_acid_k, amino_acid_y, amino_acid_p, amino_acid_v, amino_acid_w, amino_acid_d, amino_acid_c, amino_acid_e, amino_acid_l])

        db.session.add_all([codon_1, codon_2, codon_3, codon_4, codon_5, codon_6, codon_7, codon_8, codon_9, codon_10, codon_11, codon_12, codon_13, codon_14, codon_15, codon_16, codon_17, codon_18, codon_19, codon_20, codon_21, codon_22, codon_23, codon_24, codon_25, codon_26, codon_27, codon_28, codon_29, codon_30, codon_31, codon_32, codon_33, codon_34, codon_35, codon_36, codon_37, codon_38, codon_39, codon_40, codon_41, codon_42, codon_43, codon_44, codon_45, codon_46, codon_47, codon_48, codon_49, codon_50, codon_51, codon_52, codon_53, codon_54, codon_55, codon_56, codon_57, codon_58, codon_59, codon_60, codon_61, codon_62, codon_63, codon_64])

        db.session.commit()

        print('Database "test_1_db" seeded successfully')

        conn.close()


if __name__ == "__main__":
    cli()
