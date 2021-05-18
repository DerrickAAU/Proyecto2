import tkinter
from tkinter  import *
"""
Nombre: Menú Principal
Entrada: Sin entrada
Parametros: No posee
Salida: El retorno a un siguente menú
Restricciones: No posee
"""

def ventanaPrincipal():
    vtnPrincipal =tkinter.Tk()
    vtnPrincipal.geometry("500x400")
    vtnPrincipal.title("Ventana Principal")
    vtnPrincipal.config(bg="SteelBlue3", cursor="hand2")
    vtnPrincipal.resizable(False,False )

    tkinter.Label(vtnPrincipal, text="۝   MENÚ PRINCIPAL   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnPrincipal, text="¡Bienvenid@ al Sistema de Reservación de Boletos!" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=75,y=35)
    tkinter.Label(vtnPrincipal, text="Precione una opción para continuar:" , font=("Times New Roman",14),bg="SteelBlue3",fg="black").place(x=2,y=70)
    tkinter.Label(vtnPrincipal, text="Esto es un programa de reservacion de boletos\npara realizar transaciones con algún servicio." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=290,y=370)
    tkinter.Label(vtnPrincipal, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=280,y=367)
    #Decorativo
    tkinter.Label(vtnPrincipal, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=95)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=115)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=135)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=155)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=175)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=195)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=215)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=235)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=255)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=275)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=295)
    tkinter.Label(vtnPrincipal, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=20,y=310)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=470,y=115)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=470,y=135)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=470,y=155)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=470,y=175)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=470,y=195)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=470,y=215)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=470,y=235)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=470,y=255)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=470,y=275)
    tkinter.Label(vtnPrincipal, text="I" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=470,y=295)
    #Botones
    boton1=tkinter.Button(vtnPrincipal, text="1-Menú administrativo", font=("Arial",12),bg="DeepSkyBlue4",fg="black", command= vtnAcceso).place(x=60,y=150)
    tkinter.Button(vtnPrincipal, text="  2-Menú de usuarios  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black").place(x=275,y=150)
    tkinter.Button(vtnPrincipal, text="3-Salir", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command=exit).place(x=225,y=230)

"""
Nombre: vntAcceso
Entrada: Sin entrada
Parametros: No posee
Salida: El retorno a un siguente menú
Restricciones:
"""

def vtnAcceso():
    vtnAcceso =tkinter.Tk()
    vtnAcceso.geometry("500x400")
    vtnAcceso.title("Ventana de Acceso")
    vtnAcceso.config(bg="SteelBlue3", cursor="hand2")
    vtnAcceso.resizable(False,False )

    tkinter.Label(vtnAcceso, text="۝   MENÚ DE ACCESO   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnAcceso, text="¡Debe ingresar la contraseña para continuar!" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=75,y=35)






ventanaPrincipal()
