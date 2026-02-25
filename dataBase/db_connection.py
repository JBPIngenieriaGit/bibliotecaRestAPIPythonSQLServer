import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

#funcion para retornar un objeto de conexión a la base de datos
def get_db_connection():
    try:
        connection_string = os.getenv('DB_CONNECTION_STRING')
        connection = pyodbc.connect(connection_string)
        print ("conexión a la base de datos exitosa")
        return connection
    except Exception as ex:
        print(f"Error al conectar a la base de datos: {ex}")
        return None
    
# Llamada a la función para probar la conexión
if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        conn.close() # Es buena práctica cerrar la conexión después de probar