import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import math as mt


class Aplication:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Simulacion")
        self.labelframe1=ttk.LabelFrame(self.root, text="Ingrese los datos correspondientes")
        self.labelframe1.grid(column=0, row=0, padx=8, pady=8)
        self.root.configure(bg="white")
        self.root.resizable(False,False)
        self.componentes()
        self.option_menu()
        self.root.mainloop()

    def componentes(self):
        
        self.label1=tk.Label(self.labelframe1, text="Valores")
        self.label1.grid(column=1, row=0, padx=5, pady=5)
        #-------------------------------------------------------------------------------------#
        self.label2=tk.Label(self.labelframe1, text="Masa en kg: ")
        self.label2.grid(column=0, row=1, padx=5, pady=5)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.labelframe1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=1, padx=5, pady=5)
        
        #-------------------------------------------------------------------------------------#
        self.label3=tk.Label(self.labelframe1, text="Radio en m: ")
        self.label3.grid(column=0, row=2, padx=5, pady=5, sticky="we")
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.labelframe1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=2, padx=5, pady=5)

        #-------------------------------------------------------------------------------------#
        self.label4=tk.Label(self.labelframe1, text="Frecuencia en rad/s: ")
        self.label4.grid(column=0, row=3, padx=5, pady=5, sticky="e")
        self.dato3=tk.StringVar()
        self.entry3=tk.Entry(self.labelframe1, textvariable=self.dato3)
        self.entry3.grid(column=1, row=3, padx=5, pady=5)

        #-------------------------------------------------------------------------------------#
        self.label5=tk.Label(self.labelframe1, text="¿De cuantos watts\nes el bombilo?")
        self.label5.grid(column=0, row=5, padx=5, pady=5, sticky="we")
        
        self.opcion = tk.IntVar()

        self.opcion1=tk.Radiobutton(self.labelframe1, text="1 Watt ", variable=self.opcion,value=1)
        self.opcion1.grid(column=1, row=4, padx=5, pady=5)

        self.opcion2=tk.Radiobutton(self.labelframe1, text="3 Watts", variable=self.opcion,value=2)
        self.opcion2.grid(column=1, row=5, padx=5, pady=5)

        self.opcion3=tk.Radiobutton(self.labelframe1, text="6 Watts", variable=self.opcion,value=3)
        self.opcion3.grid(column=1, row=6, padx=5, pady=5)

        #-------------------------------------------------------------------------------------#
        self.label5=tk.Label(self.labelframe1, text="Segundos que quiere\nencender el bombillo: ")
        self.label5.grid(column=0, row=7, padx=5, pady=5, sticky="e")
        self.dato4=tk.StringVar()
        self.entry4=tk.Entry(self.labelframe1, textvariable=self.dato4)
        self.entry4.grid(column=1, row=7, padx=5, pady=15)

        #-------------------------------------------------------------------------------------#
        self.boton1=tk.Button(self.labelframe1, text="Calcular", command=self.calculo)
        self.boton1.grid(column=0, row=8, padx=5, pady=15, sticky="we")

        self.boton2=tk.Button(self.labelframe1, text="Limpiar", command=self.clear)
        self.boton2.grid(column=1, row=8, padx=5, pady=5, sticky="we")


    def option_menu(self):
        self.menubar1 = tk.Menu(self.root)
        self.root.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label="Opciones", menu=self.opciones1) 
        self.opciones1.add_command(label="Acerca de...", command=self.info)
        
        self.opciones2 = tk.Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label="Motores", menu=self.opciones2)
        self.opciones2.add_command(label="Motor 1", command=self.motor1)

    def calculo(self):
        try:
            if self.dato1.get()=="" or self.dato2.get()=="" or self.dato3.get()=="" or self.dato4.get()=="":
                mb.showerror("Error","No puede dejar un recuadro vacio")
            elif float(self.dato1.get())<=0 or float(self.dato2.get())<=0 or float(self.dato3.get())<=0 or float(self.dato4.get())<=0:
                mb.showerror("Error","Uno o mas de los datos esta fuera del rango permitido")
            else:
                m=float(self.dato1.get())
                r=float(self.dato2.get())
                fr=float(self.dato3.get())
                t=float(self.dato4.get())
                #----------------------------------#
                i=(0.4)*m*(r**2)
                v_an=2*mt.pi*(fr**2)
                #----------------------------------#
                Ecr= (0.5)*(v_an**2)*(i)
                Ecr*=150
                #----------------------------------#
                p=Ecr/t
                if self.opcion.get()==1:
                    if p>=1:
                        mb.showinfo("Resultado","El bombillo ha sido encendido con exito")
                    else:
                        mb.showinfo("Resultado","No se ha logrado encender el bombillo")
                elif self.opcion.get()==2:
                    if p>=3:
                        mb.showinfo("Resultado","El bombillo ha sido encendido con exito")
                    else:
                        mb.showinfo("Resultado","No se ha logrado encender el bombillo")
                elif self.opcion.get()==3:
                    if p>=6:
                        mb.showinfo("Resultado","El bombillo ha sido encendido con exito")
                    else:
                        mb.showinfo("Resultado","No se ha logrado encender el bombillo")
        except:
            mb.showerror("Error","Solo se admiten numeros")

    def motor1(self):
        self.entry1.delete(0,"end")
        self.entry1.insert(0, "4")
        self.entry1.config(state="disabled")
        #--------------------------#
        self.entry2.delete(0,"end")
        self.entry2.insert(0, "0.15")
        self.entry2.config(state="disabled")
        #--------------------------#
        self.entry3.delete(0,"end")
        self.entry3.insert(0, "3.75")
        self.entry3.config(state="disabled")


    def clear(self):
        self.entry1.config(state="normal")
        self.entry1.delete(0,"end")
        #--------------------------#
        self.entry2.config(state="normal")
        self.entry2.delete(0,"end")
        #--------------------------#
        self.entry3.config(state="normal")
        self.entry3.delete(0,"end")
        #--------------------------#
        self.entry4.delete(0,"end")
        self.opcion.set(None)

    def info(self):
        mb.showinfo("Información", "Este programa sirve para ver si un motor de heron con X medidas produce la energia suficiente para encender una bombilla de 1, 3 o 6 watts")   
    

Aplication1=Aplication() 