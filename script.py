from data import tables


def convert_dna_to_rna():
    dna = input('Enter DNA sequence: ')
    rna = dna.translate(str.maketrans("tT", "uU"))
    '''
    I want to return correct RNA sequence in case DNA contains small letters 
    '''
    return rna


def convert_rna_to_protein():
    rna = input('Enter RNA sequence: ').upper()
    protein = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) == 3:
            protein.append(tables.codon_table.get(codon))
    result = ''.join(protein)
    return result
