import psycopg2
from main import *

def manage_connection(query):
    try:
        conn = psycopg2.connect(
            host="rogue.db.elephantsql.com",
            port=5432,  
            database="wocsykfv", 
            user="wocsykfv",  
            password="rwPJlc2S6ceN1uDanxX3cS9f2w9NCDJQ"  
        )
        with conn:
            with conn.cursor() as cur:
                if "SELECT" in query:
                    cur.execute(query)
                    result = cur.fetchall()
                    return result
                else:
                    cur.execute(query)
                    conn.commit()
    except Exception as e:
        print(f'Error: {e}')
        return 'ERROR'
    cur = conn.cursor()
    try:
        query = """
        CREATE TABLE game_results (
        game_id SERIAL PRIMARY KEY, 
        name VARCHAR(50) NOT NULL, 
        capital VARCHAR(50) NOT NULL,
        flag_code VARCHAR(50) NOT NULL, 
        subregion VARCHAR(50) NOT NULL, 
        points INTEGER
        level INTEGER
    )
        """
        cur.execute(query)
    except:
        return None
    
    conn.commit()
    conn.close()
    cur.close()

