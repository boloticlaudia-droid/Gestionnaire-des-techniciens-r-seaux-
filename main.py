import tkinter as tk 
import sqlite3


connexion=sqlite3.connect("Techniciens.db")

curseur=connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS techniciens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    age INTEGER,
    specialite TEXT,
    niveau_etude TEXT,
    experience INTEGER,
    domaine TEXT,
    grade TEXT,
    telephone TEXT NOT NULL,
    email TEXT,
    ville TEXT
)
""")

connexion.commit()

connexion.close()

app=tk.Tk()
app.geometry("800x600")
app.title("Gestionnaire des techniciens")

frame1=tk.LabelFrame(app,text="Informations Techniciens",width=500,height=380,bg="white",fg="black",font="Anton 12")
frame1.place(x=10,y=15)





app.mainloop()