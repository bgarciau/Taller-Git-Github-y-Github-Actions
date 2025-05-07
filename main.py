import estudiantes.registro as registro

validados = registro.validar_estudiantes("estudiantes.csv")
print("ESTUDIANTES VALIDADOS,CON NOTAS EN EL RANGO")
registro.mostrar_estudiantes(validados)
print("PROMEDIO DE LAS NOTAS DE CADA ESTUDIANTE")
registro.calcular_promedio(validados)




