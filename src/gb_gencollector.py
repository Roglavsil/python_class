"""
NAME

        gb_gencollector
      
VERSION

        1.0
AUTHOR

        Rogelio Avila
        
DESCRIPTION

        Imprime datos de genes en un 
        archivo con formato GENBANK.
       
CATEGORY

        Anotaciones.
        
USAGE

        python gb_gencollector.py
        
ARGUMENTS
        
        options:
            -h, --help            show this help message and exit
            -i INPUT, --input INPUT
                        Path al archivo gb
            -g GENES [GENES ...], --genes GENES [GENES ...]
                        Lista con los nombres de los genes a buscar

SEE ALSO

        None

"""
# ===========================================================================
# =                            Imports
# ===========================================================================
from typing import List
from Bio import SeqIO
import argparse

# ===========================================================================
# =                            Arguments
# ===========================================================================
bio_parser = argparse.ArgumentParser(
    description="Script para buscar datos de genes en un archivo de genbank")
# Crear los argumentos que recibirá el programa para funcionar.
bio_parser.add_argument(
    "-i", "--input", help="Path al archivo gb", required=True)

bio_parser.add_argument(
    "-g", "--genes", help="Lista con los nombres de los genes a buscar", nargs='+', required=True)
arguments = bio_parser.parse_args()

# ===========================================================================
# =                            Main
# ===========================================================================

# Se declara la función.


def resumen(path, genes):
    # Obtenemos país, organismo y fecha del archivo.
    for genb in SeqIO.parse(path, 'genbank'):
        print("Organismo:", genb.annotations['organism'])
        print("País:\t", genb.features[0].qualifiers['country'])
        print("Fecha:\t", genb.annotations['date'])
        # En caso de haber un número de aislado, lo imprimimos.
        if ('isolate' in genb.features[0].qualifiers):
            print("Aislado:", genb.features[0].qualifiers['isolate'])

    # Contador para imprimir el número del gen dentro de la función.
    i = 0
    # Obtenemos los datos de cada organismo con un ciclo for.
    for genb in SeqIO.parse('data/virus.gb', 'genbank'):
        # Nos apoyamos con otro ciclo for para obtener solo los tipo gen entre los features.
        for feature in genb.features:
            if (feature.type == 'gene'):
                # Comprobar que sea uno de los genes deseados.
                for gen in genes:
                    if (feature.qualifiers['gene'] == [f'{gen}']):
                        i += 1
                        print(f"\nGen_{i}:\t", gen)
                        # Usamos la localización del inicio y sumamos 15 para obtener los primeros
                        # quince nucleotidos del gen.
                        print(f'ADN:\t',
                              genb.seq[feature.location.start:(feature.location.start + 15)])
                        # Obtenemos el transcrito.
                        print(
                            f'ARN:\t', genb.seq[feature.location.start:(feature.location.start + 15)].transcribe())
                        # Obtenemos los aminoácidos.
                        print(
                            f'Proteína:', genb.seq[feature.location.start:(feature.location.start + 15)].translate())


# Se utiliza la función previamente hecha con los argumentos del script.
gengb_collector(arguments.input, arguments.genes)
