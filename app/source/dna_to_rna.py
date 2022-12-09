from data.app import app
from conn import cursor


def convert_dna_to_rna(dna: str) -> str:
    try:
        with app.app_context():
            cursor.execute("SELECT * FROM dna")
            dna_db = cursor.fetchall()
            rna = ''
            for base in dna.upper():
                '''Iterating over DNA database to compare it with the input, then saving the corresponding id in rna_index variable'''
                for dna_row in dna_db:
                    if base == dna_row[1]:
                        rna_index = dna_row[0]
                        cursor.execute("SELECT * FROM rna")
                        rna_db = cursor.fetchall()
                        '''Searching the right rna_base by previously saved rna_index'''
                        for rna_row in rna_db:
                            if rna_index == rna_row[2]:
                                rna += rna_row[1]
            print(f'mRNA sequence is: {rna}')
            return rna

    except(TypeError, AttributeError):
        return 'Please provide DNA sequence in "ACGT" format'


if __name__ == '__main__':
    user_input = input('Enter DNA sequence: ')
    if user_input.isalpha():
        rna = convert_dna_to_rna(user_input)
    else:
        print('Please provide DNA sequence in "ACGT" format')
