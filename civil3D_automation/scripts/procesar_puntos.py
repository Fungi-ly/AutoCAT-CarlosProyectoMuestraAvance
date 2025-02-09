from pyautocad import APoint

def procesar_puntos(puntos, acad):
    """
    Esta función se encarga de procesar y agregar los puntos a AutoCAD.
    """
    for punto in puntos:
        try:
            x = float(punto['x'])
            y = float(punto['y'])
            z = float(punto['z'])
            descripcion = punto['descripcion']

            point = APoint(x, y, z)
            acad.model.AddPoint(point)
            acad.model.AddText(descripcion, point, 2.5)

        except KeyError as e:
            print(f"Error: Falta la clave {e} en los datos de los puntos.")
        except ValueError:
            print("Error: No se pudo convertir los valores a float.")
        except Exception as e:
            print(f"Error al agregar el punto {descripcion}: {e}")
