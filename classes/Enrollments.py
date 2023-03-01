from classes.DbMongo import DbMongo
from classes import DATA

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

        b=[]
        c=[]#lista para capturar cursos sin repetirse para primer for
        k=[]#lista para capturar cursos con repeticion para primer for

        bb=[]
        cc=[]#lista para capturar carreras sin repetirse para primer for
        kk=[]#lista para capturar carreras con repeticion para primer for





        for i in range(len(DATA)): #el  rango deberia estar en 200 pero lo dejo en 5 para hacer pruebas


            v=[]
            w=[]

            vv=[]

            for m in range(len(DATA)):
                
                carrer = DATA[m]['carrera'] #aqui almacenamos el dato de la carrera
                vv.append(carrer) #lista de carreras con repeticion 
 
            carrera = DATA[i]['carrera'] #aqui almacenamos el la carrera del alumno
            alumno = DATA[i]['nombre_completo'] #alamcenamos el nombre del alumno
            kk.append(carrera)
 

            if(c.count(DATA[i]['carrera']) == 0):
                cc.append(carrera)
                bb.append([{'carrera': carrera,'numeroDeEstudiantes':[alumno]}])

                #result = collection.insert_one({'carrera': carrera,'numeroDeEstudiantes':vv.count(cc[len(cc)-1])})
  


            
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

            if (i < len(z)):
                result = collection.insert_one({'curso': z[i],'aprobados':v.count(z[i]),'reprobados':w.count(z[i])})
                ##print(i)
                
    @staticmethod
    def print_full_report_long_path(db):
        collection = db["create_enrollments"]

        for e in collection.find():
            r = { 
                "Curso" : e["curso"]
                , "aprobados": e["aprobados"] 
                , "reprobados": e["reprobados"]
                
            }
            print(r)

        #self.id =  result.inserted_id

    