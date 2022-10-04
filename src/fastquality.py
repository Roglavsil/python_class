"""
NAME

        fastquality
      
VERSION

        1.0
AUTHOR

        Rogelio Avila
        
DESCRIPTION

        Da como output un archivo que contiene las secuencias fastq cuyas bases
        superen un cierto umbral de calidad.
       
CATEGORY

        Fastq.
        
USAGE

        python fastquality.py
        
ARGUMENTS
        
        options:
        -h, --help            
            show this help message and exit
        -i --input 
            Path al archivo fastq
        -u --umbral
            Umbral de calidad a superar para cada base

SEE ALSO

        None

"""
# ===========================================================================
# =                            Imports
# ===========================================================================
from Bio import SeqIO
import argparse

# ===========================================================================
# =                            Function
# ===========================================================================
bio_parser = argparse.ArgumentParser(
    description="Script para buscar orf más largo en archivo fasta")
# Crear los argumentos que recibirá el programa para funcionar.
bio_parser.add_argument(
    "-i", "--input", help="Path al archivo fastq", required=True)
bio_parser.add_argument(
    "-u", "--umbral", help="Umbral de calidad a superar para cada base", required=True)
arguments = bio_parser.parse_args()

# Creamos un archivo de salida
salida = open('results/fastquality_results.txt', 'w')

# Declaramos un contador para el número de secuencias.
i = 0

# Declaramos una variable que indique si una secuencia cumple con el
# umbral.
qual_umbral = True

# Iteramos las calidades y si encontramos una que no supera el umbral
# saltamos a la siguiente secuencia.
sec_fastq = SeqIO.parse(arguments.input, 'fastq')
for seq in sec_fastq:
    qual_umbral = True
    for quality in seq.letter_annotations["phred_quality"]:
        if quality <= int(arguments.umbral):
            qual_umbral = False
    if qual_umbral == True:
        salida.write(f'{seq.id}:\n{str(seq.seq)}\n')
        i += 1
print(f"Número de secuencias que cumplen con el umbral:", i)
salida.close
