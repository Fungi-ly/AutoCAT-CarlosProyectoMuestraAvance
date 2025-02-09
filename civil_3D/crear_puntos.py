import csv
from pyautocad import Autocad, APoint

coordenadas_csv = 'civil_3D/coordenadas.csv'
tuberias_csv = 'civil_3D/tuberias.csv'

def leer_csv(file_path):
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo {file_path}: {e}")
    return data

datos_coordenadas = leer_csv(coordenadas_csv)
datos_tuberias = leer_csv(tuberias_csv)

try:
    acad = Autocad(create_if_not_exists=True)
except Exception as e:
    print(f"Error al conectar con AutoCAD: {e}")
    acad = None

if acad:
    puntos = {}

    for row in datos_coordenadas:
        try:
            x = float(row['x'])
            y = float(row['y'])
            z = float(row['z'])
            descripcion = row['descripcion']
            id_punto = int(row['id'])

            point = APoint(x, y, z)
            acad.model.AddPoint(point)
            acad.model.AddText(descripcion, point, 2.5)
            puntos[id_punto] = point

        except (KeyError, ValueError) as e:
            print(f"Error con los datos del punto: {e}")
        except Exception as e:
            print(f"Error al agregar punto y texto: {e}")

    # Dibujar tuberías
    for row in datos_tuberias:
        try:
            pk_inicio = int(row['PK_INICIO'])
            pk_fin = int(row['PK_FIN'])
            id_tuberia = row['ID_TUBERIA']

            if pk_inicio in puntos and pk_fin in puntos:
                start_point = puntos[pk_inicio]
                end_point = puntos[pk_fin]

                acad.model.AddLine(start_point, end_point)

                descripcion_tuberia = f"Tubería {id_tuberia}"
                mid_point = APoint(
                    (start_point.x + end_point.x) / 2,
                    (start_point.y + end_point.y) / 2,
                    (start_point.z + end_point.z) / 2
                )
                acad.model.AddText(descripcion_tuberia, mid_point, 3)
            else:
                print(f"Error: Puntos PK_INICIO o PK_FIN no encontrados para la tubería {id_tuberia}")

        except (KeyError, ValueError) as e:
            print(f"Error con los datos de la tubería: {e}")
        except Exception as e:
            print(f"Error al agregar línea para la tubería: {e}")

    print("Proceso completado.")

else:
    print("No se pudo conectar con Civil 3D. El programa terminará.")