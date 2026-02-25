USE [miBibliotecaDB]

Create table tbEditoriales(
idEditorial INT Primary key identity(1,1),
nameEditorial VARCHAR(100) NOT NULL,
paisEditorial VARCHAR(50)
);

CREATE TABLE tbAutores (
idAutor INT Primary Key Identity(1,1),
nameAutor VARCHAR(100),
apellidoAutor VARCHAR(100)
);

CREATE TABLE tbLibros(
idLibro INT Primary key Identity(1,1),
tituloLibro VARCHAR(100),
anioPublicacion INT,
idAutor INT,
idEditorial INT,
FOREIGN KEY (idAutor) REFERENCES tbAutores(idAutor),
FOREIGN KEY (idEditorial) REFERENCES tbEditoriales(idEditorial)
);


SELECT 
L.tituloLibro,
L.anioPublicacion,
A.nameAutor ,
A.apellidoAutor,
E.nameEditorial
FROM tbLibros AS L
INNER JOIN tbAutores AS A
ON L.idAutor = A.idAutor
INNER JOIN tbEditoriales AS E
ON L.idEditorial = E.idEditorial

INSERT INTO [dbo].[tbEditoriales] ([nameEditorial], [paisEditorial])
VALUES('Planeta','España'),('Anagrama','España');

INSERT INTO [dbo].[tbAutores]([nameAutor], [apellidoAutor])
VALUES ('Gabriel','Garcia Márquez'),('Isabel','Allende')

INSERT INTO tbLibros([tituloLibro], [anioPublicacion], [idAutor], [idEditorial]) 
VALUES('cien años de soledad',1967,1,1),('Mi nombre es Emilia del Valle',2025,2,2)