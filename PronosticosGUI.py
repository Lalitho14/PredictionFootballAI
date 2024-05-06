from tkinter import *
from chatowndata02 import Predecir
import shutil

root = Tk()
root.title("Pronosticos")
root.geometry("700x800")

gol_l_x_gral = StringVar()
gol_l_x_local = StringVar()
gol_l_x_visita = StringVar()

gol_x_p_eq_a = StringVar()
gol_x_against_eq_a = StringVar()
golx_p_local_eq_a = StringVar()
golx_against_local_eq_a = StringVar()
historyeqA = [StringVar() for _ in range(5)]
history_entries = []

gol_x_p_eq_b = StringVar()
gol_x_against_eq_b = StringVar()
golx_p_local_eq_b = StringVar()
golx_against_local_eq_b = StringVar()
historyeqB = [StringVar() for _ in range(5)]
history_entries_B = []

def DatosLiga():
    with open("data_.txt", "w") as archivo:
        archivo.write("Datos de Liga X:\n")
        archivo.write("Goles esperados en la LIGA X general = " + gol_l_x_gral.get() + "\n")
        archivo.write("Goles esperados en la LIGA X de local = " + gol_l_x_local.get() + "\n")
        archivo.write("Goles esperados en la LIGA X de visitante = " + gol_l_x_visita.get() + "\n")

def DatosEquipoA():
    with open("data_.txt", "a") as archivo:
        archivo.write("\nDatos EQUIPO A:\n")
        archivo.write("Goles a favor de EQUIPO A por partido = " + gol_x_p_eq_a.get() + "\n")
        archivo.write("Goles en contra de EQUIPO A por partido = " + gol_x_against_eq_a.get() + "\n")
        archivo.write("Goles a favor de EQUIPO A por partido como local = " + golx_p_local_eq_a.get() + "\n")
        archivo.write("Goles a en contra de EQUIPO A por partido como local = " + golx_against_local_eq_a.get() + "\n")
        archivo.write("Ultimos resultados del EQUIPO A como local : \n")
        for i in range(len(history_entries)):
            historyeqA[i].set(history_entries[i].get())
            archivo.write(CalResultado(historyeqA[i]))

def CalResultado(x):
    marcador = x.get()
    res = marcador.split()
    print(res)
    if res[0] > res[1]:
        return marcador + " victoria\n"
    if res[0] < res[1]:
        return marcador + " derrota\n"
    if res[0] == res[1]:
        return marcador + " empate\n"

def CalResultado_V(x):
    marcador = x.get()
    res = marcador.split()
    print(res)
    if res[0] < res[1]:
        return marcador + " victoria\n"
    if res[0] > res[1]:
        return marcador + " derrota\n"
    if res[0] == res[1]:
        return marcador + " empate\n"

def DatosEquipoB():
    with open("data_.txt", "a") as archivo:
        archivo.write("\nDatos EQUIPO B:\n")
        archivo.write("Goles a favor de EQUIPO B por partido = " + gol_x_p_eq_b.get() + "\n")
        archivo.write("Goles en contra de EQUIPO B por partido = " + gol_x_against_eq_b.get() + "\n")
        archivo.write("Goles a favor de EQUIPO B por partido como visita = " + golx_p_local_eq_b.get() + "\n")
        archivo.write("Goles a en contra de EQUIPO B por partido como visita = " + golx_against_local_eq_b.get() + "\n")
        archivo.write("Ultimos resultados del EQUIPO B como visita : \n")
        for i in range(len(history_entries_B)):
            historyeqB[i].set(history_entries_B[i].get())
            archivo.write(CalResultado_V(historyeqB[i]))

def EnviarDatos():
    DatosLiga()
    DatosEquipoA()
    DatosEquipoB()
    # Especifica la ruta de la carpeta que deseas eliminar
    carpeta = "__pycache__"
    # Intenta eliminar la carpeta y su contenido
    try:
        shutil.rmtree(carpeta)
        print("Carpeta eliminada exitosamente.")
    except OSError as e:
        print(f"No se pudo eliminar la carpeta: {e}")
    prediccion = Predecir()
    n_ventana = Toplevel(root)
    resultado = Label(n_ventana, text=prediccion)
    resultado.pack()

###DATOS DE LIGA####################################
label_1 = Label(root, text = "Datos de Liga")
label_1.grid(row=0, column=0)

label_2 = Label(root, text="Goles esperados en general = ")
label_2.grid(row=1, column=0)
geg = Entry(root, textvariable=gol_l_x_gral)
geg.grid(row=1, column=1)

label_3 = Label(root, text="Goles esperados de local = ")
label_3.grid(row=2, column=0)
gel = Entry(root, textvariable=gol_l_x_local)
gel.grid(row=2, column=1)

label_4 = Label(root, text="Goles esperados en visita = ")
label_4.grid(row=3, column=0)
gev = Entry(root, textvariable=gol_l_x_visita)
gev.grid(row=3, column=1)

############# DATOS EQUIPO A ################################
label_5 = Label(root, text="Datos Equipo A")
label_5.grid(row=4, column=0)

label_6 = Label(root, text="Goles a favor por partido = ")
label_6.grid(row=5, column=0)
gxpeqA_grl = Entry(root, textvariable=gol_x_p_eq_a)
gxpeqA_grl.grid(row=5, column=1)

label_7 = Label(root, text="Goles en contra por partido = ")
label_7.grid(row=6, column=0)
no_gxpeqA_grl = Entry(root, textvariable=gol_x_against_eq_a)
no_gxpeqA_grl.grid(row=6, column=1)

label_8 = Label(root, text="Goles a favor como local por partido = ")
label_8.grid(row=7, column=0)
no_gxpeqA_grl = Entry(root, textvariable=golx_p_local_eq_a)
no_gxpeqA_grl.grid(row=7, column=1)

label_9 = Label(root, text="Goles en contra como local por partido = ")
label_9.grid(row=8, column=0)
no_gxpeqA_grl = Entry(root, textvariable=golx_against_local_eq_a)
no_gxpeqA_grl.grid(row=8, column=1)

for i in range(5):
    label_historial = Label(root, text="Partido " + str((i+1)))
    label_historial.grid(row=9+i, column=0)
    entry = Entry(root, textvariable=historyeqA[i])
    entry.grid(row=9+i, column=1)
    history_entries.append(entry)

############ DATOS EQUIPO B ##########################
label_10 = Label(root, text="Datos Equipo B")
label_10.grid(row=4, column=2)

label_11 = Label(root, text="Goles a favor por partido = ")
label_11.grid(row=5, column=2)
gxpeqA_grl = Entry(root, textvariable=gol_x_p_eq_b)
gxpeqA_grl.grid(row=5, column=3)

label_12 = Label(root, text="Goles en contra por partido = ")
label_12.grid(row=6, column=2)
no_gxpeqA_grl = Entry(root, textvariable=gol_x_against_eq_b)
no_gxpeqA_grl.grid(row=6, column=3)

label_13 = Label(root, text="Goles a favor como visita por partido = ")
label_13.grid(row=7, column=2)
no_gxpeqA_grl = Entry(root, textvariable=golx_p_local_eq_b)
no_gxpeqA_grl.grid(row=7, column=3)

label_14 = Label(root, text="Goles en contra como visita por partido = ")
label_14.grid(row=8, column=2)
no_gxpeqA_grl = Entry(root, textvariable=golx_against_local_eq_b)
no_gxpeqA_grl.grid(row=8, column=3)

for i in range(5):
    label_historial = Label(root, text="Partido " + str((i+1)))
    label_historial.grid(row=9+i, column=2)
    entry = Entry(root, textvariable=historyeqB[i])
    entry.grid(row=9+i, column=3)
    history_entries_B.append(entry)

boton1 = Button(root, text="Calcular", command=EnviarDatos)
boton1.grid(row=0, column=2)

root.mainloop()
