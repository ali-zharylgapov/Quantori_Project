from data.app import app
from conn import conn, cursor


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


if __name__ == '__main__':
    user_input = input('Enter DNA sequence: ')
    rna = convert_dna_to_rna(user_input)
    print(f'mRNA sequence is: {rna}')
