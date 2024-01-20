import psycopg2


def connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="root",
        password="root"
    )


