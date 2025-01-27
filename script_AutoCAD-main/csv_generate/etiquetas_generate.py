import csv

data_etiquetas = [
    {'x': 10.0, 'y': 20.0, 'z': 30.0, 'etiqueta': 'Etiqueta A'},
    {'x': 15.0, 'y': 25.0, 'z': 35.0, 'etiqueta': 'Etiqueta B'},
    {'x': 20.0, 'y': 30.0, 'z': 40.0, 'etiqueta': 'Etiqueta C'}
]

csv_file_etiquetas = './tareas_AutoCAD/etiquetas.csv'

with open(csv_file_etiquetas, mode='w', newline='') as file:
    fieldnames = ['x', 'y', 'z', 'etiqueta']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in data_etiquetas:
        writer.writerow(row)

print(f"Archivo {csv_file_etiquetas} creado con éxito.")