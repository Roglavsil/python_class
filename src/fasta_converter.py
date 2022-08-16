"""
NAME

    fasta_converter
        
VERSION

    1.0
        
AUTHOR

    Rogelio Lael Avila Silva
        
DESCRIPTION

    Transforma secuencias de un archivo de prueba a fasta.
       
CATEGORY

    Fasta 
        
USAGE

    python fasta_converter.py
        
ARGUMENTS
      
    none
    
SEE ALSO
    none
"""
import argparse

bio_parser = argparse.ArgumentParser(
    description="Script para convertir un archivo a fasta.")
# Crear los argumentos que recibirá el programa para funcionar.
bio_parser.add_argument(
    "-i", "--input", help="Path al archivo con secuencias", required=True)

arguments = bio_parser.parse_args()

try:
    # Obtener el contenido del archivo.
    in_file = open(arguments.input)
    sequences = in_file.readlines()
    in_file.close()

    # Crear archivo de output.
    out_file = open("./results/dna_output.fasta", "w")

    # Eliminar caracteres no deseados y letras minusculas.
    # Agregar simbolo de encabezado a cada secuencia.
    # Escribir en el archivo.
    for sequence in sequences:
        header = sequence.split("\t")
        seq = sequence.split("\t").replace(
            '-', '').upper().replace('\t', '\n')
        data = ">" + header + "\n" + seq
        out_file.write(data)

    out_file.close()

    # Imprimir ubicacion del output.
    print("results/dna_output.fasta")
except IOError as ex:
    print(
        f"El archivo {ex.filename} no se encuentra en la dirección indicada o no existe.")
