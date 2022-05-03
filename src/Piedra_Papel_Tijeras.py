"""
NAME
        piedra_papel_tijeras
      
VERSION
        1.1
AUTHOR
        Rogelio Lael Avila Silva
        
DESCRIPTION
       Juego recreativo de piedra, papel o tijera.
CATEGORY
        Recreativo
       
USAGE
        Olvidarse de los problemas
        del día a día.
ARGUMENTS
        none
SEE ALSO
        none
"""
#Importar la libreria necesaria para aleatoriedad.
import random
jugar= "si"

# Definir opciones validas y el usuario selecciona su opción.
print("Bienvenido, por favor introduce tu nombre para empezar a jugar.")
nom_usuario= input()

while jugar == "si":

        nom_usuario= input("Bienvenido, por favor introduce tu nombre para empezar a jugar.\n")
        usuario= input("Elija su opcion: piedra, papel o tijeras\n").lower()

        if usuario not in ["piedra","papel","tijeras"]:
                print("Error! Selecciona una de las opciones disponibles")
                exit()
        
# La computadora elige su opción.
        opcion_cpu= random.randint(1,3)
        if opcion_cpu == 1:
                        computadora= "piedra"
        elif opcion_cpu == 2:
                        computadora= "papel"
        else:
                        computadora= "tijeras"
        
#Mostramos ambas elecciones.
        print("La computadora eligio:", computadora)
        print("Tu eleccion fue:", usuario)

#Definimos todos los casos.
# Igualdad es empate.
        if usuario == computadora:
                print("Empate. No hay un ganador")

#Si el usuario eligio tijera.
# Tijera gana a papel. Usuario gana.
# Tijera pierde contra piedra. Computadora gana.
        if usuario == "tijeras":
                if computadora == "papel":
                        print("Felicidades has ganado", nom_usuario)
                elif computadora == "piedra": 
                        print("Has perdido", nom_usuario)

#Si el usuario eligio papel.
# Papel gana a la piedra. Usuario gana.
# Papel pierde contra tijeras. Computadora gana.
        if usuario == "papel":
                if computadora == "piedra":
                        print("Felicidades has ganado", nom_usuario)
                elif computadora == "tijeras": 
                        print("Has perdido", nom_usuario)

#Si el usuario eligio papel.
# Piedra gana a tijeras. Usuario gana.
# Piedra pierde contra papel. Computadora gana.
        if usuario == "piedra":
                if computadora == "tijeras":
                        print("La buena piedra nada le gana, felicitaciones", nom_usuario)
                elif computadora == "papel": 
                        print("Has perdido", nom_usuario)
        print("¿Desea volver a jugar? (si/no)")
        jugar = input()
print("\n\n¡Gracias por jugar, vuelve pronto!\n\n")
