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

#---------------------------------------------------------------------------------------
"""
Nombre: validarCedula
Entrada: la cedula a evaluar
Parametro: cedula
Salida: True / False
Restricciones: no posee
"""
def validarCedula(cedula):
    if(cantidadDeindices(cedula)==10):
        return True
    else:
        False

#---------------------------------------------------------------------------------------
"""
Nombre:ValidarCed
Entrada: la cedula pra ver si esta en el archivo de texto
Parametro: cedula, empresas
Salida: True / False
Restricciones: no posee
"""
def validarCed(cedula,empresas):
    empresas1= open("Empresas.txt")
    empresasred= empresas1.readlines()
    if(seEncuentra("Cedula:"+cedula + "\n", empresasred)):
        return True
    else:
        False

#---------------------------------------------------------------------------------------
"""
Nombre: validarPla
Entrada: la placa para ver si esta en el archivo
Parametro: placa, transportes
Salida: True / False
Restricciones: no posee
"""
def validarPla(placa, transportes):
    transportes1=open("Transportes.txt")
    transportesred= transportes1.readlines()
    if(seEncuentra("Placa:"+placa+"\n", transportesred)):
        return True
    else:
        False
         
#----------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------
"""
Nombre: eliminarInformacion
Entrada: la lista a eliminar
Parametro: listaEmpresas,indice,cont
Salida: empresa eliminada
Restricciones: no posee
"""
def eliminarInformacion(listaEmpresas, indice, cont):
    if cont==4:
        return convertirstr(listaEmpresas)
    else:
        listaEmpresas.pop(indice)
        return eliminarInformacion(listaEmpresas, indice, cont + 1)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Para eliminar la informacion en el archivo transporte
#---------------------------------------------------------------------------------------
"""
Nombre: eliminarInformacion_Aux
Entrada: la lista a eliminar
Parametro: listaTransportes,indice,cont
Salida: transporte eliminada
Restricciones: no posee
"""
def eliminarInformacion_aux(listaTransportes, indice, cont):
    if cont==10:
        return convertirstr(listaTransportes)
    else:
        listaTransportes.pop(indice)
        return eliminarInformacion_aux(listaTransportes, indice, cont + 1)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Para eliminar la informacion de el archivo de Viajes
#---------------------------------------------------------------------------------------
"""
Nombre: eliminarInformacion_aux1
Entrada: la lista a eliminar
Parametro: listaViajes,indice,cont
Salida: viaje eliminado
Restricciones: no posee
"""
def eliminarInformacion_aux1(listaViajes,indice,cont):
    if cont==13:
        return convertirstr(listaViajes)
    else:
        listaViajes.pop(indice)
        return eliminarInformacion_aux1(listaViajes, indice, cont + 1)



     
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
    tkinter.Button(vtnPrincipal, text="  2-Menú de usuarios  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command= menuGenaral).place(x=275,y=150)
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
#---------------------------------------------------------------------------------------
"""
Nombre:comprobarClave
Entrada: la clave
Parametro: entrada
Salida: permite o deniega el acceso
Restricciones: no posee
"""   
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
    boton4=tkinter.Button(vtnAdmin, text="      4-Consultar historial de reservaciones", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command= consultaReservaciones).place(x=10,y=190)
    boton5=tkinter.Button(vtnAdmin, text="5-Estadistica de viaje                ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command=estadisticaViaje).place(x=10,y=230)
    tkinter.Label(vtnAdmin, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=270)
    tkinter.Label(vtnAdmin, text="Este apartado es el de la administación\ntoca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=290,y=370)
    tkinter.Label(vtnAdmin, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=280,y=367)
    btnAtras=tkinter.Button(vtnAdmin, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command= lambda:ventanaPrincipal()).place(x=20,y=350)

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
    btnMostare=tkinter.Button(vtnge, text="Mostar Empresas  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command= mostarEmpresas).place(x=10,y=200)
    btnAtrase=tkinter.Button(vtnge, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=lambda:vtnAdministracion()).place(x=20,y=350)
    tkinter.Label(vtnge, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnge, text="En esta ventana estan todas las opciones de \ngestion de empresas toca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=200,y=370)
    tkinter.Label(vtnge, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnge.mainloop()

#------------------------Añadir--------------------------------------------------------------------------------------------------------------
"""
Nombre: añadirEmpresa
Entrada: es un menu
Parametro:no posee
Salida: agrega una empresa
Restricciones: no posee
"""
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
    tkinter.Button(vtnae,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:gestionEmpresa()).place(x=190,y=215)
    tkinter.Label(vtnae, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnae, text="En esta ventana puedes agregar tu empresa \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnae, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnae.mainloop()
#-------------------Añadir al archivo de texto---------------------------------------------------------------------------------
"""
Nombre: añadirEmpresaptxt
Entrada: datos de empresa
Parametro: cedula,nombre,ubicacion
Salida: acepta o niega 
Restricciones: debe llenar los campos, no se puede repetir la cedula
"""
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
"""
Nombre: eliminarEmpresa
Entrada: cedula de la empresa a eliminar
Parametro: no posee
Salida: borra o da error al eliminar la cedula
Restricciones: debe ser existente 
"""
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
    tkinter.Button(vtnee,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black",command=lambda:gestionEmpresa()).place(x=190,y=215)
    tkinter.Label(vtnee, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnee, text="En esta ventana puedes eliminar tu empresa \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnee, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnee.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre:eliminarEmpresaptxt
Entrada: la cedula
Parametro: cedula
Salida: la empresa eliminada exitosamente
Restricciones: la empresa debe estar registrada
"""
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
"""
Nombre: modificarEmpresa
Entrada: cedula de empresa a modificar
Parametro: no posee
Salida: otra ventana para ingresar nuevos datos
Restricciones: la empresa debe ser existente
"""
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
    tkinter.Button(vtnme,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black",command=lambda:gestionEmpresa()).place(x=190,y=215)
    tkinter.Label(vtnme, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnme, text="En esta ventana puedes modificar tu empresa \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnme, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnme.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre: modificarEmpresatxt
Entrada: borra la informacion para modificar
Parametro: cedula
Salida: la ventana para ingresar la nueva informacion
Restricciones:debe llenar los campos 
"""
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
        messagebox.showerror(title = "Modificar Empresa", message = "No se encuentra ninguna cedula registrada con "+cedula)
        

#---------------------------------------------------------------------------------------
#Pidiendo los nuevos datos
"""
Nombre:modificarEmpresa
Entrada: nuevos datos
Parametro: no posee
Salida: Empresa modificada
Restricciones: no posee
"""
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

#---------------------------------------------------------------------------------------
#Añade al archivo
"""
Nombre:añdirEmpresatxtm
Entrada: datos de empresa
Parametro: cedula,nombre,ubicacion
Salida: empresa modificada
Restricciones: debe llenar los campos y la cedula no se debe repetir
"""
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
"""
Nombre: mostrarEmpresas
Entrada: no posee
Parametros: no posee
Salida: muestra las empresas existentes
Restricciones: no posee
"""
def mostarEmpresas():
    vtnmtt= tkinter.Tk()
    Empresa=("Empresas.txt")
    mostrar= open(Empresa)
    lista=mostrar.readlines()
    vtnmtt.title("Mostar Empresas")
    vtnmtt.geometry("500x500")
    vtnmtt.config(bg="SteelBlue3")
    info=Listbox(vtnmtt,font=("Arial",14), bg="SteelBlue4", fg="Black",width=300,height=300)
    info.pack()
    cont=0     
    for infot in lista:
        info.insert(cont,infot)
        cont+=1 
    mostrar.close()
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
    btnModificart=tkinter.Button(vtnT, text="Modificar Transporte", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=lambda:modificarTransporte()).place(x=10,y=160)
    btnMostart=tkinter.Button(vtnT, text="Mostar Transporte  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command= mostrarTransportes).place(x=10,y=200)
    btnAtrast=tkinter.Button(vtnT, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=lambda:vtnAdministracion()).place(x=20,y=350)
    tkinter.Label(vtnT, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnT, text="En esta ventana estan todas las opciones de \ngestion de transporte toca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=200,y=370)
    tkinter.Label(vtnT, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnT.mainloop()
    
#-------------Añadir T------------------------------------------------------------------------------------
#Añade un transporte
"""
Nombre:añadirTranporte
Entrada: no posee
Parametro: no posee
Salida: menu del transporte a elejir
Restricciones:no posee
"""
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
    tkinter.Button(vtnat,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:gestionTransporte()).place(x=200,y=290)
    tkinter.Label(vtnat, text="En esta ventana puedes agregar tu transporte \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnat, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnat.mainloop()
#
#Aladir Transporte Buseta
#---------------------------------------------------------------------------------------
"""
Nombre: añadirBuseta
Entrada: datos de la buseta
Parametro: no posee
Salida:transporte agregado o error de entrada
Restricciones: la placa no puede repetirse.
"""
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
    tkinter.Button(vtnab,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:añadirTransporte()).place(x=190,y=400)
    tkinter.Label(vtnab, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=450)
    tkinter.Label(vtnab, text="En esta ventana puedes agregar tu buseta \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=510)
    tkinter.Label(vtnab, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=507)  
    vtnab.mainloop()

#------------------------------------------------------------------------------------
"""
Nombre:añadirBusetatxt
Entrada: agrega los datos al archivo texto
Parametro: placa,tipo,marca,modelo,año,empresa
Salida: datos agregados o error de contenido
Restricciones: debe llenarse todos los campos
"""
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

#---------------------------------------------------------------------------------------
"""
Nombre:camposBuseta
Entrada: asientos de la buseta
Parametro: no posee
Salida: campos agregados o error de contenido
Restricciones: dee llenar todos los campos
"""
def camposBuseta():
    vtncb=tkinter.Tk()
    vtncb.geometry("700x650")
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

    imagenB=tkinter.PhotoImage(file="Buseta.gif")
    lblImagen=tkinter.Label(vtncb,image=imagenB).place(x=350,y=150)

    tkinter.Button(vtncb,text="     ",bg="green2").place(x=452,y=380)
    tkinter.Button(vtncb,text="     ",bg="green2").place(x=502,y=380)
    tkinter.Button(vtncb,text="     ",bg="green2").place(x=554,y=380)

    
    tkinter.Button(vtncb,text="AGREGAR ASIENTOS",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: añadirBusetatxt2(vip.get(),normal.get(),economico.get())).place(x=10,y=280)
    tkinter.Button(vtncb,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:añadirBuseta()).place(x=10,y=310)
    vtncb.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre:añadirBusetatxt2
Entrada: los añade al archivo de texto
Parametro:vip,normal,economico
Salida: transporte agregado o error de contenido
Restricciones: debe llenar los campos
"""
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

#---------------------------------------------------------------------------------------
"""
Nombre:añadirLimusina
Entrada: no posee
Parametro: no posee
Salida: pide los datos de limusina para agregar archivo
Restricciones: debe llenar los campos
"""
def añadirLimosina():
    vtnal=tkinter.Tk()
    vtnal.title("Agregando Transporte")
    vtnal.geometry("500x550")
    vtnal.resizable(False,False)
    vtnal.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnal, text="۝   AGREGANDO LIMUSIA   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnal, text="Registre la limusina llenando los campos:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)

    lblplacal=tkinter.Label(vtnal,text="Placa:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblplacal.place(x=5,y=80)
    placal=tkinter.Entry(vtnal,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    placal.place(x=145,y=80)

    lbltipol=tkinter.Label(vtnal,text="Tipo:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lbltipol.place(x=5,y=120)
    tipol=tkinter.Entry(vtnal,text="Limusina",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    tipol.place(x=145,y=120)

    lblmarcal=tkinter.Label(vtnal,text="Marca:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblmarcal.place(x=5,y=160)
    marcal=tkinter.Entry(vtnal,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    marcal.place(x=145,y=160)

    lblmodelol=tkinter.Label(vtnal,text="Modelo:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblmodelol.place(x=5,y=200)
    modelol=tkinter.Entry(vtnal,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    modelol.place(x=145,y=200)

    lblañol=tkinter.Label(vtnal,text="Año:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblañol.place(x=5,y=240)
    añol=tkinter.Entry(vtnal,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    añol.place(x=145,y=240)

    lblempresal=tkinter.Label(vtnal,text="Empresa:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblempresal.place(x=5,y=280)
    lblempresall=tkinter.Label(vtnal,text="-Debe ser una empresa existente-",font=("Times New Roman",10), bg="SteelBlue3",fg="Black").place(x=315,y=165)
    empresal=tkinter.Entry(vtnal,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    empresal.place(x=145,y=280)

    tkinter.Button(vtnal,text="AGREGAR LIMUSINA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: añadirLimusinatxt(placal.get(),tipol.get(),marcal.get(),modelol.get(),añol.get(),empresal.get())).place(x=155,y=370)
    tkinter.Button(vtnal,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:añadirTransporte()).place(x=190,y=400)
    tkinter.Label(vtnal, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=450)
    tkinter.Label(vtnal, text="En esta ventana puedes agregar tu limusina \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=510)
    tkinter.Label(vtnal, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=507)  
    vtnal.mainloop()
    
#---------------------------------------------------------------------------------------
"""
Nombre: añadirLimusinatxt
Entrada: datos del transporte
Parametro: placa,tipo,marca,modelo,año,empresa
Salida: transporte agregado en el archivo
Restricciones: debe llenar los campos y no deben haber dos placas iguales
"""

def añadirLimusinatxt(placa,tipo,marca,modelo,año,empresa):
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
            return camposLimusina()

    else:
        messagebox.showerror(title = "Error de contenido", message = "Para agregar un Transporte debe llenar los espacios")
#---------------------------------------------------------------------------------------
"""
Nombre: camposLimusina
Entrada: datso de asientos
Parametro: no posee
Salida: agregado al archivo de transportes
Restricciones: no posee
"""
def camposLimusina():
    vtncl=tkinter.Tk()
    vtncl.geometry("700x650")
    vtncl.title("Gestion de Transporte")
    vtncl.config(bg="SteelBlue3", cursor="hand2")
    vtncl.resizable(False,False )
        
    tkinter.Label(vtncl, text="۝  CANTIDAD DE ASIENTOS  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtncl, text="Estos son los ascientos disponibles\nColor verde = Asientos VIP\nColor amarillo = Asientos Normal\nColor azul = Asiento Economicos\nSegún su categoría elija " , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    lblasiento= tkinter.Label(vtncl, text="Estos son los ascientos disponibles\nColor verde = Asientos VIP\nColor amarillo = Asientos Normal\nColor azul = Asiento Economicos\nSegún su categoría escriba los que desee" , font=("Times New Roman",12),bg="SteelBlue3",fg="blue4").place(x=1,y=40)

    lblvip=tkinter.Label(vtncl,text="VIP:",font=("Angency FB",10), bg="SteelBlue3", fg="Black")
    lblvip.place(x=5,y=160)
    vip=tkinter.Entry(vtncl,text="", font=("Agency FB",10), bg="SkyBlue1", fg="Black")
    vip.place(x=100,y=160)

    lblnormal=tkinter.Label(vtncl,text="Normal:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lblnormal.place(x=5,y=200)
    normal=tkinter.Entry(vtncl,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    normal.place(x=100,y=200)

    lbleconomico=tkinter.Label(vtncl,text="Economico:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lbleconomico.place(x=5,y=240)
    economico=tkinter.Entry(vtncl,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    economico.place(x=100,y=240)

    tkinter.Button(vtncl,text="AGREGAR ASIENTOS",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: añadirLimusinatxt2(vip.get(),normal.get(),economico.get())).place(x=155,y=370)
    tkinter.Button(vtncl,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:añadirBuseta()).place(x=190,y=400)
    vtncl.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre: añadirLimusinatxt2
Entrada: datos de asientos
Parametro: vip,normal,economico
Salida: transporte agregado
Restricciones: debe llenar todos los campos
"""
def añadirLimusinatxt2(vip,normal,economico):
    if(vip!="" and normal!="" and economico!=""):    
        Transportes=open("Transportes.txt","a")
        Transportes.write("VIP:"+vip+"\n")
        Transportes.write("Normal:"+normal+"\n")
        Transportes.write("Economico:"+economico+"\n")
        Transportes.write("--------------------------------------" + "\n")
        messagebox.showinfo(title = "Transporte agregado", message = "El transporte se agregó con exito")
    else:
        messagebox.showerror(title = "Error de contenido", message = "Para agregar un Transporte debe llenar los espacios")
#----------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------  
"""
Nombre: mostrarTransportes
Entrada: no posee
Parametro: no posee
Salida: vista de los datos en la ventana
Restricciones: no posee
"""
def mostrarTransportes():
    vtnmttt= tkinter.Tk()
    Transporte=("Transportes.txt")
    mostrar= open(Transporte)
    lista=mostrar.readlines()
    vtnmttt.title("Mostar Transportes")
    vtnmttt.geometry("500x500")
    vtnmttt.config(bg="SteelBlue3")
    info=Listbox(vtnmttt,font=("Arial",14), bg="SteelBlue4", fg="Black",width=300,height=300)
    info.pack()
    cont=0     
    for infot in lista:
        info.insert(cont,infot)
        cont+=1 
    mostrar.close()

#-----------------------------------------------------------------------------------
#Eliminar Transportes

"""
Nombre:eliminarTransporte
Entrada: placa del transporte a eliminar
Parametro: no posee
Salida: transporte eliminado
Restricciones: no posee
"""
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
    tkinter.Button(vtnet,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:gestionTransporte()).place(x=190,y=215)
    tkinter.Label(vtnet, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnet, text="En esta ventana puedes eliminar tu transporte \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnet, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnet.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre:eliminarTransportetxt
Entrada: la placa 
Parametro: placa
Salida: que el transporte se eliminó
Restricciones: debe estar registrado en el archivo texto
"""
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

#-----------ModificarT------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"""
Nombre: modificarTransporte
Entrada: tipo de vehiculo a modificar
Parametro: no posee
Salida: retorno al menu para ver cual modificar
Restricciones: no posee
"""
def modificarTransporte():
    vtnmt=tkinter.Tk()
    vtnmt.title("Modificando Transporte")
    vtnmt.geometry("500x400")
    vtnmt.resizable(False,False)
    vtnmt.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnmt, text="۝   MODIFICAR TRANSPORTE   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnmt, text="Este apartado es para modificar un transporte registrado al sistema\nSolo son permitidos dos tipos de vehículos\nPor favor elija el tipo de vehiculo que desea modificar" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=25,y=60)
    tkinter.Button(vtnmt,text="MODIFICAR BUSETA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="black", command= lambda:modificarTB()).place(x=300,y=170)
    tkinter.Button(vtnmt,text="MODIFICAR LIMOSINA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="black", command= lambda:modificarTL()).place(x=80,y=170)
    tkinter.Label(vtnmt, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Button(vtnmt,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:gestionTransporte()).place(x=240,y=290)
    tkinter.Label(vtnmt, text="En esta ventana puedes modificar t transporte \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnmt, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnmt.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre:modificarTB
Entrada: debe ingresar la placa del vehiculo
Parametro: no posee
Salida: menu para modificar datos del transporte
Restricciones: no posee
"""
def modificarTB():
    vtnmtt=tkinter.Tk()
    vtnmtt.title("Modificar Empresa")
    vtnmtt.geometry("500x400")
    vtnmtt.resizable(False,False)
    vtnmtt.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnmtt, text="۝  MODIFICAR TRANSPORTE  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnmtt, text="Este apartado es para modificar un transporte ya registrada\nPor favor ingrese en el siguiente apartado la placa respectiva al\n transporte" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=25,y=60)
    lblPlaca=tkinter.Label(vtnmtt,text="Placa:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblPlaca.place(x=5,y=130)
    placatm=tkinter.Entry(vtnmtt,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    placatm.place(x=145,y=130)
    botonm=tkinter.Button(vtnmtt,text="MODIFICAR EMPRESA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda:modificarTransportetxt(placatm.get()))
    botonm.place(x=145,y=180)
    tkinter.Button(vtnmtt,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black",command=lambda:gestionTransporte()).place(x=190,y=215)
    tkinter.Label(vtnmtt, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnmtt, text="En esta ventana puedes modificar tu buseta \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnmtt, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnmtt.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre:modificarTransportetxt
Entrada: la placa para ver si existe y proceder a modificarlo
Parametro: placa
Salida: pide nuevamente los datos a modificar
Restricciones:debe ser una placa registrada el el archivo texto
"""
def modificarTransportetxt(placa):
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
        return modificarTransporte2()
    else:
        messagebox.showerror(title = "Eliminar Transporte", message = "No se encuentra ninguna placa registrada con "+placa)
        
#---------------------------------------------------------------------------------------
"""
Nombre:modificarTransporte2
Entrada:datos
Parametro:no posee
Salida: pasar los nuevos datos al archivo de texto
Restricciones: no posee
"""
def modificarTransporte2():
    vtnmb=tkinter.Tk()
    vtnmb.title("Modifiacando Transporte")
    vtnmb.geometry("500x550")
    vtnmb.resizable(False,False)
    vtnmb.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnmb, text="۝   MODIFICANDO BUSETA   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnmb, text="Modifique la buseta llenando los campos:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)

    lblplacabm=tkinter.Label(vtnmb,text="Nueva Placa:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblplacabm.place(x=5,y=80)
    placabm=tkinter.Entry(vtnmb,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    placabm.place(x=145,y=80)

    lbltipobm=tkinter.Label(vtnmb,text="Nueva Tipo:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lbltipobm.place(x=5,y=120)
    tipobm=tkinter.Entry(vtnmb,text="Buseta",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    tipobm.place(x=145,y=120)

    lblmarcabm=tkinter.Label(vtnmb,text="Nueva Marca:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblmarcabm.place(x=5,y=160)
    marcabm=tkinter.Entry(vtnmb,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    marcabm.place(x=145,y=160)

    lblmodelobm=tkinter.Label(vtnmb,text="Nuevo Modelo:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblmodelobm.place(x=5,y=200)
    modelobm=tkinter.Entry(vtnmb,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    modelobm.place(x=145,y=200)

    lblañobm=tkinter.Label(vtnmb,text="Nuevo Año:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblañobm.place(x=5,y=240)
    añobm=tkinter.Entry(vtnmb,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    añobm.place(x=145,y=240)

    lblempresabm=tkinter.Label(vtnmb,text="Nueva Empresa:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblempresabm.place(x=5,y=280)
    lblempresabbm=tkinter.Label(vtnmb,text="-Debe ser una empresa existente-",font=("Times New Roman",10), bg="SteelBlue3",fg="Black").place(x=315,y=165)
    empresabm=tkinter.Entry(vtnmb,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    empresabm.place(x=145,y=280)

    tkinter.Button(vtnmb,text="MODIFICAR BUSETA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: modificarBusetatxt(placabm.get(),tipobm.get(),marcabm.get(),modelobm.get(),añobm.get(),empresabm.get())).place(x=155,y=370)
    tkinter.Button(vtnmb,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:gestionTransporte()).place(x=190,y=400)
    tkinter.Label(vtnmb, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=450)
    tkinter.Label(vtnmb, text="En esta ventana puedes modificar tu transporte \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=510)
    tkinter.Label(vtnmb, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=507)  
    vtnmb.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre:modificarBusetatxt
Entrada: datos para modificar
Parametro:placa,tipo,marca,modelo,año,empresa
Salida: seguri añadiento datos
Restricciones:debe llenar todos los campos y la placa no debe estar registrada
"""
def modificarBusetatxt(placa,tipo,marca,modelo,año,empresa):
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
            return camposBusetam()

#---------------------------------------------------------------------------------------
"""
Nombre: camposBusetam
Entrada: pedir datos
Parametro: no posee
Salida:datos para ser agregados
Restricciones: no posee
"""
def camposBusetam():
    vtncbm=tkinter.Tk()
    vtncbm.geometry("600x600")
    vtncbm.title("Gestion de Transporte")
    vtncbm.config(bg="SteelBlue3", cursor="hand2")
    vtncbm.resizable(False,False )
        
    tkinter.Label(vtncbm, text="۝  CANTIDAD DE ASIENTOS  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtncbm, text="Estos son los ascientos disponibles\nColor verde = Asientos VIP\nColor amarillo = Asientos Normal\nColor azul = Asiento Economicos\nSegún su categoría elija " , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    lblasientom= tkinter.Label(vtncbm, text="Estos son los ascientos disponibles\nColor verde = Asientos VIP\nColor amarillo = Asientos Normal\nColor azul = Asiento Economicos\nSegún su categoría escriba los que desee" , font=("Times New Roman",12),bg="SteelBlue3",fg="blue4").place(x=1,y=40)

    lblvipm=tkinter.Label(vtncbm,text="VIP:",font=("Angency FB",10), bg="SteelBlue3", fg="Black")
    lblvipm.place(x=5,y=160)
    vipm=tkinter.Entry(vtncbm,text="", font=("Agency FB",10), bg="SkyBlue1", fg="Black")
    vipm.place(x=100,y=160)

    lblnormalm=tkinter.Label(vtncbm,text="Normal:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lblnormalm.place(x=5,y=200)
    normalm=tkinter.Entry(vtncbm,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    normalm.place(x=100,y=200)

    lbleconomicom=tkinter.Label(vtncbm,text="Economico:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lbleconomicom.place(x=5,y=240)
    economicom=tkinter.Entry(vtncbm,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    economicom.place(x=100,y=240)

    tkinter.Button(vtncbm,text="AGREGAR ASIENTOS",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: modificarBusetatxt2(vipm.get(),normalm.get(),economicom.get())).place(x=155,y=370)
    tkinter.Button(vtncbm,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:añadirBuseta()).place(x=190,y=400)
    vtncbm.mainloop()
    
#---------------------------------------------------------------------------------------
"""
Nombre:modificarBusetatxt2
Entrada: datos de ma buseta
Parametro: vip,normal,economico
Salida: transporte agregado
Restricciones:debe llenar los campos 
"""
def modificarBusetatxt2(vip,normal,economico):
    if(vip!="" and normal!="" and economico!=""):    
        Transportes=open("Transportes.txt","a")
        Transportes.write("VIP:"+vip+"\n")
        Transportes.write("Normal:"+normal+"\n")
        Transportes.write("Economico:"+economico+"\n")
        Transportes.write("--------------------------------------" + "\n")
        messagebox.showinfo(title = "Transporte agregado", message = "El transporte se agregó con exito")
    else:
        messagebox.showerror(title = "Error de contenido", message = "Para agregar un Transporte debe llenar los espacios")

#---------------------------------------------------------------------------------------
"""
Nombre:modificarTL
Entrada: debe ingresar la placa
Parametro: no posee
Salida: menu para modificar el transporte
Restricciones: no posee
"""
def modificarTL():
    vtnmttl=tkinter.Tk()
    vtnmttl.title("Modificar Empresa")
    vtnmttl.geometry("500x400")
    vtnmttl.resizable(False,False)
    vtnmttl.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnmttl, text="۝  MODIFICAR TRANSPORTE  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnmttl, text="Este apartado es para modificar un transporte ya registrada\nPor favor ingrese en el siguiente apartado la placa respectiva al\n transporte" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=25,y=60)
    lblPlacal=tkinter.Label(vtnmttl,text="Placa:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblPlacal.place(x=5,y=130)
    placatml=tkinter.Entry(vtnmttl,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    placatml.place(x=145,y=130)
    botonml=tkinter.Button(vtnmttl,text="MODIFICAR LIMUSINA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda:modificarTransportetxtl(placatml.get()))
    botonml.place(x=145,y=180)
    tkinter.Button(vtnmttl,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black",command=lambda:gestionTransporte()).place(x=190,y=215)
    tkinter.Label(vtnmttl, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnmttl, text="En esta ventana puedes modificar tu limusina \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnmttl, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnmttl.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre: modificarTransportetxtl
Entrada: la placa
Parametro: placa
Salida: borra para modificar el transporte
Restricciones: debe ser un transporte existe
"""
def modificarTransportetxtl(placa):
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
        return modificarTransporte2l()
    else:
        messagebox.showerror(title = "Modificar Transporte", message = "No se encuentra ninguna placa registrada con "+placa)
        
#---------------------------------------------------------------------------------------
"""
Nombre: modificarTransporte2l
Entrada: pedir nuevos datos
Parametro: no posee
Salida: pasar datos nuevos
Restricciones: no posee
"""
def modificarTransporte2l():
    vtnmbl=tkinter.Tk()
    vtnmbl.title("Modifiacando Transporte")
    vtnmbl.geometry("500x550")
    vtnmbl.resizable(False,False)
    vtnmbl.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnmbl, text="۝   MODIFICANDO LIMUSINA   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnmbl, text="Modifique la limusina llenando los campos:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)

    lblplacabml=tkinter.Label(vtnmbl,text="Nueva Placa:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblplacabml.place(x=5,y=80)
    placabml=tkinter.Entry(vtnmbl,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    placabml.place(x=145,y=80)

    lbltipobml=tkinter.Label(vtnmbl,text="Nueva Tipo:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lbltipobml.place(x=5,y=120)
    tipobml=tkinter.Entry(vtnmbl,text="Buseta",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    tipobml.place(x=145,y=120)

    lblmarcabml=tkinter.Label(vtnmbl,text="Nueva Marca:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblmarcabml.place(x=5,y=160)
    marcabml=tkinter.Entry(vtnmbl,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    marcabml.place(x=145,y=160)

    lblmodelobml=tkinter.Label(vtnmbl,text="Nuevo Modelo:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblmodelobml.place(x=5,y=200)
    modelobml=tkinter.Entry(vtnmbl,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    modelobml.place(x=145,y=200)

    lblañobml=tkinter.Label(vtnmbl,text="Nuevo Año:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblañobml.place(x=5,y=240)
    añobml=tkinter.Entry(vtnmbl,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    añobml.place(x=145,y=240)

    lblempresabml=tkinter.Label(vtnmbl,text="Nueva Empresa:",font=("Angency FB",14), bg="SteelBlue3",fg="Black")
    lblempresabml.place(x=5,y=280)
    lblempresabbml=tkinter.Label(vtnmbl,text="-Debe ser una empresa existente-",font=("Times New Roman",10), bg="SteelBlue3",fg="Black").place(x=315,y=165)
    empresabml=tkinter.Entry(vtnmbl,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    empresabml.place(x=145,y=280)

    tkinter.Button(vtnmbl,text="MODIFICAR LIMUSINA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: modificarBusetatxtl(placabml.get(),tipobml.get(),marcabml.get(),modelobml.get(),añobml.get(),empresabml.get())).place(x=155,y=370)
    tkinter.Button(vtnmbl,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:gestionTransporte()).place(x=190,y=400)
    tkinter.Label(vtnmbl, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=450)
    tkinter.Label(vtnmbl, text="En esta ventana puedes modificar tu limusina \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=510)
    tkinter.Label(vtnmbl, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=507)  
    vtnmbl.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre:modificarBusetatxtl
Entrada: datos nuevos para que se agreguen al archivo
Parametro:placa,tipo,marca,modelo,año,empresa
Salida: dost agregados, pedir mas datos
Restricciones: llenar los campos de netrada y que la placa no se repita
"""
def modificarBusetatxtl(placa,tipo,marca,modelo,año,empresa):
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
            return camposLimusinam()
#---------------------------------------------------------------------------------------
"""
Nombre: camposLimusinam
Entrada: pedir datos de asientos
Parametro: no posee
Salida: pasar datos para agregarlos al archivo
Restricciones: no posee
"""  
def camposLimusinam():
    vtnclm=tkinter.Tk()
    vtnclm.geometry("600x600")
    vtnclm.title("Gestion de Transporte")
    vtnclm.config(bg="SteelBlue3", cursor="hand2")
    vtnclm.resizable(False,False )
        
    tkinter.Label(vtnclm, text="۝  CANTIDAD DE ASIENTOS  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnclm, text="Estos son los ascientos disponibles\nColor verde = Asientos VIP\nColor amarillo = Asientos Normal\nColor azul = Asiento Economicos\nSegún su categoría elija " , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    lblasientoml= tkinter.Label(vtnclm, text="Estos son los ascientos disponibles\nColor verde = Asientos VIP\nColor amarillo = Asientos Normal\nColor azul = Asiento Economicos\nSegún su categoría escriba los que desee" , font=("Times New Roman",12),bg="SteelBlue3",fg="blue4").place(x=1,y=40)

    lblvipml=tkinter.Label(vtnclm,text="VIP:",font=("Angency FB",10), bg="SteelBlue3", fg="Black")
    lblvipml.place(x=5,y=160)
    vipml=tkinter.Entry(vtnclm,text="", font=("Agency FB",10), bg="SkyBlue1", fg="Black")
    vipml.place(x=100,y=160)

    lblnormalml=tkinter.Label(vtnclm,text="Normal:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lblnormalml.place(x=5,y=200)
    normalml=tkinter.Entry(vtnclm,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    normalml.place(x=100,y=200)

    lbleconomicoml=tkinter.Label(vtnclm,text="Economico:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lbleconomicoml.place(x=5,y=240)
    economicoml=tkinter.Entry(vtnclm,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    economicoml.place(x=100,y=240)

    tkinter.Button(vtnclm,text="AGREGAR ASIENTOS",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: modificarBusetatxt2l(vipml.get(),normalml.get(),economicoml.get())).place(x=30,y=280)
    tkinter.Button(vtnclm,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:añadirLimusina()).place(x=30,y=320)
    vtnclm.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre: modificarBusetatxt2l
Entrada: datos
Parametro: vip,normal,economico
Salida: transporte modificado
Restricciones: debe llenar los campos
"""
def modificarBusetatxt2l(vip,normal,economico):
    if(vip!="" and normal!="" and economico!=""):    
        Transportes=open("Transportes.txt","a")
        Transportes.write("VIP:"+vip+"\n")
        Transportes.write("Normal:"+normal+"\n")
        Transportes.write("Economico:"+economico+"\n")
        Transportes.write("--------------------------------------" + "\n")
        messagebox.showinfo(title = "Transporte agregado", message = "El transporte se modificó con exito")
    else:
        messagebox.showerror(title = "Error de contenido", message = "Para agregar un Transporte debe llenar los espacios")


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
    btnAñadirv=tkinter.Button(vtnV, text="Añadir Viaje    ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=lambda:añadirViaje()).place(x=10,y=80)
    btnEliminarv=tkinter.Button(vtnV, text="Eliminar Viaje  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black",command=lambda:eliminarViaje()).place(x=10,y=120)
    btnModificarv=tkinter.Button(vtnV, text="Modificar Viaje", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=lambda:modificarViaje()).place(x=10,y=160)
    btnMostarv=tkinter.Button(vtnV, text="Mostar Viaje  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=mostrarViajes).place(x=10,y=200)
    btnAtrasv=tkinter.Button(vtnV, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=vtnAdministracion).place(x=20,y=350)
    tkinter.Label(vtnV, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnV, text="En esta ventana estan todas las opciones de \ngestion de viaje toca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=200,y=370)
    tkinter.Label(vtnV, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnV.mainloop()

#--------Añadir  V-----------------------------------------------------------------------------------------------------------------------------
"""
Nombre: añadirViaje
Entrada: pedir datos
Parametro: no posee
Salida: pasar datos para añadirlos
Restricciones: no posee
"""
def añadirViaje():
    vtnav=tkinter.Tk()
    vtnav.title("Agregando Viaje")
    vtnav.geometry("550x550")
    vtnav.resizable(False,False)
    vtnav.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnav, text="۝   AGREGANDO VIAJE   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnav, text="Registre el viaje llenando los campos:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)

    lblnumerov=tkinter.Label(vtnav,text="Numero de Viaje:\n",font=("Angency FB",12), bg="SteelBlue3", fg="Black")
    lblnumerov.place(x=5,y=80)
    numerov=tkinter.Entry(vtnav,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    numerov.place(x=180,y=80)

    lblprovs=tkinter.Label(vtnav,text="Provincia,ciudad salida:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblprovs.place(x=5,y=120)
    provs=tkinter.Entry(vtnav,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    provs.place(x=180,y=120)

    lblfechasv=tkinter.Label(vtnav,text="Fecha de salida:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblfechasv.place(x=5,y=160)
    fechasv=tkinter.Entry(vtnav,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    fechasv.place(x=180,y=160)

    lblhorasv=tkinter.Label(vtnav,text="Hora de salida:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblhorasv.place(x=5,y=200)
    horasv=tkinter.Entry(vtnav,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    horasv.place(x=180,y=200)

    lblprovl=tkinter.Label(vtnav,text="Provincia,ciudad llegada:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblprovl.place(x=5,y=240)
    provl=tkinter.Entry(vtnav,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    provl.place(x=180,y=240)

    lblfechalv=tkinter.Label(vtnav,text="Fecha de llegada:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblfechalv.place(x=5,y=280)
    fechalv=tkinter.Entry(vtnav,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    fechalv.place(x=180,y=280)

    lblhorasv=tkinter.Label(vtnav,text="Hora de llegada:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblhorasv.place(x=5,y=320)
    horasv=tkinter.Entry(vtnav,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    horasv.place(x=180,y=320)

    lblempresav=tkinter.Label(vtnav,text="Empresa:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblempresav.place(x=5,y=360)
    lblempresavv=tkinter.Label(vtnav,text="-Debe ser una empresa existente-",font=("Times New Roman",10), bg="SteelBlue3",fg="Black").place(x=350,y=165)
    empresav=tkinter.Entry(vtnav,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    empresav.place(x=180,y=360)

    lblempresatv=tkinter.Label(vtnav,text="Transporte:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblempresatv.place(x=5,y=400)
    lblempresatv=tkinter.Label(vtnav,text="-Debe ser un transporte existente-",font=("Times New Roman",10), bg="SteelBlue3",fg="Black").place(x=350,y=405)
    empresatv=tkinter.Entry(vtnav,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    empresatv.place(x=180,y=400)

    tkinter.Button(vtnav,text="AGREGAR VIAJE",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: añadirViajetxt(numerov.get(),provs.get(),fechasv.get(),horasv.get(),provl.get(), fechalv.get(),horasv.get(),empresav.get(),empresatv.get())).place(x=185,y=433)
    tkinter.Button(vtnav,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:añadirTransporte()).place(x=5,y=500)
    tkinter.Label(vtnav, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=460)
    tkinter.Label(vtnav, text="En esta ventana puedes agregar tu viaje \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=240,y=510)
    tkinter.Label(vtnav, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=507)  
    vtnav.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre:añadirViajetxt
Entrada: datos añadir al archivo
Parametro: nv,provs,fechas,horas,provl,fechal,horal,empresa,transporte
Salida: vaije agragado al archivo texto
Restricciones: debe llenar los campos de entrada
"""
def añadirViajetxt(nv,provs,fechas,horas,provl,fechal,horal,empresa,transporte):
    if(nv!="" and provs!="" and fechas!="" and horas!="" and provl!="" and fechal!="" and horal!="" and empresa!="" and transporte!=""):        
        Viajes=open("Viajes.txt","a")
        Viajes.write("Numero:"+nv+"\n")
        Viajes.write("Provincia,ciudad salida:"+provs+"\n")
        Viajes.write("Fecha salida:"+fechas+"\n")
        Viajes.write("Hora salida:"+horas+"\n")
        Viajes.write("Provincia,ciudad llegada:"+provl+"\n")
        Viajes.write("Fecha llegada:"+fechal+"\n")
        Viajes.write("Hora llegada:"+horal+"\n")
        Viajes.write("Empresa:"+empresa+"\n")
        Viajes.write("Transporte:"+transporte+"\n")
        #Viajes.write("--------------------------------------" + "\n")
        Viajes.close()
        return añadirVA()
        #messagebox.showinfo(title = "Viaje agregado", message = "El viaje se agregó con exito")
    else:
        messagebox.showerror(title = "Error de contenido", message = "Para agregar un viaje debe llenar los espacios")

def añadirVA():
    vtncva=tkinter.Tk()
    vtncva.geometry("500x500")
    vtncva.title("Gestion de Transporte")
    vtncva.config(bg="SteelBlue3", cursor="hand2")
    vtncva.resizable(False,False )
        
    tkinter.Label(vtncva, text="۝  VALOR DE ASIENTOS  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtncva, text="Estos son los ascientos del viaje por favor \nIngrese el valor de cada de ellos en los campos de entrada. " , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=50)
    lblasientom= tkinter.Label(vtncva, text="Estos son los ascientos disponibles" , font=("Times New Roman",12),bg="SteelBlue3",fg="blue4").place(x=1,y=50)

    lblvipm=tkinter.Label(vtncva,text="VIP:",font=("Angency FB",10), bg="SteelBlue3", fg="Black")
    lblvipm.place(x=5,y=160)
    vipm=tkinter.Entry(vtncva,text="", font=("Agency FB",10), bg="SkyBlue1", fg="Black")
    vipm.place(x=100,y=160)

    lblnormalm=tkinter.Label(vtncva,text="Normal:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lblnormalm.place(x=5,y=200)
    normalm=tkinter.Entry(vtncva,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    normalm.place(x=100,y=200)

    lbleconomicom=tkinter.Label(vtncva,text="Economico:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lbleconomicom.place(x=5,y=240)
    economicom=tkinter.Entry(vtncva,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    economicom.place(x=100,y=240)

    tkinter.Button(vtncva,text="AGREGAR ASIENTOS",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: añadirvatxt(vipm.get(),normalm.get(),economicom.get())).place(x=155,y=370)
    tkinter.Button(vtncva,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:añadirViaje()).place(x=190,y=400)
    vtncva.mainloop()


def añadirvatxt(vip,normal,economico):
    if(vip!="" and normal!="" and economico!=""):    
        Viajes=open("Viajes.txt","a")
        Viajes.write("VIP:"+vip+"\n")
        Viajes.write("Normal:"+normal+"\n")
        Viajes.write("Economico:"+economico+"\n")
        Viajes.write("--------------------------------------" + "\n")
        Viajes.close()
        messagebox.showinfo(title = "Viaje agregado", message = "El viaje se agregó con exito")




    
#-----------------------------------------------------------------------------------------------------------
"""
Nombre:eliminarViaje
Entrada: numero de viaje a eliminar
Parametro:n posee
Salida: transporte eliminado
Restricciones: no posee
"""
def eliminarViaje():
    vtnev=tkinter.Tk()
    vtnev.title("Borrando Transporte")
    vtnev.geometry("500x400")
    vtnev.resizable(False,False)
    vtnev.config(bg="SteelBlue3", cursor="X_cursor")
    tkinter.Label(vtnev, text="۝  ELIMINANDO VIAJE  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnev, text="Este apartado es para eliminar un Viaje ya registrada\nPor favor ingrese en el siguiente apartado el numero de viaje respectiva del\n viaje" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=25,y=60)
    lblnumero=tkinter.Label(vtnev,text="Numero de viaje:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblnumero.place(x=5,y=130)
    numv=tkinter.Entry(vtnev,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    numv.place(x=145,y=130)
    tkinter.Button(vtnev,text="ELIMINAR VIAJE",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Red", command= lambda:eliminarViajetxt(numv.get())).place(x=145,y=180)
    tkinter.Button(vtnev,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:gestionTransporte()).place(x=190,y=215)
    tkinter.Label(vtnev, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnev, text="En esta ventana puedes eliminar tu viaje \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnev, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnev.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre: eliminarViajetxt
Entrada: numero del viaje a borrar
Parametro:numv
Salida: viaje elminado
Restricciones: debe ser un numero de viaje registrado 
"""
def eliminarViajetxt(numv):
    Viajes = open("Viajes.txt")
    listaViajes = Viajes.readlines()
    if(seEncuentra(numv+"\n",listaViajes)):
        vumv=str(numv)
        indice = listaViajes.index("Numero:"+numv+"\n")
        numv = eliminarInformacion_aux1(listaViajes, indice, 0)
        Viajes.close()
        Viajes = open("Viajes.txt", "w")
        Viajes.write(numv)
        Viajes.close()
        messagebox.showinfo(title = "Eliminar Viajes", message = "El Viajes ha sido borrada exitosamente ")

    else:
        messagebox.showerror(title = "Eliminar Viajes", message = "No se encuentra ningun numero registrado con "+numv)

#MODIFICAR VIAJE--------------------------------------------------------------------------------------------------------------------------
"""
Nombre:modificarViaje
Entrada: numero de viaje a modificar
Parametro: no posee
Salida: pedir neuvos datos del viaje
Restricciones: no posee
"""
def modificarViaje():
    vtnmv=tkinter.Tk()
    vtnmv.title("Modificar Viaje")
    vtnmv.geometry("500x400")
    vtnmv.resizable(False,False)
    vtnmv.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnmv, text="۝  MODIFICAR VIAJE  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnmv, text="Este apartado es para modificar un viaje ya registrada\nPor favor ingrese en el siguiente apartado el numero de viaje " , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=25,y=60)
    lblnumv=tkinter.Label(vtnmv,text="Numero de viaje:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black")
    lblnumv.place(x=5,y=130)
    nummv=tkinter.Entry(vtnmv,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    nummv.place(x=145,y=130)
    botonmv=tkinter.Button(vtnmv,text="MODIFICAR VIAJE",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda:modificarViajetxt(nummv.get()))
    botonmv.place(x=145,y=180)
    tkinter.Button(vtnmv,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black",command=lambda:gestionViaje()).place(x=190,y=215)
    tkinter.Label(vtnmv, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnmv, text="En esta ventana puedes modificar tu viaje \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnmv, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    
    vtnmv.mainloop()


#---------------------------------------------------------------------------------------
"""
Nombre: modificarViajetxt
Entrada: numero de viaje a modificar
Parametro: nummv
Salida: modificar datos
Restricciones: el numero de viaje debe estar registrado
"""
def modificarViajetxt(nummv):
    Viajes= open("Viajes.txt")
    listaViajes = Viajes.readlines()
    if(seEncuentra(nummv+"\n",listaViajes)):
        nummv=str(nummv)
        indice = listaViajes.index("Numero:"+nummv+"\n")
        nummv = eliminarInformacion_aux1(listaViajes, indice, 0)
        Viajes.close()
        Viajes = open("Viajes.txt", "w")
        Viajes.write(nummv)
        Viajes.close()
        return modificarViaje1()
    else:
        messagebox.showerror(title = "Modificar Viaje", message = "No se encuentra ningun viaje registrada con "+nummv)
          
#---------------------------------------------------------------------------------------
"""
Nombre:modificarViaje1
Entrada:datos nuevos del viaje
Parametro: no posee
Salida: pasar datos para modificar
Restricciones: no posee
"""
def modificarViaje1():
    vtnmvv=tkinter.Tk()
    vtnmvv.title("Modifiacando Viaje")
    vtnmvv.geometry("550x550")
    vtnmvv.resizable(False,False)
    vtnmvv.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnmvv, text="۝   MODIFICANDO VIAJE  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnmvv, text="Modifique el viaje llenando los campos:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)

    lblnumerom=tkinter.Label(vtnmvv,text="Nuevo numero:",font=("Angency FB",12), bg="SteelBlue3", fg="Black")
    lblnumerom.place(x=5,y=70)
    numerom=tkinter.Entry(vtnmvv,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black")
    numerom.place(x=190,y=70)

    lblprovsm=tkinter.Label(vtnmvv,text="Nueva Provincia,Ciudad salida:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblprovsm.place(x=5,y=110)
    provsm=tkinter.Entry(vtnmvv,text="B",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    provsm.place(x=240,y=110)

    lblfechasm=tkinter.Label(vtnmvv,text="Nueva Fecha Salida:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblfechasm.place(x=5,y=150)
    fechasm=tkinter.Entry(vtnmvv,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    fechasm.place(x=190,y=150)

    lblhorasm=tkinter.Label(vtnmvv,text="Nuevo Hora salida:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblhorasm.place(x=5,y=190)
    horasm=tkinter.Entry(vtnmvv,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    horasm.place(x=190,y=190)

    lblprovlm=tkinter.Label(vtnmvv,text="Nueva Provincia,Ciudad llegada:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblprovlm.place(x=5,y=230)
    provlm=tkinter.Entry(vtnmvv,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    provlm.place(x=240,y=230)

    lblfechalm=tkinter.Label(vtnmvv,text="Nueva Fecha llegada:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblfechalm.place(x=5,y=270)
    fechalm=tkinter.Entry(vtnmvv,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    fechalm.place(x=200,y=270)

    lblhoralm=tkinter.Label(vtnmvv,text="Nueva Hora llegada:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblhoralm.place(x=5,y=310)
    horalm=tkinter.Entry(vtnmvv,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    horalm.place(x=190,y=310)

    lblempresablm=tkinter.Label(vtnmvv,text="Nueva Empresa:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lblempresablm.place(x=5,y=350)
    lblempresabblm=tkinter.Label(vtnmvv,text="-Debe ser una empresa existente-",font=("Times New Roman",10), bg="SteelBlue3",fg="Black").place(x=355,y=350)
    empresalm=tkinter.Entry(vtnmvv,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    empresalm.place(x=190,y=350)

    lbltransportelm=tkinter.Label(vtnmvv,text="Nuevo Transporte:",font=("Angency FB",12), bg="SteelBlue3",fg="Black")
    lbltransportelm.place(x=5,y=390)
    lbltransportebblm=tkinter.Label(vtnmvv,text="-Debe ser un transporte existente-",font=("Times New Roman",10), bg="SteelBlue3",fg="Black").place(x=355,y=390)
    transportelm=tkinter.Entry(vtnmvv,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    transportelm.place(x=190,y=390)

    tkinter.Button(vtnmvv,text="MODIFICAR VIAJE",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: modificarViajetxt1(numerom.get(),provsm.get(),fechasm.get(),horasm.get(),provlm.get(),fechalm.get(),horalm.get(),empresalm.get(),transportelm.get())).place(x=210,y=423)
    tkinter.Button(vtnmvv,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:gestionViaje()).place(x=10,y=485)
    tkinter.Label(vtnmvv, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=450)
    tkinter.Label(vtnmvv, text="En esta ventana puedes modificar tu viaje \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=510)
    tkinter.Label(vtnmvv, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=507)  
    vtnmvv.mainloop()

#---------------------------------------------------------------------------------------
"""
Nombre:modificarViajetxt1
Entrada: datos nuevos
Parametro:numero,provs,fechas,horas,provl,fechal,horal,empresa,transporte
Salida: viaje modificado
Restricciones: debe llenar los campos de entrada de datos
"""
def modificarViajetxt1(numero,provs,fechas,horas,provl,fechal,horal,empresa,transporte):
    if(numero!="" and provs!="" and fechas!="" and horas!="" and provl!="" and fechal!="" and horal!="" and empresa!="" and transporte!=""):        
        Viajes=open("Viajes.txt","a")
        Viajes.write("Numero:"+numero+"\n")
        Viajes.write("Provincia,ciudad salida:"+provs+"\n")
        Viajes.write("Fecha salida:"+fechas+"\n")
        Viajes.write("Hora salida:"+horas+"\n")
        Viajes.write("Provincia,ciudad llegada:"+provl+"\n")
        Viajes.write("Fecha llegada:"+fechal+"\n")
        Viajes.write("Hora llegada:"+horal+"\n")
        Viajes.write("Empresa:"+empresa+"\n")
        Viajes.write("Transporte:"+transporte+"\n")
        #Viajes.write("--------------------------------------" + "\n")
        Viajes.close()
        return modificarav()
        #messagebox.showinfo(title = "Viaje modificado", message = "El viaje se agregó con exito")
    else:
        messagebox.showerror(title = "Error de contenido", message = "Para modificar un viaje debe llenar los espacios")

def modificarav():
    vtncvam=tkinter.Tk()
    vtncvam.geometry("500x500")
    vtncvam.title("Modificando de Viaje")
    vtncvam.config(bg="SteelBlue3", cursor="hand2")
    vtncvam.resizable(False,False )
        
    tkinter.Label(vtncvam, text="۝  VALOR DE ASIENTOS  ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtncvam, text="Estos son los ascientos del viaje por favor \nIngrese el valor de cada de ellos en los campos de entrada. " , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=50)
    lblasientom= tkinter.Label(vtncvam, text="Estos son los ascientos disponibles" , font=("Times New Roman",12),bg="SteelBlue3",fg="blue4").place(x=1,y=50)

    lblvipm=tkinter.Label(vtncvam,text="VIP:",font=("Angency FB",10), bg="SteelBlue3", fg="Black")
    lblvipm.place(x=5,y=160)
    vipm=tkinter.Entry(vtncvam,text="", font=("Agency FB",10), bg="SkyBlue1", fg="Black")
    vipm.place(x=100,y=160)

    lblnormalm=tkinter.Label(vtncvam,text="Normal:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lblnormalm.place(x=5,y=200)
    normalm=tkinter.Entry(vtncvam,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    normalm.place(x=100,y=200)

    lbleconomicom=tkinter.Label(vtncvam,text="Economico:",font=("Angency FB",10), bg="SteelBlue3",fg="Black")
    lbleconomicom.place(x=5,y=240)
    economicom=tkinter.Entry(vtncvam,text="",font=("Agency FB",10), bg="SkyBlue1",fg="Black")
    economicom.place(x=100,y=240)

    tkinter.Button(vtncvam,text="MODIFICAR ASIENTOS",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command= lambda: añadirvatxt(vipm.get(),normalm.get(),economicom.get())).place(x=155,y=370)
    tkinter.Button(vtncvam,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=lambda:añadirViaje()).place(x=190,y=400)
    vtncvam.mainloop()


def añadirvatxt(vip,normal,economico):
    if(vip!="" and normal!="" and economico!=""):    
        Viajes=open("Viajes.txt","a")
        Viajes.write("VIP:"+vip+"\n")
        Viajes.write("Normal:"+normal+"\n")
        Viajes.write("Economico:"+economico+"\n")
        Viajes.write("--------------------------------------" + "\n")
        Viajes.close()
        messagebox.showinfo(title = "Viaje modificado", message = "El viaje se modificó con éxito")

#---------------------------------------------------------------------------------------
"""
Nombre:mostrarViajes
Entrada:no posee
Parametro: no posee
Salida: muestra los viajes
Restricciones: no posee
"""
def mostrarViajes():
    vtnmtttt= tkinter.Tk()
    Viajes=("Viajes.txt")
    mostrar= open(Viajes)
    lista=mostrar.readlines()
    vtnmtttt.title("Mostar Viajes")
    vtnmtttt.geometry("500x500")
    vtnmtttt.config(bg="SteelBlue3")
    info=Listbox(vtnmtttt,font=("Arial",14), bg="SteelBlue4", fg="Black",width=300,height=300)
    info.pack()
    cont=0     
    for infot in lista:
        info.insert(cont,infot)
        cont+=1 
    mostrar.close()

#---------------------------------------------------------------------------------------
"""
Nombre:consultaReservaciones
Entrada: no posee
Parametro: no posee
Salida: la ventana del fltro que elija el usuario
Restricciones:sin restricciones
"""
def consultaReservaciones():
    vtnVr=tkinter.Tk()
    vtnVr.geometry("500x400")
    vtnVr.title("Consulta de Reservaciones")
    vtnVr.config(bg="SteelBlue3", cursor="hand2")
    vtnVr.resizable(False,False )
    def rangoSalida():
       vtnVr.destroy()
       return rangoSalida_Aux()
    def rangoLlegada():
        vtnVr.destroy()
        return rangoLlegada_Aux()
    def rangoFecha():
        vtnVr.destroy()
        return rangoFecha_Aux()
    def rangoSLS():
        vtnVr.destroy()
        return rangoSLS_Aux()
    def rangoSLS2():
        vtnVr.destroy()
        return rangoSLS2_Aux()
        
    tkinter.Label(vtnVr, text="۝ HISTORIAL DE RESERVACIONES ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnVr, text="Filtrar Información por:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    btnrangofs=tkinter.Button(vtnVr, text="Rango de fecha de salida", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=rangoSalida).place(x=10,y=80)
    btnrangofl=tkinter.Button(vtnVr, text="Rango de fecha de llegada", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black",command=rangoLlegada).place(x=10,y=120)
    btnrangofr=tkinter.Button(vtnVr, text="Rango de fecha de reservación", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=rangoFecha).place(x=10,y=160)
    btnrangors=tkinter.Button(vtnVr, text="Rango de salida       ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=rangoSLS).place(x=10,y=200)
    btnrangorl=tkinter.Button(vtnVr, text="Rango de llegada     ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=rangoSLS2).place(x=10,y=240)
    btnAtrasv=tkinter.Button(vtnVr, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=20,y=350)
    tkinter.Label(vtnVr, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=280)
    tkinter.Label(vtnVr, text="En esta ventana estan todas las opciones de \nhistrorial de reservaciones toca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=200,y=370)
    tkinter.Label(vtnVr, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnVr.mainloop()

def rangoSalida_Aux():
    ventanaRango=Tk()
    ventanaRango.geometry("400x300")
    ventanaRango.config(bg="SteelBlue3")
    archivo=open("Reservaciones.txt")
    reservaciones=archivo.readlines()
    etiqueta=tkinter.Label(ventanaRango,text="Ingrese el rango de fecha de salida a buscar",font=("Times New Roman",14),bg="SteelBlue3",fg="Black")
    etiqueta.pack()
    entry=tkinter.Entry(ventanaRango, text="", font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    entry.pack()
    def BuscarIReser():
        buscar=entry.get()
        Buscar_historial(reservaciones,buscar,9,9)
        archivo.close()
        ventanaRango.destroy()
    boton=tkinter.Button(ventanaRango, text="Filtrar",font=("Times New Roman",14), bg="DeepSkyBlue4", fg="Black",command=BuscarIReser)
    boton.pack()
#--------------------
def Buscar_historial(reservaciones,buscar,indice,indice2):
    ventanaBuscar=Tk()
    ventanaBuscar.geometry("600x400")
    ventanaBuscar.config(bg="SteelBlue3",cursor="hand2")
    resultado=[]
    while indice < len(reservaciones):
        if buscar in reservaciones[indice]:
            contador=0
            indice3=indice-indice2
            while contador!=20:
                resultado+=[reservaciones[indice3]]
                indice3+=1
                contador+=1
            indice+=20
        else:
            indice+=20  
    mostrar=Listbox(ventanaBuscar, font=("Times New Roman",14),bg="SteelBlue3",fg="Black",width=50,height=10)
    mostrar.pack()
    cont=0
    for datos in resultado:
        mostrar.insert(cont,datos)
        cont+=1
    tkinter.Label(ventanaBuscar,text=f"Estos son las reservaciones encontrados según el dato que ingreso. ",font=("Times New Roman",14),bg="SteelBlue3", fg="Black").pack()
    def salirR():
        mensaje=messagebox.askyesno("Salir", "¿Volver al Menu del Histroial de reservaciones?")
        if(mensaje):
            ventanaBuscar.destroy()
            return consultaReservaciones()
    
    tkinter.Button(ventanaBuscar,text="Salir",font=("Times New Roman",14), bg="DeepSkyBlue4",fg="Black",command=salirR).pack()

#-----------------------
def rangoLlegada_Aux():
    ventanaRLL=Tk()
    ventanaRLL.geometry("400x300")
    ventanaRLL.config(bg="SteelBlue3",cursor="hand2")
    archivo=open("Reservaciones.txt")
    reservaciones=archivo.readlines()
    etiqueta=tkinter.Label(ventanaRLL,text="Digite el rango de la fecha de llegada a filtar:",font=("Times New Roman",14),bg="SteelBlue3",fg="Black")
    etiqueta.pack()
    entry=tkinter.Entry(ventanaRLL, text="", font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    entry.pack()
    def BuscarIReser1():
        buscar=entry.get()
        Buscar_historial(reservaciones,buscar,13,13)
        archivo.close()
    boton=tkinter.Button(ventanaRLL, text="Filtrar", font=("Times New Roman",14), bg="DeepSkyBlue4", fg="Black",command=BuscarIReser1)
    boton.pack()
#--------------------------
def rangoFecha_Aux():
    ventanaRLL=Tk()
    ventanaRLL.geometry("400x300")
    ventanaRLL.config(bg="SteelBlue3")
    ventanaRLL.title("Rango de salida")
    archivo=open("Reservaciones.txt")
    reservaciones=archivo.readlines()
    etiqueta=tkinter.Label(ventanaRLL,text="Digite el rango de la fecha de reserva  a filtar:", font=("Times New Roman",14),bg="SteelBlue3",fg="Black")
    etiqueta.pack()
    entry=tkinter.Entry(ventanaRLL, text="", font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    entry.pack()
    def BuscarIReser2():
        buscar=entry.get()
        Buscar_historial(reservaciones,buscar,3,3)
        archivo.close()
    boton=tkinter.Button(ventanaRLL, text="Filtrar", font=("Times New Roman",14), bg="DeepSkyBlue4", fg="Black",command=BuscarIReser2)
    boton.pack()
#--------------------
def rangoSLS_Aux():
    ventanaRLL=Tk()
    ventanaRLL.geometry("400x300")
    ventanaRLL.config(bg="SteelBlue3")
    ventanaRLL.title("Rangos")
    archivo=open("Reservaciones.txt")
    reservaciones=archivo.readlines()
    etiqueta=tkinter.Label(ventanaRLL,text="Ingrese el lugar de salida a filtrar:",font=("Times New Roman",14),bg="SteelBlue3",fg="Black")
    etiqueta.pack()
    entry=tkinter.Entry(ventanaRLL, text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black" )
    entry.pack()
    def BuscarIReser3():
        buscar=entry.get()
        Buscar_historial(reservaciones,buscar,7,7)
        archivo.close()
    boton=tkinter.Button(ventanaRLL, text="Filtrar",font=("Times New Roman",14), bg="DeepSkyBlue4", fg="Black",command=BuscarIReser3)
    boton.pack()
#----------------------
def Buscar_historial1(reservaciones,buscar,indice,indice2):
    ventanaBuscar=Tk()
    ventanaBuscar.geometry("600x400")
    ventanaBuscar.config(bg="SteelBlue3")
    resultado=[]
    while indice < len(reservaciones):
        if buscar in reservaciones[indice] or buscar in reservaciones[indice+1] :
            contador=0
            indice3=indice-indice2
            while contador!=20:
                resultado+=[reservaciones[indice3]]
                indice3+=1
                contador+=1
            indice+=20
        else:
            indice+=20
    mostrar=Listbox(ventanaBuscar, font=("Times New Roman",14), bg="white", fg="Black")
    mostrar.pack()
    cont=0
    for datos in resultado:
        mostrar.insert(cont,datos)
        cont+=1
    tkinter.Label(ventanaBuscar,text=f"Estos son las reservaciones encontrados según el dato que ingreso. ",font=("Times New Roman",14),bg="white", fg="Black").pack()
    def salirR():
        mensaje=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
        if(mensaje):
            ventanaBuscar.destroy()
            return vtnVr()
    tkinter.Button(ventanaBuscar,text="continuar",font=("Times New Roman",14), bg="white", fg="Black",command=salirR).pack()
#--------------------------------
def rangoSLS2_Aux():
    ventanaRLL=Tk()
    ventanaRLL.geometry("400x300")
    ventanaRLL.config(bg="SteelBlue3")
    ventanaRLL.title("Rango de llegada")
    archivo=open("Reservaciones.txt")
    reservaciones=archivo.readlines()
    etiqueta=tkinter.Label(ventanaRLL,text="Ingrese el lugar de llegada a filtrar:",font=("Times New Roman",14),bg="SteelBlue3",fg="Black")
    etiqueta.pack()
    entry=tkinter.Entry(ventanaRLL, text="", font=("Agency FB",14), bg="SkyBlue1",fg="Black")
    entry.pack()
    def BuscarIReser4():
        buscar=entry.get()
        Buscar_historial(reservaciones,buscar,11,11)
        archivo.close()
    boton=tkinter.Button(ventanaRLL, text="Filtrar", font=("Times New Roman",14), bg="DeepSkyBlue4", fg="Black",command=BuscarIReser4)
    boton.pack()

    
#---------------------------------------------------------------------------------------
"""
Nombre: estadisticaViaje
Entrada: debe ingresar el numero de viaje
Parametro: no posee
Salida: menu estadisticas de viaje
Restricciones: no posee
"""
def estadisticaViaje():
    vtnev=tkinter.Tk()
    vtnev.geometry("500x500")
    vtnev.title("Estadisticas de Viaje")
    vtnev.config(bg="SteelBlue3", cursor="hand2")
    archivo=open("viajes.txt")
    viajes=archivo.readlines()
    mostrar=tkinter.Listbox(vtnev,font=("Times New Roman",15),bg="SteelBlue4",fg="black",width=50,height=10)
    mostrar.pack()
    contador=0
    for indices in viajes:
        mostrar.insert(contador,indices)
        contador+=1
    etiqueta=tkinter.Label(vtnev,text="Escriba un numero de viaje disponible:",font=("Times New Roman",15),bg="SteelBlue3",fg="black")
    etiqueta.pack()
    entry=tkinter.Entry(vtnev,text="",font=("Times New Roman",15),bg="SteelBlue1",fg="black")
    entry.pack()
    def estadisticaViaje_aux():
        numero=entry.get()
        informacion=[]
        if("Numero:"+numero+"\n") in viajes:
            mostrar.destroy()
            etiqueta.destroy()
            entry.destroy()
            boton.destroy()
            indice=viajes.index("Numero:"+numero+"\n")
            informacion+=[viajes[indice]]
            informacion+=[viajes[indice+7]]
            informacion+=[viajes[indice+8]]
            informacion+=[viajes[indice+1]]
            informacion+=[viajes[indice+2]]
            informacion+=[viajes[indice+3]]
            informacion+=[viajes[indice+4]]
            informacion+=[viajes[indice+5]]
            informacion+=[viajes[indice+6]]
            archivo2=open("Reservaciones.txt")
            reservaciones=archivo2.readlines()
            if(viajes[indice])in reservaciones:
                archivo3=open("Transportes.txt")
                Transporte=archivo3.readlines()
                indice3=Transporte.index("Placa:"+viajes[indice+8][11:])
                indice2=reservaciones.index(viajes[indice])
                informacion+=["Asiento VIP reservado:"+reservaciones[indice2+13]]
                disponibleVip=Transporte[indice3+6][4:-1]
                informacion+=["Asiento VIP disponible:"+str(int(disponibleVip)-int(reservaciones[indice2+13]))]
                informacion+=["Asiento Normal reservado:"+reservaciones[indice2+14]]
                disponibleNormal=Transporte[indice3+7][7:-1]
                informacion+=["Asiento Normal disponible:"+str(int(disponibleNormal)-int(reservaciones[indice2+14]))]
                informacion+=["Asiento Economico reservado:"+reservaciones[indice2+15]]
                disponibleEconomico=Transporte[indice3+8][10:-1]
                informacion+=["Asiento Economico  disponible:"+str(int(disponibleEconomico)-int(reservaciones[indice2+15]))]
                informacion+=["monto recaudado por el viaje:"+reservaciones[indice2+16]]
                contador=0
                mostrar1=tkinter.Listbox(vtnev,font=("Times New Roman",15),bg="SteelBlue4",fg="black",width=50,height=10)
                mostrar1.pack()
                etiqueta1=tkinter.Label(vtnev,text="Esta son las estadisticas del viaje seleccionado",font=("Times New Roman",15),bg="SteelBlue3",fg="black")
                etiqueta1.pack()
                for indices in informacion:
                    mostrar1.insert(contador,f"{indices}")
                    contador+=1
                def salir4():
                    vtnev.destroy()
                tkinter.Button(vtnev,text="Salir",font=("Times New Roman",15),bg="SteelBlue4",fg="black",command=salir4)
            else:
                archivo3=open("Transportes.txt")
                Transporte=archivo3.readlines()
                indice3=Transporte.index("Placa:"+viajes[indice+8][11:])
                informacion+=["Asiento VIP reservado:"+"0"]
                disponibleVip=Transporte[indice3+6][4:-1]
                informacion+=["Asiento VIP disponible:"+str(int(disponibleVip))]
                informacion+=["Asiento Normal reservado:"+"0"]
                disponibleNormal=Transporte[indice3+7][7:-1]
                informacion+=["Asiento Normal disponible:"+str(int(disponibleNormal))]
                informacion+=["Asiento Economico reservado:"+"0"]
                disponibleEconomico=Transporte[indice3+8][10:-1]
                informacion+=["Asiento Economico  disponible:"+str(int(disponibleEconomico))]
                informacion+=["monto recaudado por el viaje:"+"0"]
                contador=0
                mostrar1=tkinter.Listbox(vtnev,font=("Times New Roman",15),bg="SteelBlue4",fg="black")
                mostrar1.pack()
                etiqueta1=tkinter.Label(vtnev,text="Esta son las estadisticas del viaje seleccionado",font=("Times New Roman",15),bg="SteelBlue4",fg="black")
                etiqueta1.pack()
                for indices in informacion:
                    mostrar1.insert(contador,f"{indices}")
                    contador+=1
                def salir4():
                    vtnev.destroy()
                tkinter.Button(vtnev,text="Salir",font=("Times New Roman",15),bg="SteelBlue4",fg="black",command=salir4).pack()          
    boton=tkinter.Button(vtnev,text="Continuar",font=("Times New Roman",15),bg="SteelBlue4",fg="black",command=estadisticaViaje_aux)
    boton.pack()
    
    btnAtrasv=tkinter.Button(vtnev, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=vtnAdministracion).place(x=20,y=450)
    vtnev.mainloop()

#--------------------------------------------------------------------------------------------
"""
Nombre: menuGenaral
Entrada: no posee
Parametros: no posee
Salida: otro menú de opciones
Restricciones: no posee
"""
def menuGenaral():
    vtngen =tkinter.Tk()
    vtngen.geometry("500x400")
    vtngen.title("Menú de General")
    vtngen.config(bg="SteelBlue3", cursor="hand2")
    vtngen.resizable(False,False )
        
    tkinter.Label(vtngen, text="۝   MENÚ GENERAL   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtngen, text="Elija una de las siguentes opciones:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    #Botón
    boton6=tkinter.Button(vtngen, text="      1-Consulta de viajes           ", font=("Arial",12),bg="DeepSkyBlue4",fg="black", command= consultaViajesF).place(x=10,y=80)
    boton7=tkinter.Button(vtngen, text="      2- Reservacion de viaje        ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command= gestionTransporte).place(x=10,y=130)
    boton8=tkinter.Button(vtngen, text="      3-Cancelacion de reservación                  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command= gestionViaje).place(x=10,y=180)
    tkinter.Label(vtngen, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=270)
    tkinter.Label(vtngen, text="Este apartado es el de las opciones generales\ntoca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=290,y=370)
    tkinter.Label(vtngen, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=280,y=367)
    btnAtras=tkinter.Button(vtngen, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command= lambda:ventanaPrincipal()).place(x=20,y=350)

    vtngen.mainloop()

#-------------------------------------------------------------------------------------------------------------
"""
Nombre: consultaViajesF
Entrada: no posee
Parametros: no posee
Salida: otro menú de opciones
Restricciones: no posee
"""
def consultaViajesF():
    vtnVF=tkinter.Tk()
    vtnVF.geometry("500x400")
    vtnVF.title("Consulta de Viaje")
    vtnVF.config(bg="SteelBlue3", cursor="hand2")
    vtnVF.resizable(False,False )
        
    tkinter.Label(vtnVF, text="۝ CONSULTAR VIAJES ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnVF, text="Filtrar Información por:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=40)
    btnrangofs=tkinter.Button(vtnVF, text="Empresa", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=lambda:rangoSalida()).place(x=10,y=80)
    btnrangofl=tkinter.Button(vtnVF, text="Lugar de salida", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black",command=lambda:rangoLlegada()).place(x=10,y=120)
    btnrangofr=tkinter.Button(vtnVF, text="Lugar de llegada", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=lambda:rangoFecha()).place(x=10,y=160)
    btnrangors=tkinter.Button(vtnVF, text="Rango por fecha de salida       ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=rangoSLS()).place(x=10,y=200)
    btnrangorl=tkinter.Button(vtnVF, text="Rango por fecha de llegada      ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=rangoSLS()).place(x=10,y=240)
    btnAtrasv=tkinter.Button(vtnVF, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=vtnAdministracion).place(x=20,y=350)
    tkinter.Label(vtnVF, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=280)
    tkinter.Label(vtnVF, text="En esta ventana estan todas las opciones consulta viajes \ntoca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=200,y=370)
    tkinter.Label(vtnVF, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnVF.mainloop()

#######################################
"""
Nombre:atras
Entrada: no posee
Parametro: ventana, funcion
Salida: vulve a la ventana anterior
Restricciones: no posee
"""
def atras(ventana, funcion):
    ventana.withdraw()
    funcion()
#-----------------------------------------
"""
Nombre:esconder
Entrada: no posee
Parametro: ventana
Salida: esconde la ventana para pasar a otra
Restricciones: no posee
"""
def esconder(ventana):
    ventana.withdraw()    

###################
ventanaPrincipal()#
###################
