"""
NAME

        function_aa
      
VERSION

        1.0
AUTHOR

        Rogelio Avila
        
DESCRIPTION

        Se toma como input una secuencia de aminoacidos dada por el usuario y un aminoacido cuyo
        porcentaje dentro de esa secuencia es retornado al usuario.
       
CATEGORY

        Aminoacidos.
        
USAGE

        python function_aa.py
        
ARGUMENTS
        
        positional arguments:
        path        Path al archivo con secuencias

        options:

        -h, --help  show this help message and exit

SEE ALSO

        None

"""
# Definir la función con nombre y parametros.
def get_aa_percentage(sec, aminoacid, decimals=0):
    # Realizamos todos los calculos para obtener el porcentaje.
    length = len(sec)
    amino_count = sec.upper().count(aminoacid.upper())
    percentage = (amino_count/length)*100
    return round(percentage, decimals)

# Pruebas para analizar la robustez de la funcion.
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert get_aa_percentage("msrslllrfllfllllpplp", "L") == 50
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0