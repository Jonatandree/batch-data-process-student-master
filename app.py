import pymongo
from classes import DATA, Dataprocess,DbMongo,Students,Careers,Courses,Enrollments
from dotenv import load_dotenv


def main():
    
    client, db = DbMongo.getDB()
    #pipeline = Dataprocess(DATA)
    #pipeline.create_careers(db)
    #Dataprocess(DATA).create_careers(db)
    ###################################################################################################################################
    #print(k[0]['alumnos'])
    #######################################################################################
    
    Careers("","").create_careers(db)###############s#########################
    Courses("").create_courses(db)
    Students("","","","","").create_students(db)
    Enrollments("","","").create_enrollments(db)


    print("--------------------------------------------------------------------------------------")
    Enrollments.print_full_report_long_path(db)
    print("--------------------------------------------------------------------------------------")
    
    Careers.print_full_report_long_path(db)
    
    




    """
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
                    ########
        
    print(z)
    

    """



    #####################################
    #print(DATA[0]['carrera'])
    #print(type(DATA))
    #l=[]
    #print(type(l))
    #l='hola'
    #print(l[0])
    #####################################




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
