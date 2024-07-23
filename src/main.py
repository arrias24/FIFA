import time
import os 
from controller.bd_conect import conectar_db,desconectar_db #importamos la funcion que conecta la BD
from modulos.verificacion import *
from modulos.insert import *

conexion = conectar_db() # conectar base de datos
    

reset = True
while reset == True:
    os.system("cls")
  
    #guarda todos los usuarios en un arreglo users 

    with conexion.cursor() as cursor: 
        sentencia_sql= "SELECT * FROM users"
        cursor.execute(sentencia_sql)
        users = cursor.fetchall()

    #comprobamos usuario    
    print("\tINICIO DE LA APLICACION")
    nombre = input("usuario: ")
    clave = input("clave: ")
    rol = verificacion(users,nombre,clave)
    print("\n")
    if rol == "admin" or rol == "user":
        
        if rol == "admin":

            while True:
                    decision = mostrar_menu()
                    if decision == "1":
                        insertar_jugador(conexion)
                    elif decision == "2":
                        insertar_equipo(conexion)
                    elif decision == "3":
                        insertar_pais(conexion)
                    elif decision == "4":
                        insertar_estadio(conexion)
                    elif decision == "5":
                        insertar_ciudad(conexion)
                    elif decision == "6":
                        insertar_hotel(conexion)
                    elif decision == "7":
                        insertar_bus(conexion)
                    elif decision == "8":
                        insertar_arbitro(conexion)
                    elif decision == "9":
                        insertar_estadistica_equipo(conexion)
                    elif decision == "10":
                        insertar_estadistica_jugador(conexion)
                    elif decision == "0":
                        break
                    else:
                        print("Opción no válida. Por favor, elige una opción del menú.")
        if rol == "user":
            print("Eres un usuario")
    else:
        if rol == -1:
         print("[ERROR] - Usuario incorrecto.")

    #repetimos bucle
    decision = ""
    while decision != 's' and decision != 'n': 
        decision = input("Reiniciar (s/n): ")
        print('\n')

    if decision == 'n':
        reset = False

desconectar_db(conexion) # desconectar base de datos 