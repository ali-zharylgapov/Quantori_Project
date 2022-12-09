import numpy as np
import matplotlib.pyplot as plt

from data.config import gc_content_address
'''Importing the location of user's input'''

def gc_content(dna: str, step: int = 100):
    sliced_dna = np.array([i for i in dna])
    gc = np.array([])
    position = np.array([])
    position_count = 0

    for i in range(0, len(sliced_dna), step):
        '''Calculating the gc-content for every step(100 bases)'''
        step_slice = sliced_dna[i:i+step]
        g = np.char.count(step_slice, 'G')
        c = np.char.count(step_slice, 'C')
        result = ((np.sum(c) + np.sum(g)) / step) * 100
        gc = np.append(gc, int(result))

        position_count += step
        position = np.append(position, position_count)

    '''Creating a graph based on the position and gc'''
    x = position
    y = gc
    plt.plot(x, y)
    plt.xlabel('Genome position')
    plt.ylabel('GC-ratio(%)')
    plt.title('GC_content ratio')
    plt.savefig('GC_content/GC-content_ratio.jpg')
    print('GC-ratio graph is saved at "GC_content/GC-content_ratio.jpg"')


doc = open(gc_content_address, 'r').read().splitlines()
# Reading the document from the second line if the first line is descriptive
if doc[0].startswith('>NC'):
    dna_sequence = ''.join(doc[1:])
else:
    dna_sequence = ''.join(doc)

gc_content(dna_sequence)
