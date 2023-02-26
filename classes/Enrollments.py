from classes.DbMongo import DbMongo


class Enrollments:

    #@staticmethod
    def __init__(self,nombre,cursos_aprobados,cursos_reprobados):
        self.nombre = nombre
        self.cursos_aprobados=cursos_aprobados
        self.cursos_reprobados=cursos_reprobados
        self.__collection = "Enrollments"

    #@staticmethod
    def create_enrollments(self,db):

        client, db = DbMongo.getDB()
        collection = db["create_enrollments"]
        result = collection.insert_one(self.__dict__)
        self.id =  result.inserted_id