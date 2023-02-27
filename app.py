import pymongo
from classes import DATA, Dataprocess,DbMongo,Students,Careers,Courses,Enrollments
from dotenv import load_dotenv


def main():
    
    client, db = DbMongo.getDB()


    #pipeline = Dataprocess(DATA)
    #pipeline.create_careers(db)
    #Dataprocess(DATA).create_careers(db)


    ###################################################################################################################################
    carrera = DATA[0]['carrera']
    alumno = DATA[0]['nombre_completo']

    #b=[""] #esta variable es para acumlar las carreas que sustraemos de DATA y que no se repitan esta lista para implementarla solo fatal guardas los alumnos par cada carrera
    #l=[{'carrera': carrera,'alumnos':[alumno ]}]
    #k=[{'carrera': 'Matematica', 'alumnos': ['keydi', 'vicky', 'Daniel']}]
    #k.append(b)


    #print(k[0]['alumnos'])
    #######################################################################################

    b=[]
    
    c=[]#lista para capturar carreras sin repetirse
    k=[]#lista para capturar carreras con repeticion

    c=[]#lista para capturar cursos sin repetirse
    k=[]#lista para capturar cursos con repeticion

    for i in range(10): #el  rango deberia estar en 200 pero lo dejo en 5 para hacer pruebas
        contador = 1
        carrera = DATA[i]['carrera'] #aqui almacenamos el la carrera del alumno
        alumno = DATA[i]['nombre_completo'] # alamcenamos el nombre del alumno
        k.append(carrera)
        

        if(c.count(DATA[i]['carrera']) == 0):
            c.append(carrera)
            b.append([{'carrera': carrera,'primer_estudiante':[alumno]}])
            #print(len(c))
            l=c[len(c)-1]
            Careers(l,alumno).create_careers(db)



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
