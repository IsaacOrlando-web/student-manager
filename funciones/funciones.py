#guardar estudiante
def SaveStudent(studentName, notas):
    f = open("funciones/estudiantes.txt", "a")
    f.write(f'\n{studentName} , {notas}')
    f.close()

#Imprimir estudiantes
def ShowStudents():
    #into an array
    text_list = []
    with open("funciones/estudiantes.txt", "rt") as text_file:
        for line in text_file:
            nombre, nota = line.strip().split(",")
            text_list.append({"nombre": nombre, "nota": float(nota)})
    return text_list

#Calcular promedio de notas
def calculate():
    students = ShowStudents()
    notas = []
    for nota in students:
        notas.append(nota['nota'])
    return round(sum(notas)/len(notas),3)

#Aprobados
def aprovados():
    aprovados = []
    estudiantes = ShowStudents()
    for estudiante in estudiantes:
        if estudiante['nota'] >= 50.0:
            aprovados.append(estudiante['nombre'])
    return aprovados
