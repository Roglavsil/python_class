"""
NAME

    bioclase.py

VERSION

    1.0

AUTHOR

    Rogelio Lael Avila Silva

DESCRIPTION

    Script que contiene clases con metodos y atributos utiles 
    para el manejo de secuencias. 

CATEGORY

    Bio_classes

USAGE

    python bioclase.py

ARGUMENTS

    none

SEE ALSO

"""
# ===========================================================================
# =                            Imports
# ===========================================================================

import re

# ===========================================================================
# =                            Clases
# ===========================================================================

# Definir clase.


class nucleic_acids():

    # Damos atributos.
    sequence = ""
    length = 0
    start_codons = 0
    stop_codons = 0

    # Constructor.
    def __init__(self, sequence, length, start_codons, stop_codons):
        self.sequence = sequence.upper()
        self.length = length
        self.start_codons = start_codons
        self.stop_codons = stop_codons

    # Metodos.
    def base_check(self):
        if re.search("[^ATCGU]", self.sequence):
            error = re.finditer("[^ATCGU]", self.sequence)
            for invalid in error:
                print("Caracter inválido:", invalid.group() +
                      " posición:", invalid.start())

    def length_check(self):
        self.length = len(self.sequence)

# Creamos una clase hija de la anterior.


class DNA(nucleic_acids):

    # Metodos.
    def stop_check(self):
        codons = re.finditer("TAG|TGA|TAA",
                             self.sequence)
        if codons:
            print("Se encontraron codones de paro en las siguientes posiciones:")
            for codon in codons:
                self.stop_codons += 1
                print(codon.span())
        else:
            print("No se encontraron codones de paro.")

    def start_check(self):
        codons = re.finditer("ATG", self.sequence)
        if codons:
            print("Se encontraron codones de inicio en las siguientes posiciones:")
            for codon in codons:
                self.start_codons += 1
                print(codon.span())
        else:
            print("No se encontraron codones de inicio.")

    # Overriding.

    def base_check(self):
        if re.search("[^ATCG]", self.sequence):
            error = re.finditer("[^ATCG]", self.sequence)
            for invalid in error:
                print("Caracter inválido:", invalid.group() +
                      " posición:", invalid.start())

# Clase hija de nucleic_acids.


class RNA(nucleic_acids):
    # Metodos.
    def stop_check(self):
        codons = re.finditer("UAG|UAA|UGA",
                             self.sequence)
        if codons:
            print("Se encontraron codones de paro en las siguientes posiciones:")
            for codon in codons:
                self.stop_codons += 1
                print(codon.span())
        else:
            print("No se encontraron codones de paro.")

    def start_check(self):
        codons = re.finditer("AUG", self.sequence)
        if codons:
            print("Se encontraron codones de inicio en las siguientes posiciones:")
            for codon in codons:
                self.start_codons += 1
                print(codon.span())
        else:
            print("No se encontraron codones de inicio.")

    def base_check(self):
        if re.search("[^ACGU]", self.sequence):
            error = re.finditer("[^ACGU]", self.sequence)
            for invalid in error:
                print("Caracter inválido:", invalid.group() +
                      " posición:", invalid.start())
