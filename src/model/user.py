def autenticacion(conexion): #guarda todos los usuarios en un arreglo users 

    with conexion.cursor() as cursor: 
        sentencia_sql= "SELECT * FROM users"
        cursor.execute(sentencia_sql)
        users = cursor.fetchall()
        return users