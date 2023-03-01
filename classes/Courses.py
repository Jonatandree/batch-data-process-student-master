from classes.DbMongo import DbMongo
from classes import DATA

class Courses:
    #@staticmethod
    def __init__(self,alumno, id=""):
        self.alumno=alumno
        self.__collection = "Courses"

    #@staticmethod
    def create_courses(self,db):

        client, db = DbMongo.getDB()
        collection = db["create_courses"]

        b=[]
        c=[]#lista para capturar cursos sin repetirse para primer for
        k=[]#lista para capturar cursos con repeticion para primer for
        for i in range(len(DATA)): #el  rango deberia estar en 200 pero lo dejo en 5 para hacer pruebas
            v=[]
            w=[]
            
            for m in range(len(DATA)):
                for g in range(len(DATA[m]['cursos_aprobados'])):
                    cursos_aprobados1 = DATA[m]['cursos_aprobados'][g] #aqui almacenamos el dato de la cursos
                    v.append(cursos_aprobados1) #lista de cursos aprovados con repeticion 

            for m in range(len(DATA)):
                for g in range(len(DATA[m]['cursos_reprobados'])):
                    cursos_reprobados1 = DATA[m]['cursos_reprobados'][g] #aqui almacenamos el dato de la cursos
                    w.append(cursos_reprobados1) #lista de cursos aprovados con repeticion 

            b=v+w # cursos repetidos

            z=[]
            for m in range(len(b)):
                if(z.count(b[m]) == 0):
                        z.append(b[m])
                        #########


            ##print(len(z))

            if (i < len(z)):
                result = collection.insert_one({'curso': z[i],'aprobados':v.count(z[i]),'reprobados':w.count(z[i])})
                ##print(i)
    
    