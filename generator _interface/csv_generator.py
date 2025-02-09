import json
import csv

# Función para leer datos JSON y escribirlos en archivos CSV
def json_a_csv(json_file, csv_file, fieldnames):
    with open(json_file, 'r') as jf:
        data = json.load(jf)
    
    with open(csv_file, 'w', newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Definir rutas de archivos JSON y CSV
json_datos = './tareas_AutoCAD/datos.json'
csv_datos = './tareas_AutoCAD/datos.csv'

json_tuberias = './tareas_AutoCAD/tuberias.json'
csv_tuberias = './tareas_AutoCAD/tuberias.csv'

json_etiquetas = './tareas_AutoCAD/etiquetas.json'
csv_etiquetas = './tareas_AutoCAD/etiquetas.csv'

# Definir los encabezados para los archivos CSV
fieldnames_datos = ['x', 'y', 'z', 'descripcion']
fieldnames_tuberias = ['x', 'y', 'z', 'descripcion']
fieldnames_etiquetas = ['x', 'y', 'z', 'etiqueta']

# Generar archivos CSV desde los JSON
json_a_csv(json_datos, csv_datos, fieldnames_datos)
json_a_csv(json_tuberias, csv_tuberias, fieldnames_tuberias)
json_a_csv(json_etiquetas, csv_etiquetas, fieldnames_etiquetas)

print("Archivos CSV generados con éxito.")