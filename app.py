import pymongo
from classes import DATA, Dataprocess,DbMongo,Students,Careers,Courses,Enrollments
from dotenv import load_dotenv


def main():
    
    client, db = DbMongo.getDB()


    #pipeline = Dataprocess(DATA)
    #pipeline.create_careers(db)
    #Dataprocess(DATA).create_careers(db)


    ###################################################################################################################################

    for i in range(4):
        carrera = DATA[i]['carrera']
        alumno = DATA[i]['nombre_completo']
        Careers(carrera,alumno).create_careers(db)

        cursos_aprobados = DATA[i]['cursos_aprobados']
        cursos_reprobados = DATA[i]['cursos_reprobados']
        Courses(alumno,cursos_aprobados,cursos_reprobados).create_courses(db)

        cuenta=DATA[i]['numero_cuenta']
        edad=DATA[i]['edad']
        Students(alumno,cuenta,edad,cursos_aprobados,cursos_reprobados).create_students(db)

        Enrollments(alumno,cursos_aprobados,cursos_reprobados).create_enrollments(db)
        

        #estado = DATA[i]['cursos_reprobados']
        #Dataprocess(estado).create_enrollments(db)
    ####################################################################################################################################


    

    #print(DATA[198]['carrera'])
   
    
    #estudiante = Estudiante("juan","vasquez","32344")
    #estudiante.save(db)

    

if __name__ == "__main__":
    load_dotenv()
    main()
