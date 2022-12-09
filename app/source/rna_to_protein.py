from data.app import app
from conn import cursor

codon_length = 3

def convert_rna_to_protein(rna: str) -> str:
    try:
        with app.app_context():
            cursor.execute("SELECT * FROM codons")
            codon_db = cursor.fetchall()
            protein = ''
            for i in range(0, len(rna), codon_length):
                '''Iterating over Codon database to compare the database Codon with the input Codon'''
                for codon_row in codon_db:
                    new_codon = rna[i:i+codon_length]
                    '''If the input codon is equal to the Codon in the Database, saving the corresponding id in amino_id'''
                    if new_codon == codon_row[1]:
                        amino_id = codon_row[2]
                        cursor.execute("SELECT * FROM amino")
                        amino_db = cursor.fetchall()
                        '''Iterating over Amino acid table to fetch the value by previously saved amino_id'''
                        for amino_row in amino_db:
                            if amino_id == amino_row[0]:
                                protein += amino_row[1]
            print(f'Protein sequence is: {protein}')
            return protein
    except(TypeError, AttributeError):
        return 'Please provide RNA sequence in "ACGU" format'


if __name__ == '__main__':
    user_input = input('Enter RNA sequence: ')
    if user_input.isalpha():
        protein = convert_rna_to_protein(user_input)
    else:
        print('Please provide RNA sequence in "ACGU" format')
