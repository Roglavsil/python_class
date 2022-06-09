"""
NAME

        function_aa
      
VERSION

        2.0
AUTHOR

        Rogelio Avila
        
DESCRIPTION

        Se toma como input una secuencia de aminoacidos dada por el usuario y aminoacidos cuyo
        porcentaje dentro de esa secuencia es retornado al usuario.
       
CATEGORY

        Aminoacidos.
        
USAGE

        python function_aa.py
        
ARGUMENTS
        
        options:
        -h, --help            show this help message and exit
        
        -s SECUENCIA, --secuencia 
                                Path archivo con la secuencia de aminoacidos a leer.
                                
        -a AMINOACIDOS, --aminoacidos 
                                Aminoacidos a calcular. Default: aminoacidos hidrofobicos.
                                
        -d DECIMALS, --decimals 
                                Decimales para redondear el porcentaje. Default: 2.

SEE ALSO

        None

"""
# ===========================================================================
# =                            imports
# ===========================================================================

import argparse
import aminoacid_counter

# ===========================================================================
# =                            main
# ===========================================================================


# Se crea un codigo de error para el primer argumento.
class ValueError2(Exception):
    pass


aa_parser = argparse.ArgumentParser(
    description="Script para calcular el porcentaje de un aminoácido en una secuencia.")
# Crear los argumentos que recibirá el programa para funcionar.
aa_parser.add_argument("-s", "--secuencia",
                       help="Path archivo con la secuencia de aminoacidos a leer.", required=True,)

aa_parser.add_argument("-a", "--aminoacidos",
                       help="Aminoacidos a calcular. Default: aminoacidos hidrofobicos.", required=False, type=str, default=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V'])

aa_parser.add_argument("-d", "--decimals",
                       help="Decimales para redondear el porcentaje. Default: 2.", required=False, type=int, default=2)
arguments = aa_parser.parse_args()

try:

    # Abrir el archivo y copiar su contenido a una variable.
    archivo = open(arguments.secuencia)
    contenido_archivo = archivo.read()
    archivo.close()
    secuencia = contenido_archivo.replace("\n", "")
    # Comprobar que el segundo argumento sea un aminoácido.
    for aminoacido in arguments.aminoacidos:
        if aminoacido.upper() not in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
                                      'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']:
            raise ValueError(
                "El segundo argumento no contiene solamente aminoacidos.")

    # Comprobar que la secuencia contenga solo aminoácidos.
    for aminoacido in secuencia:
        if aminoacido.upper() not in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
                                      'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']:
            raise ValueError2(
                "El primer argumento no contiene solamente aminoacidos.")

    # Llamar a la funcion.
    aminoacid_counter.get_aa_percentage(secuence=secuencia,
                                        aminoacids=arguments.aminoacidos, decimals=arguments.decimals)

# Se agregan errores por si el usuario se equivoca con los argumentos.
except ValueError:
    print("Error: ¡Caracter invalido en el segundo argumento!")
except ValueError2:
    print("Error: ¡Caracter invalido en el primer argumento!")
except IOError as ex:
    print(
        f"Error: ¡El archivo {ex.filename} no se encuentra en la dirección indicada o no existe!")
