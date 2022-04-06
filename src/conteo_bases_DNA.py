"""
NAME
        Conteo_bases_DNA
      
VERSION
        1.1
AUTHOR
        Rogelio Lael Avila Silva
        
DESCRIPTION
       Se toma como input una secuencia de DNA introudcida por el usuario y se hace un conteo de la aparición de cada base nitrogenada.
CATEGORY
        Metodo
       
USAGE
        Conteo del numero de A, T, C y G en una secuencia de DNA
ARGUMENTS

SEE ALSO
       
"""

"""
Primero obtenemos una secuencia de DNA proporcionado por el usuario
y despues usamos los metodos de python para cadenas para obtener el
numero de bases.
"""
print("Introduzca una secuencia de DNA: ")
dna= input()
print(f"Frecuencia de nucleotidos A:{dna.count('A')} C:{dna.count('C')} G:{dna.count('G')} T:{dna.count('T')}")