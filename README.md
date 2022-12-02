# Quantori_Project

### About

Application that mimics DNA transcription and translation processes. 

### Docker:

To deploy - from the root folder:

```
docker compose up -d --build
```

### Commands:

First, to seed "DNA", "RNA" and "Amino Acids" tables with initial data run:

```
docker compose run web python init.py seed_db
```

<br />
To convert DNA to mRNA run:

```
docker compose run web python dna_to_rna.py
```

<br />
To convert RNA to a protein sequence:

```
docker compose run web python rna_to_protein.py
```

<br />
To create GC-content graph in .jpg format run:

```
docker compose run web python gc_content.py
```