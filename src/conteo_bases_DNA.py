"""
NAME
        Conteo_bases_DNA
      
VERSION
        1.0
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
#Se le solicita al usuario introducir una secuencia con un mensaje simpatico.
print("Introduzca una secuencia de DNA: ")
#Comando para solicitar la escritura de una secuencia de DNA por medio del teclado.
dna= input()
#Se imprime la frecuencia de cada uno de los nucleotidos que se obtiene por medio de metodos.
print(f"Frecuencia de nucleotidos A:{dna.count('A')} C:{dna.count('C')} G:{dna.count('G')} T:{dna.count('T')}")