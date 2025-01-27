import csv
from pyautocad import Autocad, APoint

# Rutas a los archivos CSV
csv_file_path = './tareas_AutoCAD/datos.csv'
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

# Conectar con AutoCAD
acad = Autocad(create_if_not_exists=True)

# Agregar puntos y etiquetas usando los datos de los CSV
for row in data_datos:
    x = float(row['x'])
    y = float(row['y'])
    z = float(row['z'])
    descripcion = row['descripcion']

    point = APoint(x, y, z)
    acad.model.AddPoint(point)
    acad.model.AddText(descripcion, point, 2.5)

# (Opcional) Agregar más datos de los otros archivos CSV (por ejemplo, tuberías)
for row in data_tuberias:
    x = float(row['x'])
    y = float(row['y'])
    z = float(row['z'])
    descripcion = row['descripcion']

    point = APoint(x, y, z)
    acad.model.AddPoint(point)
    acad.model.AddText(descripcion, point, 2.5)

# (Opcional) Agregar tuberías con número si lo necesitas
for row in data_tuberias_con_numero:
    x = float(row['x'])
    y = float(row['y'])
    z = float(row['z'])
    numero = row['numero']

    point = APoint(x, y, z)
    acad.model.AddPoint(point)
    acad.model.AddText(f"Tubería {numero}", point, 2.5)

# Agregar etiquetas si lo necesitas
for row in data_etiquetas:
    x = float(row['x'])
    y = float(row['y'])
    z = float(row['z'])
    etiqueta = row['etiqueta']

    point = APoint(x, y, z)
    acad.model.AddText(etiqueta, point, 2.5)