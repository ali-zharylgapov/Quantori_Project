# Quantori Project

### About

Application that mimics DNA transcription and translation.

Deoxyribonucleic acid (DNA) is the molecule that carries genetic information for the development and functioning of an organism. For the body to read DNA, it has to go through the processes of transcription and translation. 

mRNA stands for messenger ribonucleic acid. It carries the genetic code from the DNA in a cell's nucleus to a ribosome which makes the protein. 

1. Transcription is the process by which DNA is copied into a new molecule called messenger RNA (mRNA).

2. Translation is the process by which the information on mRNA is turned into a series of amino acids that form a protein.

### Source:

1. File "source/dna_to_rna.py" converts DNA into mRNA sequence.
2. File "source/rna_to_protein.py" converts mRNA sequence into a protein sequence.
3. File "source/gc_content.py" calculates the GC-Ratio. For more information: [GC-Content](https://en.wikipedia.org/wiki/GC-content)

### Docker:

To deploy - from the root folder:

```
docker-compose up -d --build
```

### Commands:

First, to create the database and seed the tables with initial data run:

```
docker-compose run web python data/init.py create_seed_db
```

<br />
To convert DNA to mRNA run:

```
docker-compose run web python source/dna_to_rna.py
```

<br />
To convert RNA to a protein sequence:

```
docker-compose run web python source/rna_to_protein.py
```

<br />
To create GC-content graph in .jpg format put your data in "GC_content_input.fna" file and run:

```
docker-compose run web python source/gc_content.py
```