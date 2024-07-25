#librerias
import time
import os 
#funciones
from controller.bd_conect import conectar_db,desconectar_db #importamos la funcion que conecta la BD
from model.verificacion import *
from model.insert import *
from model.delete import *
from model.visualizar import *
from model.user import *
from model.delete import *
from model.consulta import *


os.system("cls") #limpiamos la consola

conexion = conectar_db() # conectar base de datos

users = autenticacion(conexion) # reconocer el usuario

#comprobamos usuario    

print("\nINGRESA TUS DATOS\n")
nombre = input("usuario: ")
clave = input("clave: ")
rol = verificacion(users,nombre,clave)

#Empezamos las opciones

reset = True
while reset == True:
    
    if rol == "admin" or rol == "cliente" or rol == "empleado":
        
        if rol == "admin": #admin

            os.system("cls")
            print("\n Menu - Admin \n")
            print("1- Insertar")
            print("2- Eliminar")
            print("3- Visualizar ")
            print("4- Consultar\n")
            decision = int(input("decision: "))
            os.system("cls")

            if decision == 1:
                os.system("cls")
                insert(conexion)
            if decision == 2: 
                MENU_delete(conexion)

            if decision == 3:
                os.system("cls")
                visualizar(conexion)    
            
            if decision == 4:
                os.system("cls")
                MENU_consultas(conexion)     

        if rol == "cliente": #cliente
                os.system("cls")
                print("\n Menu Cliente \n")
                print("1- Visualizar\n")
                decision = int(input("decision: "))

                if decision == 1:
                    os.system("cls")
                    visualizar(conexion)

        if rol == "empleado":
            os.system("cls")
            print("\n Menu - Empleado \n")
            print("1- Insertar")
            print("2- Visualizar ")
            
            decision = int(input("decision: "))
            os.system("cls")

            if decision == 1:
                os.system("cls")
                insert(conexion)

            if decision == 2:
                os.system("cls")
                visualizar(conexion)    
             
    else:
        if rol == -1:
         print("[ERROR] - Usuario o Clave incorrecta.")
         print("Por favor verificar los datos ")
         time.sleep(2)
         print("\nINGRESA TUS DATOS\n")
         nombre = input("usuario: ")
         clave = input("clave: ")
         rol = verificacion(users,nombre,clave)

    #repetimos bucle

    decision = ""
    while decision != 's' and decision != 'n': 
        decision = input("\nREINICIAR EL PROGRAMA (s/n): ")

    if decision == 'n':
        reset = False

desconectar_db(conexion) # desconectar base de datos 