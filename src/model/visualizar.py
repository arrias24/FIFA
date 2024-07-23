import psycopg2
import os 

def visualizar(conexion):

    print("Seleccione la tabla para visualizar los datos.\n")
    print("1. Jugador")
    print("2. Equipo")
    print("3. País")
    print("4. Estadio")
    print("5. Ciudad")
    print("6. Hotel")
    print("7. Bus")
    print("8. Árbitro")
    print("9. Estadística de Equipo")
    print("10. Estadística de Jugador\n")
    decision = int(input("decision: "))

    if decision == 1:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM jugador"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<8}\t{:<20}\t{:<8}\t{:<15}\t{:<8}\t{:<10}\t{:<12}".format("id", "Nombre", "Numero", "Fecha de Nacimiento", "Genero", "Equipo id", "Posicion id"))
            for row in data:
                print("{:<8}\t{:<20}\t{:<8}\t{:<20}\t{:<8}\t{:<10}\t{:<12}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    
    if decision == 2:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM equipo"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<8}\t{:<20}\t{:<8}\t{:<15}".format("id", "Nombre", "id_Pais", "id_Bus"))
            for row in data:
                print("{:<8}\t{:<20}\t{:<8}\t{:<20}".format(row[0], row[1], row[2], row[3]))

    if decision == 3:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM pais"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<8}\t{:<20}".format("id", "Nombre, equipos"))
            for row in data:
                print("{:<8}\t{:<20}".format(row[0], row[1]))