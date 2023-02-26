from classes.DbMongo import DbMongo
from classes import DATA, Students

#This class creates the methods and then migrates them one by one to their respective classes

class Dataprocess:

    #@staticmethod
    def __init__(self,data, id=""):
        self.data=data
        self.id=id

    #@staticmethod
    def create_careers(self,db):

        client, db = DbMongo.getDB()
        collection = db["create_careers"]
        result = collection.insert_one(self.__dict__)
        self.id =  result.inserted_id
    
    def create_courses(self,db):
        client, db = DbMongo.getDB()
        collection = db["create_courses"]
        result = collection.insert_one(self.__dict__)
        self.id =  result.inserted_id

    def create_students(self,db):
        client, db = DbMongo.getDB()
        collection = db["create_students"]
        result = collection.insert_one(self.__dict__)
        self.id =  result.inserted_id

    def create_enrollments(self,db):
        client, db = DbMongo.getDB()
        collection = db["create_enrollments"]
        result = collection.insert_one(self.__dict__)
        self.id =  result.inserted_id