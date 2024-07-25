def MENU_consultas(conexion):
    print("MENU- CONSULTAS")
    print("1- consultar las estadisticas de un jugador")
    print("2- consultar jugadores activos en un pais segun la copa")
    print("3- Consultar los campeones de la copa del mundo")
    print("4- Consultar las posiciones de un equipo segun un partido en un copa.")
    print("5- Consultar los hoteles donde se hospedaran los equipos y los buses asignados para cada equipo con su conductor.")
    print("6- Mostrar los jugadores que fueron prohibidos de participar en una copa y que participaron en la copa")
    print("7- Ver los estadios habilitados para un copa y los partidos a jugarse")
    decision = int(input(""))

    if decision == 1:
        try:
            Copa = input("Ingrese el ID de la copa: ")
            equipo = input("Ingrese el ID del equipo: ")
            jugador = input("Ingrese el ID del jugador: ")

            with conexion.cursor() as cursor:
                sentencia_sql = """
                    SELECT * FROM copa AS copa
                    JOIN estadisticas AS e ON copa.id = %s
                    JOIN equipo ON id_equipo = %s
                    JOIN jugador ON id_jugador = %s
                    WHERE copa.id = %s AND equipo.id = %s
                """
                #se repiten dos veces el ID de la copa y el ID del equipo en la llamada cursor.execute
                #porque se utilizan en dos lugares diferentes en la consulta SQL.
                cursor.execute(sentencia_sql, (Copa, equipo, jugador, Copa, equipo))
            
            conexion.commit()
            print("...")
        
        except Exception as e:
            print("[Error] - No se ha conseguido un dato:", str(e))

    if decision == 2:
        #⁠Consultar los jugadores activos de un pais en una copa:
        try:
            id_pais = input("Ingrese el ID del país: ")
            año_copa = input("Ingrese el año de la copa: ")
        
            with conexion.cursor() as cursor:
                sentencia_sql = """
                    SELECT j.nombre
                    FROM jugador j
                    INNER JOIN equipo e ON j.id_equipo = e.id
                    INNER JOIN participa_en pe ON e.id = pe.id_equipo
                    INNER JOIN copa c ON pe.copa_participacion = c.id
                    WHERE e.id_pais = %s AND c.año = %s
                    AND j.estado_jugador = 'activo';
                """
                cursor.execute(sentencia_sql, (id_pais, año_copa))
                jugadores = cursor.fetchall()
                
                # Imprimir los nombres de los jugadores o mensaje en caso de no encontrar jugadores activos
                if jugadores:
                    print("Jugadores activos del país con ID {} durante la copa {}:".format(id_pais, año_copa))
                    for jugador in jugadores:
                        print(jugador[0])  # Mostrar cada nombre de jugador
                else:
                    print("No se encontraron jugadores activos del país con ID {} durante la copa {}.".format(id_pais, año_copa))

        except Exception as e:
            print("[Error] - No se ha podido obtener los datos:", str(e))
        
    if decision == 3:
        #⁠Ver los ultimos campeones de las copas del mundo o las copas de cada continente, 
        #junto a los miembros del equipo y cuerpo tecnico:
        try:
            with conexion.cursor() as cursor:
                sentencia_sql = """
                    WITH Campeones AS (
                        SELECT e.nombre AS equipo, c.nombre AS copa
                        FROM ganador g
                        INNER JOIN equipo e ON g.id_ganador = e.id
                        INNER JOIN copa c ON g.tipo_copas = c.id
                    )
                    SELECT c.equipo,
                        e.nombre AS jugador,
                        et.cargo
                    FROM Campeones c
                    INNER JOIN equipo e ON c.equipo = e.nombre
                    INNER JOIN jugador j ON e.id = j.id_equipo
                    INNER JOIN equipo_tecnico et ON e.id = et.id_equipo;
                """
                cursor.execute(sentencia_sql)
                jugadores_cargos = cursor.fetchall()
                
                # Imprimir encabezado
                print("{:<20} {:<20} {:<10}".format("Equipo", "Jugador", "Cargo"))
                
                for jugador_cargo in jugadores_cargos:
                    print("{:<20} {:<20} {:<10}".format(*jugador_cargo))  # Mostrar cada resultado en una línea con formato

        except Exception as e:
            print("[Error] - No se ha podido obtener los datos:", str(e))

    if decision == 4:       
        try:
            id_equipo = input("Ingrese el ID del equipo: ")
            id_copa = input("Ingrese el ID de la copa: ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = """
                    SELECT posicion
                    FROM participa_en pe
                    INNER JOIN equipo e ON pe.id_equipo = e.id
                    INNER JOIN copa c ON pe.copa_participacion = c.id
                    WHERE e.id = %s AND c.id = %s;
                """
                cursor.execute(sentencia_sql, (id_equipo, id_copa))
                posiciones = cursor.fetchall()
                
                # Imprimir las posiciones
                print("Posiciones de los jugadores en el equipo {} durante la copa {}:".format(id_equipo, id_copa))
                for posicion in posiciones:
                    print(posicion[0])  # Mostrar cada posición

        except Exception as e:
            print("[Error] - No se ha podido obtener los datos:", str(e))

    if decision == 5:
        try:
            equipo_id = input("Ingrese el ID del equipo: ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = """
                    SELECT e.nombre AS equipo, h.nombre AS hotel, b.nombre AS bus, c.nombre AS conductor
                    FROM equipo e
                    INNER JOIN se_hospeda sh ON e.id = sh.id_equipo
                    INNER JOIN hotel h ON sh.id_hotel = h.id
                    INNER JOIN traslada_en te ON e.id = te.id_equipo
                    INNER JOIN bus b ON te.id_bus = b.id
                    INNER JOIN conductor c ON b.id_conductor = c.id
                    WHERE e.id = %s
                """
                cursor.execute(sentencia_sql, (equipo_id,))
                estadisticas = cursor.fetchall()
                
                # Imprimir los resultados o mensaje en caso de no encontrar datos
                if estadisticas:
                    print("\nResultados:")
                    print("{:<20} {:<20} {:<20} {:<20}".format("Equipo", "Hotel", "Bus", "Conductor"))
                    for fila in estadisticas:
                        print("{:<20} {:<20} {:<20} {:<20}".format(*fila))
                else:
                    print("No se encontraron datos para el equipo con ID {}.".format(equipo_id))
            
        except Exception as e:
            print("[Error] - No se ha podido obtener los datos:", str(e))

    if decision == 6:
        try:
            Copa = input("Ingrese el ID de la copa: ")
            equipo = input("Ingrese el ID del equipo: ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = """
                    SELECT equipo.nombre AS equipo,
                        SUM(estadisticas_equipo.goles_a_favor) AS goles,
                        SUM(estadisticas_equipo.minutos_jugados) AS minutos_jugados
                    FROM
                        equipo
                    INNER JOIN estadisticas_equipo ON equipo.id = estadisticas_equipo.id_equipo
                    INNER JOIN participa_en ON equipo.id = participa_en.id_equipo
                    INNER JOIN equipo_copa ON participa_en.copa_participacion = equipo_copa.id_copa
                    WHERE
                        equipo_copa.id_copa = %s AND equipo.id = %s
                    GROUP BY
                        equipo.nombre;
                """
                cursor.execute(sentencia_sql, (Copa, equipo))
                estadisticas = cursor.fetchall()
                
                # Imprimir encabezado
                print("{:<10} {:<10} {:<10}".format("Equipo", "Goles", "Minutos jugados"))
                
                for equipo_stats in estadisticas:
                    print("{:<10} {:<10} {:<10}".format(*equipo_stats))  # Mostrar cada resultado en una línea con formato

        except Exception as e:
            print("[Error] - No se ha podido obtener los datos:", str(e))


    if decision == 7:
        try:
            fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/aaaa): ")
            fecha_fin = input("Ingrese la fecha de fin (dd/mm/aaaa): ")
            
            with conexion.cursor() as cursor:
                sentencia_sql = """
                    SELECT
                        partido.fecha,
                        equipo.nombre AS equipo_local,
                        equipo_visitante.nombre AS equipo_visitante
                    FROM
                        partido
                    INNER JOIN equipo ON partido.id_equipo_local = equipo.id
                    INNER JOIN equipo AS equipo_visitante ON partido.id_equipo_visitante = equipo_visitante.id
                    WHERE
                        partido.fecha BETWEEN STR_TO_DATE(%s, '%%d/%%m/%%Y') AND STR_TO_DATE(%s, '%%d/%%m/%%Y');
                """
                cursor.execute(sentencia_sql, (fecha_inicio, fecha_fin))
                partidos = cursor.fetchall()
                
                # Imprimir encabezado
                print("{:<10} {:<20} {:<20}".format("Fecha", "Equipo Local", "Equipo Visitante"))
                
                for partido in partidos:
                    print("{:<10} {:<20} {:<20}".format(*partido))  # Mostrar cada resultado en una línea con formato

        except Exception as e:
            print("[Error] - No se ha podido obtener los datos:", str(e))


