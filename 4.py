#Cree una función que dibuje un rectángulo de X filas y X columnas determinadas por el usuario

def Rectangulo1():
    print("Dibujemos un rectángulo")
    b=int(input("Cuan ancha será la base?:"))
    a=int(input("Cual será su altura?:"))

    for i in range(1,a+1):
        for j in range(1,b+1):
            print("$", end="")
        print(" ")
        
Rectangulo1()