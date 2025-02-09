
def procesar_tuberias(tuberias, acad):
    """
    Esta función procesa y agrega las tuberías a AutoCAD.
    """
    for tuberia in tuberias:
        try:
            pk_inicio = int(tuberia['PK_INICIO'])
            pk_fin = int(tuberia['PK_FIN'])
            diametro = float(tuberia['DIAMETRO'])
            material = tuberia['MATERIAL']

            # Aquí agregas la lógica para representar la tubería en AutoCAD
            # Si tienes que generar líneas, agregar texto o crear objetos, lo haces aquí.

        except KeyError as e:
            print(f"Error: Falta la clave {e} en los datos de las tuberías.")
        except ValueError:
            print("Error: No se pudo convertir los valores a los tipos correctos.")
        except Exception as e:
            print(f"Error al procesar la tubería: {e}")
