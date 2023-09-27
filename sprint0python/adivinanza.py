print("Adivina adivinanza... que tiene Iago Pombo en la panza?")
print("a. Empanadillas\nb. Yogures\nc. El ombligo")

opcion = input("Elegir: ")
while (opcion != "a") & (opcion != "b") & (opcion != "c"):
    opcion = input("Elige entre a, b o c: ")

if opcion == "a":
    print("¡RESPUESTA CORRECTA!")
elif (opcion == "b") | (opcion == "c"):
    print("¡Respuesta errónea!")
