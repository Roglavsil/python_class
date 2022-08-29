"""
NAME

    AT_region_searcher.py

VERSION

    1.0

AUTHOR

    Rogelio Lael Avila Silva

DESCRIPTION

    Script que busca dentro de un archivo con una secuencia de DNA una region rica en AT
    de una longitud dada por el usuario.

CATEGORY

    DNA

USAGE

    python AT_region_searcher.py

ARGUMENTS

      -h, --help            show this help message and exit
      -f, --file            Path al archivo con la secuencia
      -s, --sequence        Tamaño de la region a buscar 

SEE ALSO

"""
# ===========================================================================
# =                            imports
# ===========================================================================

import argparse
import re

# ===========================================================================
# =                            Functions
# ===========================================================================


def ATCG_check(DNAseq):
    if re.search("[^ATCG]", DNAseq):
        global error
        error = re.finditer("[^ATCG]", DNAseq, re.IGNORECASE)
        raise ValueError2()


# ===========================================================================
# =                            main
# ===========================================================================
# Se crea un codigo de error para el segundo argumento.
class ValueError2(Exception):
    pass


# Configurar el parser y añadir los argumentos requeridos.
at_parser = argparse.ArgumentParser(
    description='Script de búsqueda de regiones ricas en AT')

at_parser.add_argument(
    "-f", "--file", help="Path al archivo con la secuencia", required=True)

at_parser.add_argument(
    "-s", "--sequence", help="Tamaño de la region a buscar", required=True)

arguments = at_parser.parse_args()

# Comprobar que el segundo argumento sea un numero entero.
try:
    s = int(arguments.sequence)
    if s < 1:
        raise ValueError()


except ValueError:
    print("El segundo argumento solo puede ser un número natural.")
    exit(0)

# Cerciorarse de que el archivo exista en el path indicado.
try:
    # Abrir el archivo y leer su contenido.
    with open(arguments.file) as f:
        DNAseq = f.read()
        DNAseq = str(DNAseq.replace("\n", ""))

    # Comprobar que la secuencia obtenida solo contenga bases.
    ATCG_check(str(DNAseq))

    # Imprimir la región rica en AT.
    AT_region = re.finditer("[A|T]{" + str(s) + "}", DNAseq, re.IGNORECASE)
    if AT_region:
        for region in AT_region:
            print("La posición de la región es:", region.span())
            print("La región es:", region.group())
    exit(0)


except IOError as ex:
    print(
        f"El archivo {ex.filename} no se encuentra en la dirección indicada o no existe.")
except ValueError2:
    for invalid in error:
        print("Caracter inválido:", invalid.group() +
              " posición:", invalid.start())
