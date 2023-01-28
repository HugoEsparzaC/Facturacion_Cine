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
        self.nombre = tk.StringVar()
        self.pelicula = tk.StringVar()
        self.sala = tk.StringVar()
        self.palomitas = tk.StringVar()
        self.tam_palomitas = tk.StringVar()
        self.refresco = tk.StringVar()
        self.tam_refresco = tk.StringVar()
        self.acompanamiento = tk.StringVar()
        self.b_palomitas = tk.IntVar()
        self.b_refresco = tk.IntVar()
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
        ABC2.grid(row=1, column=0, sticky='N')
        ABC3 = tk.Frame(ABC, bd=14, width=450, height=488, padx=10, bg='powder blue', relief=tk.RIDGE)
        ABC3.grid(row=1, column=1, sticky='w')
        ABC4 = tk.Frame(ABC, bd=14, width=460, height=488, padx=10, bg='cadet blue', relief=tk.RIDGE)
        ABC4.grid(row=1, column=2, sticky='w')
        ABC5 = tk.Frame(ABC4, bd=14, width=370, height=340, padx=10, bg='cadet blue', relief=tk.RIDGE)
        ABC5.grid(row=0, column=0, sticky='w')
        ABC6 = tk.Frame(ABC4, bd=14, width=370, height=120, padx=10, bg='cadet blue', relief=tk.RIDGE)
        ABC6.grid(row=1, column=0, columnspan=4, sticky='w')
        # =============================================================================================
        # Cliente, Pelicula y Sala
        # =============================================================================================
        self.lbl_cliente = tk.Label(ABC2, font=('arial', 12, 'bold'), text="Nombre Cliente:", padx=2, fg="cornsilk", bg='cadet blue').grid(row=0, column=0, sticky='w')
        self.txt_cliente = tk.Entry(ABC2, font=('arial', 12, 'bold'), textvariable= self.nombre, width=30).grid(row=0, column=1, pady=3)

        self.lbl_pelicula = tk.Label(ABC2, font=('arial', 12, 'bold'), text="Pelicula:", padx=2, fg="cornsilk", bg='cadet blue').grid(row=1, column=0, sticky='w')
        self.caja_pelicula = ttk.Combobox(ABC2, textvariable=self.pelicula, state='readonly', font=('arial', 12, 'bold'), width=28)
        self.caja_pelicula['value'] = ('', 'AVENGERS', 'LA MONJA', 'EL HOMBRE ARAÑA', 'DRAGON BALL')
        self.caja_pelicula.current(0)
        self.caja_pelicula.grid(row=1, column=1, pady=3)

        self.lbl_sala = tk.Label(ABC2, font=('arial', 12, 'bold'), text="Sala:", padx=2, fg="cornsilk", bg='cadet blue').grid(row=2, column=0, sticky='w')
        self.caja_sala = ttk.Combobox(ABC2, textvariable=self.sala, state='readonly', font=('arial', 12, 'bold'), width=28)
        self.caja_sala['value'] = ('', 'SENCILLA', '3D')
        self.caja_sala.current(0)
        self.caja_sala.grid(row=2, column=1, pady=3)
        # =============================================================================================
        # Fecha, titulo y hora
        # =============================================================================================
        fecha = tk.StringVar()
        fecha.set(time.strftime("%d/%m/%Y"))
        self.lbl_fecha=tk.Label(ABC1, textvariable=fecha, font=('arial', 30, 'bold'), pady=9, bd=5, bg='cadet blue', fg="cornsilk").grid(row=0, column=0)
        self.lbl_titulo=tk.Label(ABC1, text='          Sistema de Facturación de Clientes\t', font=('arial', 30, 'bold'), pady=9, bd=5, bg='cadet blue', fg="cornsilk", justify=tk.CENTER).grid(row=0, column=1)
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