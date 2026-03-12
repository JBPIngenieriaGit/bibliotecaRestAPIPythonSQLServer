Library Management API (REST) 📚

Esta es una API REST robusta desarrollada en Python utilizando el framework Flask. El proyecto permite la gestión integral (CRUD) de una base de datos bibliotecaria, conectándose de forma segura a SQL Server.

🚀 Características

Operaciones CRUD Completas: Gestión de tablas relacionadas para tbLibros, tbAutores y tbEditoriales.

Seguridad de Credenciales: Implementación de variables de entorno mediante python-dotenv para proteger cadenas de conexión.

Persistencia de Datos: Integración directa con Microsoft SQL Server (miBibliotecaDB).

Endpoints Estructurados:

GET, POST, PUT, DELETE para la entidad de Libros.

GET, PUT para la entidad de Autores.

🛠️ Stack Tecnológico

Lenguaje: Python

Framework: Flask

Base de Datos: SQL Server

Librerías Clave: pyodbc, python-dotenv, flask-cors

📋 Requisitos Previos
Antes de ejecutar el proyecto, asegúrate de tener instalado:

Python 3.x

SQL Server (Local o Remoto)

Driver ODBC para SQL Server

🔧 Configuración e Instalación

Clonar el repositorio:
git clone [URL_DE_TU_REPOSITORIO]
cd [NOMBRE_DE_TU_CARPETA]

Configurar el entorno:

Crea un archivo .env en la raíz del proyecto con tus credenciales:
DB_SERVER=tu_servidor
DB_DATABASE=miBibliotecaDB
DB_USERNAME=tu_usuario
DB_PASSWORD=tu_password

Instalar dependencias:

Bash
pip install flask pyodbc python-dotenv
Ejecutar la API:

Bash
python app.py

📖 Uso de Endpoints (Ejemplos)

Método	| Endpoint	   | Descripción
GET	    | /libros	     | Obtener lista de libros
POST	  | /libros	     | Registrar nuevo libro
PUT	    | /libros/<id> | Actualizar información de un libro
DELETE	| /libros/<id> | Eliminar un libro

Método	| Endpoint	    | Descripción
GET	    | /autores	    | Obtener lista de autores
POST	  | /autores	    | Registrar nuevo autor
PUT	    | /autores/<id> | Actualizar información de un autor
DELETE	| /autores/<id> | Eliminar un autor

Método	| Endpoint	        | Descripción
GET	    | /editoriales	    | Obtener lista de editoriales
POST	  | /editoriales	    | Registrar nueva editorial
PUT	    | /editoriales/<id> | Actualizar información de una editorial
DELETE	| /editoriales/<id> | Eliminar una editorial

Desarrollado por: Jonathan Bernal Pérez
