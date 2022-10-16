"""
NAME

        genL_obtainer
      
VERSION

        1.0
AUTHOR

        Rogelio Ávila
        
DESCRIPTION

        Imprime datos de secuencia de un virus en
        archivo de ejemplo con formato genbank.
       
CATEGORY

        Anotaciones.
        
USAGE

        python genL_obtainer.py
        
ARGUMENTS
        
        None

SEE ALSO

        anotation_collector

"""
# ===========================================================================
# =                            Imports
# ===========================================================================
from Bio import SeqIO
import argparse

# ===========================================================================
# =                            Main
# ===========================================================================

# Obtenemos los datos de cada organismo con un ciclo for.
for genb in SeqIO.parse('data/virus.gb', 'genbank'):
    # Nos apoyamos con otro ciclo for para obtener solo los tipo gen entre los features.
    for feature in genb.features:
        if (feature.type == 'gene'):
            # Vemos si el gene es L.
            if (feature.qualifiers['gene'] == ['L']):
                # Usamos la localización del inicio y final del gen L para obtener su secuencia.
                print(f'\nSecuencia:\n',
                      genb.seq[feature.location.start:feature.location.end])
                # Obtenemos el transcrito.
                print(
                    f'\nTranscrito:\n', genb.seq[feature.location.start:feature.location.end].transcribe())
                # Obtenemos los aminoácidos.
                print(
                    f'\nProteína:\n', genb.seq[feature.location.start:feature.location.end].translate())
