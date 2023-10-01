import random

jugadas = {1: "Piedra", 2: "Papel", 3: "Tijera"}
ronda = 1
tusPtos = 0
rivalPtos = 0

while ronda<6:

    opcion = int(input("\nPiedra (1), papel (2) o tijera (3): "))

    while opcion not in [1, 2, 3]:
        opcion = int(
            input("Por favor, elige 1 para Piedra, 2 para Papel o 3 para Tijera: ")
        )

    rival = random.randint(1, 3)
    print("\nRonda " + str(ronda))
    print("Tú: " + jugadas[opcion])
    print("Rival: " + jugadas[rival])


    if opcion == rival:
        print("Empate, no cuenta la ronda.")

    elif(opcion == 1 and rival == 3) or (opcion ==2 and rival == 1) or (opcion == 3 and rival == 2):
        print("Ganas.")
        ronda += 1
        tusPtos += 1
        print("Resultado: "+ str(tusPtos) + ":" + str(rivalPtos))
    else:
        print("Pierdes.")
        ronda += 1
        rivalPtos += 1
        print("Resultado: "+ str(tusPtos) + ":" + str(rivalPtos))

if tusPtos > rivalPtos:
    print("\n¡GANASTE!")
else:
    print("\n¡PERDISTE!")

print("\nFIN DEL JUEGO")