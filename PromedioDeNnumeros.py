#Promedio de n numeros

contador = 0 
suma = 0
numero = 1

while numero != 0:
    numero = int(input("Ingrese un numero entero: "))
    print ("Si no desea continuar presione 0")

    if numero != 0:
        suma += numero
        contador += 1

if contador == 0:
    print("No ha digitado un número: ")
else:
    promedio = suma / contador

    print("El promedio de los {} numeros digitados es {} " .format(contador, promedio))