# Examen OOP I

<p align="center">
  <img src="head.jpg" alt="Python and Mongo" style="text-align:center" />
</p>

En este proyectos cargamos mediante un proceso BATCH hecho en python los datos que se encuentran en ``` classes.data.DATA ``` en diferentes collections de una MongoDB

Note que en el archivo ```app.py``` ya se encuentra cargada en una variable ```data``` los datos crudos que se desean procesar. 

la variable DATA que ya se cargo en el ```main``` es una arreglo donde cada objeto tiene la siguiente estructura:

```python

{
    'numero_cuenta': 4069666
    , 'nombre_completo': 'Lucía 1390 Sánchez 1390'
    , 'cursos_aprobados': ['Ciencias políticas', 'Derecho', 'Geografía', 'Cine']
    , 'cursos_reprobados': ['Veterinaria', 'Ciencias políticas', 'Biología']
    , 'edad': 24
    , 'carrera': 'Psicología'
}

```

## Procedimiento solicitado:

De esa estructura debe de crear las siguientes clases, recuerde que en clases no creamos atributos que fueran multivaluados o arreglos, procure que todos los atributos se valores y recuerde que debe de exister una relacion entre estas clases. (10 puntos):
- Careers 
- Courses 
- Students
- Enrollments

(*pista: un enrollment representa un estudiante y un curso. junto su estado si aprobo o no*)

Considera las operaciones del CRUD que sean necesarias implementar para hacer sync con la base de datos de mongodb en la plataforma de Atlas. posiblemente no todas las clases ocupen todas las operaciones. (10 puntos)

Una vez que ya hayas creado esas clases, toca trabajar en el proceso de migracion de datos, este esta propuesto en el metodo ```main``` del archivo ```app.py``` (30 puntos)

```python

pipeline.create_careers()
pipeline.create_students()
pipeline.create_enrollments()

```

Cada una de esas lineas hacen lo que describe la invocacion de sus metodos. muy probable ocupen como parametro el objeto de la BD, haga los cambios respectivos. 

Por ultimo, cree los siguientes reportes partiendo de los datos almacenados en la collection de enrollments:

- Cantidad de Estudiantes por carrera, la estructura podria ser (15 puntos):
```python

## Aqui se deberian de ver en total todas las carreras
{
    "carrera 1": 100
    , "carrera 2": 331 
}

```

- Historicamente por curso, cuantos estudiantes han reprobado y aprobado. la estructura podria ser (20 puntos):
```python

## Aqui se deberian de ver en total todas las carreras
{
    "Matematicas": { "aprobados": 122, "reprobados": 22 }
    , "OOP": { "aprobados": 30, "reprobados": 0 } 
}

```

Estos dos reportes deberian de ser invocados despues de las lineas de la migracion. trate de programar estos en la clase mas adecuada y con el tipo de metodo mas apropiado. 

## Observaciones: 

- Cuidado con ejecutar su codigo varias veces y duplicar data en las collections, esto podria afectar los numeros que se solicitan en su reporte. (5 puntos)
-  Cuando termine de migrar los datos de carreras y cursos, deberian de existir unicamente valores unicos en cada una de ellas. (5 puntos)

## Que debe de entregar en su tarea:

- En un documento de word, link de su repositorio donde se encuentra la solucion de su examen. adicione el ID de su ultimo commit. en caso que se encuentren commits despues de la hora de examen sera calificado con cero.
- Su documento de word debe de tener como nombre de archivo: NUMEROCUENTA_NOMBRE1_APELLIDO1.docx
- El reporsitorio debe de ser PUBLICO
- Cree una carpeta que llame imagenes y guarde capturas de pantallas de las colecciones con los resultados migrados (5 puntos)