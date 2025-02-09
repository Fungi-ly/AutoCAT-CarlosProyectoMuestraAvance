import csv
from pyautocad import Autocad, APoint, ACircle, AArc

coordenadas_csv = 'civil_3D/coordenadas.csv'
tuberias_csv = 'civil_3D/tuberias_con_curva.csv'

def leer_csv(file_path):
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado: {file_path}")
    except Exception as e:
        print(f"Error al leer archivo: {e}")
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

    for row in datos_tuberias:
        try:
            pk_inicio = int(row['PK_INICIO'])
            pk_fin = int(row['PK_FIN'])
            id_tuberia = row['ID_TUBERIA']
            tipo_curva = row.get('TIPO_CURVA')
            radio_curva = float(row.get('RADIO_CURVA')) if row.get('RADIO_CURVA') else None

            if pk_inicio in puntos and pk_fin in puntos:
                start_point = puntos[pk_inicio]
                end_point = puntos[pk_fin]

                if tipo_curva == "RECTO":
                    acad.model.AddLine(start_point, end_point)
                elif tipo_curva == "CURVO" and radio_curva:
                    mid_point = APoint(
                        (start_point.x + end_point.x) / 2,
                        (start_point.y + end_point.y) / 2,
                        (start_point.z + end_point.z) / 2
                    )

                    dx = end_point.x - start_point.x
                    dy = end_point.y - start_point.y

                    perp_x = -dy
                    perp_y = dx

                    magnitude = (perp_x**2 + perp_y**2)**0.5
                    perp_x /= magnitude
                    perp_y /= magnitude

                    center_x = mid_point.x + perp_x * radio_curva
                    center_y = mid_point.y + perp_y * radio_curva
                    center_z = mid_point.z

                    center_point = APoint(center_x, center_y, center_z)

                    arc = AArc(center_point, radio_curva, start_point, end_point)
                    acad.model.AddArc(arc)

                else:
                    acad.model.AddLine(start_point, end_point)

                descripcion_tuberia = f"Tubería {id_tuberia}"
                mid_point_text = APoint(
                    (start_point.x + end_point.x) / 2,
                    (start_point.y + end_point.y) / 2,
                    (start_point.z + end_point.z) / 2
                )
                acad.model.AddText(descripcion_tuberia, mid_point_text, 3)

            else:
                print(f"Error: Puntos no encontrados para tubería {id_tuberia}")

        except (KeyError, ValueError) as e:
            print(f"Error con los datos de la tubería: {e}")
        except Exception as e:
            print(f"Error al agregar línea/arco para tubería: {e}")

    print("Proceso completado.")

else:
    print("No se pudo conectar con AutoCAD.")