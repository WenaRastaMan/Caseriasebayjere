#Variables globales
Perdigones = 1520
Silenciador = 500
Rifle = 29
Cuchillas = 98
Fundas = 31
edad = 0
nombre = str
#Definicion de Funciones:
def comprar_rifles():
    global Rifle
    cantidad_rifles = int(input("¿Cuántos Rifles Desea Llevar? Precio De Rifle $42500: "))
    compra_total = cantidad_rifles * 42500
    print("Valor total: $", compra_total)
    Rifle -= cantidad_rifles
    print("Stock restante de Rifles:", Rifle)
    return compra_total

def comprar_perdigones():
    global Perdigones
    cantidad_perdigones = int(input("¿Cuántos Perdigones Desea Llevar? Precio De Perdigones $5990: "))
    compra_total = cantidad_perdigones * 5990
    print("Valor total: $", compra_total)
    Perdigones -= cantidad_perdigones
    print("Stock restante de Perdigones:", Perdigones)
    return compra_total

def comprar_silenciador():
    global Silenciador
    cantidad_silenciadores = int(input("¿Cuántos Silenciadores Desea Llevar? Precio De Silenciador $10990: "))
    compra_total = cantidad_silenciadores * 10990
    print("Valor total: $", compra_total)
    Silenciador -= cantidad_silenciadores
    print("Stock restante de Silenciadores:", Silenciador)
    return compra_total

def comprar_cuchillas():
    global Cuchillas
    cantidad_cuchillas = int(input("¿Cuántas Cuchillas Desea Llevar? Precio De Cuchillas $11500: "))
    compra_total = cantidad_cuchillas * 11500
    print("Valor total: $", compra_total)
    Cuchillas -= cantidad_cuchillas
    print("Stock restante de Cuchillas:", Cuchillas)
    return compra_total

def comprar_fundas():
    global Fundas
    cantidad_fundas = int(input("¿Cuántas Fundas Desea Llevar? Precio De Fundas $7990: "))
    compra_total = cantidad_fundas * 7990
    print("Valor total: $", compra_total)
    Fundas -= cantidad_fundas
    print("Stock restante de Fundas:", Fundas)
    return compra_total