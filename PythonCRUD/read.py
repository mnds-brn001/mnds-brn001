import sqlite3

def Read():
    conn= sqlite3.connect("mydatabase.db")
    cursor= conn.cursor()

    # Argumento utilizado para ler ou pegar todas as colunas de uman tabela em Sqlite3 utilizando Python
    cursor.execute('SELECT *FROM mytable')
    all_rows= cursor.fetchall()

    conn.close()

    return all_rows
