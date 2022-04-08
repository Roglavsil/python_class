"""
NAME
        fasta_converter
        
VERSION
        1.0
AUTHOR
        Rogelio Lael Avila Silva
DESCRIPTION
       Transforma secuencias de un archivo de prueba a fasta.
CATEGORY
        Fasta 
USAGE
        Convierte secuencias a fasta.
ARGUMENTS
        none
SEE ALSO
        none
"""
# Obtener el contenido del archivo.
archivo = open("data/dna_sequences.txt")
secuencias = archivo.readlines()
archivo.close()

#Crear archivo de output.
archivo = open("results/dna_output.fasta", "w")

#Eliminar caracteres no deseados y letras minusculas.
#Agregar simbolo de encabezado a cada secuencia.
#Escribir en el archivo.
for secuencia in secuencias:
    i= ">" + secuencia
    archivo.write(i.replace('-', '').upper().replace('\t', '\n'))
archivo.close()

#Imprimir ubicacion del output.
print("results/dna_output.fasta")
        