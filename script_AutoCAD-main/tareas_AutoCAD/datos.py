import csv

# Rutas a los archivos CSV
csv_file_path = 'datos.csv'
csv_file_tuberias = './tareas_AutoCAD/tuberias.csv'
csv_tuberias_con_numero = './tareas_AutoCAD/tuberias_con_numero.csv'
csv_etiquetas = './tareas_AutoCAD/etiquetas.csv'

# Función para leer un archivo CSV y retornar los datos
def leer_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Leer todos los archivos CSV
data_datos = leer_csv(csv_file_path)
data_tuberias = leer_csv(csv_file_tuberias)
data_tuberias_con_numero = leer_csv(csv_tuberias_con_numero)
data_etiquetas = leer_csv(csv_etiquetas)

# Imprimir los datos leídos de cada archivo
print("Datos:")
for row in data_datos:
    print(row)

print("\nTuberías:")
for row in data_tuberias:
    print(row)

print("\nTuberías con Número:")
for row in data_tuberias_con_numero:
    print(row)

print("\nEtiquetas:")
for row in data_etiquetas:
    print(row)