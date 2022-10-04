"""
NAME

        fasta_codons

VERSION

        1.0
AUTHOR

        Rogelio Avila

DESCRIPTION

        Contiene una función que toma una cadena de DNA y busca en ella el orf de mayor tamaño tanto en la hebra forward como en la reverse.

CATEGORY

        Fasta.

USAGE

        python fasta_codons.py

ARGUMENTS

        None

SEE ALSO

        None

"""
# ===========================================================================
# =                            Imports
# ===========================================================================
from Bio import SeqIO
import re
# ===========================================================================
# =                            Main
# ===========================================================================
# Guardamos la dirección del archivo
file = "data/seq.nt.fa"
dict = SeqIO.to_dict(SeqIO.parse(file, 'fasta'))
print(dict)

for sec in dict:
    for i in range(6):
        # Escribimos el id de la secuencia.
        print(f">{sec} frame #{i+1}")
        # Imprimimos los primeros 3 marcos de lectura.
        if i < 3:
            for codon in re.findall(r"(.{3})", str(dict[sec].seq[i::])):
                print(codon, end=' ')
        # Imprimimos los ultimos 3 marcos de lectura
        if i >= 3:
            for codon in re.findall(r"(.{3})", str((((dict[sec].seq).reverse_complement())[i - 3::]))):
                print(codon, end=' ')

        print('\n')
