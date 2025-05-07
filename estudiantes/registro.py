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
                        'nombre': fila['Nombre']
                    })
            except (ValueError, KeyError):
                continue  
            
    return estudiantes_validos

