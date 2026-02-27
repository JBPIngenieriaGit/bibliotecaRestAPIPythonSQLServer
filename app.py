from flask import Flask, jsonify, request
from  dataBase.db_connection import get_db_connection

app = Flask(__name__)


###########-- Metodos CRUD para tabla Libros --###########

# EndPoint (rutas) para obtener los detalles de libros, metodo GET
@app.route("/libros", methods=['GET'])
def get_libros():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'No connection to database'}), 500
    
    cursor = conn.cursor()

    #Consulta de SQL que une las tablas de la base de datos, puede ser cualquier consulta
    query = """
    SELECT 
        L.tituloLibro,
        L.anioPublicacion,
        A.nameAutor,
        A.apellidoAutor,
        E.nameEditorial
    FROM tbLibros AS L
    INNER JOIN tbAutores AS A
    ON L.idAutor = A.idAutor
    INNER JOIN tbEditoriales AS E
    ON L.idEditorial = E.idEditorial
    """

    cursor.execute(query)
    
    libros = []

    for row in cursor.fetchall():
        libros.append({
            "tituloLibro": row.tituloLibro,
            "anioPublicacion": row.anioPublicacion,
            "nombreAutor": row.nameAutor,
            "Editorial": row.nameEditorial
        })

    conn.close()
    return jsonify(libros)

#Endpoint (ruta) para crear un nuevo libro, metodo POST
@app.route("/libros", methods=['POST'])
def add_libro():

    nuevo_libro = request.get_json()

    #Validación sencilla
    if not nuevo_libro or 'tituloLibro' not in nuevo_libro or 'idAutor' not in nuevo_libro:
        return jsonify({'error': 'El autor y idEditorial son requeridos'}), 400
    
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'no connection to database'}), 500
    
    cursor = conn.cursor()

    query = "INSERT INTO tbLibros([tituloLibro], [anioPublicacion], [idAutor], [idEditorial]) VALUES(?,?,?,?)"

    try:
        cursor.execute(
            query,
            nuevo_libro['tituloLibro'],
            nuevo_libro['anioPublicacion'],
            nuevo_libro['idAutor'],
            nuevo_libro['idEditorial']
        )
        conn.commit()
        return jsonify({'success': True}), 201
    
    except Exception as ex:
        
        return jsonify({'error': str(ex)}), 500
    
        # Esto siempre se ejecuta haya error o no, en este caso, cerrar la conexión para no tener que cerrarla en cada secuencia
    finally:
        if conn:
            conn.close()


# Metodo PUT, para actualizar un registro
@app.route("/libros/<int:id>", methods = ['PUT'])
def update_libro(id):
    datos_actualizados = request.get_json()

    #validacion verificar que almenos venga el titulo de libro 
    if not datos_actualizados or 'tituloLibro' not in datos_actualizados:
        return jsonify({'error':'Falta el campo tituloLibro'}), 400
    
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "No hay conexión con la base de datos"}), 500
    
    cursor = conn.cursor()

    # Aqui se pueden agregar los campos que se desean modificar
    query = "UPDATE tbLibros SET [tituloLibro] = ? WHERE idLibro = ?"

    try:
        # Pasar el nuevo titulo y el idLibro que viene en la URL
        cursor.execute(query, datos_actualizados['tituloLibro'], id)

        # verificar si realmente se encontro el registro y se acualizo
        if cursor.rowcount == 0:
            conn.close()
            return jsonify({"error":"Libro no encontrado"}), 404
        
        conn.commit()
        #conn.close()
        return jsonify({'success': True, 'message': 'Libro actualizado correctamente'}), 200
    except Exception as ex:
        #conn.close()
        return jsonify({'error':str(ex)}), 500
    
    # Esto siempre se ejecuta haya error o no, en este caso, cerrar la conexión
    finally:
        if conn:
            conn.close()


# EndPoint Metodo Delete, se hace directo, solo recibe el idLibro

@app.route("/libros/<int:id>", methods=['DELETE'])
def delete_libro(id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error':'No hay conexión con la base de datos'}), 500
    
    cursor = conn.cursor()
    query = "DELETE FROM tbLibros WHERE idLibro = ?"
    
    try:
        cursor.execute(query, id)

        if cursor.rowcount == 0:
            return jsonify({'error':'Libro no encontrado'}), 404
        
        conn.commit()
        return jsonify({'success': True, 'message': 'Libro eliminado con éxito'}), 200
    
    except Exception as ex:
        
        #si el libro esta prestado o referenciado en otra tabla, saltará al siguiente error de llave foranea
        return jsonify({'error': f'No se puede eliminar, llave foranea: {str(ex)}'}), 500
    
    finally:
        if conn:
            conn.close()


###########-- Metodos CRUD para tabla Autores --###########

@app.route("/autores", methods=['GET'])
def get_autores():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error':'There is not conection to the Data Base'}), 500
    
    cursor = conn.cursor()
    query = """
    SELECT
	    [idAutor],
	    [nameAutor],
	    [apellidoAutor]
    FROM [dbo].[tbAutores] WITH(NOLOCK)
    """
    cursor.execute(query)

    autores = []

    for row in cursor.fetchall():
        autores.append({
            "idAutor": row.idAutor,
            "Nombre": f"{row.nameAutor} {row.apellidoAutor}"
        })

    conn.close()
    return jsonify(autores) 

# Agregar un nuevo autor metodo POST 
@app.route("/autores", methods = ['POST'])
def add_Autor():
    nuevo_autor = request.get_json()

    # Validación simple
    if not nuevo_autor or 'idAutor' not in nuevo_autor or 'nameAutor' not in nuevo_autor or 'apellidoAutor' not in nuevo_autor:
        return jsonify({'error': 'The fields idAutor, nameAutor and Lastname are required'}), 400
    
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error':'No conection to the Data Base'}), 500
    
    cursor = conn.cursor()
    query = "INSERT INTO tbAutores (idAutor, nameAutor, apellidoAutor) VALUES(?, ?, ?)"
    try:
        cursor.execute(
            query,
            nuevo_autor['idAutor'],
            nuevo_autor['nameAutor'],
            nuevo_autor['apellidoAutor'],
        )
        conn.commit()
        return jsonify({'success':True}), 201
    except Exception as ex:
        return jsonify({'error':str(ex)}), 500

    finally:
        if conn:
            conn.close() 

# Para iniciar la app
     
if __name__ == "__main__":
    app.run(debug=True)

