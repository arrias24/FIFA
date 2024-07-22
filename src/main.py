import time
from controller.bd_conect import conectar_db,desconectar_db #importamos la funcion que conecta la BD
from modulos.verificacion import verificacion

conexion = conectar_db()
#guarda todos los usuarios en un arreglo users 
with conexion.cursor() as cursor:
    sentencia_sql= "SELECT * FROM users"
    cursor.execute(sentencia_sql)
    users = cursor.fetchall()
    
nombre = input("Ingrese su nombre: \n")
#print(users[0][1])


clave = input("ingrese su clave: \n")
#print(users[0][2])
verificacion(users,nombre,clave)

#time.slepp(10)
desconectar_db(conexion)
#id nombre user cargo 
#0  1  2  3
#4  5 