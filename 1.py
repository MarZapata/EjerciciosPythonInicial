#Cree una función que calcule el promedio de N notas

def Promedio1():
    print("PROMEDIO DE NOTAS")
    numero = int(input("¿Cuántos notas va a promediar? "))

    if numero <= 0:
        print("¡Imposible!")
    else:
        valor = float(input("Escriba la nota número 1: "))
        suma = valor
        for i in range(2, numero + 1):
            valor = float(input(f"Escriba la nota número {i}: "))
            suma = suma + valor
        print(f"El promedio de las notas introducidas es {suma / numero}")
Promedio1()
