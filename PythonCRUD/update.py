from tkinter import messagebox
import sqlite3

def Update(name,id):
    try:
        conn= sqlite3.connect("mydatabase.db")
        c = conn.cursor()

        # Argumento utilizado para Atualizar(Update) uma linha em SQLITE3 utilizando Python
        c.execute("UPDATE mytable SET myname= ? WHERE id=?",(name,id))

        conn.commit()
        conn.close()
        messagebox.showinfo("Sucess","Informações Atualizadas com Sucesso!")
    except sqlite3.Error as e:
        messagebox.showinfo("Error", e)
    finally:
        conn.close()