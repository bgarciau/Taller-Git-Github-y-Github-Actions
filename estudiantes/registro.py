import csv

def validar_estudiantes(nombre_archivo):
    estudiantes_validos = []

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            try:
                notas = [float(fila['nota 1']), float(fila['nota 2']), float(fila['nota 3'])]
                if all(0.0 <= nota <= 5.0 for nota in notas):
                    estudiantes_validos.append({
                        'nombre': fila['Nombre'],
                        'nota 1': fila['nota 1'],
                        'nota 2': fila['nota 2'],
                        'nota 3': fila['nota 3'],
                    })
            except (ValueError, KeyError):
                continue  
            
    return estudiantes_validos

def mostrar_estudiantes(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['nombre'])
    print(f"{'Nombre':<15} {'nota 1':<8} {'nota 2':<8} {'nota 3':<8}")
    print("-" * 25)
    for e in estudiantes_ordenados:
        print(f"{e['nombre']:<15} {e['nota 1']:<8} {e['nota 2']:<8} {e['nota 3']:<8}")
        
def calcular_promedio(estudiantes):
    for estudiante in estudiantes:
        try:
            notas = [
                float(estudiante['nota 1']),
                float(estudiante['nota 2']),
                float(estudiante['nota 3'])
            ]
            promedio = sum(notas) / len(notas)
            print(f"{estudiante['nombre']}: Promedio = {promedio:.2f}")
        except (ValueError, KeyError):
            print(f"{estudiante['nombre']}: Error en las notas")
