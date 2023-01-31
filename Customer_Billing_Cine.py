# importar librerias
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import time

class Cliente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Facturación de clientes")
        self.geometry("1366x768+0+0")
        self.iconbitmap('Cine.ico')
        self.config(background="white")
        self.hora = tk.StringVar()
        self.num_boletos = tk.StringVar()
        self.num_palomitas = tk.StringVar()
        self.num_refrescos = tk.StringVar()
        self.num_acompanamientos = tk.StringVar()
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
        self.b_queso = tk.IntVar()
        self.total = 0
        self.temp = ''
        self._creacion_componentes()
        self.actualizar_hora()
        self._Queso()

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
        # Numero de boletos, Pelicula y Sala
        # =============================================================================================
        self.lbl_Pelicula = tk.Label(ABC2, font=('arial', 16, 'bold'), text="Peliculas", padx=2, fg="black", bg='white').grid(row=0, column=0, sticky='w')
        self.lbl_num_boletos = tk.Label(ABC2, font=('arial', 12, 'bold'), text="Número de boletos:", padx=2, fg="black", bg='white').grid(row=1, column=0, sticky='w')
        self.txt_num_boletos = tk.Entry(ABC2, font=('arial', 12, 'bold'), textvariable= self.num_boletos, width=31, relief='solid')
        self.txt_num_boletos.grid(row=1, column=1, pady=3)

        self.lbl_pelicula = tk.Label(ABC2, font=('arial', 12, 'bold'), text="Pelicula:", padx=2, fg="black", bg='white').grid(row=2, column=0, sticky='w')
        self.caja_pelicula = ttk.Combobox(ABC2, textvariable=self.pelicula, state='readonly', font=('arial', 12, 'bold'), width=29)
        self.caja_pelicula['value'] = ('', 'AVENGERS', 'LA MONJA', 'EL HOMBRE ARAÑA', 'DRAGON BALL')
        self.caja_pelicula.current(0)
        self.caja_pelicula.grid(row=2, column=1, pady=3)

        self.lbl_sala = tk.Label(ABC2, font=('arial', 12, 'bold'), text="Sala:", padx=2, fg="black", bg='white').grid(row=3, column=0, sticky='w')
        self.caja_sala = ttk.Combobox(ABC2, textvariable=self.sala, state='readonly', font=('arial', 12, 'bold'), width=29)
        self.caja_sala['value'] = ('', 'SENCILLA', '3D')
        self.caja_sala.current(0)
        self.caja_sala.grid(row=3, column=1, pady=3)

        self.boton_Agregar_Pelicula = tk.Button(ABC2, padx=0, pady=0, bd=5, fg='black', font=('arial', 12, 'bold'), width=1, height=1, bg='sky blue', text="Agregar Pedido", command=self._Agregar_Pelicula).grid(row=4, column=0, columnspan=2, sticky='we')
        # =============================================================================================
        # Palomitas, Refresco y acompanamiento (agregar cantidades de cada uno)
        # =============================================================================================
        self.lbl_Comida = tk.Label(ABC2, font=('arial', 16, 'bold'), text="Comida", padx=2, fg="black", bg='white').grid(row=5, column=0, sticky='w')
        self.lbl_palomitas = tk.Checkbutton(ABC2, text='Palomitas', variable=self.b_palomitas, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg='white', command=self._Palomitas)
        self.lbl_palomitas.grid(row=6, sticky='w')
        self.txt_num_palomitas = tk.Entry(ABC2, font=('arial', 12, 'bold'), state='disabled', textvariable= self.num_palomitas, width=31, relief='solid')
        self.txt_num_palomitas.grid(row=6, column=1, pady=3)
        self.caja_palomitas = ttk.Combobox(ABC2, textvariable=self.palomitas, state='disabled', font=('arial', 12, 'bold'), width=29)
        self.caja_palomitas['value'] = ('', 'MANTEQUILLA', 'NATURALES', 'QUESO', 'ACARAMELADAS', 'VALENTINA', 'BUFALO')
        self.caja_palomitas.current(0)
        self.caja_palomitas.grid(row=7, column=1, pady=3)
        self.caja_tam_palomitas = ttk.Combobox(ABC2, textvariable=self.tam_palomitas, state='disabled', font=('arial', 12, 'bold'), width=29)
        self.caja_tam_palomitas['value'] = ('', 'CHICA', 'MEDIANA', 'GRANDE', 'PARA LLEVAR')
        self.caja_tam_palomitas.current(0)
        self.caja_tam_palomitas.grid(row=8, column=1, pady=3)

        self.lbl_acompanamiento = tk.Checkbutton(ABC2, text='Acompañamiento', variable=self.b_acompanamiento, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg='white', command=self._Acompanamiento).grid(row=9, sticky='w')
        self.txt_num_acompanamiento = tk.Entry(ABC2, font=('arial', 12, 'bold'), state='disabled', textvariable= self.num_acompanamientos, width=31, relief='solid')
        self.txt_num_acompanamiento.grid(row=9, column=1, pady=3)
        self.caja_acompanamiento = ttk.Combobox(ABC2, textvariable=self.acompanamiento, state='disabled', font=('arial', 12, 'bold'), width=29)
        self.caja_acompanamiento['value'] = ('', 'NACHOS', 'HOT-DOG', 'HOT-DOG JUMBO', 'CHOCOLATE', 'HELADO', 'DULCES')
        self.caja_acompanamiento.current(0)
        self.caja_acompanamiento.grid(row=10, column=1, pady=3)
        self.lbl_queso = tk.Checkbutton(ABC2, text='Queso extra', variable=self.b_queso, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg='white', state='disabled', command=self._Queso)
        self.lbl_queso.grid(row=11, column=1, sticky='w')

        self.boton_Agregar_Comida = tk.Button(ABC2, padx=0, pady=0, bd=5, fg='black', font=('arial', 12, 'bold'), width=1, height=1, bg='sky blue', text="Agregar Pedido", command=self._Agregar_Comida).grid(row=12, column=0, columnspan=2, sticky='we')

        self.lbl_refresco = tk.Checkbutton(ABC2, text='Refresco', variable=self.b_refresco, onvalue=1, offvalue=0, font=('arial', 12, 'bold'), bg='white', command=self._Refresco).grid(row=13, sticky='w')
        self.txt_num_refrescos = tk.Entry(ABC2, font=('arial', 12, 'bold'), state='disabled', textvariable= self.num_refrescos, width=31, relief='solid')
        self.txt_num_refrescos.grid(row=13, column=1, pady=3)
        self.caja_refresco = ttk.Combobox(ABC2, textvariable=self.refresco, state='disabled', font=('arial', 12, 'bold'), width=29)
        self.caja_refresco['value'] = ('', 'COCA COLA', 'COCA COLA S/A', 'SPRITE', 'MANZANA', 'FANTA', 'FUZE TEA')
        self.caja_refresco.current(0)
        self.caja_refresco.grid(row=14, column=1, pady=3)
        self.caja_tam_refresco = ttk.Combobox(ABC2, textvariable=self.tam_refresco, state='disabled', font=('arial', 12, 'bold'), width=29)
        self.caja_tam_refresco['value'] = ('', 'CHICO', 'MEDIANO', 'GRANDE', 'JUMBO')
        self.caja_tam_refresco.current(0)
        self.caja_tam_refresco.grid(row=15, column=1, pady=3)

        self.boton_Agregar_Refresco = tk.Button(ABC2, padx=0, pady=0, bd=5, fg='black', font=('arial', 12, 'bold'), width=1, height=1, bg='sky blue', text="Agregar Pedido", command=self._Total).grid(row=16, column=0, columnspan=2, sticky='we')
        # =============================================================================================
        # Combos
        # =============================================================================================

        # =============================================================================================
        # Ticket
        # =============================================================================================
        self.ticket = tk.Text(ABC5, height=25, width=43, bd=10, state = 'disabled', font=('arial', 9, 'bold'), wrap=tk.WORD)
        self.ticket.grid(row=0, column=0)
        # =============================================================================================
        # Botones Pagar, Cancelar, Salir
        # =============================================================================================
        self.boton_Total = tk.Button(ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=5, height=2, bg='white', text="Pagar", command=self._Total).grid(row=0, column=0)
        self.boton_limpiar = tk.Button(ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=5, height=2, bg='white', text="Cancelar", command=self._Limpiar).grid(row=0, column=1)
        self.boton_salir = tk.Button(ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=5, height=2, bg='white', text="Salir", command=self._Exit).grid(row=0, column=2)

    def actualizar_hora(self):
        self.hora.set(time.strftime("%H:%M:%S"))
        self.after(1000, self.actualizar_hora)

    def _Palomitas(self):
        if self.b_palomitas.get() == 1:
            self.caja_palomitas.configure(state='readonly')
            self.caja_tam_palomitas.configure(state='readonly')
            self.txt_num_palomitas.configure(state='normal')
        else:
            self.caja_palomitas.configure(state='disabled')
            self.caja_palomitas.current(0)
            self.caja_tam_palomitas.configure(state='disabled')
            self.caja_tam_palomitas.current(0)
            self.txt_num_palomitas.delete(0, tk.END)
            self.txt_num_palomitas.configure(state='disabled')

    def _Refresco(self):
        if self.b_refresco.get() == 1:
            self.caja_refresco.configure(state='readonly')
            self.caja_tam_refresco.configure(state='readonly')
            self.txt_num_refrescos.configure(state='normal')
        else:
            self.caja_refresco.configure(state='disabled')
            self.caja_refresco.current(0)
            self.caja_tam_refresco.configure(state='disabled')
            self.caja_tam_refresco.current(0)
            self.txt_num_refrescos.delete(0, tk.END)
            self.txt_num_refrescos.configure(state='disabled')

    def _Acompanamiento(self):
        if self.b_acompanamiento.get() == 1:
            self.caja_acompanamiento.configure(state='readonly')
            self.txt_num_acompanamiento.configure(state='normal')
        else:
            self.caja_acompanamiento.configure(state='disabled')
            self.caja_acompanamiento.current(0)
            self.b_queso.set(0)
            self.txt_num_acompanamiento.delete(0, tk.END)
            self.txt_num_acompanamiento.configure(state='disabled')

    def _Queso(self):
        self.after(100, self._Queso)
        if self.acompanamiento.get() == "NACHOS":
            self.lbl_queso.configure(state='normal')
        else:
            self.lbl_queso.configure(state='disabled')

    def _Total(self):
        pass

    def _Agregar_Pelicula(self):
        self.ticket.configure(state='normal')
        self.ticket.delete(1.0, tk.END)
        self.temp = self.temp + f'{self.num_boletos.get()} boletos\nPelicula: {self.pelicula.get()}\nSala: {self.sala.get()}\n'
        if self.sala.get() == 'SENCILLA':
            self.total += float(self.num_boletos.get()) * 50.00
            aux = float(self.num_boletos.get()) * 50.00
            self.temp = self.temp + f'Costo boletos: ${aux:.2f}\n'
        else:
            self.total += float(self.num_boletos.get()) * 90.00
            aux = float(self.num_boletos.get()) * 90.00
            self.temp = self.temp + f'Costo boletos: ${aux:.2f}\n'
        self.ticket.insert(tk.END, f'{self.temp}\nTotal ${self.total:.2f}')
        self.caja_pelicula.current(0)
        self.caja_sala.current(0)
        self.txt_num_boletos.delete(0, tk.END)
        self.ticket.configure(state='disabled')

    def _Agregar_Comida(self):
        self.ticket.configure(state='normal')
        self.ticket.delete(1.0, tk.END)
        # =============================================================================================
        # Costo Palomitas
        # =============================================================================================
        if self.b_palomitas:
            if self.tam_palomitas.get() == 'CHICA':
                self.total += float(self.num_palomitas.get()) * 30
                aux = float(self.num_palomitas.get()) * 30
                self.temp = self.temp + f'{self.num_palomitas.get()} Palomitas:\n      Sabor: {self.palomitas.get()}\n      Tamaño: {self.tam_palomitas.get()}\n      Costo: ${aux:.2f}\n'
            elif self.tam_palomitas.get() == 'MEDIANA':
                self.total += float(self.num_palomitas.get()) * 40
                aux = float(self.num_palomitas.get()) * 40
                self.temp = self.temp + f'{self.num_palomitas.get()} Palomitas:\n      Sabor: {self.palomitas.get()}\n      Tamaño: {self.tam_palomitas.get()}\n      Costo: ${aux:.2f}\n'
            elif self.tam_palomitas.get() == 'GRANDE':
                self.total += float(self.num_palomitas.get()) * 50
                aux = float(self.num_palomitas.get()) * 50
                self.temp = self.temp + f'{self.num_palomitas.get()} Palomitas:\n      Sabor: {self.palomitas.get()}\n      Tamaño: {self.tam_palomitas.get()}\n      Costo: ${aux:.2f}\n'
            elif self.tam_palomitas.get() == 'PARA LLEVAR':
                self.total += float(self.num_palomitas.get()) * 60
                aux = float(self.num_palomitas.get()) * 60
                self.temp = self.temp + f'{self.num_palomitas.get()} Palomitas:\n      Sabor: {self.palomitas.get()}\n      Tamaño: {self.tam_palomitas.get()}\n      Costo: ${aux:.2f}\n'
        # =============================================================================================
        # Costo Acompanamientos
        # =============================================================================================
        if self.b_acompanamiento:
            if self.acompanamiento.get() == 'NACHOS':
                if self.b_queso.get():
                    self.total += float(self.num_acompanamientos.get()) * 50
                    aux = float(self.num_acompanamientos.get()) * 50
                    self.temp = self.temp + f'{self.num_acompanamientos.get()} Acompañamientos:\n      Acompañamiento: {self.acompanamiento.get()}\n      Queso extra: 5.00\n      Costo: ${aux:.2f}\n'
                else:
                    self.total += float(self.num_acompanamientos.get()) * 45
                    aux = float(self.num_acompanamientos.get()) * 45
                    self.temp = self.temp + f'{self.num_acompanamientos.get()} Acompañamientos:\n      Acompañamiento: {self.acompanamiento.get()}\n      Costo: ${aux:.2f}\n'
            elif self.acompanamiento.get() == 'HOT-DOG':
                self.total += float(self.num_acompanamientos.get()) * 45
                aux = float(self.num_acompanamientos.get()) * 45
                self.temp = self.temp + f'{self.num_acompanamientos.get()} Acompañamientos:\n      Acompañamiento: {self.acompanamiento.get()}\n      Costo: ${aux:.2f}\n'
            elif self.acompanamiento.get() == 'HOT-DOG JUMBO':
                self.total += float(self.num_acompanamientos.get()) * 70
                aux = float(self.num_acompanamientos.get()) * 70
                self.temp = self.temp + f'{self.num_acompanamientos.get()} Acompañamientos:\n      Acompañamiento: {self.acompanamiento.get()}\n      Costo: ${aux:.2f}\n'
            elif self.acompanamiento.get() == 'CHOCOLATE':
                self.total += float(self.num_acompanamientos.get()) * 30
                aux = float(self.num_acompanamientos.get()) * 30
                self.temp = self.temp + f'{self.num_acompanamientos.get()} Acompañamientos:\n      Acompañamiento: {self.acompanamiento.get()}\n      Costo: ${aux:.2f}\n'
            elif self.acompanamiento.get() == 'HELADO':
                self.total += float(self.num_acompanamientos.get()) * 45
                aux = float(self.num_acompanamientos.get()) * 45
                self.temp = self.temp + f'{self.num_acompanamientos.get()} Acompañamientos:\n      Acompañamiento: {self.acompanamiento.get()}\n      Costo: ${aux:.2f}\n'
            elif self.acompanamiento.get() == 'DULCES':
                self.total += float(self.num_acompanamientos.get()) * 25
                aux = float(self.num_acompanamientos.get()) * 25
                self.temp = self.temp + f'{self.num_acompanamientos.get()} Acompañamientos:\n      Acompañamiento: {self.acompanamiento.get()}\n      Costo: ${aux:.2f}\n'
        self.ticket.insert(tk.END, f'{self.temp}\nTotal ${self.total:.2f}')
        self.caja_palomitas.configure(state='disabled')
        self.caja_palomitas.current(0)
        self.caja_tam_palomitas.configure(state='disabled')
        self.caja_tam_palomitas.current(0)
        self.b_palomitas.set(0)
        self.txt_num_palomitas.delete(0, tk.END)
        self.txt_num_palomitas.configure(state='disabled')
        self.caja_acompanamiento.configure(state='disabled')
        self.caja_acompanamiento.current(0)
        self.b_acompanamiento.set(0)
        self.b_queso.set(0)
        self.txt_num_acompanamiento.delete(0, tk.END)
        self.txt_num_acompanamiento.configure(state='disabled')
        self.ticket.configure(state='disabled')

    def _Agregar_Refresco(self):
        self.ticket.configure(state='normal')
        self.ticket.delete(1.0, tk.END)
        # =============================================================================================
        # Costo Refresco
        # =============================================================================================
        if self.b_refresco:
            if self.tam_refresco.get() == 'CHICO':
                self.total += float(self.num_refrescos.get()) * 30
                aux = float(self.num_refrescos.get()) * 30
                self.temp = self.temp + f'{self.num_refrescos.get()} Refrescos:\nSabor: {self.refresco.get()}\nTamaño: {self.tam_refresco.get()}\nCosto: ${aux:.2f}\n'
            elif self.tam_refresco.get() == 'MEDIANO':
                self.total += float(self.num_refrescos.get()) * 40
                aux = float(self.num_refrescos.get()) * 40
                self.temp = self.temp + f'{self.num_refrescos.get()} Refrescos:\nSabor: {self.refresco.get()}\nTamaño: {self.tam_refresco.get()}\nCosto: ${aux:.2f}\n'
            elif self.tam_refresco.get() == 'GRANDE':
                self.total += float(self.num_refrescos.get()) * 50
                aux = float(self.num_refrescos.get()) * 50
                self.temp = self.temp + f'{self.num_refrescos.get()} Refrescos:\nSabor: {self.refresco.get()}\nTamaño: {self.tam_refresco.get()}\nCosto: ${aux:.2f}\n'
            elif self.tam_refresco.get() == 'JUMBO':
                self.total += float(self.num_refrescos.get()) * 60
                aux = float(self.num_refrescos.get()) * 60
                self.temp = self.temp + f'{self.num_refrescos.get()} Refrescos:\nSabor: {self.refresco.get()}\nTamaño: {self.tam_refresco.get()}\nCosto: ${aux:.2f}\n'
        self.ticket.insert(tk.END, f'{self.temp}\nTotal ${self.total:.2f}')
        self.caja_refresco.configure(state='disabled')
        self.caja_refresco.current(0)
        self.caja_tam_refresco.configure(state='disabled')
        self.caja_tam_refresco.current(0)
        self.b_refresco.set(0)
        self.txt_num_refrescos.delete(0, tk.END)
        self.txt_num_refrescos.configure(state='disabled')
        self.ticket.configure(state='disabled')

    def _Limpiar(self):
        self.ticket.configure(state='normal')
        self.ticket.delete(1.0, tk.END)
        self.temp = ''
        self.total = 0.00
        # Peliculas
        self.caja_pelicula.current(0)
        self.caja_sala.current(0)
        self.txt_num_boletos.delete(0, tk.END)
        # Palomitas
        self.caja_palomitas.configure(state='disabled')
        self.caja_palomitas.current(0)
        self.caja_tam_palomitas.configure(state='disabled')
        self.caja_tam_palomitas.current(0)
        self.b_palomitas.set(0)
        self.txt_num_palomitas.delete(0, tk.END)
        self.txt_num_palomitas.configure(state='disabled')
        # Refresco
        self.caja_refresco.configure(state='disabled')
        self.caja_refresco.current(0)
        self.caja_tam_refresco.configure(state='disabled')
        self.caja_tam_refresco.current(0)
        self.b_refresco.set(0)
        self.txt_num_refrescos.delete(0, tk.END)
        self.txt_num_refrescos.configure(state='disabled')
        # Acompanamiento
        self.caja_acompanamiento.configure(state='disabled')
        self.caja_acompanamiento.current(0)
        self.b_acompanamiento.set(0)
        self.b_queso.set(0)
        self.txt_num_acompanamiento.delete(0, tk.END)
        self.txt_num_acompanamiento.configure(state='disabled')
        # Ticket
        self.ticket.configure(state='disabled')

    def _Exit(self):
        Exit = messagebox.askyesno("Sistema de Facturación de clientes", "Confirma que quiere salir")
        if Exit > 0:
            self.destroy()
            return

if __name__ == '__main__':
    aplicacion = Cliente()
    aplicacion.mainloop()