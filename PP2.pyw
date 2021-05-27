import tkinter
from tkinter  import *
from tkinter import messagebox


##########################
#Primeramente agregaremos unas validaciones al codigo. 
"""  
Nombre: convertirstr 
Entrada: una lista
Parametros: lista
Salida: un string
Restricciones: La entrada debe ser una lista.
"""
def convertirstr(lista):
    if isinstance(lista, list):
        string = ""
        for indice in lista:
            string += indice
        return string
    else:
        print("Error: No se puede convertir a String, el tipo de dato de entrada, no es una lista")
        
#----------------------------------------------------------
#Cantidad de indice que contiene
"""
Nombre: CantidadDeindices
Entrada: sin estrada
Parametros: convertirstr
Salida: sin salida
Restricciones: sin restriccion
"""
def cantidadDeindices(convertirstr):
    if convertirstr == "" or convertirstr==[]:
        return 0
    else:
        return 1+ cantidadDeindices(convertirstr[1:])


def validarCedula(cedula):
    if(cantidadDeindices(cedula)==10):
        return True
    else:
        False

#----------------------------------------------------------------------------------
def validarCed(cedula,empresas):
    empresas1= open("Empresas.txt")
    empresasred= empresas1.readlines()
    if(seEncuentra("Cedula:"+cedula + "\n", empresasred)):
        return True
    else:
        False

#--------------------------

def validarPla(placa, transportes):
    transportes1=open("Transportes.txt")
    transportesred= transportes1.readlines()
    if(seEncuentra("Placa:"+placa+"\n", transportesred)):
        return True
    else:
        False
         
    

"""
Nombre: seEncuentra
Entrada: lo que se va buscar y los dattos en str
Parametros: buscar,covertirstr
Salida: True o False
Restricciones: sin restricciones
"""

def seEncuentra(buscar,convertirstr):
    indicesBuscar= cantidadDeindices(buscar)
    if isinstance(convertirstr,list):
        return seEncuentraA(buscar,indicesBuscar,convertirstr,0)
    else:
        return seEncuentraEnstring(buscar,convertirstr,indicesBuscar)

def seEncuentraA(buscar,indicesBuscar,lista,cont):
    if lista == []:
        return False
    else:
        if seEncuentraEnstring(buscar,lista[0],indicesBuscar):
            return True
        else:
            return seEncuentraA(buscar,indicesBuscar,lista[1:],cont +1)

def seEncuentraEnstring(buscar,cadena,indicesBuscar):
    if cadena =="":
        return False
    else:
        if buscar== cadena [0: indicesBuscar]:
            return True
        else:
            return seEncuentraEnstring(buscar,cadena[1:], indicesBuscar)
        

#------------------------------------------------------------------------------------------
#Eliminar informacion para empresas
def eliminarInformacion(listaEmpresas, indice, cont):
    if cont==4:
        return convertirstr(listaEmpresas)
    else:
        listaEmpresas.pop(indice)
        return eliminarInformacion(listaEmpresas, indice, cont + 1)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Para eliminar la informacion en el archivo transporte
def eliminarInformacion_aux(listaTransportes, indice, cont):
    if cont==10:
        return convertirstr(listaTransportes)
    else:
        listaTransportes.pop(indice)
        return eliminarInformacion_aux(listaTransportes, indice, cont + 1)
     
##########################


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
    boton1=tkinter.Button(vtnPrincipal, text="1-Menú administrativo", font=("Arial",12),bg="DeepSkyBlue4",fg="black", command= lambda:vtnAcceso(vtnPrincipal)).place(x=60,y=150)
    tkinter.Button(vtnPrincipal, text="  2-Menú de usuarios  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black").place(x=275,y=150)
    tkinter.Button(vtnPrincipal, text="3-Salir", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command=exit).place(x=225,y=230)
    vtnPrincipal.mainloop()

"""
Nombre: vntAcceso
Entrada: Sin entrada
Parametros: No posee
Salida: El retorno a un siguente menú
Restricciones: No posee
"""

def vtnAcceso(vtnPrincipal):
    esconder(vtnPrincipal)
    vtnAcceso =tkinter.Tk()
    vtnAcceso.geometry("500x400")
    vtnAcceso.title("Ventana de Acceso")
    vtnAcceso.config(bg="SteelBlue3", cursor="hand2")
    vtnAcceso.resizable(False,False )
    
    tkinter.Label(vtnAcceso, text="۝   MENÚ DE ACCESO   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnAcceso, text="¡Debe ingresar la contraseña para continuar!" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=75,y=35)
    tkinter.Label(vtnAcceso, text="Escriba la contraseña para ingresar a la Administración:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=90)
    entrada=tkinter.Entry(vtnAcceso, text="",show="*", font=("Arial",14), bg="white", fg="Black")
    entrada.place(x=140, y=140)
    button=tkinter.Button(vtnAcceso,text="  Continuar  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command =lambda:comprobarClave(entrada.get())).place(x=210,y=180)
    tkinter.Label(vtnAcceso, text="Para entrar a la administracion es necesario\nla contraseña de acceso." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=290,y=370)
    tkinter.Label(vtnAcceso, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=280,y=367)
    btnAtras=tkinter.Button(vtnAcceso, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=lambda:atras(vtnAcceso,ventanaPrincipal)).place(x=20,y=350)

    vtnAcceso.mainloop()
    
def comprobarClave(entrada):
    archivo_clave=open("Clave.txt")
    clave1=archivo_clave.readlines()
    clave1=clave1[0]
    archivo_clave.close()
    if(entrada==clave1):
        return vtnAdministracion()
    else:
        messagebox.showerror(title = "Clave incorrecta", message = "La clave no es correcta")
        


#############
"""
Nombre: vtnAdministracion
Entrada: no posee
Parametros: no posee
Salida: otro menú de opciones
Restricciones: no posee
"""
def vtnAdministracion():
    vtnAdmin =tkinter.Tk()
    vtnAdmin.geometry("500x400")
    vtnAdmin.title("Menú de Administración")
    vtnAdmin.config(bg="SteelBlue3", cursor="hand2")
    vtnAdmin.resizable(False,False )
        
    tkinter.Label(vtnAdmin, text="۝   MENÚ ADIMINISTRATIVO   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnAdmin, text="Elija una de las siguentes opciones:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    #Botón
    boton1=tkinter.Button(vtnAdmin, text="      1-Gestion de Empresa            ", font=("Arial",12),bg="DeepSkyBlue4",fg="black", command= gestionEmpresa).place(x=10,y=70)
    boton2=tkinter.Button(vtnAdmin, text="      2- Gestion de Transporte        ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command= gestionTransporte).place(x=10,y=110)
    boton3=tkinter.Button(vtnAdmin, text="      3-Gestion de viaje                    ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command= gestionViaje).place(x=10,y=150)
    boton4=tkinter.Button(vtnAdmin, text="      4-Estadistica de viaje              ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command= consultaReservaciones).place(x=10,y=190)
    boton5=tkinter.Button(vtnAdmin, text="5-Consultar historial de reservaciones", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command=estadisticaViaje).place(x=10,y=230)
    tkinter.Label(vtnAdmin, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=270)
    tkinter.Label(vtnAdmin, text="Este apartado es el de la administación\ntoca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=290,y=370)
    tkinter.Label(vtnAdmin, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=280,y=367)
    btnAtras=tkinter.Button(vtnAdmin, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command= lambda:atras(vtnAdmin,vtnAcceso(vtnPrincipal))).place(x=20,y=350)

    vtnAdmin.mainloop()
#___________________________________________________________________________________#
"""
Nombre: gestionEmpresas
Entrada: no posee
Parametros: no posee
Salida: otro menú
Restricciones: no posee
"""
def gestionEmpresa():
    vtnge=tkinter.Tk()
    vtnge.geometry("500x400")
    vtnge.title("Gestion de Empresas")
    vtnge.config(bg="SteelBlue3", cursor="hand2")
    vtnge.resizable(False,False )
        
    tkinter.Label(vtnge, text="۝   GESTION DE EMPRESAS   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnge, text="Precione lo que desea realizar en este menú:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    btnAñadire=tkinter.Button(vtnge, text="Añadir Empresa     ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=añadirEmpresa).place(x=10,y=80)
    btnEliminare=tkinter.Button(vtnge, text="Eliminar Empresa  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=eliminarEmpresa).place(x=10,y=120)
    btnModificare=tkinter.Button(vtnge, text="Modificar Empresa", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command= modificarEmpresa).place(x=10,y=160)
    btnMostare=tkinter.Button(vtnge, text="Mostar Empresas  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=200)
    btnAtrase=tkinter.Button(vtnge, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=vtnAdministracion).place(x=20,y=350)
    tkinter.Label(vtnge, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnge, text="En esta ventana estan todas las opciones de \ngestion de empresas toca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=200,y=370)
    tkinter.Label(vtnge, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnge.mainloop()

#------------------------Añadir--------------------------------------------------------------------------------------------------------------

def añadirEmpresa():
    vtnae=tkinter.Tk()
    vtnae.title("Agregando Empresa")
    vtnae.geometry("500x400")
    vtnae.resizable(False,False)
    vtnae.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnae, text="۝   AGREGANDO EMPRESA   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    lblCedula=tkinter.Label(vtnae,text="Cédula Juridica:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblCedula.place(x=5,y=40)
    cedulae=tkinter.Entry(vtnae,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    cedulae.place(x=145,y=40)
    lblNombre=tkinter.Label(vtnae,text="Nombre:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblNombre.place(x=5,y=80)
    nombree=tkinter.Entry(vtnae,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    nombree.place(x=145,y=85)
    lblubicacion=tkinter.Label(vtnae,text="Ubicación:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblubicacion.place(x=5,y=124)
    ubicacione=tkinter.Entry(vtnae,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    ubicacione.place(x=145,y=129)
    tkinter.Button(vtnae,text="AGREGAR EMPRESA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda:añadirEmpresaptxt(cedulae.get(),nombree.get(),ubicacione.get())).place(x=145,y=180)
    tkinter.Button(vtnae,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black").place(x=190,y=215)
    tkinter.Label(vtnae, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnae, text="En esta ventana puedes agregar tu empresa \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnae, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnae.mainloop()
#-------------------Añadir al archivo de texto---------------------------------------------------------------------------------
    

def añadirEmpresaptxt(cedula,nombre,ubicacion):
    if(validarCedula(cedula)):
        if(cedula!="" and nombre!="" and ubicacion!=""):
            if(validarCed(cedula,"")):
                messagebox.showerror(title = "Error de la Cedula", message = "Esta cedula ya está registrada")
            else:
                Empresas=open("Empresas.txt","a")
                Empresas.write("Cedula:"+cedula+"\n")
                Empresas.write("Nombre:"+nombre+"\n")
                Empresas.write("ubicacion:"+ubicacion+"\n")
                Empresas.write("--------------------------------------" + "\n")
                Empresas.close()
                messagebox.showinfo(title = "Empresa agregada", message = "La empresa se agregó con exito")
        else:
            messagebox.showerror(title = "Error de contenido", message = "Para agregar una empresa debe llenar los espacios")
    else:
        messagebox.showerror(title = "Error de la Cedula", message = "La cedula no contiene 10 digitos")


#------------------------Eliminar--------------------------------------------------------------------------------------------------------------def añadirEmpresa():
def eliminarEmpresa():
    vtnee=tkinter.Tk()
    vtnee.title("Agregando Empresa")
    vtnee.geometry("500x400")
    vtnee.resizable(False,False)
    vtnee.config(bg="SteelBlue3", cursor="X_cursor")
    tkinter.Label(vtnee, text="۝   ELIMINANDO EMPRESA   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnee, text="Este apartado es para eliminar una empresa ya registrada\nPor favor ingrese en el siguiente apartado la cedula respectiva a la\n empresa" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=25,y=60)
    lblCedula=tkinter.Label(vtnee,text="Cédula Juridica:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblCedula.place(x=5,y=130)
    cedulae=tkinter.Entry(vtnee,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    cedulae.place(x=145,y=130)
    tkinter.Button(vtnee,text="ELIMINAR EMPRESA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Red", command= lambda:eliminarEmpresaptxt(cedulae.get())).place(x=145,y=180)
    tkinter.Button(vtnee,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black").place(x=190,y=215)
    tkinter.Label(vtnee, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnee, text="En esta ventana puedes agregar tu empresa \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnee, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnee.mainloop()


def eliminarEmpresaptxt(cedula):
    Empresas = open("Empresas.txt")
    listaEmpresas = Empresas.readlines()
    if(seEncuentra(cedula+"\n",listaEmpresas)):
        cedula=str(cedula)
        indice = listaEmpresas.index("Cedula:"+cedula+"\n")
        cedula = eliminarInformacion(listaEmpresas, indice, 0)
        Empresas.close()
        Empresas = open("Empresas.txt", "w")
        Empresas.write(cedula)
        Empresas.close()
        messagebox.showinfo(title = "Eliminar Empresa", message = "La empresa ha sido borrada exitosamente ")

    else:
        messagebox.showerror(title = "Eliminar Empresa", message = "No se encuentra ninguna cedula registrada con "+cedula)


#------------------------Modificarr--------------------------------------------------------------------------------------------------------------def añadirEmpresa():
#Ventana Principal
def modificarEmpresa():
    vtnme=tkinter.Tk()
    vtnme.title("Modificar Empresa")
    vtnme.geometry("500x400")
    vtnme.resizable(False,False)
    vtnme.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnme, text="۝   MODIFICAR EMPRESA   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnme, text="Este apartado es para modificar una empresa ya registrada\nPor favor ingrese en el siguiente apartado la cedula respectiva a la\n empresa" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=25,y=60)
    lblCedula=tkinter.Label(vtnme,text="Cédula Juridica:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblCedula.place(x=5,y=130)
    cedulaem=tkinter.Entry(vtnme,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    cedulaem.place(x=145,y=130)
    botonm=tkinter.Button(vtnme,text="MODIFICAR EMPRESA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda:modificarEmpresatxt(cedulaem.get()))
    botonm.place(x=145,y=180)
    tkinter.Button(vtnme,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black").place(x=190,y=215)
    tkinter.Label(vtnme, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnme, text="En esta ventana puedes agregar tu empresa \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnme, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnme.mainloop()

#Verifica si se encuentra
def modificarEmpresatxt(cedula):
    Empresas = open("Empresas.txt")
    listaEmpresas = Empresas.readlines()
    if(seEncuentra(cedula+"\n",listaEmpresas)):
        cedula=str(cedula)
        indice = listaEmpresas.index("Cedula:"+cedula+"\n")
        cedula = eliminarInformacion(listaEmpresas, indice, 0)
        Empresas.close()
        Empresas = open("Empresas.txt", "w")
        Empresas.write(cedula)
        Empresas.close()
        return modificarEmpresa1()
    else:
        messagebox.showerror(title = "Eliminar Empresa", message = "No se encuentra ninguna cedula registrada con "+cedula)
        
#Pidiendo los nuevos datos
def modificarEmpresa1():
    vtnmme=tkinter.Tk()
    vtnmme.title("Modificar Empresa")
    vtnmme.geometry("500x400")
    vtnmme.resizable(False,False)
    vtnmme.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnmme, text="۝ AGREGAR NUEVA EMPRESA ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    lblCedula=tkinter.Label(vtnmme,text="Cédula Juridica nueva:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblCedula.place(x=5,y=40)
    cedulae=tkinter.Entry(vtnmme,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    cedulae.place(x=200,y=40)
    lblNombre=tkinter.Label(vtnmme,text="Nombre nuevo:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblNombre.place(x=5,y=80)
    nombree=tkinter.Entry(vtnmme,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    nombree.place(x=200,y=85)
    lblubicacion=tkinter.Label(vtnmme,text="Ubicación nueva:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblubicacion.place(x=5,y=124)
    ubicacione=tkinter.Entry(vtnmme,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    ubicacione.place(x=200,y=129)
    tkinter.Button(vtnmme,text="AGREGAR EMPRESA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda:añadirEmpresaptxtm(cedulae.get(),nombree.get(),ubicacione.get())).place(x=205,y=180)
    tkinter.Button(vtnmme,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black").place(x=250,y=215)
    tkinter.Label(vtnmme, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnmme, text="En esta ventana puedes modificar tu empresa \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnmme, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnmme.mainloop()

#Añade al archivo
def añadirEmpresaptxtm(cedula, nombre, ubicacion):
    if(validarCedula(cedula)):
        if(cedula!="" and nombre!="" and ubicacion!=""):
            if(validarCed(cedula,"")):
                messagebox.showerror(title = "Error de la Cedula", message = "Esta cedula ya está registrada")
            else:
                Empresas=open("Empresas.txt","a")
                Empresas.write("Cedula:"+cedula+"\n")
                Empresas.write("Nombre:"+nombre+"\n")
                Empresas.write("ubicacion:"+ubicacion+"\n")
                Empresas.write("--------------------------------------" + "\n")
                Empresas.close()
                messagebox.showinfo(title = "Empresa agregada", message = "La empresa se agregó con exito")
        else:
            messagebox.showerror(title = "Error de contenido", message = "Para agregar una empresa debe llenar los espacios")
    else:
        messagebox.showerror(title = "Error de la Cedula", message = "La cedula no contiene 10 digitos")

#-----------------------------------------------------------------------------------------------------------------------------
#---------Mostrar--------------------------------------------------------------------------------------------------------

#def mostarEmpresas():





#___________________________________________________________________________________________________________#
"""
Nombre: gestionTransporte
Entrada: no posee
Parametros: no posee
Salida: otro menu de opciones
Restricciones: no posee
"""
def gestionTransporte():
    vtnT=tkinter.Tk()
    vtnT.geometry("500x400")
    vtnT.title("Gestion de Transporte")
    vtnT.config(bg="SteelBlue3", cursor="hand2")
    vtnT.resizable(False,False )
        
    tkinter.Label(vtnT, text="۝   GESTION TRANSPORTE   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnT, text="Precione lo que desea realizar en este menú:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    btnAñadirt=tkinter.Button(vtnT, text="Añadir Transporte     ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command= lambda: añadirTransporte()).place(x=10,y=80)
    btnEliminart=tkinter.Button(vtnT, text="Eliminar Transporte  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command= lambda:eliminarTransporte()).place(x=10,y=120)
    btnModificart=tkinter.Button(vtnT, text="Modificar Transporte", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=160)
    btnMostart=tkinter.Button(vtnT, text="Mostar Transporte  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=200)
    btnAtrast=tkinter.Button(vtnT, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=vtnAdministracion).place(x=20,y=350)
    tkinter.Label(vtnT, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnT, text="En esta ventana estan todas las opciones de \ngestion de transporte toca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=200,y=370)
    tkinter.Label(vtnT, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnT.mainloop()
    
#-------------Añadir T------------------------------------------------------------------------------------
def añadirTransporte():
    vtnat=tkinter.Tk()
    vtnat.title("Agregando Transporte")
    vtnat.geometry("500x400")
    vtnat.resizable(False,False)
    vtnat.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnat, text="۝   AÑADIR TRANSPORTE   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnat, text="Este apartado es para añadir un transporte nuevo al sistema\nSolo son permitidos dos tipos de vehículos\nPor favor elija el tipo de vehiculo que desea registrar" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=25,y=60)
    tkinter.Button(vtnat,text="BUSETA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="black", command= lambda:añadirBuseta()).place(x=300,y=170)
    tkinter.Button(vtnat,text="LIMOSINA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="black", command= lambda:añadirLimosina()).place(x=80,y=170)
    tkinter.Label(vtnat, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Button(vtnat,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black").place(x=200,y=290)
    tkinter.Label(vtnat, text="En esta ventana puedes agregar tu empresa \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnat, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnat.mainloop()
#
#Aladir Transporte Buseta
def añadirBuseta():
    vtnab=tkinter.Tk()
    vtnab.title("Agregando Transporte")
    vtnab.geometry("500x550")
    vtnab.resizable(False,False)
    vtnab.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnab, text="۝   AGREGANDO BUSETA   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnab, text="Registre la buseta llenando los campos:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)

    lblplacab=tkinter.Label(vtnab,text="Placa:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblplacab.place(x=5,y=80)
    placab=tkinter.Entry(vtnab,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    placab.place(x=145,y=80)

    lbltipob=tkinter.Label(vtnab,text="Tipo:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lbltipob.place(x=5,y=120)
    tipob=tkinter.Entry(vtnab,text="Buseta",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    tipob.place(x=145,y=120)

    lblmarcab=tkinter.Label(vtnab,text="Marca:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblmarcab.place(x=5,y=160)
    marcab=tkinter.Entry(vtnab,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    marcab.place(x=145,y=160)

    lblmodelob=tkinter.Label(vtnab,text="Modelo:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblmodelob.place(x=5,y=200)
    modelob=tkinter.Entry(vtnab,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    modelob.place(x=145,y=200)

    lblañob=tkinter.Label(vtnab,text="Año:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblañob.place(x=5,y=240)
    añob=tkinter.Entry(vtnab,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    añob.place(x=145,y=240)

    lblempresab=tkinter.Label(vtnab,text="Empresa:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblempresab.place(x=5,y=280)
    lblempresabb=tkinter.Label(vtnab,text="-Debe ser una empresa existente-",font=("Times New Roman",10), bg="SteelBlue3",fg="Black").place(x=315,y=165)
    empresab=tkinter.Entry(vtnab,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    empresab.place(x=145,y=280)

    tkinter.Button(vtnab,text="AGREGAR BUSETA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: añadirBusetatxt(placab.get(),tipob.get(),marcab.get(),modelob.get(),añob.get(),empresab.get())).place(x=155,y=370)
    tkinter.Button(vtnab,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black").place(x=190,y=400)
    tkinter.Label(vtnab, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=450)
    tkinter.Label(vtnab, text="En esta ventana puedes agregar tu empresa \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=510)
    tkinter.Label(vtnab, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=507)  
    vtnab.mainloop()
    
def añadirBusetatxt(placa,tipo,marca,modelo,año,empresa):
    if(placa!="" and tipo!="" and marca!="" and modelo!="" and año!="" and empresa!=""):
        if(validarPla(placa,"")):
            messagebox.showerror(title = "Error de la Placa", message = "Esta placa ya está registrada")
        else:
            Transportes=open("Transportes.txt","a")
            Transportes.write("Placa:"+placa+"\n")
            Transportes.write("Tipo:"+tipo+"\n")
            Transportes.write("Marca:"+marca+"\n")
            Transportes.write("Modelo:"+modelo+"\n")
            Transportes.write("Año:"+año+"\n")
            Transportes.write("Empresa:"+empresa+"\n")
            Transportes.close()
            return camposBuseta()

    else:
        messagebox.showerror(title = "Error de contenido", message = "Para agregar un Transporte debe llenar los espacios")

def camposBuseta():
    vtncb=tkinter.Tk()
    vtncb.geometry("600x600")
    vtncb.title("Gestion de Transporte")
    vtncb.config(bg="SteelBlue3", cursor="hand2")
    vtncb.resizable(False,False )
        
    tkinter.Label(vtncb, text="۝  CANTIDAD DE ASIENTOS  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtncb, text="Estos son los ascientos disponibles\nColor verde = Asientos VIP\nColor amarillo = Asientos Normal\nColor azul = Asiento Economicos\nSegún su categoría elija " , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    lblasiento= tkinter.Label(vtncb, text="Estos son los ascientos disponibles\nColor verde = Asientos VIP\nColor amarillo = Asientos Normal\nColor azul = Asiento Economicos\nSegún su categoría escriba los que desee" , font=("Times New Roman",12),bg="SteelBlue3",fg="blue4").place(x=1,y=40)

    lblvip=tkinter.Label(vtncb,text="VIP:",font=("Angency FB",10), bg="SteelBlue3", fg="Black")
    lblvip.place(x=5,y=160)
    vip=tkinter.Entry(vtncb,text="", font=("Agency FB",10), bg="SkyBlue1", fg="Black")
    vip.place(x=100,y=160)

    lblnormal=tkinter.Label(vtncb,text="Normal:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lblnormal.place(x=5,y=200)
    normal=tkinter.Entry(vtncb,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    normal.place(x=100,y=200)

    lbleconomico=tkinter.Label(vtncb,text="Economico:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lbleconomico.place(x=5,y=240)
    economico=tkinter.Entry(vtncb,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    economico.place(x=100,y=240)

    tkinter.Button(vtncb,text="AGREGAR ASIENTOS",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: añadirBusetatxt2(vip.get(),normal.get(),economico.get())).place(x=155,y=370)
    tkinter.Button(vtncb,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black").place(x=190,y=400)
    vtncb.mainloop()

def añadirBusetatxt2(vip,normal,economico):
    if(vip!="" and normal!="" and economico!=""):    
        Transportes=open("Transportes.txt","a")
        Transportes.write("VIP:"+vip+"\n")
        Transportes.write("Normal:"+normal+"\n")
        Transportes.write("Economico:"+economico+"\n")
        Transportes.write("--------------------------------------" + "\n")
        messagebox.showinfo(title = "Transporte agregado", message = "El transporte se agregó con exito")
    else:
        messagebox.showerror(title = "Error de contenido", message = "Para agregar un Transporte debe llenar los espacios")


#Eliminar Transportes
def eliminarTransporte():
    vtnet=tkinter.Tk()
    vtnet.title("Borrando Transporte")
    vtnet.geometry("500x400")
    vtnet.resizable(False,False)
    vtnet.config(bg="SteelBlue3", cursor="X_cursor")
    tkinter.Label(vtnet, text="۝  ELIMINANDO TRANSPORTE  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnet, text="Este apartado es para eliminar untransporte ya registrada\nPor favor ingrese en el siguiente apartado la placa respectiva del\n transporte" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=25,y=60)
    lblplaca=tkinter.Label(vtnet,text="Placa:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblplaca.place(x=5,y=130)
    placat=tkinter.Entry(vtnet,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    placat.place(x=145,y=130)
    tkinter.Button(vtnet,text="ELIMINAR TRANSPORTE",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Red", command= lambda:eliminarTransportetxt(placat.get())).place(x=145,y=180)
    tkinter.Button(vtnet,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black").place(x=190,y=215)
    tkinter.Label(vtnet, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnet, text="En esta ventana puedes eliminar tu transporte \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnet, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnet.mainloop()

def eliminarTransportetxt(placa):
    Transportes = open("Transportes.txt")
    listaTransportes = Transportes.readlines()
    if(seEncuentra(placa+"\n",listaTransportes)):
        placa=str(placa)
        indice = listaTransportes.index("Placa:"+placa+"\n")
        placa = eliminarInformacion_aux(listaTransportes, indice, 0)
        Transportes.close()
        Transportes = open("Transportes.txt", "w")
        Transportes.write(placa)
        Transportes.close()
        messagebox.showinfo(title = "Eliminar Transporte", message = "El transporte ha sido borrada exitosamente ")

    else:
        messagebox.showerror(title = "Eliminar Transportes", message = "No se encuentra ninguna placa registrada con "+placa)



    
#_________________________________________________________________________________________________________#
"""
Nombre: gestionViaje
Entrada: no posee
Parametros: no posee
Salida: otro menu de opciones
Restricciones: no posee
"""
def gestionViaje():
    vtnV=tkinter.Tk()
    vtnV.geometry("500x400")
    vtnV.title("Gestion de Viaje")
    vtnV.config(bg="SteelBlue3", cursor="hand2")
    vtnV.resizable(False,False )
        
    tkinter.Label(vtnV, text="۝   GESTION DE VIAJE   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnV, text="Precione lo que desea realizar en este menú:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    btnAñadirv=tkinter.Button(vtnV, text="Añadir Viaje    ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=80)
    btnEliminarv=tkinter.Button(vtnV, text="Eliminar Viaje  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=120)
    btnModificarv=tkinter.Button(vtnV, text="Modificar Viaje", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=160)
    btnMostarv=tkinter.Button(vtnV, text="Mostar Viaje  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=200)
    btnAtrasv=tkinter.Button(vtnV, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=vtnAdministracion).place(x=20,y=350)
    tkinter.Label(vtnV, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnV, text="En esta ventana estan todas las opciones de \ngestion de viaje toca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=200,y=370)
    tkinter.Label(vtnV, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnV.mainloop()
#_________________________#
def consultaReservaciones():
    pass

#_________________________#
def estadisticaViaje():
    pass

#######################################



def atras(ventana, funcion):
    ventana.withdraw()
    funcion()


def esconder(ventana):
    ventana.withdraw()    





    


    

ventanaPrincipal()
