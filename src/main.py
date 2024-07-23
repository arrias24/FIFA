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
    
    if rol == "admin" or rol == "user":
        
        if rol == "admin":

            os.system("cls")
            print("\nMENU - ADMIN \n")
            print("1- Insertar")
            print("2- Eliminar")
            print("3- Visualizar \n")
            decision = int(input("decision: "))
            os.system("cls")
            
            if decision == 1:
                while True:
                    decision = mostrar_insercion()
                    os.system("cls")
                    if decision == "1":
                        os.system("cls")
                        insertar_jugador(conexion)
                    elif decision == "2":
                        os.system("cls")
                        insertar_equipo(conexion)
                    elif decision == "3":
                        os.system("cls")
                        insertar_pais(conexion)
                    elif decision == "4":
                        os.system("cls")
                        insertar_estadio(conexion)
                    elif decision == "5":
                        os.system("cls")
                        insertar_ciudad(conexion)
                    elif decision == "6":
                        os.system("cls")
                        insertar_hotel(conexion)
                    elif decision == "7":
                        os.system("cls")
                        insertar_bus(conexion)
                    elif decision == "8":
                        os.system("cls")
                        insertar_arbitro(conexion)
                    elif decision == "9":
                        os.system("cls")
                        insertar_estadistica_equipo(conexion)
                    elif decision == "10":
                        os.system("cls")
                        insertar_estadistica_jugador(conexion)
                    elif decision == "0":
                        break
                    else:
                        os.system("cls")
                        print("Opción no válida. Por favor, elige una opción del menú.")
            if decision == 2: 
                print("En proceso beibi ;)")
                #eliminar_jugador(conexion)
                #eliminar_equipo(conexion)

            if decision == 3:
                os.system("cls")
                visualizar(conexion)    
            
        if rol == "user":
                print("Eres un usuario")
    else:
        if rol == -1:
         print("[ERROR] - Usuario incorrecto.")

    #repetimos bucle

    decision = ""
    while decision != 's' and decision != 'n': 
        decision = input("\nREINICIAR EL PROGRAMA (s/n): ")

    if decision == 'n':
        reset = False

desconectar_db(conexion) # desconectar base de datos 