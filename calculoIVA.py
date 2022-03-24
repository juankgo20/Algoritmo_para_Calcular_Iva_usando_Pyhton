# Realice un algoritmo que a partir de un valor total a pagar sea capaz de informar el valor
# del IVA (16%) y que permita etiquetar dicho precio bajo la categoría “BARATO” si el precio es menor de
# $100.000, “COMUN” si el precio es mayor de $100.000 y menor de $150.000 o “CARO” si el precio es mayor igual
# a $150.000


class SolucionA():
    def __init__(self):
        self.IVA = 0.16

    def Solucion(self, PrecioItem):
        self.Precio = PrecioItem
        self.PrecioIva = (self.Precio * self.IVA)
        self.PrecioTot = (self.Precio + self.PrecioIva)
        
        print ("El (16%) del IVA de su producto es: "), (self.PrecioIva)
        print ("El valor total a pagar es de: $"), (self.PrecioTot)

    def Comparar(self):
        if (self.PrecioTot < 100000):
            print ("El precio del producto con IVA es de categoria (BARATO): " )

        elif (self.PrecioTot > 100000 and self.PrecioTot < 150000):
            print ("El precio del producto con IVA es de categoria (COMUN) : ")

        else:
            (self.PrecioTot > 150000)
            print ("El precio del productoo con IVA es de categoria (CARO) : ")


ImprimirSoluA = SolucionA()

Precio = int(input("Ingrese el precio del producto: "))


ImprimirSoluA.Solucion(Precio)
ImprimirSoluA.Comparar()
