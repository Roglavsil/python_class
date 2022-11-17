"""
NAME

        ncbi_functions2

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

        ncbi_functions.py

"""
# ===========================================================================
# =                            Imports
# ===========================================================================

from io import StringIO
from Bio import Entrez, Medline
import argparse
from ncbi_functions import crear_terminos, buscar_db

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
# Funciona que toma un diccionario con ids asociados a
# a bases de dataos y retorna ids de articulos que citen
# a los ids de bases de datos de articulos


def get_titles(db_dict):
    # Diccionario que almacena un diccionario de ids y títulos junto a su db.
    final_ids = {}
    dict_ids = {}  # Diccionario de ids y títulos
    # Discriminamos entre las bases de datos aquellas que contengan artículos.
    for key in db_dict.keys():
        handle = Entrez.einfo(db=key)
        record = Entrez.read(handle)
        handle.close()
        # Si la base de datos tiene características de artículos entonces almacenamos
        # sus IDs junto con los títulos en el diccionario.
        if (record["DbInfo"]['FieldList'][1]['Description'] ==
                'Unique number assigned to publication'):
            results = Entrez.efetch(
                db=key, id=db_dict[key], rettype='docsum', retmode='xml')
            recorder = Entrez.read(results)
            results.close()
            for id in recorder:
                dict_ids[id['Id']] = id['Title']
        # Finalmente vamos almacenando ids y sus titulos asociados a su base de datos
        # en el diccionario final.
        final_ids[key] = dict_ids
    # Se devuelve un diccionario.
    return (final_ids)


# Función que se utiliza para obtener los ids,
# abstract y títulos de los artículos que citan
# a los artículos introducido.
def get_cited(ids_dict):
    # Generamos las listas y diccionarios que almacenaran
    # ids, titulos y abstracts.
    cite_ids = []
    cite_titles_abs = {}
    id_cites = {}

    for db in ids_dict.keys():
        # De cada id obtendremos los ids de artículos que lo citan.
        for id in ids_dict[db].keys():
            handle = Entrez.elink(dbfrom=db, db=db, id=id)
            results = Entrez.read(handle)
            handle.close()
            for cite in results[0]['LinkSetDb'][0]['Link']:
                # Si no hay artículos que lo citen pasaremos al siguiente id.
                if cite_ids.append(cite.get('Id')) == None:
                    continue
                else:
                    # Agregamos los ids de los artículos que lo citan.
                    cite_ids = cite_ids.append(cite.get('Id'))

            # Obtenemos los títulos y abstracts de los artículos.
            for cite_id in cite_ids:
                data_id = Entrez.efetch(
                    db=db, id=cite_id, rettype='medline', retmode='text')
                # Transformar el output de la búsqueda en un formato manejable.
                abstract = data_id.read()
                data_id.close()
                abstract = StringIO(abstract)
                abstract = Medline.read(abstract)
                # Si el artículo contiene un abstract lo almacenamos asociado al
                # título.
                if 'AB' in abstract:
                    cite_titles_abs[abstract['TI']] = abstract['AB']
                    continue
                # En caso contrario se deja vacío.
                cite_titles_abs[abstract['TI']] = None
        # Asociamos la lista de titulos y abstracts con el id
        # del artículo al que citan.
        id_cites[id] = cite_titles_abs
    # Retornamos el diccionario de titulos y abstracts con id del artículo
    # al que citan.
    return (id_cites)

    # ===========================================================================
    # =                            Main
    # ===========================================================================
    # Identificarse ante NCBI.
Entrez.email = 'ravila@lcg.unam.mx'

# A partir de la información de búsqueda introducida
# se utiliza la función para crear los términos de cada organismo.
terminos = crear_terminos(arguments.informacion)

for termino in terminos:

    # Obtener los ids de los resultados de cada base de datos.
    # Imprimir los resultados de la función.
    db_dict = buscar_db(termino)

    # Obtener ids de los resultados de bases de datos que contengan
    # articulos y sus respectivos títulos en un diccionario y
    art_ids = get_titles(db_dict)

    # Mostrar el nombre del artículo del que se obtuvieron las citas.
    for db in art_ids.keys():
        for id in art_ids[db]:
            print("Artículo: " + art_ids[db][id])
    # Obtener los artículos que lo citan con título y abstracts.
    cited_by = get_cited(art_ids)

    # Impriremos los títulos y abstracts que citan al artículo en cuestión.
    for key in cited_by.keys():
        for title in cited_by[key]:
            print("Título: " + title)
            # Si el título no tiene un abstract se itera al siguiente título.
            if cited_by[key][title] == None:
                continue
            # Si el título tiene un abstract asociado se imprime.
            else:
                print("Abstract: " + cited_by[key][title] + "\n\n")
