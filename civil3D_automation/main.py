
from scripts.procesar_puntos import procesar_puntos
from scripts.procesar_tuberias import procesar_tuberias
from utils.archivo_csv import leer_csv

def main():
    ruta_puntos = 'data/puntos.csv'
    ruta_tuberias = 'data/tuberias.csv'

    puntos = leer_csv(ruta_puntos)
    tuberias = leer_csv(ruta_tuberias)

    try:
        acad = Autocad(create_if_not_exists=True)
    except Exception as e:
        print(f"Error al conectar con AutoCAD: {e}")
        return

    procesar_puntos(puntos, acad)

    procesar_tuberias(tuberias, acad)


if __name__ == '__main__':
    main()
