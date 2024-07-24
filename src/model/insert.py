import psycopg2
import os

def insert(conexion):
    print("\n======= MENÚ DE INSERCION =======\n")
    print("1. Insertar Jugador")
    print("2. Insertar Equipo")
    print("3. Insertar País")
    print("4. Insertar Estadio")
    print("5. Insertar Ciudad")
    print("6. Insertar Hotel")
    print("7. Insertar Bus")
    print("8. Insertar Árbitro")
    print("9. Insertar Estadística de Equipo")
    print("10. Insertar Estadística de Jugador")
    print("11. Insertar Conductor")
    print("12. Insertar Copa")
    print("13. Insertar Ganador")
    print("14. Insertar Estadios_Copa")
    print("15. Insertar Participa En")
    print("16. Insertar Se Hospeda")
    print("17. Insertar Traslada en")
    print("18. Insertar Equipo Tecnico")
    print("19. Insertar Arbitro_Partido")
    print("20. Insertar Partido")
    print("0. Salir")
    decision = int(input("Selecciona una opción: "))

    if decision == 1:
        try:
            os.system("cls")
            print("Insertar a un jugador.\n")
            nombre = input("Nombre: ")
            dorsal = input("Dorsal: ")
            fecha = input("Fecha de nacimiento (YYYY-MM-DD): ")
            genero = input("Género (M/F): ")
            estado_jugador = input("Estado del jugador: ")
            id_equipo = input("id del equipo: ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = """
                    INSERT INTO jugador (nombre, dorsal, fecha_nacimiento, genero, estado_jugador, id_equipo) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                valores = (nombre, dorsal, fecha, genero,estado_jugador, id_equipo,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Jugador insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar jugador: {e}")

    if decision == 2:
        try:
            os.system("cls")
            print("Inserta un Equipo.\n")
            nombre = input("Nombre: ")
            id_pais = input("ID del país: ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO equipo (nombre, id_pais) VALUES (%s, %s)"
                valores = (nombre, id_pais,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Equipo insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar equipo: {e}")

    if decision == 3:
        try:
            os.system("cls")
            print("Insertar un Pais.\n")
            nombre = input("Nombre: ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO pais (nombre) VALUES (%s)"
                valores = (nombre,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("País insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar país: {e}")

    if decision == 4:
        try:
            os.system("cls")
            print("Insertar un Estadio.\n")
            nombre = input("Nombre: ")
            capacidad = input("Capacidad: ")
            id_ciudad = input("ID de la ciudad: ")

            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO estadio (nombre, capacidad, id_ciudad) VALUES (%s, %s, %s)"
                valores = (nombre, capacidad, id_ciudad,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Estadio insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar estadio: {e}")

    if decision == 5:
        try:
            os.system("cls")
            print("Insertar una Ciudad.\n")
            nombre = input("Nombre: ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO ciudad (nombre) VALUES (%s)"
                valores = (nombre,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Ciudad insertada con éxito.")
        except Exception as e:
            print(f"Error al insertar ciudad: {e}")

    if decision == 6:
        try:
            os.system("cls")
            print("Insertar un Hotel.\n")
            nombre = input("Nombre: ")
            id_ciudad = input("ID de la ciudad: ")
            id_pais = input("ID del país: ")

            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO hotel (nombre, id_ciudad, id_pais) VALUES (%s, %s, %s)"
                valores = (nombre,id_ciudad,id_pais,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Hotel insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar hotel: {e}")

    if decision == 7:
        try:
            os.system("cls")
            print("Insertar un Bus.\n")
            nombre = input("Nombre: ")
            id_conductor = input("id_conductor: ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO bus (nombre, id_conductor) VALUES (%s, %s)"
                valores = (nombre,id_conductor,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Bus insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar bus: {e}")

    if decision == 8:
        try:
            os.system("cls")
            print("Insertar un Arbitro.\n")
            nombre = input("Nombre: ")
            fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
            cargo = input("Cargo: ")
            genero = input("Género (M/F): ")
            id_pais = input("ID del país: ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO arbitro (nombre, fecha_nacimiento, cargo, genero, id_pais) VALUES (%s, %s, %s, %s, %s)"
                valores = (nombre, fecha_nacimiento, cargo, genero, id_pais,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Árbitro insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar árbitro: {e}")

    if decision == 9:
        try:
            os.system("cls")
            print("Insertar una Estadistica del Equipo")
            resultado = input("resultado: ")
            tarjetas_amarillas = input("Tarjetas amarillas: ")
            tarjetas_rojas = input("Tarjetas rojas: ")
            goles_favor = input("Goles a favor: ")
            goles_contra = input("Goles en contra: ")
            id_partido = input("ID del partido: ")

            with conexion.cursor() as cursor:
                sentencia_sql = """
                    INSERT INTO estadisticas_equipo (resultado,tarjetas_amarillas, tarjetas_rojas, goles_a_favor, goles_en_contra, id_partido) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                valores = (resultado, tarjetas_amarillas, tarjetas_rojas, goles_favor, goles_contra, id_partido,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Estadística de equipo insertada con éxito.")
        except Exception as e:
            print(f"Error al insertar estadística de equipo: {e}")

    if decision == 10:
        try:
            os.system("cls")
            print("Insertar una Estadistica de Jugador")
            tarjetas_amarillas = input("Tarjetas amarillas: ")
            tarjetas_rojas = input("Tarjetas rojas: ")
            goles_a_favor = input("Goles: ")
            minutos_jugados = input("Minutos jugados: ")
            cantidad_atajadas = input("Cantidad de atajadas: ")

            with conexion.cursor() as cursor:
                sentencia_sql = """
                    INSERT INTO estadistica_jugador (tarjetas_amarillas, tarjetas_rojas, goles_a_favor, minutos_jugados, cantidad_atajadas) 
                    VALUES (%s, %s, %s, %s, %s)
                """
                valores = (tarjetas_amarillas, tarjetas_rojas, goles_a_favor, minutos_jugados, cantidad_atajadas,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Estadística de jugador insertada con éxito.")
        except Exception as e:
            print(f"Error al insertar estadística de jugador: {e}")

    if decision == 11:
        try:
            os.system("cls")
            print("Insertar un Conductor.\n")
            nombre = input("Nombre: ")
 
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO conductor (nombre) VALUES (%s)"
                valores = (nombre,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Conductor insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar Conductor: {e}")

    if decision == 12:
        try:
            os.system("cls")
            print("Insertar una Copa.\n")
            ano = input("Ano: ")
            nombre = input("nombre: ")
            lugar_copa = input("lugar_copa: ")

 
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO copa (ano, nombre, lugar_copa) VALUES (%s,%s,%s)"
                valores = (ano,nombre,lugar_copa,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Copa insertada con éxito.")
        except Exception as e:
            print(f"Error al insertar Copa: {e}")

    if decision == 13:
        try:
            os.system("cls")
            print("Insertar un Ganador.\n")
            id_ganador = input("id_ganador: ")
            tipo_copa = input("tipo_copa: ")
 
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO ganador (id_ganador, tipo_copa) VALUES (%s, %s)"
                valores = (id_ganador, tipo_copa,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Ganador insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar Ganador: {e}")

    if decision == 14:
        try:
            os.system("cls")
            print("Insertar Estadios_Copa.\n")
            id_estadio = input("id_estadio: ")
            id_copa = input("id_copa: ")
 
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO estadios_copa (id_estadio, id_copa) VALUES (%s, %s)"
                valores = (id_estadio, id_copa,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Estadio_Copa insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar Estadio_Copa: {e}")

    if decision == 15:
        try:
            os.system("cls")
            print("Insertar Participa_En.\n")
            id_equipo = input("id_equipo: ")
            posicion = input("posicion: ")
            copa_participacion = input("copa_participacion: ")
            grupo = input("grupo: ")
 
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO participa_en (id_equipo,posicion,copa_participacion,grupo) VALUES (%s, %s,%s,%s)"
                valores = (id_equipo, posicion, copa_participacion, grupo,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Participa En insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar Participa En {e}")

    if decision == 16:
        try:
            os.system("cls")
            print("Insertar se hospeda.\n")
            id_equipo = input("id_equipo: ")
            id_hotel = input("id_hotel: ")
 
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO  (id_equipo, id_hotel) VALUES (%s, %s)"
                valores = (id_equipo, id_hotel,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("insertado se hospeda con éxito.")
        except Exception as e:
            print(f"Error al insertar se hospeda {e}")

    if decision == 17:
        try:
            os.system("cls")
            print("Insertar Traslada En.\n")
            id_equipo = input("id_equipo: ")
            id_bus = input("id_bus: ")
 
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO  (id_equipo, id_bus) VALUES (%s, %s)"
                valores = (id_equipo, id_bus,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print(" insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar  Traslada En{e}")

    if decision == 18:
        try:
            os.system("cls")
            print("Insertar Equipo Tecnico.\n")
            nombre = input("nombre: ")
            id_equipo = input("id_equipo: ")
            genero = input("genero: ")
            cargo = input("cargo: ")
            equipo = input("equipo: ")
 
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO  (nombre, id_equipo, genero, cargo, equipo) VALUES (%s, %s,%s,%s, %s)"
                valores = (nombre, id_equipo, genero, cargo, equipo,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Equipo Tecnico insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar Equipo Tecnico {e}")

    if decision == 19:
        try:
            os.system("cls")
            print("Insertar Arbitro_Partido.\n")
            id_arbitro = input("id_arbitro: ")
            id_partido = input("id_partido: ")
 
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO  (id_arbitro, id_partido) VALUES (%s, %s)"
                valores = (id_arbitro, id_partido,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print(" insertado Arbitro_Partido con éxito.")
        except Exception as e:
            print(f"Error al insertar Arbitro_Partido {e}")

    if decision == 20:
        try:
            os.system("cls")
            print("Insertar Partido.\n")
            duracion = input("duracion: ")
            fecha = input("fecha: ")
            hora = input("hora: ")
            estado_partido = input("estado_partido: ")
            id_estadio = input("id_estadio: ")
            id_equipo_visitante = input("id_equipo_visitante: ")
            id_equipo_local = input("id_equipo_local: ")
 
            with conexion.cursor() as cursor:
                sentencia_sql = "INSERT INTO  (duracio, fecha, hora, estado_partido, id_estadio, id_equipo_visitante, id_equipo_local) VALUES (%s, %s,%s,%s,%s,%s,%)"
                valores = (duracion,fecha,hora,estado_partido, id_estadio, id_equipo_visitante, id_equipo_local,)
                cursor.execute(sentencia_sql, valores)
                conexion.commit()
                print("Partido insertado con éxito.")
        except Exception as e:
            print(f"Error al insertar Partido {e}")

    if decision == "0":
        return        