import tkinter
from tkinter  import *

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


#----------------------------------------------------------
#Para ver si se encuentra en un archivo
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
        
#-------------------------------------------------------------------------------------------------
#Esta funcion elimina la informacion del archivo Empresas
"""
Nombre: eliminarInformacion
Entrada: una lista a eliminar
Parametros: listaEmpresas, indice, cont
Salida: sin salida, solo elimina la informacion
Restricciones: sin restricciones
"""
def eliminarInformacion(listaEmpresas, indice, cont):
    if cont==4:
        return convertirstr(listaEmpresas)
    else:
        print(listaEmpresas[indice].strip())
        listaEmpresas.pop(indice)
        return eliminarInformacion(listaEmpresas, indice, cont + 1)
    
#-----------------------------------------------------
#Para eliminar la informacion en el archivo transporte
def eliminarInformacion_aux(listaTransportes, indice, cont):
    if cont==9:
        return convertirstr(listaTransportes)
    else:
        print(listaTransportes[indice].strip())
        listaTransportes.pop(indice)
        return eliminarInformacion_aux(listaTransportes, indice, cont + 1)

#-----------------------------------------------------
#Para eliminar la información de los viajes
def eliminarInformacion_aux1(listaViajes,indice,cont):
    if cont==13:
        return convertirstr(listaViajes)
    else:
        print(listaViajes[indice].strip())
        listaViajes.pop(indice)
        return eliminarInformacion_aux1(listaViajes, indice, cont + 1)

#--------------------------------------------------------------------------------
#Imprime en pantalla las empresas que se encuntran en el archivo Empresas
"""
Nombre: mostrarEmpresas
Entrada: datos a mostrar
Parameteros: listaEmpresas, indice, cont
Salida: muestra en pantalla los datos
Restricciones: sin restricciones
"""
def mostrarEmpresas(listaEmpresas, indice, cont):
    if cont > 2:
        print("-------------------------------------")
    else:
        if(cont == 0):
            print(listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)
        elif(cont == 1):
            print(listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)
        else:
            print(listaEmpresas[indice][0:-1])
            return mostrarEmpresas(listaEmpresas, indice + 1, cont + 1)

#---------------------------------------------------------------------------------
#Convierte datos de la lista en string
"""
Nombre: convertir_a_string
Entrada: una lista
Parametro: lista
Salida: datos string
Restricciones: sin restricciones
"""
def convertir_a_string(lista):
    if isinstance(lista, list):
        string = ""
        for indice in lista:
            string += indice
        return string
    else:
        print("Error: no se puede convertir a String, porque, el tipo de dato de entrada, no es una lista")


#-----------------------------------------------------------------------------------------------
#Con esta funcion podemos asegurarnos que la cedula ingresada contenga la cantidad requerida de numeros ingresados
"""
Nombre: cedValidar
Entrada: cedula a validar
Parametros: cedula,Empresas
Salida: True o False
Restricciones: la cedula debe contener 10 digitos
"""
def cedValidar( cedula,Empresas):
    if (seEncuentra(cedula + "\n", Empresas)):
        return False
    else:
        if(cantidadDeindices(cedula) == 10 and isinstance(int(cedula), int)):
            return True
        else:
            print("\nERROR: La cédula no contiene 10 dígitos exactos, vuelva intentar")
            return gestionEmpresas()

#---------------------------------------------------
#Con esta funcion podemos asegurarnos que la placa ingresada contenga la cantidad requerida de numeros ingresados
def matValidar(placa,Transportes):
    if(seEncuentra(placa + "\n", Transportes)):
        return False
    else:
        if(cantidadDeindices(placa) == 6 and isinstance(int(placa), int)):
            return  True
        else:
            print("\nERROR: La placa no contiene 6 dígitos exactos, vuelva intentar")
            return gestionTransporteEmpresa()
#--------------------------------------------------------------------------------------------------------
#Validar que el usuario indique algo str
"""
*******************************************
*COMPROBAR SI LA OPCIÓN DIGITADA ES VÁLIDA*
*******************************************
Nombre: validar
Entradas: la opcion
Parametros: opcion
Salidas: True si la entráda es un String. False si la entrada no es un String. 
Restricciones: La entrada debe ser un String.
"""
def validar(opcion):
    if (isinstance(opcion, str) and opcion != ""):
        return True
    else:
        return False
#-------------------------------------------------------------
#Parte del manejo de archivos, para obtener la lista en este caso de la empresa
"""
Nombre: obtenerListaContactos
Entradas: no posee
Salidas: una lista que contiene todas las líneas del archivo Empresas.txt
Restricciones: no posee
"""
def obtenerListaEmpresas():
    Empresas = open("Empresas.txt")
    listaEmpresas = Empresas.readlines()
    Empresas.close()
    return listaEmpresas

#-------------------------------------------------------------
#Esta funcion es para obtener a lista del transporte, en este caso del archivo Transportes.txt
def obtenerListaTransportes():
    Transportes = open("Transportes.txt")
    listaTransportes = Transportes.readlines()
    Transportes.close()
    return listaTransportes
#-------------------------------------------------------------





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
    boton1=tkinter.Button(vtnPrincipal, text="1-Menú administrativo", font=("Arial",12),bg="DeepSkyBlue4",fg="black", command= vtnAcceso).place(x=60,y=150)
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

def vtnAcceso():
    vtnAcceso =tkinter.Tk()
    vtnAcceso.geometry("500x400")
    vtnAcceso.title("Ventana de Acceso")
    vtnAcceso.config(bg="SteelBlue3", cursor="hand2")
    vtnAcceso.resizable(False,False )
    
    tkinter.Label(vtnAcceso, text="۝   MENÚ DE ACCESO   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    tkinter.Label(vtnAcceso, text="¡Debe ingresar la contraseña para continuar!" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=75,y=35)
    tkinter.Label(vtnAcceso, text="Escriba la contraseña para ingresar a la Administración:" , font=("Times New Roman",13),bg="SteelBlue3",fg="blue4").place(x=1,y=90)
    entrada=tkinter.Entry(vtnAcceso, text="", font=("Arial",14), bg="white", fg="Black").place(x=140, y=140)
    button=tkinter.Button(vtnAcceso,text="  Continuar  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="black", command =vtnAdministracion).place(x=210,y=180)
    tkinter.Label(vtnAcceso, text="Para entrar a la administracion es necesario\nla contraseña de acceso." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=290,y=370)
    tkinter.Label(vtnAcceso, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=280,y=367)
    vtnAcceso.mainloop()
    
def comprobarClave():
    contraseña=entrada.get()
    contraseña=open("Clave.txt")
    Clave1=contraseña.readlines()
    if(contraseña in Clave1):
        contraseña.close()
        return vtnAdministracion()
    else:
        print("CLAVE INCORRECTA, POR FAVOR INTENTE DE NUEVO")
        return vtnAcceso()
        


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
    btnAtras=tkinter.Button(vtnAdmin, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command= ventanaPrincipal).place(x=20,y=350)

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
    btnEliminare=tkinter.Button(vtnge, text="Eliminar Empresa  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=120)
    btnModificare=tkinter.Button(vtnge, text="Modificar Empresa", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=160)
    btnMostare=tkinter.Button(vtnge, text="Mostar Empresas  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=200)
    btnAtrase=tkinter.Button(vtnge, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=vtnAdministracion).place(x=20,y=350)
    tkinter.Label(vtnge, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnge, text="En esta ventana estan todas las opciones de \ngestion de empresas toca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=200,y=370)
    tkinter.Label(vtnge, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnge.mainloop()

#Añadir

def añadirEmpresa():
    vtnae=tkinter.Tk()
    vtnae.title("Agregando Empresa")
    vtnae.geometry("500x400")
    vtnae.resizable(False,False)
    vtnae.config(bg="SteelBlue3", cursor="plus")
    tkinter.Label(vtnae, text="۝   AGREGANDO EMPRESA   ۝", font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black").pack(fill=tkinter.X)
    lblCedula=tkinter.Label(vtnae,text="Cédula Juridica:\n",font=("Angency FB",14), bg="SteelBlue3", fg="Black").place(x=5,y=40)
    cedulae=tkinter.Entry(vtnae,text="", font=("Agency FB",14), bg="SkyBlue1", fg="Black").place(x=145,y=40)
    lblNombre=tkinter.Label(vtnae,text="Nombre:",font=("Angency FB",14), bg="SteelBlue3",fg="Black").place(x=5,y=80)
    nombree=tkinter.Entry(vtnae,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black").place(x=145,y=85)
    lblubicacion=tkinter.Label(vtnae,text="Ubicación:",font=("Angency FB",14), bg="SteelBlue3",fg="Black").place(x=5,y=124)
    ubicacione=tkinter.Entry(vtnae,text="",font=("Agency FB",14), bg="SkyBlue1",fg="Black").place(x=145,y=129)
    tkinter.Button(vtnae,text="AGREGAR EMPRESA",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black", command=añadirEmpresaptxt).place(x=145,y=180)
    tkinter.Button(vtnae,text="SALIR",font=("Angency FB",10),bg="DeepSkyBlue4",fg="Black").place(x=190,y=215)
    tkinter.Label(vtnae, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnae, text="En esta ventana puedes agregar tu empresa \ndebes llenar los campos de entrada con lo solicitado." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=225,y=370)
    tkinter.Label(vtnae, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnae.mainloop()

def añadirEmpresaptxt():
    cedulae=cedulae.get()
    nombree=nombree.get()
    ubicacione=ubicacione.get
    Empresas=open("Empresas.txt","a")
    Empresas.write("Cedula:"+cedula + "\n")
    Empresas.write("Nombre:"+nombre + "\n")
    Empresas.write("ubicacion:"+ubicacion + "\n")
    Empresas.write("--------------------------------------" + "\n")
    Empresas.close()

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
    btnAñadirt=tkinter.Button(vtnT, text="Añadir Transporte     ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=80)
    btnEliminart=tkinter.Button(vtnT, text="Eliminar Transporte  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=120)
    btnModificart=tkinter.Button(vtnT, text="Modificar Transporte", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=160)
    btnMostart=tkinter.Button(vtnT, text="Mostar Transporte  ", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black").place(x=10,y=200)
    btnAtrast=tkinter.Button(vtnT, text="Atrás", fon=("Arial",12), bg="DeepSkyBlue4",fg="Black", command=vtnAdministracion).place(x=20,y=350)
    tkinter.Label(vtnT, text=" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _" , font=("Arial Black",12),bg="SteelBlue3",fg="Black").place(x=5,y=250)
    tkinter.Label(vtnT, text="En esta ventana estan todas las opciones de \ngestion de transporte toca un boton deacuerdo a lo que desea hacer." , font=("Arial",7),bg="SteelBlue3",fg="Black").place(x=200,y=370)
    tkinter.Label(vtnT, text="?" , font=("Arial Black",8),bg="SteelBlue3",fg="Black").place(x=230,y=367)
    vtnT.mainloop()
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


    

ventanaPrincipal()
