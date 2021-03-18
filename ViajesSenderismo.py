'''
Created on 17 mar. 2021

@author: Ivi
'''
import tkinter
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import Tk, IntVar, Checkbutton, Button, W

ventana = tkinter.Tk()
ventana.title("Agencia de Viajes")
ventana.geometry("1200x650")
ventana.resizable(0,0)
etiqueta = tkinter.Label(ventana, text="Viajes de Senderismo", font='5').place(x=550,y=10)


canvas = Canvas(ventana, width = 142, height = 110)
canvas.place(x=1020,y=20)
img = PhotoImage(file="logo.png")
canvas.create_image(1,1, anchor = NW, image=img) 


v=tkinter.StringVar()

tk.Label(ventana, 
       text="Selecciona una Excursion:", font='5',).place(x=20,y=50)

tk.Radiobutton(ventana, text="Monte Abantos", variable=v, 
             value="Monte Abantos").place(x=20,y=80)

tk.Radiobutton(ventana, text="La Pedriza",variable=v, 
             value="La Pedriza").place(x=20,y=100)

tk.Radiobutton(ventana, text="Las dehesas de Cercedilla",variable=v, 
             value="Las dehesas de Cercedilla").place(x=20,y=120)

tk.Radiobutton(ventana, text="La Cabrera-Pico de la Miel", variable=v, 
             value="La Cabrera-Pico de la Miel").place(x=20,y=140)

etiqueta = Label(ventana, text="Seleccione los objetos que se va llevar", font='5').place(x=300,y=50)


CheckVar1 = IntVar()

CheckVar2 = IntVar()

CheckVar3 = IntVar()

CheckVar4 = IntVar()

CheckVar5 = IntVar()

CheckVar6 = IntVar()

CheckVar7 = IntVar()

CheckVar8 = IntVar()



C1 = Checkbutton(ventana, text = "Mochila", variable = CheckVar1, 
                onvalue = 1, offvalue = 0, 
                width = 10).place(x=400,y=80)

C2 = Checkbutton(ventana, text = "Linterna", variable = CheckVar2, 
                onvalue = 1, offvalue = 0, 
                width = 10).place(x=400,y=100)

C3 = Checkbutton(ventana, text = "GPS", variable = CheckVar3, 
                onvalue = 1, offvalue = 0, 
                width = 10).place(x=400,y=120)

C4 = Checkbutton(ventana, text = "Mapa", variable = CheckVar4, 
                onvalue = 1, offvalue = 0,
                width = 10).place(x=400,y=140)

C5 = Checkbutton(ventana, text = "Prismáticos", variable = CheckVar5, 
                onvalue = 1, offvalue = 0,
                width = 10).place(x=400,y=160)

C6 = Checkbutton(ventana, text = "Cantimplora", variable = CheckVar6, 
                onvalue = 1, offvalue = 0, 
                width = 10).place(x=400,y=180)

C7 = Checkbutton(ventana, text = "Botiquín", variable = CheckVar7, 
                onvalue = 1, offvalue = 0,
                width = 10).place(x=400,y=200)

C8 = Checkbutton(ventana, text = "Crema_Solar", variable = CheckVar8, 
                onvalue = 1, offvalue = 0,
                width = 10).place(x=400,y=220)



def remove(event):
    ctextoNombre.delete(0, END)
def remove2(event):
    ctextoApellidos.delete(0, END)
def remove3(event):
    ctextoDirección.delete(0, END)
def remove4(event):
    ctextoTelefono.delete(0, END)


titulo = Label(ventana, text="Datos del Excursionista", font='5')
titulo.place(x=20, y=215)

LabelNombre = Label(ventana, text="Nombre", bd = 1, width = 20)
LabelNombre.place(x=30, y=250)
nombre = StringVar()
ctextoNombre = Entry(ventana, fg="red3", width=200, textvariable = nombre)
ctextoNombre = Entry(ventana)
ctextoNombre.insert(0, "Escribe el nombre")
ctextoNombre.bind('<FocusIn>', remove)
ctextoNombre.place(x=40, y=270)

LabelApellidos = Label(ventana, text="Apellidos", bd = 1, width = 20)
LabelApellidos.place(x=30, y=300)
apellidos = StringVar()
ctextoApellidos = Entry(ventana)
ctextoApellidos.insert(0, "Escribe los apellidos")
ctextoApellidos.bind('<FocusIn>', remove2)
ctextoApellidos.place(x=40, y=320)

LabelDirección = Label(ventana, text="Direccion", bd = 1, width = 20)
LabelDirección.place(x=30, y=350)
direccion = StringVar()
ctextoDirección = Entry(ventana, fg="red3", width=30, textvariable = direccion)
ctextoDirección = Entry(ventana)
ctextoDirección.insert(0, "Escribe la direccion")
ctextoDirección.bind('<FocusIn>', remove3)
ctextoDirección.place(x=40, y=370)

LabelTeléfono = Label(ventana, text="Telefono", bd = 1, width = 20)
LabelTeléfono.place(x=30, y=400)
telefono = StringVar()
ctextoTelefono = Entry(ventana, fg="red3", width=30, textvariable = telefono)
ctextoTelefono = Entry(ventana)
ctextoTelefono.insert(0, "Escribe el telefono")
ctextoTelefono.bind('<FocusIn>', remove4)
ctextoTelefono.place(x=40, y=420)

TituloLocalidades =Label(ventana, text= 'Elige tu Población:', font='5').place(x=745,y=50)


def seleccion(ventana, event):
   print("Elemento seleccionado:", combo.get())



combo = ttk.Combobox(ventana, width=20, height= 7, font='5')

combo.place(x=725,y=80)

combo["values"] = ["Madrid", "Alcobendas", "San Sebastián de los Reyes", "Algete", "Pozuelo", "Las Rozas", "Majadahonda", "Móstoles","Alcorcón","Boadilla del Monte","Villaviciosa de Odón",]


combo.set("Poblacion")

combo.bind("<<ComboboxSeleccionado>>", seleccion)


Lb = Listbox(ventana, width=75, height= 12,font='5')


Lb.place(x=400, y=350)

listaCheck = [CheckVar1,CheckVar2,CheckVar3,CheckVar4,CheckVar5,CheckVar6,CheckVar7,CheckVar8]
listacombo = ["Mochila", "Linterna", "GPS", "Mapa", "Prismáticos", "Cantimplora", "Botiquín", "Crema_Solar"]


class excursionista(object):
    marcados = []
    localidad = ""
    nombre = ""
    apellidos = ""
    telefono = ""
    direccion = ""
    destino = ""

    def __init__(self, marcados, poblacion, ctextoNombre, ctextoApellidos, ctextoTelefono, ctextoDirección, excur):
        self.marcados = marcados
        self.poblacion = poblacion
        self.ctextoNombre = ctextoNombre
        self.ctextoApellidos = ctextoApellidos
        self.ctextoTelefono = ctextoTelefono
        self.ctextoDirección = ctextoDirección
        self.excur = excur

    def __str__(self):
        return "Nombre: "+self.ctextoNombre+", Apellidos: "+self.ctextoApellidos+", Direccion: "+self.ctextoDirección+", Telefono: "+self.ctextoTelefono
    def objetos(self):   
        return "Objetos seleccionados: "+self.marcados.__str__()


contadorExcur = 1 

def actualizar():
    global contadorExcur
    
    listaCheckeados = []
    for item in range(0, listaCheck.__len__()):
        if listaCheck.__getitem__(item).get() == 1:
            listaCheckeados.append(listacombo.__getitem__(item))

    # listaCheckeados.append()
    excursi = excursionista(listaCheckeados, combo.get(), ctextoNombre.get(), 
                            ctextoApellidos.get(), ctextoTelefono.get(), ctextoDirección.get(), v.get())
    Lb.insert(tk.ANCHOR, "Excursionista "+str(contadorExcur))
    Lb.insert(tk.ANCHOR, excursi)
    Lb.insert(tk.ANCHOR,"Poblacion: "+excursi.poblacion+", Excursion a: "+excursi.excur)
    Lb.insert(tk.ANCHOR, excursi.objetos())
    Lb.insert(tk.ANCHOR, "-----------------------------------------------------------------------------------------------------------------------------------------")
    contadorExcur=contadorExcur+1
boton = Button(ventana, text="Enviar Excursionista",font='5', command=actualizar, height=2, width=16, activebackground="#F50743").place(x=730, y=250)

ventana.mainloop()