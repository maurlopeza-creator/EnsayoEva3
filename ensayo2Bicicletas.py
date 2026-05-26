print("Bienvenido al sistema de gestion de bicicletas")
capacidad_maxima = 25
bicis_disponibles = 25
viajes_activos = 0
ejecutando = True
#ciclo principal
while ejecutando:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Bicicletas disponibles")
    print("2. Arrendar bicicletas (Salida)")
    print("3. Devolver bicicletas (Entrada)")
    print("4. Historial de viajes activos")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opcion (1-5): "))
    except ValueError:
        print("Opcion no valida, por favor, ingrese un numero valido entre 1 y 5")
        continue
#opcion 1 Bicis disponibles
if opcion == 1:
        print(f"\n [INFO] Cantidad de bicicletas disponibles: {bicis_disponibles}")
#opcion 2 Arrendar bicicletas1
elif opcion == 2:
        print(f"\n--- Arrendar bicicletas (Disponibles): {bicis_disponibles} ")
        if bicis_disponibles == 0:
            print ("Lo sentimos, no quedan bicicletas disponibles")
        else:
            try:
                cantidad_a_arrendar = int(input("¿Cuantas bicicletas desea arrendar?"))
                if cantidad_a_arrendar <=0:
                    print("Error: La cantidad a arrendar debe ser mayor a 0")
                elif cantidad_a_arrendar > bicis_disponibles:
                    print(f"No hay suficientes bicicletas, pede arrendar hasta: {bicis_disponibles}")
                else:
                    bicis_disponibles -= cantidad_a_arrendar
                    viajes_activos += cantidad_a_arrendar
                    print(f"Arriendo exitoso, ah retirado {cantidad_a_arrendar} bicis")
            except ValueError:
                print("Error, Debe ingresar un numero entero")
#opcion 3 
elif opcion == 3:
        diferencia = capacidad_maxima-bicis_disponibles
        print(f"\n--- DEVOLCER BICICLETAS (espacio libre en estacion: {diferencia})---")
        try:
            cantidad_a_devolver = int(input("¿Cuantas bicicletas desea devlver?:"))
            if cantidad_a_devolver <= 0:
                print ("Error: La cantidad a devolver debe ser mayor a 0")
            elif bicis_disponibles + cantidad_a_devolver > capacidad_maxima:
                print(f"Error: No se puden devolver tantas bicicletas, supera la capacidad maxima de 25 bicis")
            else:
                bicis_disponibles += cantidad_a_devolver
                viajes_activos -= cantidad_a_devolver
                print(f"Devolucion exitosa ha regresado {cantidad_a_devolver} bicicletas")
        except ValueError:
            print("Error: Debe ingresar un numero entero valido")
#Opcion 4 Viajes activos
elif opcion == 4:
        print(f"\n [HISTORIAL] actualmente hay {viajes_activos} bicicleta(s) en uso por ususarios")
#opcion 5 Salir
elif opcion == 5:
     print("GRacias por utilizar nuestro software, hasta la proxima")
     ejecutando = False
else:
    print ("Opcion fuera de rango")
