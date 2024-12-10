import psycopg2

try:
    conn = psycopg2.connect(
        dbname="test",
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port="5432"
    )

    cur = conn.cursor()

    query = 'DROP TABLE psycopg2'
    cur.execute(query)
    
    query = '''
        CREATE TABLE IF NOT EXISTS psycopg2 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            dob DATE NOT NULL
        )
    '''
    cur.execute(query)
    
    cur.execute("INSERT INTO psycopg2 (name, dob) VALUES (%s, %s)", ('Adarsh', '1975-08-19',))
    conn.commit()
    
    cur.execute("DROP TABLE s")
    cur.close()
    conn.close()
except Exception as ex:
    print(f'Exception: {ex}')
