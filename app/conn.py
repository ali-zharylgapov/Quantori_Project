import psycopg2

conn = psycopg2.connect(
    database="new_database_db",
    host="db",
    user="postgres",
    password="postgres",
    port="5432"
        )
cursor = conn.cursor()