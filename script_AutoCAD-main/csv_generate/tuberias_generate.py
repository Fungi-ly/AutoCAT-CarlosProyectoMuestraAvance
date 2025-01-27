import csv

data_tuberias = [
    {'x': 10.0, 'y': 20.0, 'z': 30.0, 'descripcion': 'Tubería principal'},
    {'x': 15.0, 'y': 25.0, 'z': 35.0, 'descripcion': 'Tubería secundaria'},
    {'x': 20.0, 'y': 30.0, 'z': 40.0, 'descripcion': 'Tubería de distribución'}
]

csv_file_tuberias = './tareas_AutoCAD/tuberias.csv'

with open(csv_file_tuberias, mode='w', newline='') as file:
    fieldnames = ['x', 'y', 'z', 'descripcion']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in data_tuberias:
        writer.writerow(row)

print(f"Archivo {csv_file_tuberias} creado con éxito.")