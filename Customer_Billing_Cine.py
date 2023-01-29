# importar librerias
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import time

class Cliente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Facturación de clientes")
        self.geometry("1350x750")
        self.iconbitmap('Cine.ico')
        self.config(background="white")
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
        self.b_acompanamiento = tk.IntVar()
        self._creacion_componentes()
        self.actualizar_hora()

    def _creacion_componentes(self):
        # =============================================================================================
        # Plantilla divisoria
        # =============================================================================================
        ABC = tk.Frame(self, bg='royal blue', bd=20, relief=tk.RIDGE)
        ABC.grid()
        ABC1 = tk.Frame(ABC, bd=14, width=1350, height=100, padx=10, bg='royal blue', relief=tk.RIDGE)
        ABC1.grid(row=0, column=0, columnspan=4, sticky='n')
        ABC2 = tk.Frame(ABC, bd=14, width=450, height=488, padx=10, bg='white', relief=tk.RIDGE)
        ABC2.grid(row=1, column=0, sticky='NS')
        ABC3 = tk.Frame(ABC, bd=14, width=450, height=488, padx=10, bg='white', relief=tk.RIDGE)
        ABC3.grid(row=1, column=1, sticky='NS')
        ABC4 = tk.Frame(ABC, bd=14, width=460, height=488, padx=0, bg='white', relief=tk.RIDGE)
        ABC4.grid(row=1, column=2, sticky='w')
        ABC5 = tk.Frame(ABC4, bd=14, width=370, height=340, padx=0, bg='white', relief=tk.RIDGE)
        ABC5.grid(row=0, column=0, sticky='w')
        ABC6 = tk.Frame(ABC4, bd=14, width=370, height=120, padx=0, bg='white', relief=tk.RIDGE)
        ABC6.grid(row=1, column=0, columnspan=4, sticky='w')
        # =============================================================================================
        # Fecha, titulo y hora
        # =============================================================================================
        fecha = tk.StringVar()
        fecha.set(time.strftime("%d/%m/%Y"))
        self.lbl_fecha=tk.Label(ABC1, textvariable=fecha, font=('arial', 30, 'bold'), pady=9, bd=5, bg='royal blue', fg="white").grid(row=0, column=0)
        self.lbl_titulo=tk.Label(ABC1, text='            Sistema de Facturación de Clientes         ', font=('arial', 30, 'bold'), pady=9, bd=5, bg='royal blue', fg="white", justify=tk.CENTER).grid(row=0, column=1)
        self.lbl_hora=tk.Label(ABC1, textvariable=self.hora, font=('arial', 30, 'bold'), pady=9, bd=5, bg='royal blue', fg="white").grid(row=0, column=2)
        # =============================================================================================
        # Cliente, Pelicula y Sala
        # =============================================================================================
        self.lbl_cliente = tk.Label(ABC2, font=('arial', 12, 'bold'), text="Nombre Cliente:", padx=2, fg="black", bg='white').grid(row=0, column=0, sticky='w')
        self.txt_cliente = tk.Entry(ABC2, font=('arial', 12, 'bold'), textvariable= self.nombre, width=30, relief='solid').grid(row=0, column=1, pady=3)

        self.lbl_pelicula = tk.Label(ABC2, font=('arial', 12, 'bold'), text="Pelicula:", padx=2, fg="black", bg='white').grid(row=1, column=0, sticky='w')
        self.caja_pelicula = ttk.Combobox(ABC2, textvariable=self.pelicula, state='readonly', font=('arial', 12, 'bold'), width=28)
        self.caja_pelicula['value'] = ('', 'AVENGERS', 'LA MONJA', 'EL HOMBRE ARAÑA', 'DRAGON BALL')
        self.caja_pelicula.current(0)
        self.caja_pelicula.grid(row=1, column=1, pady=3)

        self.lbl_sala = tk.Label(ABC2, font=('arial', 12, 'bold'), text="Sala:", padx=2, fg="black", bg='white').grid(row=2, column=0, sticky='w')
        self.caja_sala = ttk.Combobox(ABC2, textvariable=self.sala, state='readonly', font=('arial', 12, 'bold'), width=28)
        self.caja_sala['value'] = ('', 'SENCILLA', '3D')
        self.caja_sala.current(0)
        self.caja_sala.grid(row=2, column=1, pady=3)
        # =============================================================================================
        # Palomitas, Refresco y acompanamiento
        # =============================================================================================
        self.lbl_palomitas = tk.Checkbutton(ABC3, text='Palomitas', variable=self.b_palomitas, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg='white', command=self._Palomitas).grid(row=0, sticky='w')
        self.caja_palomitas = ttk.Combobox(ABC3, textvariable=self.palomitas, state='disabled', font=('arial', 12, 'bold'), width=30)
        self.caja_palomitas['value'] = ('', 'MANTEQUILLA', 'NATURALES', 'QUESO', 'ACARAMELADAS', 'VALENTINA', 'BUFALO')
        self.caja_palomitas.current(0)
        self.caja_palomitas.grid(row=0, column=1, pady=3)
        self.caja_tam_palomitas = ttk.Combobox(ABC3, textvariable=self.tam_palomitas, state='disabled', font=('arial', 12, 'bold'), width=30)
        self.caja_tam_palomitas['value'] = ('', 'CHICA', 'MEDIANA', 'GRANDE', 'PARA LLEVAR')
        self.caja_tam_palomitas.current(0)
        self.caja_tam_palomitas.grid(row=2, column=1, pady=3)

        self.lbl_refresco = tk.Checkbutton(ABC3, text='Refresco', variable=self.b_refresco, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg='white', command=self._Refresco).grid(row=3, sticky='w')
        self.caja_refresco = ttk.Combobox(ABC3, textvariable=self.refresco, state='disabled', font=('arial', 12, 'bold'), width=30)
        self.caja_refresco['value'] = ('', 'COCA COLA', 'COCA COLA S/A', 'SPRITE', 'MANZANA', 'FANTA', 'FUZE TEA')
        self.caja_refresco.current(0)
        self.caja_refresco.grid(row=3, column=1, pady=3)
        self.caja_tam_refresco = ttk.Combobox(ABC3, textvariable=self.tam_refresco, state='disabled', font=('arial', 12, 'bold'), width=30)
        self.caja_tam_refresco['value'] = ('', 'CHICO', 'MEDIANO', 'GRANDE', 'JUMBO')
        self.caja_tam_refresco.current(0)
        self.caja_tam_refresco.grid(row=4, column=1, pady=3)

        self.lbl_acompanamiento = tk.Checkbutton(ABC3, text='Acompañamiento', variable=self.b_acompanamiento, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg='white', command=self._Acompanamiento).grid(row=5, sticky='w')
        self.caja_acompanamiento = ttk.Combobox(ABC3, textvariable=self.acompanamiento, state='disabled', font=('arial', 12, 'bold'), width=30)
        self.caja_acompanamiento['value'] = ('', 'NACHOS', 'NACHOS CON QUESO EXTRA', 'HOT-DOG', 'HOT-DOG JUMBO', 'CHOCOLATE', 'HELADO', 'DULCES')
        self.caja_acompanamiento.current(0)
        self.caja_acompanamiento.grid(row=5, column=1, pady=3)
        # =============================================================================================
        # Ticket
        # =============================================================================================
        self.ticket = tk.Text(ABC5, height=25, width=43, bd=10, font=('arial', 9, 'bold'), wrap=tk.WORD)
        self.ticket.grid(row=0, column=0)
        # =============================================================================================
        # Botones Total, limpiar, salir
        # =============================================================================================
        self.boton_Total = tk.Button(ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=5, height=2, bg='white', text="Total", command=self._Total).grid(row=0, column=0)
        self.boton_limpiar = tk.Button(ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=5, height=2, bg='white', text="Limpiar").grid(row=0, column=1)
        self.boton_salir = tk.Button(ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=5, height=2, bg='white', text="Salir", command=self._Exit).grid(row=0, column=2)

    def actualizar_hora(self):
        self.hora.set(time.strftime("%H:%M:%S"))
        self.after(1000, self.actualizar_hora)

    def _Palomitas(self):
        if self.b_palomitas.get() == 1:
            self.caja_palomitas.configure(state='readonly')
            self.caja_tam_palomitas.configure(state='readonly')
        else:
            self.caja_palomitas.configure(state='disabled')
            self.caja_palomitas.current(0)
            self.caja_tam_palomitas.configure(state='disabled')
            self.caja_tam_palomitas.current(0)

    def _Refresco(self):
        if self.b_refresco.get() == 1:
            self.caja_refresco.configure(state='readonly')
            self.caja_tam_refresco.configure(state='readonly')
        else:
            self.caja_refresco.configure(state='disabled')
            self.caja_refresco.current(0)
            self.caja_tam_refresco.configure(state='disabled')
            self.caja_tam_refresco.current(0)

    def _Acompanamiento(self):
        if self.b_acompanamiento.get() == 1:
            self.caja_acompanamiento.configure(state='readonly')
        else:
            self.caja_acompanamiento.configure(state='disabled')
            self.caja_acompanamiento.current(0)

    def _Total(self):
        self.ticket.insert(
            tk.END,
            f'''Cuenta de {self.nombre.get()}
Pelicula: {self.pelicula.get()}
Sala: {self.sala.get()}
        ''')

    def _Exit(self):
        Exit = messagebox.askyesno("Sistema de Facturación de clientes", "Confirma que quiere salir")
        if Exit > 0:
            self.destroy()
            return

if __name__ == '__main__':
    aplicacion = Cliente()
    aplicacion.mainloop()