import sqlite3
from tkinter import messagebox

def Delete(id):
    try:
        conn = sqlite3.connect("mydatabase.db")
        cursor= conn.cursor()

        # Argumento para Deletar uma linha em Sqlite3 utilizando Python
        cursor.execute("DELETE FROM mytable WHERE id= ?",(id))

        conn.commit()
        conn.close()
        messagebox.showinfo("Sucess", "Informação Deletada com Sucesso!")
    except sqlite3.Error as e:
        messagebox.showinfo('Error', e)
    finally:
        conn.close()