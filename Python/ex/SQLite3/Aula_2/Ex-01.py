import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "users"


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

try:
    comando = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} 
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL
        )
    """
    connection.commit()
    cursor.execute(comando)

except Exception as e:
    print(f"ERRO: {e}")

finally:
    print("FIM")


def insertValue(name_value, weight_value):
    comando = f"""
    INSERT INTO {TABLE_NAME} (name, weight)
    VALUES ("{name_value}", "{weight_value}")
    """
    cursor.execute(comando)

insertValue("Lucas", 95.45)


connection.commit()
cursor.close()
connection.close()
