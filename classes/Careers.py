from classes.DbMongo import DbMongo
from classes import DATA




class Careers:
    #@staticmethod
    def __init__(self,nombreCarrera,numeroDeEstudiantes=""):
        self.nombreCarrera=nombreCarrera
        self.numeroDeEstudiantes=numeroDeEstudiantes
        self.__collection = "Careers"


    #@staticmethod
    def save(self,db):

        client, db = DbMongo.getDB()
        collection = db["create_careers"]
        result = collection.insert_one(self.__dict__)
        self.id =  result.inserted_id
    
    def create_careers(self,db):

        client, db = DbMongo.getDB()
        collection = db["create_careers"]
        b=[]
        c=[]#lista para capturar carreras sin repetirse para primer for
        k=[]#lista para capturar carreras con repeticion para primer for

        for i in range(len(DATA)): #el  rango deberia estar en 200 pero lo dejo en 5 para hacer pruebas
            v=[]

            for m in range(len(DATA)):
                
                carrer = DATA[m]['carrera'] #aqui almacenamos el dato de la carrera
                v.append(carrer) #lista de carreras con repeticion 
        

            #contador = 1
            carrera = DATA[i]['carrera'] #aqui almacenamos el la carrera del alumno
            alumno = DATA[i]['nombre_completo'] #alamcenamos el nombre del alumno
            k.append(carrera)
        
            if(c.count(DATA[i]['carrera']) == 0):
                c.append(carrera)
                b.append([{'carrera': carrera,'numeroDeEstudiantes':[alumno]}])
                
                result = collection.insert_one({'carrera': carrera,'numeroDeEstudiantes':v.count(c[len(c)-1])})
        ##################

    @staticmethod
    def print_full_report_long_path(db):
        collection = db["create_careers"]

        for e in collection.find():
            r = { 
                "Carrera de" : e["carrera"]
                , "numero de estudiantes": e["numeroDeEstudiantes"] 

            }
            print(r)    