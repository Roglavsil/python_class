"""
NAME
        adapter_eraser
        
VERSION
        1.0
AUTHOR
        Rogelio Lael Avila Silva
DESCRIPTION
       Elimina los adaptadores de secuencias en un archivo de practica.
CATEGORY
        Modificacion secuencia DNA. 
USAGE
        Eliminar adaptadores.
ARGUMENTS
        none
SEE ALSO
        none
"""
# Leer el archivo por líneas y guardarlo.
archivo = open("data/4_input_adapters.txt")
secuencias = archivo.readlines()
archivo.close()

# Creación y escritura del archivo resultado del script.
archivo = open("results/output_sequences.txt", "w")

# Eliminación de los adaptadores.
# Escribir las secuencias en el archivo output.
for adaptadores in secuencias:
    archivo.write(f"{adaptadores[14:-1]}\n")
archivo.close()

# Se imprime la ubicación del output.
print("results/output_sequences.txt")
