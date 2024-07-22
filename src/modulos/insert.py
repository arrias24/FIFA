import psycopg2

def mostrar_menu():
    print("\n======= MENÚ PRINCIPAL =======")
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
    print("0. Salir")
    return input("Selecciona una opción: ")

def insertar_jugador(conexion):
    try:
        nombre = input("Nombre: ")
        dorsal = input("Dorsal: ")
        fecha = input("Fecha de nacimiento (YYYY-MM-DD): ")
        genero = input("Género (M/F): ")
        id_equipo = input("ID del equipo: ")
        id_ciudad = input("ID de la ciudad: ")
        
        with conexion.cursor() as cursor:
            sentencia_sql = """
                INSERT INTO jugador (nombre, dorsal, fecha_nacimiento, genero, id_equipo, id_ciudad) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (nombre, dorsal, fecha, genero, id_equipo, id_ciudad)
            cursor.execute(sentencia_sql, valores)
            conexion.commit()
            print("Jugador insertado con éxito.")
    except Exception as e:
        print(f"Error al insertar jugador: {e}")

def insertar_equipo(conexion):
    try:
        nombre = input("Nombre: ")
        id_pais = input("ID del país: ")
        id_bus = input("ID del bus: ")
        
        with conexion.cursor() as cursor:
            sentencia_sql = "INSERT INTO equipo (nombre, id_pais, id_bus) VALUES (%s, %s, %s)"
            valores = (nombre, id_pais, id_bus)
            cursor.execute(sentencia_sql, valores)
            conexion.commit()
            print("Equipo insertado con éxito.")
    except Exception as e:
        print(f"Error al insertar equipo: {e}")

def insertar_pais(conexion):
    try:
        nombre = input("Nombre: ")
        
        with conexion.cursor() as cursor:
            sentencia_sql = "INSERT INTO pais (nombre) VALUES (%s)"
            valores = (nombre,)
            cursor.execute(sentencia_sql, valores)
            conexion.commit()
            print("País insertado con éxito.")
    except Exception as e:
        print(f"Error al insertar país: {e}")

def insertar_estadio(conexion):
    try:
        nombre = input("Nombre: ")
        capacidad = input("Capacidad: ")
        id_ciudad = input("ID de la ciudad: ")

        with conexion.cursor() as cursor:
            sentencia_sql = "INSERT INTO estadio (nombre, capacidad, id_ciudad) VALUES (%s, %s, %s)"
            valores = (nombre, capacidad, id_ciudad)
            cursor.execute(sentencia_sql, valores)
            conexion.commit()
            print("Estadio insertado con éxito.")
    except Exception as e:
        print(f"Error al insertar estadio: {e}")

def insertar_ciudad(conexion):
    try:
        nombre = input("Nombre: ")
        
        with conexion.cursor() as cursor:
            sentencia_sql = "INSERT INTO ciudad (nombre) VALUES (%s)"
            valores = (nombre,)
            cursor.execute(sentencia_sql, valores)
            conexion.commit()
            print("Ciudad insertada con éxito.")
    except Exception as e:
        print(f"Error al insertar ciudad: {e}")

def insertar_hotel(conexion):
    try:
        nombre = input("Nombre: ")
        id_ciudad = input("ID de la ciudad: ")
        id_pais = input("ID del país: ")
        id_bus = input("ID del bus: ")
        
        with conexion.cursor() as cursor:
            sentencia_sql = "INSERT INTO hotel (nombre, id_ciudad, id_pais, id_bus) VALUES (%s, %s, %s, %s)"
            valores = (nombre, id_ciudad, id_pais, id_bus)
            cursor.execute(sentencia_sql, valores)
            conexion.commit()
            print("Hotel insertado con éxito.")
    except Exception as e:
        print(f"Error al insertar hotel: {e}")

def insertar_bus(conexion):
    try:
        nombre = input("Nombre: ")
        
        with conexion.cursor() as cursor:
            sentencia_sql = "INSERT INTO bus (nombre) VALUES (%s)"
            valores = (nombre,)
            cursor.execute(sentencia_sql, valores)
            conexion.commit()
            print("Bus insertado con éxito.")
    except Exception as e:
        print(f"Error al insertar bus: {e}")

def insertar_arbitro(conexion):
    try:
        nombre = input("Nombre: ")
        fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
        cargo = input("Cargo: ")
        genero = input("Género (M/F): ")
        id_pais = input("ID del país: ")
        
        with conexion.cursor() as cursor:
            sentencia_sql = "INSERT INTO arbitro (nombre, fecha_nacimiento, cargo, genero, id_pais) VALUES (%s, %s, %s, %s, %s)"
            valores = (nombre, fecha_nacimiento, cargo, genero, id_pais)
            cursor.execute(sentencia_sql, valores)
            conexion.commit()
            print("Árbitro insertado con éxito.")
    except Exception as e:
        print(f"Error al insertar árbitro: {e}")

def insertar_estadistica_equipo(conexion):
    try:
        resultado = input("Resultado: ")
        tarjetas_amarillas = input("Tarjetas amarillas: ")
        tarjetas_rojas = input("Tarjetas rojas: ")
        goles_favor = input("Goles a favor: ")
        goles_contra = input("Goles en contra: ")
        id_partido = input("ID del partido: ")

        with conexion.cursor() as cursor:
            sentencia_sql = """
                INSERT INTO estadisticas_equipo (resultado, tarjetas_amarillas, tarjetas_rojas, goles_a_favor, goles_en_contra, id_partido) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (resultado, tarjetas_amarillas, tarjetas_rojas, goles_favor, goles_contra, id_partido)
            cursor.execute(sentencia_sql, valores)
            conexion.commit()
            print("Estadística de equipo insertada con éxito.")
    except Exception as e:
        print(f"Error al insertar estadística de equipo: {e}")

def insertar_estadistica_jugador(conexion):
    try:
        resultado = input("Resultado: ")
        tarjetas_amarillas = input("Tarjetas amarillas: ")
        tarjetas_rojas = input("Tarjetas rojas: ")
        goles = input("Goles: ")
        minutos_jugados = input("Minutos jugados: ")
        cantidad_atajadas = input("Cantidad de atajadas: ")

        with conexion.cursor() as cursor:
            sentencia_sql = """
                INSERT INTO estadistica_jugador (resultado, tarjetas_amarillas, tarjetas_rojas, goles, minutos_jugados, cantidad_atajadas) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (resultado, tarjetas_amarillas, tarjetas_rojas, goles, minutos_jugados, cantidad_atajadas)
            cursor.execute(sentencia_sql, valores)
            conexion.commit()
            print("Estadística de jugador insertada con éxito.")
    except Exception as e:
        print(f"Error al insertar estadística de jugador: {e}")