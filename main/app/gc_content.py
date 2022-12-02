import numpy as np
import matplotlib.pyplot as plt


def gc_content(dna: str, step: int = 100):
    sliced_dna = np.array([i for i in dna])
    gc = np.array([])
    position = np.array([])
    position_count = 0

    for i in range(0, len(sliced_dna), step):
        step_slice = sliced_dna[i:i+step]
        c = np.char.count(step_slice, 'C')
        g = np.char.count(step_slice, 'G')
        result = ((np.sum(c) + np.sum(g)) / step) * 100
        gc = np.append(gc, int(result))

        position_count += step
        position = np.append(position, position_count)
    x = position
    y = gc
    plt.plot(x, y)
    plt.xlabel('Genome position')
    plt.ylabel('GC-ratio(%)')
    plt.title('GC-content ratio')
    plt.savefig('./GC-content_ratio.jpg')


user_input = input('Enter DNA sequence: ').rstrip()
gc_content(user_input)
