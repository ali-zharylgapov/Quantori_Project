import psycopg2
from app import app

conn = psycopg2.connect(
    database="test_1_db",
    host="db",
    user="postgres",
    password="postgres",
    port="5432"
        )

cursor = conn.cursor()


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


user_input = input('Enter RNA sequence: ')
print(convert_rna_to_protein(user_input))
