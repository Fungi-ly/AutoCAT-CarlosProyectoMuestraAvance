import csv

data_tuberias_con_numero = [
    {'x': 10.0, 'y': 20.0, 'z': 30.0, 'numero': 1},
    {'x': 15.0, 'y': 25.0, 'z': 35.0, 'numero': 2},
    {'x': 20.0, 'y': 30.0, 'z': 40.0, 'numero': 3}
]

csv_file_tuberias_con_numero = './tareas_AutoCAD/tuberias_con_numero.csv'

with open(csv_file_tuberias_con_numero, mode='w', newline='') as file:
    fieldnames = ['x', 'y', 'z', 'numero']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in data_tuberias_con_numero:
        writer.writerow(row)

print(f"Archivo {csv_file_tuberias_con_numero} creado con éxito.")