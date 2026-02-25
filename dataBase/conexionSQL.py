##Esta es una forma mas directa para conectar a SQL: vídeo: https://www.youtube.com/watch?v=56pFefi2AVM&t=30s
##para probar ejecutar con: python .\dataBase\conexionSQL.py
import pyodbc

try:
    conection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-M6Q0QCR;DATABASE=miBibliotecaDB;Trusted_Connection=Yes')
    print("Conexion exitosa")
    cursor=conection.cursor()
    cursor.execute("SELECT @@Version")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT L.tituloLibro, L.anioPublicacion, A.nameAutor, A.apellidoAutor, E.nameEditorial FROM tbLibros AS L INNER JOIN tbAutores AS A ON L.idAutor = A.idAutor INNER JOIN tbEditoriales AS E ON L.idEditorial = E.idEditorial")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
