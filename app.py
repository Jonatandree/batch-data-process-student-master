import pymongo
from classes import DATA, Dataprocess,DbMongo,Students,Careers,Courses,Enrollments
from dotenv import load_dotenv


def main():
    
    client, db = DbMongo.getDB()


    #pipeline = Dataprocess(DATA)
    #pipeline.create_careers(db)
    #Dataprocess(DATA).create_careers(db)


    ###################################################################################################################################
    
    b=[]#esta variable es para acumlar las carreas que sustraemos de DATA y que no se repitan esta lista para implementarla solo fatal guardas los alumnos par cada carrera
    for i in range(5): #el  rango deberia estar en 200 pero lo dejo en 5 para hacer pruebas
        carrera = DATA[i]['carrera']
        alumno = DATA[i]['nombre_completo']

        b.count(DATA[i]['carrera'])

        if(b.count(DATA[i]['carrera']) == 0):
            b.append(DATA[i]['carrera'])
        print(b) ##con esta variable imprimimos un tipo de __dict__ con las carreras sin repetirse

        Careers(carrera,alumno).create_careers(db)

        cursos_aprobados = DATA[i]['cursos_aprobados']
        cursos_reprobados = DATA[i]['cursos_reprobados']
        Courses(alumno,cursos_aprobados,cursos_reprobados).create_courses(db)

        cuenta=DATA[i]['numero_cuenta']
        edad=DATA[i]['edad']
        Students(alumno,cuenta,edad,cursos_aprobados,cursos_reprobados).create_students(db)

        Enrollments(alumno,cursos_aprobados,cursos_reprobados).create_enrollments(db)
        estado = DATA[i]['cursos_reprobados']
        Dataprocess(estado).create_enrollments(db)

    ################################################################################################################################
    #print(DATA[0]['carrera'])
    #print(type(DATA))
    #l=[]
    #print(type(l))
    #l='hola'
    #print(l[0])




    ###aqui ando descubriendo como hacer que unas lista guarde elementos no repetidos para implementarlo en clases Careers y Courses
    """
    l=["a","b","c","d","a","g","b","t","a"]
    b=[]

    for e in range(8):
        
        b.count(l[e])

        if(b.count(l[e]) == 0):
            b.append(l[e])

    print(b)

    """





    

    #print(DATA[198]['carrera'])
   
    
    #estudiante = Estudiante("juan","vasquez","32344")
    #estudiante.save(db)

    

if __name__ == "__main__":
    load_dotenv()
    main()
