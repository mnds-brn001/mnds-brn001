import sqlite3
from tkinter import messagebox

def Create():
    conn= sqlite3.connect('mydatabase.db')
    cursor= conn.cursor()

    # Argumento utilizado para criar uma tabela no Sqlite3 utilizando Python
    cursor.execute("CREATE TABLE IF NOT EXISTS mytable (myname TEXT, id TEXT PRIMARY KEY)")

    conn.close()

def InsertData(name, id):
    Create()
    try:
        conn= sqlite3.connect("mydatabase.db")
        cursor= conn.cursor()

        # Argumento para inserir informação dentro da tabela Sqlite3 utilizando Python
        cursor.execute("INSERT INTO mytable(myname, id) VALUES (?,?)", (name, id))

        conn.commit()
        conn.close()
        messagebox.showinfo("Sucess", "Informação inserida com Sucesso!")
    except sqlite3.Error as e:
        messagebox.showinfo('Erro', e)
    finally:
        conn.close()