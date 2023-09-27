"""
# Ejercicio 1
print("Adivina adivinanza... que tiene Iago Pombo en la panza?")
print("a. Empanadillas\nb. Yogures\nc. El ombligo")

opcion = input("Elegir: ")
while (opcion != "a") & (opcion != "b") & (opcion != "c"):
    opcion = input("Elige entre a, b o c: ")

if opcion == "a":
    print("¡RESPUESTA CORRECTA!")
elif (opcion == "b") | (opcion == "c"):
    print("¡Respuesta errónea!")
"""

# Ejercicio 2
puntuacion = 0

adivinanzas = {
    1: "Adivina, adivinanza... que tiene el Iago Pombo panza?",
    2: "Cuanto tardarán en despedir a Iago Pombo del trabajo?",
    3: "Cuantos hijos tendrá Iago Pombo?",
}

opciones = {
    1: "a. Empanadillas\nb. Yogures\nc. El ombligo",
    2: "a. 2 meses\nb. 2 días\nc. No lo contratan",
    3: "a. 4 hijos\nb. 4 perros\nc. ∞",
}

respuestas = {1: "a", 2: "c", 3: "c"}

# Adivinanza 1
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

# Adivinanza 2
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

# Adivinanza 3
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
