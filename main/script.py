import psycopg2
import numpy as np
import matplotlib.pyplot as plt

from data.app import app


def get_connection():
    try:
        return psycopg2.connect(
            database="test_1db",
            host="127.0.0.1",
            user="postgres",
            password="postgres",
            port="5432"
        )
    except psycopg2.OperationalError:
        return False


conn = get_connection()
cursor = conn.cursor()

if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")


def convert_dna_to_rna(dna: str) -> str:
    with app.app_context():
        cursor.execute("SELECT * FROM dna")
        dna_db = cursor.fetchall()
        rna = ''
        for base in dna.upper():
            for dna_row in dna_db:
                if base == dna_row[1]:
                    rna_index = dna_row[0]
                    cursor.execute("SELECT * FROM rna")
                    rna_db = cursor.fetchall()
                    for rna_row in rna_db:
                        if rna_index == rna_row[2]:
                            rna += rna_row[1]
        return rna


def convert_rna_to_protein(rna: str) -> str:
    with app.app_context():
        cursor.execute("SELECT * FROM codons")
        codon_db = cursor.fetchall()
        protein = ''
        for i in range(0, len(rna), 3):
            for codon_row in codon_db:
                new_codon = rna[i:i+3]
                if new_codon == codon_row[1]:
                    amino_id = codon_row[2]
                    cursor.execute("SELECT * FROM amino")
                    amino_db = cursor.fetchall()
                    for amino_row in amino_db:
                        if amino_id == amino_row[0]:
                            protein += amino_row[1]
        return protein


def gc_content(dna: str, step: int = 100):
    sliced_dna = np.array([i for i in dna])
    gc = np.array([])
    position = np.array([])
    position_count = 0

    for i in range(0, len(sliced_dna), step):
        step_slice = sliced_dna[i:i+step]
        a = np.char.count(step_slice, 'C')
        b = np.char.count(step_slice, 'G')
        result = ((np.sum(a) + np.sum(b)) / step) * 100
        gc = np.append(gc, int(result))

        position_count += step
        position = np.append(position, position_count)

    x = position
    y = gc
    plt.plot(x, y)
    plt.xlabel('Genome position')
    plt.ylabel('GC-ratio(%)')
    plt.title('GC-content ratio')
    plt.savefig('../GC-content_ratio.jpg')


conn.close()

doc = open('../genomic.fna', 'r').read().splitlines()[1:]
sars_cov_2 = ''.join(doc)
gc_content(sars_cov_2)

