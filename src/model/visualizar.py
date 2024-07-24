import psycopg2
import os 

def visualizar(conexion):

    print("Seleccione la tabla para visualizar los datos.\n")
    print("1. Ver Jugador")
    print("2. Ver Equipo")
    print("3. Ver País")
    print("4. Ver Estadio")
    print("5. Ver Ciudad")
    print("6. Ver Hotel")
    print("7. Ver Bus")
    print("8. Ver Árbitro")
    print("9. Ver Estadística de Jugador")
    print("10. Ver Estadística de Equipo")
    print("11. Ver Conductor")
    print("12. Ver Copa")
    print("13. Ver Ganador")
    print("14. Ver Estadios_Copa")
    print("15. Ver Participa En")
    print("16. Ver Se Hospeda")
    print("17. Ver Traslada en")
    print("18. Ver Equipo Tecnico")
    print("19. Ver Arbitro_Partido")
    print("20. Ver Partido")
    print("0. Salir\n")    
    decision = int(input("decision: "))

    if decision == 1:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM jugador"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<8}\t{:<20}\t{:<8}\t{:<15}\t{:<8}\t{:<10}\t{:<12}".format("id", "nombre", "dorsal", "fecha_nacimiento", "genero", "estado_jugador", "id_equipo"))
            for row in data:
                print("{:<8}\t{:<20}\t{:<8}\t{:<20}\t{:<8}\t{:<10}\t{:<12}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    
    if decision == 2:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM equipo"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<8}\t{:<20}\t{:<8}".format("id", "nombre", "id_pais"))
            for row in data:
                print("{:<8}\t{:<20}\t{:<8}".format(row[0], row[1], row[2]))

    if decision == 3:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM pais"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<8}\t{:<20}".format("id", "Nombre"))
            for row in data:
                print("{:<8}\t{:<20}".format(row[0], row[1]))

    if decision == 4:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM estadio"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<5}\t{:<30}\t{:<30}\t{:<15}".format("id", "nombre", "capacidad", "id_ciudad"))
            for row in data:
                print("{:<5}\t{:<30}\t{:<30}\t{:<15}".format(row[0], row[1], row[2], row[3]))

    if decision == 5:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM ciudad"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}".format("id", "nombre"))
            for row in data:
                print("{:<15}\t{:<15}".format(row[0], row[1]))

    if decision == 6:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM hotel"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}\t{:<15}\t{:<15}".format("id", "nombre", "id_ciudad", "id_pais"))
            for row in data:
                print("{:<15}\t{:<15}\t{:<15}\t{:<15}".format(row[0], row[1],row[2],row[3]))

    if decision == 7:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM bus"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}\t{:<15}".format("id", "nombre", "id_conductor"))
            for row in data:
                print("{:<15}\t{:<15}\t{:<15}".format(row[0], row[1],row[2]))

    if decision == 8:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM arbitro"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}\t{:<15}\t{:<15}\t{:<15}\t{:<15}".format("id", "nombre", "fecha_nacimiento", "cargo", "genero", "id_pais"))
            for row in data:
                print("{:<15}\t{:<15}\t{:<15}\t{:<15}\t{:<15}\t{:<15}".format(row[0], row[1],row[2],row[3],row[4],row[5]))

    if decision == 9:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM estadistica_jugador"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<5}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}".format("id", "tarjetas_amarillas", "tarjetas_rojas", "goles_favor","goles_contra", "minutos_jugados", "cantidad_atajadas"))
            for row in data:
                print("{:<5}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}".format(row[0], row[1],row[2],row[3],row[4],row[5],row[6]))

    if decision == 10:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM estadisticas_equipo"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<5}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}".format("id", "resultado","tarjetas_amarillas", "tarjetas_rojas", "goles_favor","goles_contra", "id_partido"))
            for row in data:
                print("{:<5}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}".format(row[0], row[1],row[2],row[3],row[4],row[5],row[6]))

    if decision == 11:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM conductor"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}".format("id", "nombre"))
            for row in data:
                print("{:<15}\t{:<15}".format(row[0], row[1]))

    if decision == 12:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM copa"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}\t{:<15}\t{:<15}".format("id", "ano","nombre","lugar_copa"))
            for row in data:
                print("{:<15}\t{:<15}\t{:<15}\t{:<15}".format(row[0], row[1], row[2], row[3]))

    if decision == 13:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM ganador"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}".format("id_ganador", "tipo_copas"))
            for row in data:
                print("{:<15}\t{:<15}".format(row[0], row[1]))

    if decision == 14:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM estadios_copa"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}".format("id_estadio", "id_copa"))
            for row in data:
                print("{:<15}\t{:<15}".format(row[0], row[1]))

    if decision == 15:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM participa_en"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}\t{:<15}\t{:<15}".format("id_equipo", "posicion","copa_participacion","grupo"))
            for row in data:
                print("{:<15}\t{:<15}\t{:<15}\t{:<15}".format(row[0], row[1], row[2], row[3]))

    if decision == 16:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM se_hospeda"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}".format("id_equipo", "id_hotel"))
            for row in data:
                print("{:<15}\t{:<15}".format(row[0], row[1]))

    if decision == 17:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM traslada_en"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}".format("id_equipo", "id_bus"))
            for row in data:
                print("{:<15}\t{:<15}".format(row[0], row[1]))                                                  

    if decision == 18:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM equipo_tecnico"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}\t{:<15}\t{:<15}\t{:<15}".format("id", "nombre", "id_equipo", "genero", "cargo"))
            for row in data:
                print("{:<15}\t{:<15}\t{:<15}\t{:<15}\t{:<15}".format(row[0], row[1], row[2], row[3], row[4]))

    if decision == 19:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM arbitro_partido"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<15}\t{:<15}".format("id_arbitro", "id_partido"))
            for row in data:
                print("{:<15}\t{:<15}".format(row[0], row[1]))                                        

    if decision == 20:
        os.system("cls")
        with conexion.cursor() as cursor:
            sentencia_sql = "SELECT * FROM partido"
            cursor.execute(sentencia_sql)
            data = cursor.fetchall()
            print("{:<5}\t{:<8}\t{:<8}\t{:<8}\t{:<8}\t{:<8}\t{:<8}\t{:<8}".format("id", "duracion", "fecha", "hora", "estado_partido", "id_estadio", "id_equipo_visitante", "id_equipo_local"))
            for row in data:
                print("{:<5}\t{:<8}\t{:<8}\t{:<8}\t{:<8}\t{:<8}\t{:<8}\t{:<8}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))                

