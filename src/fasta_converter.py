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

    python fasta_converter.py
        
ARGUMENTS
        none
SEE ALSO
        none
"""
# Obtener el contenido del archivo.
in_file = open("../data/dna_sequences.txt")
sequences = in_file.readlines()
in_file.close()

#Crear archivo de output.
out_file = open("../results/dna_output.fasta", "w")

# Eliminar caracteres no deseados y letras minusculas.
# Agregar simbolo de encabezado a cada secuencia.
# Escribir en el archivo.
for sequence in sequences:
    header = sequence.split("   ")[0]
    seq = sequence.split("   ")[1].replace('-', '').upper().replace('\t', '\n')
    data = ">" + header + "\n" + seq
    out_file.write(data)
    
out_file.close()

#Imprimir ubicacion del output.
print("results/dna_output.fasta")
        
