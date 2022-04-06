"""
NAME
        porcentaje_AT_GC
      
VERSION
        1.1
AUTHOR
        Rogelio Avila
        
DESCRIPTION
       Se toma como input un archivo que contiene una secuencia de DNA introducido por el usuario y se hace un conteo de la aparición de cada base nitrogenada para despues calcular el porcentaje de AT y GC.
       
CATEGORY
        Lector de archivos       
USAGE
        Obtener el porcentaje de GC y AT de un archivo .txt.

ARGUMENTS

SEE ALSO       
"""

#Abrimos el archivo y copiamos su contenido a una variable.
print("Escriba la direccion de su archivo y el nombre de este: ")
nom_archivo=input()
archivo=open(nom_archivo)
contenido_archivo=archivo.read()
print(f"La secuencia del archivo es: {contenido_archivo}\n")

#Nos deshacemos de los saltos de linea y obtenemos la longitud de la secuencia.
DNAseq = contenido_archivo.rstrip('\n')
Totalnucleotidos= len(DNAseq)

#Calculamos el porcentaje de AT y GC y se imprime.
DNA_AT= {((DNAseq.count("T")+DNAseq.count("A"))/Totalnucleotidos)*100}
DNA_GC= {((DNAseq.count("G")+DNAseq.count("C"))/Totalnucleotidos)*100}
print(f"Porcentaje de AT: {DNA_AT}%\nPorcentaje de GC: {DNA_GC}% ")