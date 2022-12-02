import psycopg2
conn = psycopg2.connect(
    database="test_1_db",
    host="db",
    user="postgres",
    password="postgres",
    port="5432"
        )
cursor = conn.cursor()