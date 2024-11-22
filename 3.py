#Cree una función que determine que número de una serie de N números es mayor

def Mayor1():
    print("BUSQUEMOS EL NUMERO MAYOR")
    numero = int(input("¿Cuántos valores va a introducir? "))

    if numero <= 0:
        print("¡Imposible!")
    else:
        valor = float(input("Escriba el número 1: "))
        maximo = suma = valor
        for i in range(2, numero + 1):
            valor = float(input(f"Escriba el número {i}: "))
            suma = suma + valor
            if valor > maximo:
                maximo = valor
        print(f"El número más grande de los introducidos es {maximo}")
Mayor1()        