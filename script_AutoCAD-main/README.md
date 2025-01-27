
## Leer el archivo CSV:

Utilizar la librería csv de Python para leer el archivo CSV. Este script Imprime por consola la data.

## Usar los datos en AutoCAD:

Usa pyautocad: /teareas_AutoCAD/autoCAD.py para interactuar con AutoCAD desde Python. El script lee los datos del CSV y crea puntos en AutoCAD junto con una descripción en texto.


## Generadores csv_generate

Estos Script estan para generar los datos csv a travez de python.

1-Definir los datos: 
    En este caso, etiquetas.csv y tuberias_con_numero.csv son listas de diccionarios, donde cada diccionario representa una fila en el archivo CSV.

2-Abrir el archivo CSV para escritura:
    Usamos with open para abrir el archivo en modo escritura ('w'). La opción newline='' asegura que no se agreguen líneas en blanco adicionales en algunos sistemas operativos.

3-Crear un DictWriter: 
    Esto nos permite escribir diccionarios en el archivo CSV.
    Escribir los encabezados: Usamos writer.writeheader() para escribir la primera fila con los nombres de las columnas.

4-Escribir las filas de datos:
    Iteramos sobre las listas data_etiquetas y data_tuberias_con_numero y escribimos cada diccionario como una fila en el archivo CSV.

# Dependencias necesarias
-AutoCAD
-Python


# Generador generator_inertface

Genera el script mediante jsons que se alimentan a travez de una interface TK para hacer que la carga de los datos sea dinamica. Esta area aun se encuentra en desarrollo ...






