"""
NAME

        anotation_collector
      
VERSION

        1.0
AUTHOR

        Rogelio Avila
        
DESCRIPTION

        Imprime datos de organismos de un 
        archivo proveniente de GENBANK.
       
CATEGORY

        Anotaciones.
        
USAGE

        python anotation_collector.py
        
ARGUMENTS
        
        options:
        -h, --help            
            show this help message and exit
        -i --input 
            Path al archivo

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
arguments = bio_parser.parse_args()

# Obtenemos los datos de cada organismo con un ciclo for.
for secuencia in SeqIO.parse(arguments.input, 'genbank'):
    print("Organismo: ", secuencia.annotations['organism'])
    print("ID_proteína:", secuencia.features[2].qualifiers['protein_id'])
    print("Fecha de obtención:", secuencia.annotations['date'])
