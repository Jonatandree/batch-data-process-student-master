from classes.DbMongo import DbMongo



class Careers:
    #@staticmethod
    def __init__(self,nombreCarrera,PrimerAlumno=""):
        self.nombreCarrera=nombreCarrera
        self.PrimerAlumno=PrimerAlumno
        self.__collection = "Careers"


    #@staticmethod
    def create_careers(self,db):

        client, db = DbMongo.getDB()
        collection = db["create_careers"]
        result = collection.insert_one(self.__dict__)
        self.id =  result.inserted_id
    
    def crear_carreras(self,db):

        client, db = DbMongo.getDB()
        collection = db["create_careers"]


        ##################