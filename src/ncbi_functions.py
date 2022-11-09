"""
NAME

        ncbi_functions

VERSION

        1.0
AUTHOR

        Rogelio Avila

DESCRIPTION

        Funciones de recopilación de información de e-utilities de NCBI

CATEGORY

        Bases de datos

USAGE

        python ncbi_functions.py

ARGUMENTS

        options:
            -h, --help            show this help message and exit
            -i INFORMACION, --informacion INFORMACION
                Organismo y genes para crear el termino escritos con este formato: 'Organismo 1: Gen 1, Gen 2, Gen 3, Gen8; Organismo 2: Gen 5, Gen0...'

SEE ALSO

        None

"""
# ===========================================================================
# =                            Imports
# ===========================================================================
from Bio import Entrez
import argparse
# ===========================================================================
# =                            Arguments
# ===========================================================================
bio_parser = argparse.ArgumentParser(
    description="Script de funciones utiles para búsqueda de datos en NCBI")
# Crear los argumentos que recibirá el programa para funcionar.
bio_parser.add_argument(
    "-i", "--informacion", help="Organismo y genes para crear el termino escritos con este formato: 'Organismo 1: Gen 1, Gen 2, Gen 3, Gen8; Organismo 2: Gen 5, Gen 0...'", required=True)

arguments = bio_parser.parse_args()
# ===========================================================================
# =                            Functions
# ===========================================================================

# Definimos la función con parametros opcionales por si el usuario desea
# cambiar el campo de búsqueda del organismo o de los genes.
# Retorna una lista de términos.


def crear_terminos(informacion, campo_org='[Orgn]', campo_gen='[Gene]'):
    # Creamos una lista vacía donde se almacenarán los términos producidos con la
    # información dada.
    terminos = []

    # Separar la información por organismos
    informacion = informacion.replace(' ', '').split(';')

    # Obtener los elementos de cada organismo.
    for element in informacion:

        # Separamos el organismo de sus genes asociados.
        y = (str(element).split(':'))

        # Agregamos el nombre del organismo al termino.
        termino = f'{y[0]}' + f'{campo_org}' + ' AND' + ' ('

        # Creamos una lista de los genes asociados al organismo.
        for unity in y:
            if (unity != y[0]):
                x = (unity.split(','))

        # Recorremos la lista de los genes asociados y los vamos
        # agregando al término.
        for element in x:

            # Si solo hay un gen la expresión se cierra después de agregarlo.
            if element == x[0] and len(x) == 1:
                termino = (f'{termino}' + element + f'{campo_gen})')

            elif element == x[0]:
                termino = (f'{termino}' + element + f'{campo_gen}')
            elif element != x[-1] and element != x[0]:
                termino += ' OR ' + element + f'{campo_gen}'

            # Cuando lleguemos al último genes se cierra el parentesis
            # de la expresión.
            else:
                termino += ' OR ' + element + f'{campo_gen})'

        # Agregamos el termino final a la lista de terminos generados por
        # la función.
        terminos.append(termino)
    return (terminos)


# Definir la función. Retorna un diccionario con ids de los
# resultados y su base de datos.
def buscar_db(termino):
    # Generamos un diccionario vacío donde se irán agregando
    # las bases de datos y sus ids asociados.
    db_ids = {}

    # Realizamos la busqueda del término y
    # recopilamos los resultados.
    handle = Entrez.egquery(term=termino)
    record = Entrez.read(handle)
    handle.close()

    # Leemos los resultados.
    for row in record["eGQueryResult"]:
        if row["Count"] == '0' or row["Count"] == 'Error':
            continue
        # Si en la base de datos se encontraron resultados
        # buscaremos los ids.
        else:
            data = row["DbName"]
            search = Entrez.esearch(
                db=data, term=termino, retmax=row["Count"])
            results = Entrez.read(search)
            search.close()

            # Una vez que obtenemos los ids en la base datos que dio resultados.
            # Los agregaremos al diccionario vacío asociados con su base de datos.
            db_ids[row["DbName"]] = str(results["IdList"])
    # Retornar el diccionario con las bases de datos y sus ids asociados.
    return (db_ids)


# ===========================================================================
# =                            Main
# ===========================================================================
# Identificarse ante NCBI.
Entrez.email = 'ravila@lcg.unam.mx'

# A partir de la información de búsqueda introducida
# se utiliza la función para crear los términos de cada organismo.
terminos = crear_terminos(arguments.informacion)

# Con un for podemos buscar cada término de la lista
# y obtener los ids de los resultados de cada base
# de datos.
for termino in terminos:
    # Imprimir el nombre del organismo.
    print(termino.split('[')[0])
    # Imprimir los resultados de la función.
    print(buscar_db(termino))
