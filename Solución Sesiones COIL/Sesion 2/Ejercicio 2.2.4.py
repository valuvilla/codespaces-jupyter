dic_ejemplo = {'Alumnos': ["Carlos", "Ana", "Daniela", "Martín"],
'Curso': "Big Data",
'Edad': ('22', '21', '20', '22'),
'Presencial': True
}
setNumAlumnos=set(dic_ejemplo['Edad'])
print(setNumAlumnos)
print(len(setNumAlumnos))