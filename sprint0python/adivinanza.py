"""
# EJERCICIO 1
print("Adivina adivinanza... que tiene Iago Pombo en la panza?")
print("a. Empanadillas\nb. Yogures\nc. El ombligo")

opcion = input("Elegir: ")
while (opcion != "a") & (opcion != "b") & (opcion != "c"):
    opcion = input("Elige entre a, b o c: ")

if opcion == "a":
    print("¡RESPUESTA CORRECTA!")
elif (opcion == "b") | (opcion == "c"):
    print("¡Respuesta errónea!")



# EJERCICIO 2
puntuacion = 0

adivinanzas = {
    1: "Adivina, adivinanza... que tiene Iago Pombo en la panza?",
    2: "Cuanto tardarán en despedir a Iago Pombo del trabajo?",
    3: "Cuantos hijos tendrá Iago Pombo?",
}

opciones = {
    1: "a. Empanadillas\nb. Yogures\nc. El ombligo",
    2: "a. 2 meses\nb. 2 días\nc. No lo contratan",
    3: "a. 4 hijos\nb. 4 perros\nc. ∞",
}

respuestas = {1: "a", 2: "c", 3: "c"}

# adivinanza 1
print(adivinanzas[1])
print(opciones[1])
opcion = input("Elegir: ")
while (opcion != "a") & (opcion != "b") & (opcion != "c"):
    opcion = input("Elige entre a, b o c:")

if opcion == respuestas[1]:
    puntuacion = puntuacion + 10
    print("Respuesta correcta, +10 puntos.\nPuntuación total: " + str(puntuacion) + "\n")
elif opcion != respuestas[1]:
    puntuacion = puntuacion - 5
    print("Respuesta incorrecta, -5 puntos.\nPuntuación total: " + str(puntuacion) + "\n")

# adivinanza 2
print(adivinanzas[2])
print(opciones[2])
opcion = input("Elegir: ")
while (opcion != "a") & (opcion != "b") & (opcion != "c"):
    opcion = input("Elige entre a, b o c:")

if opcion == respuestas[3]:
    puntuacion = puntuacion + 10
    print("Respuesta correcta, +10 puntos.\nPuntuación total: " + str(puntuacion) + "\n")
elif opcion != respuestas[3]:
    puntuacion = puntuacion - 5
    print("Respuesta incorrecta, -5 puntos.\nPuntuación total: " + str(puntuacion) + "\n")

# adivinanza 3
print(adivinanzas[3])
print(opciones[3])
opcion = input("Elegir: ")
while (opcion != "a") & (opcion != "b") & (opcion != "c"):
    opcion = input("Elige entre a, b o c:")

if opcion == respuestas[3]:
    puntuacion = puntuacion + 10
    print("Respuesta correcta, +10 puntos.\nPuntuación total: " + str(puntuacion) + "\n")
elif opcion != respuestas[3]:
    puntuacion = puntuacion - 5
    print("Respuesta incorrecta, -5 puntos.\nPuntuación total: " + str(puntuacion) + "\n")
"""

# EJERCICIO 6
import random

puntuacion = 0

adivinanzas = {
    1: "Adivina, adivinanza... que tiene Iago Pombo en la panza?",
    2: "Cuanto tardarán en despedir a Iago Pombo del trabajo?",
    3: "Cuantos hijos tendrá Iago Pombo?",
}

opciones = {
    1: "a. Empanadillas\nb. Yogures\nc. El ombligo",
    2: "a. 2 meses\nb. 2 días\nc. No lo contratan",
    3: "a. 4 hijos\nb. 4 perros\nc. ∞",
}

respuestas = {1: "a", 2: "c", 3: "c"}

clavesAdivinanzas = list(adivinanzas.keys())
listaAdivinanzas = random.sample(clavesAdivinanzas, 2)

for clave in listaAdivinanzas:
    solucion = respuestas[clave]
    print("\n" + adivinanzas[clave])
    print(opciones[clave])

    opcion = input("Elegir: ").strip().lower()
    while (opcion != "a") & (opcion != "b") & (opcion != "c"):
        opcion = input("Elige entre a, b o c:").strip().lower()

    if opcion == solucion:
        print("\n¡RESPUESTA CORRECTA! +10pts :)\n")
        puntuacion = puntuacion + 10
    else:
        print("\n¡RESPUESTA INCORRECTA! -5pts :(\n")
        puntuacion = puntuacion - 5

    print("Puntos: " + str(puntuacion) + "pts\n")
