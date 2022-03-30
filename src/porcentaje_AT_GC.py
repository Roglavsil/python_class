"""
NAME
        porcentaje_AT_GC
      
VERSION
        1.0
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
#Se solicita al usuario escribir el archivo y su direccion.
print("Escriba la direccion de su archivo y el nombre de este: ")
nom_archivo=input()
#Se utiliza el comando para que se abra el archivo y se guarde en la variable.
archivo=open(nom_archivo)
#Al leer el archivo podemos guardar el contenido en una variable
contenido_archivo=archivo.read()
#Se imprime la secuencia para asegurarnos que el archvio se leyo correctamente, sin errores.
print(f"La secuencia del archivo es: {contenido_archivo}\n")
#Se usa el metodo para remvover saltos de linea y se almacenan las letras de la secuencia en una variable
DNAseq = contenido_archivo.rstrip("\n")
#Se cuentan las bases y se realizan las operaciones.
Totalnucleotidos= len(DNAseq)
DNA_T= DNAseq.count("T")
DNA_A= DNAseq.count("A")
DNA_G= DNAseq.count("G")
DNA_C= DNAseq.count("C")

#Se imprimen los porcentajes.
print(f"Porcentaje de AT: {((DNA_T+DNA_A)/Totalnucleotidos)*100}%\nPorcentaje de GC: {((DNA_G+DNA_C)/Totalnucleotidos)*100}% ")