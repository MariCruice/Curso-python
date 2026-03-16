# Ejercicio 1: Cajero Automático
# Aplicando estructuras de control y tipos de datos
# Marisa Cruz González

# 1. Variables para el inventario (inicialmente 10 billetes de cada denominación)
# Se utilizan variables de tipo entero (int) para almacenar cantidades
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 = 10

# Variables para controlar la ejecución del programa
ejecutando = True  # Variable booleana (bool) para controlar el ciclo principal

# Ciclo principal del programa (estructura de repetición while)
while ejecutando:
    # 2. Variables para billetes a entregar (se reinician en cada intento)
    # Se inicializan en 0 para cada transacción
    entregar_1000 = 0
    entregar_500 = 0
    entregar_200 = 0
    entregar_100 = 0
    entregar_50 = 0
    
    # 3. Mensaje de inicio y muestra de inventario actual
    print("\n--- Dispensadora de Billetes ---")
    print("\n--- Inventario actual ---")
    print(f"Billetes de $1000: {billetes_1000}")
    print(f"Billetes de $500:  {billetes_500}")
    print(f"Billetes de $200:  {billetes_200}")
    print(f"Billetes de $100:  {billetes_100}")
    print(f"Billetes de $50:   {billetes_50}")
    
    # 4. Solicitud del monto a retirar
    print("\nIngrese el monto a retirar (0 para salir): ")
    
    # Manejo de excepciones para validar que la entrada sea un número entero
    try:
        entrada = input()
        monto = int(entrada)  # Conversión de string a entero
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
        continue  # continue permite volver al inicio del ciclo
    
    # Condición de salida del programa
    if monto == 0:
        print("Saliendo del sistema. ¡Gracias por usar nuestro cajero!")
        ejecutando = False  # Cambio de variable booleana para terminar el ciclo
        break  # break para salir del ciclo inmediatamente
    
    # Validación de monto positivo
    if monto < 0:
        print("Error: El monto debe ser positivo")
        continue
    
    # Validación de monto mínimo (debe ser múltiplo de la denominación más pequeña)
    if monto < 50:
        print("Error: El monto mínimo para retirar es $50")
        continue
    
    # 5. Cálculo de billetes a entregar (algoritmo greedy)
    monto_restante = monto
    posible = True  # Variable booleana para controlar si es posible la transacción
    
    # Cálculo de billetes de 1000
    if monto_restante >= 1000 and billetes_1000 > 0:
        # min() calcula el máximo posible sin exceder inventario
        max_posible = min(monto_restante // 1000, billetes_1000)
        entregar_1000 = max_posible
        monto_restante -= entregar_1000 * 1000
    
    # Cálculo de billetes de 500
    if monto_restante >= 500 and billetes_500 > 0:
        max_posible = min(monto_restante // 500, billetes_500)
        entregar_500 = max_posible
        monto_restante -= entregar_500 * 500
    
    # Cálculo de billetes de 200
    if monto_restante >= 200 and billetes_200 > 0:
        max_posible = min(monto_restante // 200, billetes_200)
        entregar_200 = max_posible
        monto_restante -= entregar_200 * 200
    
    # Cálculo de billetes de 100
    if monto_restante >= 100 and billetes_100 > 0:
        max_posible = min(monto_restante // 100, billetes_100)
        entregar_100 = max_posible
        monto_restante -= entregar_100 * 100
    
    # Cálculo de billetes de 50
    if monto_restante >= 50 and billetes_50 > 0:
        max_posible = min(monto_restante // 50, billetes_50)
        entregar_50 = max_posible
        monto_restante -= entregar_50 * 50 
    
    # 6. Verificación de que se puede entregar el monto exacto
    if monto_restante != 0:
        # No se puede entregar el monto exacto (transacción cancelada)
        print("\n--- ERROR ---")
        print("No es posible entregar el monto exacto con el inventario disponible")
        print("Transacción cancelada - No se dispensaron billetes")
    else:
        # 7. Actualización del inventario
        billetes_1000 -= entregar_1000
        billetes_500 -= entregar_500
        billetes_200 -= entregar_200
        billetes_100 -= entregar_100
        billetes_50 -= entregar_50

        # 8. Mostrar resultado de la transacción
        print("\n--- TRANSACCIÓN EXITOSA ---")
        print("Billetes dispensados:")
        
        # Estructura condicional para mostrar solo denominaciones entregadas
        if entregar_1000 > 0:
            print(f"{entregar_1000} billete(s) de $1000")
        if entregar_500 > 0:
            print(f"{entregar_500} billete(s) de $500")
        if entregar_200 > 0:
            print(f"{entregar_200} billete(s) de $200")
        if entregar_100 > 0:
            print(f"{entregar_100} billete(s) de $100")
        if entregar_50 > 0:
            print(f"{entregar_50} billete(s) de $50")
        
        print(f"\nTotal retirado: ${monto}")
        
        # Verificación de inventario agotado
        if (billetes_1000 == 0 and billetes_500 == 0 and billetes_200 == 0 
            and billetes_100 == 0 and billetes_50 == 0 ):
            print("\n--- ADVERTENCIA ---")
            print("El cajero se ha quedado sin billetes")
            print("El sistema se cerrará automáticamente")
            ejecutando = False

print("\nGracias por usar nuestro cajero automático")