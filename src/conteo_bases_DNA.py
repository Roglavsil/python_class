"""
NAME

    Conteo_bases_DNA
      
VERSION
        
    1.1
    
AUTHOR

    Rogelio Lael Avila Silva
        
DESCRIPTION

    Se toma como input una secuencia de DNA introudcida por el usuario y se hace un conteo 
    de la aparición de cada base nitrogenada.
       
CATEGORY

    Metodo
       
USAGE
     python Conteo_bases_DNA.py
     
ARGUMENTS

SEE ALSO
       
"""

try:
    
# Obtener la secuencia de ADN del usuario
    dna= input("Introduzca una secuencia de DNA:\n").upper()
    for base in dna:
        #Comprobar que solo haya nucleotidos en la cadena.
        if base not in ["A", "C", "G", "T"]:
            raise ValueError()
    
# Realizar conteo de cada base
    freq_A = dna.count('A')
    freq_C = dna.count('C')
    freq_G = dna.count('G')
    freq_T = dna.count('T')

# Imprimir el resultado
    print(f"Frecuencia de nucleotidos A:{freq_A} C:{freq_C} G:{freq_G} T:{freq_T}")
except ValueError:
    print("La secuencia no contiene solamente bases.")