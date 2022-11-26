from data.main import RNA, Codons, app
import numpy as np
import matplotlib.pyplot as plt


def convert_dna_to_rna(dna):
    with app.app_context():
        rna = []
        for base in dna.upper():
            for data in RNA.query.all():
                if base == data.dna_base:
                    rna.append(data.base)
        result = ''.join(rna)
        return result


def convert_rna_to_protein(rna):
    with app.app_context():
        protein = []
        for i in range(0, len(rna), 3):
            for data in Codons.query.all():
                new_codon = rna[i:i+3]
                if new_codon == data.codon:
                    protein.append(data.amino_acid_id)
        result = ''.join(protein)
        return result


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
    plt.savefig('GC-content_ratio.jpg')


doc = open('genomic.fna', 'r').read().splitlines()[1:]
sars_cov_2 = ''.join(doc)
print(sars_cov_2)

gc_content(sars_cov_2)
