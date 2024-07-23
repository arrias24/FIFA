import psycopg2
def eliminar_jugador(conexion):
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


