from data.main import RNA, Codons, app


def convert_dna_to_rna():
    with app.app_context():
        dna = input('Enter DNA sequence: ').upper()
        rna = []
        for base in dna:
            for data in RNA.query.all():
                if base == data.dna_base:
                    rna.append(data.base)
        result = ''.join(rna)
        return result


def convert_rna_to_protein():
    with app.app_context():
        rna = input('Enter RNA sequence: ').upper()
        protein = []
        for i in range(0, len(rna), 3):
            for data in Codons.query.all():
                new_codon = rna[i:i+3]
                if new_codon == data.codon:
                    protein.append(data.amino_acid_id)
        result = ''.join(protein)
        return result
