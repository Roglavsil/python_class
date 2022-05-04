"""
NAME

        fasta_DNA
      
VERSION

        1.1
        
AUTHOR

        Rogelio Avila
        
DESCRIPTION

        Se toma como input un archivo que contiene una secuencia de DNA 
        y se transforma a un archivo fasta.
        
CATEGORY

        Fasta.   
            
USAGE

        python fasta_DNA.py

ARGUMENTS
        
        none
        
SEE ALSO
  
        none
"""
#Obtenemos el archivo que se transformara y guardamos su contenido en una variable.
try:
        nom_archivo=input("Escriba la direccion de su archivo y el nombre de este:\n")
        archivo=open(nom_archivo)
        contenido_archivo=archivo.read()

        #Removemos los saltos de linea de las secuencias.
        DNAseq=contenido_archivo.rstrip("\n")
        
        #Comprobar que solo haya nucleotidos en la cadena.
        for base in DNAseq:
                if base not in ["A", "C", "G", "T"]:
                        raise ValueError()
        
        #Crear el fasta.
        archivo= open("../results/dna.fasta","w")
        archivo.write(f">Seq_name\n{DNAseq}")
        archivo.close()
except IOError as ex:
        print(f"El archivo {ex.filename} no se encuentra en la dirección indicada o no existe.")
except ValueError:
    print("La secuencia del archivo no contiene solamente bases.")