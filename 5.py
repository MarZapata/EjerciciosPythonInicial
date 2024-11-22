#Cree una función que calcule el Factorial de un número entero positivo

def Facto1():
    print ("Calculemos el factorial")
    numero = int(input("Introduzca un número positivo: "))
    if numero <= 0:
        print("¡Le pedí un número positivo!")
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial = factorial * i
        print(f"El factorial de {numero} es {factorial}.")
Facto1()