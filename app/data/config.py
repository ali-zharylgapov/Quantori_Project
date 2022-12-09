import psycopg2

DATABASE_URI = 'postgresql://postgres:postgres@db:5432/new_database_db'
conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )
gc_content_address = 'GC_content/GC_content_input.fna'