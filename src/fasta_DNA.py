"""
NAME
        fasta_DNA
      
VERSION
        1.1
AUTHOR
        Rogelio Avila
        
DESCRIPTION
       Se toma como input un archivo que contiene una secuencia de DNA y se transforma a un archivo fasta.
CATEGORY
Creacion de archivos fasta.       
USAGE
Convertir una secuencia de DNA a un archivo fasta.
ARGUMENTS
SEE ALSO       
"""
#Obtenemos el archivo que se transformara y guardamos su contenido en una variable.
print("Escriba la direccion de su archivo y el nombre de este: ")
nom_archivo=input()
archivo=open(nom_archivo)
contenido_archivo=archivo.read()

#Removemos los saltos de linea de las secuencias y creamos el fasta.
DNAseq=contenido_archivo.rstrip("\n")
archivo= open("../results/dna.fasta","w")
archivo.write(f">Seq_name\n{DNAseq}")
archivo.close()