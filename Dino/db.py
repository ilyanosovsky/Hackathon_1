import psycopg2
from main import *


def manage_connection():
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

# manage_connection()
class TableMAnager:

    @classmethod
    def get_result(cls):
        query_user = f"""
        SELECT * FROM game_results 
        ORDER BY points DESC LIMIT 1
        """
        if manage_connection() == []:
            return None
        else:
            result = manage_connection()
            return result
        
    @classmethod
    def all_items(cls):
        query_user = f"""
        SELECT * FROM menu_items
        """
        result = manage_connection()
        return result

# item2 = MenuManager.get_by_name('Beef Stew')
items = TableMAnager.all_items()
print(items)
