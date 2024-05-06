from tkinter import *

root = Tk()

root.title("Pronosticos")
root.geometry("500x300")
#root.resizable(0, 1)
#root.config(background="red", cursor="boat")

# boton1 = Button(root, text="Minimizar", command=root.iconify, bg="red")
# #boton1.pack()
# boton1.pack(side=LEFT)

# def imprimir():
#     #print("Imprimiendo...")
#     label1 = Label(root, text="Imprimiendo")
#     label1.pack()

# boton2 = Button(root, text="Imprimir", command=imprimir, bg="blue")
# boton2.pack(side=RIGHT)

# etiqueta = Label(root, text="Etiqueta")
# #etiqueta.grid(row=0, column=0)
# #etiqueta.place(x=30, y=40)

# boton1 = Button(root, text="Boton")
# boton1.grid(row=0, column=1)
nombre = StringVar()
apellido = StringVar()

nombre.set("Escribe aqui tu nombre")
apellido.set("Escribe tu apellido")

def Saludar():
    print("Hola " + nombre.get() + " " + apellido.get())

def Saludar2():
    print("Hola " + nombre.get() + " " + apellido.get())

etiqueta1 = Label(root, text="Nombre: ")
etiqueta1.grid(row=0, column=0)
entrada1 = Entry(root, textvariable=nombre)
entrada1.grid(row=0, column=1)

etiqueta2 = Label(root, text="Apellido: ")
etiqueta2.grid(row=1, column=0)
entrada2 = Entry(root, textvariable=apellido)
entrada2.grid(row=1, column=1)

boton1 = Button(root, text="Saludar ahora", command=Saludar)
boton1.grid(row=2, column=1)

root.mainloop()
