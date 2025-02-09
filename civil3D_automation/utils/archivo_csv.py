import csv

def leer_csv(file_path):
    """
    Lee un archivo CSV y devuelve los datos como una lista de diccionarios.
    """
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
