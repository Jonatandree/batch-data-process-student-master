from classes.DbMongo import DbMongo


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
        result = collection.insert_one(self.__dict__)
        self.id =  result.inserted_id