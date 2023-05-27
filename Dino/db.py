import psycopg2
from main import *

def create_table():
    try:
        conn = psycopg2.connect(
            host="rogue.db.elephantsql.com",
            port=5432,  
            database="wocsykfv", 
            user="wocsykfv",  
            password="rwPJlc2S6ceN1uDanxX3cS9f2w9NCDJQ"  
        )
    except Exception as e:
        print(f'Error: {e}')
        return 'ERROR'
    cur = conn.cursor()
    try:
        query = """
        CREATE TABLE game_results (
        game_id SERIAL PRIMARY KEY, 
        game_title VARCHAR(50) NOT NULL,
        points INTEGER,
        level INTEGER
    )
        """
        cur.execute(query)
    except:
        return None
    
    conn.commit()
    conn.close()
    cur.close()

# create_table()