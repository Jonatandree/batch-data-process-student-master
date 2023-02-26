from classes.DbMongo import DbMongo

class Courses:
    #@staticmethod
    def __init__(self,alumno,cursos_aprobados,cursos_reprobados, id=""):
        self.alumno=alumno
        self.cursos_aprobados=cursos_aprobados
        self.cursos_reprobados=cursos_reprobados
        self.alumno=alumno
        self.__collection = "Courses"

    #@staticmethod
    def create_courses(self,db):

        client, db = DbMongo.getDB()
        collection = db["create_courses"]
        result = collection.insert_one(self.__dict__)
        self.id =  result.inserted_id