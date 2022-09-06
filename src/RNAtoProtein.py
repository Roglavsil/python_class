"""
NAME

    RNAtoProtein.py

VERSION

    1.0

AUTHOR

    Rogelio Lael Avila Silva

DESCRIPTION

    Script para traducir una secuencia de RNA.

CATEGORY

    RNA

USAGE

    python RNAtoProtein.py

ARGUMENTS

      -h, --help            show this help message and exit
      -f, --file            Path al archivo con la secuencia

SEE ALSOg

"""
# ===========================================================================
# =                            dictionaries
# ===========================================================================

gencode = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T',
    'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
    'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R',
    'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H',
    'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
    'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
    'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
    'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S',
    'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L',
    'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '', 'TAG': '',
    'TGC': 'C', 'TGT': 'C', 'TGA': '', 'TGG': 'W'}

# ===========================================================================
# =                            Imports
# ===========================================================================

import re
import argparse

# ===========================================================================
# =                            Arguments
# ===========================================================================

rna_parser = argparse.ArgumentParser(
    description='Script de traducción de RNA')

rna_parser.add_argument(
    "-f", "--file", help="Path al archivo con la secuencia", required=True)

arguments = rna_parser.parse_args()

# ===========================================================================
# =                            Functions
# ===========================================================================


def RNA_check(string):
    if re.search("[^ATUCG]", string):
        global error
        error = re.finditer("[^ATUCG]", string, re.IGNORECASE)
        raise ValueError()


def codon_spliter(string):
    return (re.findall("...", string, re.IGNORECASE))

# ===========================================================================
# =                            Main
# ===========================================================================


# Leer el archivo y guardar su contenido en una variable.
try:
    with open(arguments.file) as f:
        RNAseq = f.read()
        RNAseq = str(RNAseq.replace("\n", "").replace("U", "T")).upper()
# Comprobar que el archivo solo contenga bases de RNA.
    RNA_check(RNAseq)
    # Obtener la secuencia en codones.
    Aminoseq = codon_spliter(RNAseq)

    # Traducir los codones a aminoacidos.
    aminoacids = ""
    for codon in Aminoseq:
        aminoacids += gencode.get(codon)

    # Imprimir la secuencia de aminoacidos.
    print("La secuencia de aminoacidos es:")
    print(aminoacids)

except IOError as ex:
    print(
        f"El archivo {ex.filename} no se encuentra en la dirección indicada o no existe.")
except ValueError:
    for invalid in error:
        print("Caracter inválido:", invalid.group() +
              " posición:", invalid.start())
