"""
NAME

        orf_searcher
      
VERSION

        1.0
AUTHOR

        Rogelio Avila
        
DESCRIPTION

        Contiene una función que toma una cadena de DNA y busca en ella el orf de mayor tamaño tanto en la hebra forward como en la reverse.
       
CATEGORY

        Secuencia.
        
USAGE

        python orf_searcher.py
        
ARGUMENTS
        
        None

SEE ALSO

        None

"""
# ===========================================================================
# =                            Imports
# ===========================================================================
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import nt_search
import argparse
# ===========================================================================
# =                            Function
# ===========================================================================

bio_parser = argparse.ArgumentParser(
    description="Script para buscar orf más largo en archivo fasta")
# Crear los argumentos que recibirá el programa para funcionar.
bio_parser.add_argument(
    "-i", "--input", help="Path al archivo fasta", required=True)

arguments = bio_parser.parse_args()


def orf_searcher(Secuencia):
    # Guardar la secuencia
    seq = Seq(Secuencia)
    # Encontrar las posiciones de los codones de inicio
    start_codons = Seq('ATG')
    posiciones = nt_search(str(seq), start_codons)
    complement_pos = nt_search(str(seq.reverse_complement()), start_codons)
    # Creamos una primera cadena para comparar con las demás después con un for.
    longest_orf = seq[posiciones[1]:].translate(to_stop=True)
    orf = ''
    # Comparar los orfs tanto del forward como reverse y elegir el de mayor tamaño.
    for i in range(len(posiciones)):
        if i >= 2:
            orf = seq[posiciones[i]:].translate(to_stop=True)
        if len(longest_orf) < len(orf):
            longest_orf = orf
    for i in range(len(complement_pos)):
        if i >= 1:
            orf = ((seq.reverse_complement()[
                   complement_pos[i]:]).translate(to_stop=True))
        if len(longest_orf) < len(orf):
            longest_orf = orf
    return (longest_orf)


# ===========================================================================
# =                            Main
# ===========================================================================
for sec in SeqIO.parse(arguments.input, 'fasta'):
    print(f'>{sec.id}')
    print(orf_searcher(sec.seq))
