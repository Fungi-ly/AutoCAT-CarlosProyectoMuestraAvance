import csv
from pyautocad import Autocad, APoint

# Rutas a los archivos CSV
csv_file_path = 'datos.csv'
csv_file_tuberias = './tareas_AutoCAD/tuberias.csv'
csv_tuberias_con_numero = './tareas_AutoCAD/tuberias_con_numero.csv'
csv_etiquetas = './tareas_AutoCAD/etiquetas.csv'

# Función para leer un archivo CSV y retornar los datos
def leer_csv(file_path):
    data = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo {file_path}: {e}")
    return data

# Leer todos los archivos CSV
data_datos = leer_csv(csv_file_path)
data_tuberias = leer_csv(csv_file_tuberias)
data_tuberias_con_numero = leer_csv(csv_tuberias_con_numero)
data_etiquetas = leer_csv(csv_etiquetas)

# Conectar con AutoCAD
try:
    acad = Autocad(create_if_not_exists=True)
except Exception as e:
    print(f"Error al conectar con AutoCAD: {e}")
    acad = None

if acad:
 
    for row in data_datos:
        try:
            x = float(row['x'])
            y = float(row['y'])
            z = float(row['z'])
            descripcion = row['descripcion']

            point = APoint(x, y, z)
            acad.model.AddPoint(point)
            acad.model.AddText(descripcion, point, 2.5)
        except KeyError as e:
            print(f"Error: Falta la clave {e} en los datos.")
        except ValueError:
            print("Error: No se pudo convertir los valores a float.")
        except Exception as e:
            print(f"Error al agregar punto y texto: {e}")

    for row in data_tuberias:
        try:
            x = float(row['x'])
            y = float(row['y'])
            z = float(row['z'])
            descripcion = row['descripcion']

            point = APoint(x, y, z)
            acad.model.AddPoint(point)
            acad.model.AddText(descripcion, point, 2.5)
        except KeyError as e:
            print(f"Error: Falta la clave {e} en los datos.")
        except ValueError:
            print("Error: No se pudo convertir los valores a float.")
        except Exception as e:
            print(f"Error al agregar punto y texto: {e}")

    for row in data_tuberias_con_numero:
        try:
            x = float(row['x'])
            y = float(row['y'])
            z = float(row['z'])
            numero = row['numero']

            point = APoint(x, y, z)
            acad.model.AddPoint(point)
            acad.model.AddText(f"Tubería {numero}", point, 2.5)
        except KeyError as e:
            print(f"Error: Falta la clave {e} en los datos.")
        except ValueError:
            print("Error: No se pudo convertir los valores a float.")
        except Exception as e:
            print(f"Error al agregar punto y texto: {e}")

    for row in data_etiquetas:
        try:
            x = float(row['x'])
            y = float(row['y'])
            z = float(row['z'])
            etiqueta = row['etiqueta']

            point = APoint(x, y, z)
            acad.model.AddText(etiqueta, point, 2.5)
        except KeyError as e:
            print(f"Error: Falta la clave {e} en los datos.")
        except ValueError:
            print("Error: No se pudo convertir los valores a float.")
        except Exception as e:
            print(f"Error al agregar texto: {e}")