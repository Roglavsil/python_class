"""
NAME

        porcentaje_AT_GC
      
VERSION

        1.1
AUTHOR

        Rogelio Avila
        
DESCRIPTION

       Se toma como input un archivo que contiene una secuencia de DNA introducido por el usuario y 
       se hace un conteo de la aparición de cada base nitrogenada para despues calcular el porcentaje de AT y GC.
       
CATEGORY

        Lector de archivos
        
USAGE

        python porcentaje_AT_GC.py
        
ARGUMENTS
SEE ALSO       
"""
try:
        #Abrir el archivo y copiar su contenido a una variable.
        nom_archivo=input("Escriba la direccion de su archivo y el nombre de este:\n")
        archivo=open(nom_archivo)
        contenido_archivo=archivo.read()
        archivo.close()

        # Imprimir los datos introducidos
        print(f"La secuencia del archivo es: {contenido_archivo}\n")

        # Quitar saltos de linea obtenemos la longitud de la secuencia
        DNAseq = contenido_archivo.rstrip('\n')
        
        #Comprobar que solo haya nucleotidos en la cadena.
        for base in DNAseq:
                if base not in ["A", "C", "G", "T"]:
                        raise ValueError()
        Totalnucleotidos= len(DNAseq)

        #Calcular el porcentaje de AT y GC
        DNA_AT= {((DNAseq.count("T") + DNAseq.count("A")) / Totalnucleotidos) * 100}
        DNA_GC= {((DNAseq.count("G") + DNAseq.count("C")) / Totalnucleotidos) * 100}

        # Imprimir el resultado
        print(f"Porcentaje de AT: {DNA_AT}%\nPorcentaje de GC: {DNA_GC}% ")
except IOError as ex:
        print(f"El archivo {ex.filename} no se encuentra en la dirección indicada o no existe.")
except ValueError:
    print("La secuencia no contiene solamente bases.")