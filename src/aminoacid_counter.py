"""
NAME

        aminoacid_counter
        
VERSION

        1.0
        
AUTHOR

        Rogelio Lael Avila Silva
        
DESCRIPTION

        Funcion que calcula uno o mas aminoacidos
        en una secuencia dada.
        
CATEGORY

        Aminoacidos
         
USAGE

        import aminoacid_counter
        
ARGUMENTS
        none
        
SEE ALSO
        none        
"""

# Definir la función con nombre y parametros.


def get_aa_percentage(secuence, aminoacids, decimals):
    # Realizamos todos los calculos para obtener el porcentaje.
    length = len(secuence)
    for aminoacid in aminoacids:
        amino_count = secuence.upper().count(aminoacid.upper())
        percentage = round((amino_count / length) * 100, decimals)
        print("El porcentaje del aminoacido " +
              str(aminoacid).upper() + " es: " + str(percentage) + "%")
