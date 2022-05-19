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
    
        secuencia   Secuencia de aminoacidos a leer.
        aminoacido  Aminoacido a calcular su porcentaje.

    options:

        -h, --help  show this help message and exit

SEE ALSO

        None

"""
import argparse

aa_parser= argparse.ArgumentParser(description="Script para calcular el porcentaje de un aminoácido en una secuencia.")
# Crear los argumentos que recibirá el programa para funcionar.
aa_parser.add_argument("secuencia", help="Secuencia de aminoacidos a leer.")
aa_parser.add_argument("aminoacido", help="Aminoacido a calcular su porcentaje.")

arguments= aa_parser.parse_args()


try:

    # Comprobar que el segundo argumento sea un aminoácido.
    if arguments.aminoacido.upper() not in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
                    'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']:
                    raise ValueError("El segundo argumento no es un aminoácido.")
                    
    # Comprobar que la secuencia contenga solo aminoácidos.
    for aminoacido in arguments.secuencia:
        if aminoacido.upper() not in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
                    'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']:
                    raise IOError("La secuencia introducida no contiene solo aminoacidos.")
                    
    # Definir la función con nombre y parametros.                
    def get_aa_percentage(sec, aminoacid):
        # Realizamos todos los calculos para obtener el porcentaje.
        length = len(sec)
        amino_count = sec.upper().count(aminoacid.upper())
        percentage = (amino_count/length)*100
        return round(percentage, 2)

    # Imprimir el resultado de la función.
    print("El porcentaje de este aminoacido dentro de la secuencia es:")
    print(get_aa_percentage(arguments.secuencia, arguments.aminoacido),"%")

# Se agregan errores por si el usuario se equivoca con los argumentos.
except ValueError:
    print("El segundo argumento no es un aminoácido.")
except IOError:
    print("La secuencia introducida no contiene solo aminoacidos.")
