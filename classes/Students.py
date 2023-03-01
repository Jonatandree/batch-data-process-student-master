from classes.DbMongo import DbMongo
from classes import DATA


class Students:
    def __init__(self, nombre,cuenta,edad, cursosaprobados,cursosreprobados):
        self.nombre = nombre
        self.cuenta = cuenta
        self.edad = edad
        self.cursosaprobados = cursosaprobados
        self.cursosreprobados = cursosreprobados
        self.__collection = "Students"

    #@staticmethod
    def create_students(self,db):
        client, db = DbMongo.getDB()
        collection = db["create_students"]

        for i in range(len(DATA)):
            carrera = DATA[i]['carrera'] #aqui almacenamos el la carrera del alumno
            alumno = DATA[i]['nombre_completo'] #alamcenamos el nombre del alumno
            cuenta=DATA[i]['numero_cuenta']
            edad=DATA[i]['edad']
            cursos_aprobados = DATA[i]['cursos_aprobados']
            cursos_reprobados = DATA[i]['cursos_reprobados']

            result = collection.insert_one({
               'numero_cuenta': cuenta
            , 'nombre_completo': alumno
            , 'cursos_aprobados': cursos_aprobados
            , 'cursos_reprobados': cursos_reprobados
            , 'edad': edad
            , 'carrera': carrera
})

            ###########################


        result = collection.insert_one(self.__dict__)
        self.id =  result.inserted_id