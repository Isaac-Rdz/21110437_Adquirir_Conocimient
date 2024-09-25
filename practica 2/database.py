import sqlite3

def connect_db():
    """Conectar a la base de datos SQLite."""
    conn = sqlite3.connect('knowledge_base.db')
    return conn

def create_table():
    """Crear la tabla para almacenar conocimiento."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL UNIQUE,
            value TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_knowledge(key, value):
    """Agregar conocimiento a la base de datos."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO knowledge (key, value) VALUES (?, ?)', (key, value))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"El conocimiento para la clave '{key}' ya existe.")
    finally:
        conn.close()

def display_knowledge():
    """Mostrar todo el conocimiento almacenado."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT key, value FROM knowledge')
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(f"{row[0]}: {row[1]}")
