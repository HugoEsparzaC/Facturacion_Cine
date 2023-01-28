# importar librerias
import tkinter as tk
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time

class Cliente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de cuenta de clientes")
        self.geometry("1350x750")
        self.iconbitmap('Cine.ico')
        self.config(background="powder blue")
        self.hora = tk.StringVar()
        self._creacion_componentes()
        self.actualizar_hora()

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
        # =============================================================================================
        # Fecha, titulo y hora
        # =============================================================================================
        fecha = tk.StringVar()
        fecha.set(time.strftime("%d/%m/%Y"))
        self.lbl_fecha=tk.Label(ABC1, textvariable=fecha, font=('arial', 30, 'bold'), pady=9, bd=5, bg='cadet blue', fg="cornsilk").grid(row=0, column=0)
        self.lbl_titulo=tk.Label(ABC1, text='          Sistema de Facturacion de Clientes\t', font=('arial', 30, 'bold'), pady=9, bd=5, bg='cadet blue', fg="cornsilk", justify=tk.CENTER).grid(row=0, column=1)
        self.lbl_hora=tk.Label(ABC1, textvariable=self.hora, font=('arial', 30, 'bold'), pady=9, bd=5, bg='cadet blue', fg="cornsilk").grid(row=0, column=2)
        # =============================================================================================
        # Ticket
        # =============================================================================================
        self.ticket = tk.Text(ABC5, height=19, width=43, bd=10, font=('arial', 9, 'bold')).grid(row=0, column=0)
        # =============================================================================================
        # Botones Total, limpiar, salir
        # =============================================================================================
        self.boton_Total = tk.Button(ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=5, height=2, bg='powder blue', text="Total").grid(row=0, column=0)
        self.boton_limpiar = tk.Button(ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=5, height=2, bg='powder blue', text="Limpiar").grid(row=0, column=1)
        self.boton_salir = tk.Button(ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=5, height=2, bg='powder blue', text="Salir").grid(row=0, column=2)

    def actualizar_hora(self):
        self.hora.set(time.strftime("%H:%M:%S"))
        self.after(1000, self.actualizar_hora)

if __name__ == '__main__':
    aplicacion = Cliente()
    aplicacion.mainloop()