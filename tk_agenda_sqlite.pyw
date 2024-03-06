import tkinter as tk
from tkinter import messagebox as msg

import os

import sqlite3 as sql

conn = sql.connect("db.sqlite3")

cursor = conn.cursor()

cursor.execute("create table if not exists users (nome varchar(255), telefone varchar(255)); ")

frame = tk.Tk() 
frame.title("TextBox Input") 
frame.geometry('200x200')
frame.resizable(False, False)
  
def create(): 
    inp = inputnome.get(1.0, "end-1c")
    fone = inputfone.get(1.0, "end-1c")
    
    if len(inp) > 0:
            if len(fone) > 0:
                cursor.execute(f"insert into users (nome, telefone) values (?, ?);",(inp, fone))
                conn.commit()
    

def delete(): 
    inp = inputnome.get(1.0, "end-1c") 
    
    cursor.execute("delete from users where nome = ? ;", (inp,))

def read(): 
    inp = inputnome.get(1.0, "end-1c") 
    
    

    lista = list(cursor.execute("select * from users where nome = ? limit 5", (inp,)))

    lista_str = ''
    for i,a in lista:
        lista_str += i+","+a+"\n\n"
    msg.showinfo("Output", lista_str)


lblnome = tk.Label(frame, text = "Nome") 
lblnome.pack()  
 
inputnome = tk.Text(frame, 
                   height = 1, 
                   width = 20)
inputnome.pack()

lblfone = tk.Label(frame, text = "Fone") 
lblfone.pack()


inputfone = tk.Text(frame, 
                   height = 1, 
                   width = 20)
  
inputfone.pack() 
  
 
printButton = tk.Button(frame, 
                        text = "Salvar registro",  
                        command = create) 
printButton.pack()


printButton = tk.Button(frame, 
                        text = "Pesquisar por nome",  
                        command = read) 
printButton.pack()


printButton = tk.Button(frame, 
                        text = "Deletar por nome",  
                        command = delete) 
printButton.pack()
 
lbl = tk.Label(frame, text = "") 
lbl.pack()

frame.mainloop()
