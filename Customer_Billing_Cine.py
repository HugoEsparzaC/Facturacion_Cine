# importar librerias
import tkinter as tk
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime

class Cliente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de cuenta de clientes")
        self.geometry("1350x750")
        self.iconbitmap('Cine.ico')
        self.config(background="powder blue")
        self._creacion_componentes()

    def _creacion_componentes(self):
        # =============================================================================================
        # Plantilla divisoria
        # =============================================================================================
        ABC = tk.Frame(self, bg='powder blue', bd=20, relief=tk.RIDGE)
        ABC.grid()
        ABC1 = tk.Frame(ABC, bd=14, width=1350, height=100, padx=10, bg='powder blue', relief=tk.RIDGE)
        ABC1.grid(row=0, column=0, columnspan=4, sticky='w')
        ABC2 = tk.Frame(ABC, bd=14, width=450, height=488, padx=10, bg='cadet blue', relief=tk.RIDGE)
        ABC2.grid(row=1, column=0, sticky='w')
        ABC3 = tk.Frame(ABC, bd=14, width=450, height=488, padx=10, bg='powder blue', relief=tk.RIDGE)
        ABC3.grid(row=1, column=1, sticky='w')
        ABC4 = tk.Frame(ABC, bd=14, width=460, height=488, padx=10, bg='cadet blue', relief=tk.RIDGE)
        ABC4.grid(row=1, column=2, sticky='w')
        ABC5 = tk.Frame(ABC4, bd=14, width=370, height=340, padx=10, bg='cadet blue', relief=tk.RIDGE)
        ABC5.grid(row=0, column=0, sticky='w')
        ABC6 = tk.Frame(ABC4, bd=14, width=370, height=120, padx=10, bg='cadet blue', relief=tk.RIDGE)
        ABC6.grid(row=1, column=0, columnspan=4, sticky='w')

if __name__ == '__main__':
    aplicacion = Cliente()
    aplicacion.mainloop()