"""
NAME

        numpy.py

VERSION

        1.0
AUTHOR

        Rogelio Avila

DESCRIPTION

        Ejercicios de la calse numpy.py

CATEGORY

        Ejercicios

USAGE

        python numpy.py

ARGUMENTS

        None
        
SEE ALSO

        None

"""
# ===========================================================================
# =                            Imports
# ===========================================================================
import numpy as np

# ===========================================================================
# =                            Ejercicio 1
# ===========================================================================

# Crear los arrays con los datos de los genes
genes_g_mL = np.genfromtxt(
    r'C:\Users\Roger\OneDrive\Documentos\Universidad\UNAM\LCG\Académico\Python\python_class\docs\prod_gml.csv', delimiter=',')
costos = np.genfromtxt(
    r'C:\Users\Roger\OneDrive\Documentos\Universidad\UNAM\LCG\Académico\Python\python_class\docs\ind_cost.csv', delimiter=', ')

# Hacer la conversión correspondiente
productos_gL = genes_g_mL * 1000


# Transformar los costos para cada temperatura.
costos30C = costos * 1.75
costos35C = costos * 0.8


# ===========================================================================
# =                            Ejercicio 2
# ===========================================================================
# Obtener el costo de cada condición
costos30C = costos30C / productos_gL[:, 0]
costos35C = costos35C / productos_gL[:, 1]
print(costos30C, costos35C)

# ===========================================================================
# =                            Ejercicio 3
# ===========================================================================
# Genes que utilizaremos para imprimir los más baratos en cada condición
genes = np.array([1, 2, 3, 4])


# Calcular la diferencia de costos de cada gen
difcosto = costos30C - costos35C

# Obtenemos los genes que son más baratos en 30 grados.
print(F'Genes de menor costo a 30 grados: {genes[difcosto < 0]}')
