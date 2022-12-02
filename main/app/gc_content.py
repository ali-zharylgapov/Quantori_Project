import numpy as np
import matplotlib.pyplot as plt


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
    plt.title('GC_content ratio')
    plt.savefig('GC_content/GC-content_ratio.jpg')


doc = open('GC_content/GC_content_input.fna', 'r').read().splitlines()
sars_1 = ''.join(doc)
gc_content(sars_1)
