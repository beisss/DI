# EJERCICIO 4
from operaciones import sumaDosNumeros, restaDosNumeros, multDosNumeros, divDosNumeros

repetir = True
while(repetir == True):
    print("Introduzca dos números.")
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))

    print("Que operación desea realizar:")
    print("a. Suma\nb. Resta\nc. Multiplicación\nd. División\n")
    opc = input("Elegir: ")

    while (opc != "a") & (opc != "b") & (opc != "c") & (opc != "d"):
        print("a. Suma\nb. Resta\nc. Multiplicación\nd. División\n")
        opc = input("Elija una opción entre a, b, c o0 d: ")

    if opc == "a":
        print("El resultado es: " + str(sumaDosNumeros(n1, n2)))
    elif opc == "b":
        print("El resultado es: " + str(restaDosNumeros(n1, n2)))
    elif opc == "c":
        print("El resultado es: " + str(multDosNumeros(n1, n2)))
    elif opc == "d":
        print("El resultado es: " + str(divDosNumeros(n1, n2)))

    opc = input("Realizar otra operación? (s/n): ")
    while (opc != "s") & (opc != "n"):
            opc = input("Realizar otra operación? (s/n): ")
    if opc == "n":
        print("\nPROGRAMA FINALIZADO\n")
        break