#Cree una función que determine si un color es primario o no, se debe imprimir en pantalla la leyenda "el color X es primario" o "el color X no es primario"
  
def Primario1():
    print("SERÁ PRIMARIO???")
    color1=input("Digite el color que quieres analizar:")
    if (color1=="rojo") or (color1=="amarillo") or (color1=="azul"):
        print (f"El color {color1} es primario")
    else:
        print (f"El color {color1} no es primario")

Primario1()