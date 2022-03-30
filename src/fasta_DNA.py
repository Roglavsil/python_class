"""
NAME
        fasta_DNA
      
VERSION
        1.0
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
#Se solicita al usuario escribir el archivo y su direccion.
print("Escriba la direccion de su archivo y el nombre de este: ")
nom_archivo=input()
#Se utiliza el comando para que se abra el archivo y se guarde en la variable.
archivo=open(nom_archivo)
#Al leer el archivo podemos guardar el contenido en una variable
contenido_archivo=archivo.read()
#Se usa el metodo para remvover saltos de linea y se almacenan las letras de la secuencia en una variable
DNAseq=contenido_archivo.rstrip("\n")
#Creamos un archivo y lo abrimos que se almacenara en la carpeta results.
archivo= open("../results/dna.fasta","w")
#Se deposita la secuencia y se pone un encabezado al inicio.
archivo.write(f">Seq_name\n{DNAseq}")
#Se cierra el archivo.
archivo.close()