# Importa las funciones del archivo funciones.py
import libreria

# Define la función para solicitar datos de usuario
def solicitar_datos_usuario():
    nombre = str(input("Hola Por favor ingrese su Nombre Para el Registro: "))
    edad = int(input("Por favor, ingrese su edad: "))
    return nombre, edad

# Define la función principal del programa
def main():
    nombre, edad = solicitar_datos_usuario()
    
    if edad < 25:
        print("Lo siento,", nombre + ",", "Solo los Mayores de 24 Años pueden comprar, No cumples con los Requisitos.")
        return
    total_compra = 0
    seguir_comprando = True

    # Función que permite seguir comprando con sus opciones
    while seguir_comprando:
        
        mostrar_menu(total_compra)
        opcion = input("Ingrese el número de opción que desea: ")
        if opcion == "1":
            total_compra += libreria.comprar_rifles()
        elif opcion == "2":
            total_compra += libreria.comprar_perdigones()
        elif opcion == "3":
            total_compra += libreria.comprar_silenciador()
        elif opcion == "4":
            total_compra += libreria.comprar_cuchillas()
        elif opcion == "5":
            total_compra += libreria.comprar_fundas()
        elif opcion == "6":
            print("Gracias por su compra. El total a pagar es: $", total_compra)
            seguir_comprando = False
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        # Preguntar al usuario si quiere seguir comprando
        continuar = input("¿Quieres seguir comprando? (s/n): ")
        if continuar.lower() != 's':
            seguir_comprando = False

# Función para mostrar el menú de compra
def mostrar_menu(total_compra):
    print("Bienvenido a Captura tu Yetti ART.CAZA")
    print("Hola, este es el Menú De Compra")
    print("1) Rifle Stock: ':::", libreria.Rifle, ":::' - $42500")
    print("2) Perdigones Stock: ':::", libreria.Perdigones, ":::' - $5990")
    print("3) Silenciador Stock: '", libreria.Silenciador, ":::' - $10990")
    print("4) Cuchillas Stock: ':::", libreria.Cuchillas, ":::' - $11500")
    print("5) Funda para Armamento: ':::", libreria.Fundas, ":::' - $7990")
    print("6) Total de la Compra. " ) 

# Termina la función principal
if __name__ == "__main__":
    main()
