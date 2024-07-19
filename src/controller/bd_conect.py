import psycopg2

# Datos de conexión
conn_string = "postgresql://FIFADATABASE_owner:StHcy5PkXaO8@ep-proud-star-a5oy9rfv.us-east-2.aws.neon.tech/FIFADATABASE?sslmode=require"

# Función de establecer conexión con la base de datos
def conectar_db():
    try:
        conexion = psycopg2.connect(conn_string)
        print("Conexion exitosa")
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

# Función de cerrar la conexión con la base de datos
def desconectar_db(conexion):
    if conexion:
        conexion.close()
        print("Conexión cerrada")
