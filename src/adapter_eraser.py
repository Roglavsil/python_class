"""
NAME

        adapter_eraser
        
VERSION

        1.0
        
AUTHOR

        Rogelio Lael Avila Silva
        
DESCRIPTION

        Elimina los adaptadores de secuencias
        en un archivo de practica.
        
CATEGORY

        Modificacion secuencia DNA.
         
USAGE
        python adapter_eraser.py
        
ARGUMENTS
        none
        
SEE ALSO
        none        
"""
import os
import argparse

bio_parser = argparse.ArgumentParser(
    description="Script para borrar los adaptadores de una secuencia.")
# Crear los argumentos que recibirá el programa para funcionar.
bio_parser.add_argument(
    "-i", "--input", help="Path al archivo con secuencias", required=True)

arguments = bio_parser.parse_args()


try:
    # Leer el archivo por líneas y guardarlo.
    archivo = open(arguments.input)
    secuencias = archivo.readlines()
    archivo.close()

    # Creación y escritura del archivo resultado del script.
    archivo = open("./results/output_sequences.txt", "w")

    # Eliminación de los adaptadores.
    # Escribir las secuencias en el archivo output.
    for adaptadores in secuencias:
        seq = adaptadores[14:-1]
        archivo.write(f"{seq}\n")
    archivo.close()

    # Se imprime la ubicación del output.
    print("results/output_sequences.txt")
except IOError as ex:
    print(
        f"El archivo {ex.filename} no se encuentra en la dirección indicada o no existe.")
