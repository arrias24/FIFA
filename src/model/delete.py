import os

def MENU_delete(conexion):

    print("Seleccione la tabla para eliminar los datos.\n")
    print("1. Jugador")
    print("2. Equipo")
    print("3. Hotel")
    print("4. Estadio")
    print("5. Ciudad")
    print("6. pais")
    print("7. Bus")
    print("8. Árbitro")
    
    decision = int(input())

    if decision == 1:
        os.system("cls")
        try:
            jugador = input ("ingrese el ID del jugador a eliminar ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = """
                    DELETE FROM jugador WHERE id = %s
                """
                cursor.execute(sentencia_sql, (jugador,))
            
            conexion.commit()
            print("El jugador ha sido eliminado correctamente.")
        
        except Exception as e:
            print("Error al eliminar el jugador:", str(e))

    if decision == 2:
        os.system("cls")
        try:
            equipo = input("Ingrese el ID del equipo a eliminar ")

            with conexion.cursor() as cursor:
                # Actualizar la tabla "copa" estableciendo el valor de "id_equipo" como NULL
                sentencia_sql_copa = """
                    UPDATE copa SET id_equipo = NULL WHERE id_equipo = %s
                """
                cursor.execute(sentencia_sql_copa, (equipo,))

                # Eliminar el equipo completo de la tabla "equipos"
                sentencia_sql_equipos = """
                    DELETE FROM equipos WHERE id = %s
                """
                cursor.execute(sentencia_sql_equipos, (equipo,))

            conexion.commit()
            print("El equipo ha sido eliminado correctamente.")

        except Exception as e:
            print("Error al eliminar el equipo:", str(e))


    if decision == 3:
        os.system("cls")
        try:
            hotel = input("Ingrese el ID del hotel a eliminar ")

            with conexion.cursor() as cursor:
                
                sentencia_sql_copa = """
                    DELETE FROM hotel WHERE id = %s
                """
                cursor.execute(sentencia_sql_copa, (hotel,))

            conexion.commit()
            print("El hotel ha sido eliminado correctamente.")

        except Exception as e:
            print("Error al eliminar el hotel:", str(e))

    if decision == 4:
        os.system("cls")
        try:
            estadio = input("Ingrese el ID del estadio a eliminar ")

            with conexion.cursor() as cursor:
                
                sentencia_sql_copa = """
                    DELETE FROM estadio WHERE id = %s
                """
                cursor.execute(sentencia_sql_copa, (estadio,))

            conexion.commit()
            print("El estadio ha sido eliminado correctamente.")

        except Exception as e:
            print("Error al eliminar el estadio:", str(e))


    if decision == 5:
        os.system("cls")
        try:
            ciudad = input("Ingrese el ID del cuidad a eliminar ")

            with conexion.cursor() as cursor:
                
                sentencia_sql_copa = """
                    DELETE FROM ciudad WHERE id = %s
                """
                cursor.execute(sentencia_sql_copa, (ciudad,))

            conexion.commit()
            print("El ciudad ha sido eliminado correctamente.")

        except Exception as e:
            print("Error al eliminar el ciudad:", str(e))

    if decision == 6:
        os.system("cls")
        try:
            pais = input("Ingrese el ID del pais a eliminar ")

            with conexion.cursor() as cursor:
                
                sentencia_sql_copa = """
                    DELETE FROM pais WHERE id = %s
                """
                cursor.execute(sentencia_sql_copa, (ciudad,))

            conexion.commit()
            print("El pais ha sido eliminado correctamente.")

        except Exception as e:
            print("Error al eliminar el pais:", str(e))



