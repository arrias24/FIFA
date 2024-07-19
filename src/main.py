from controller.bd_conect import conectar_db,desconectar_db #importamos la funcion que conecta la BD


conexion = conectar_db()
desconectar_db(conexion)
