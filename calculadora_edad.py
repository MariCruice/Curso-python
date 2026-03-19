# Ejercicio 1: Calculadora de Edad
# Marisa Cruz González

import datetime

def calculadora_edad():
    """
    Función principal que calcula la edad de una persona
    a partir de su fecha de nacimiento en formato DD-MM-AAAA
    """
    print("\n" + "="*60)
    print("     CALCULADORA DE EDAD - SEGUROS NACIONALES")
    print("="*60)
    print("Complete el siguiente formulario para cotizar su póliza")
    
    while True:
        # Solicitar fecha de nacimiento
        print("\n--- DATOS DEL CONTRATANTE ---")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD-MM-AAAA): ").strip()
        
        # Validar campo vacío
        if fecha_nacimiento == "":
            print("ERROR: El campo no puede estar vacío. Intente nuevamente.")
            continue
        
        # Separar la cadena en día, mes y año
        partes = fecha_nacimiento.split("-")
        
        # Validar que tenga exactamente 3 partes
        if len(partes) != 3:
            print("ERROR: Formato incorrecto. Use DD-MM-AAAA (ejemplo: 15-05-1990)")
            continue
        
        dia_str, mes_str, anio_str = partes
        
        # Validar que día, mes y año sean números
        try:
            dia = int(dia_str)
            mes = int(mes_str)
            anio = int(anio_str)
        except ValueError:
            print("ERROR: Día, mes y año deben ser números enteros")
            continue
        
        # Validar año mayor a 1900
        if anio <= 1900:
            print("ERROR: El año de nacimiento debe ser mayor a 1900")
            continue
        
        # Validar mes (1-12)
        if mes < 1 or mes > 12:
            print("ERROR: El mes debe estar entre 1 y 12")
            continue
        
        # Validar día según el mes
        # Estructura de datos: diccionario con días por mes
        dias_por_mes = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        
        # Verificar si es año bisiesto (febrero tiene 29 días)
        def es_bisiesto(anio):
            """Función auxiliar para determinar si un año es bisiesto"""
            return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
        
        # Ajustar febrero en años bisiestos
        if es_bisiesto(anio) and mes == 2:
            max_dias = 29
        else:
            max_dias = dias_por_mes[mes]
        
        # Validar día
        if dia < 1 or dia > max_dias:
            print(f"ERROR: El mes {mes} tiene máximo {max_dias} días")
            continue
        
        # Si llegamos aquí, la fecha es válida
        break
    
    # Obtener fecha actual
    hoy = datetime.datetime.now()
    dia_actual = hoy.day
    mes_actual = hoy.month
    anio_actual = hoy.year
    
    # Calcular edad base
    edad = anio_actual - anio
    
    # Verificar si ya cumplió años este año
    if (mes_actual < mes) or (mes_actual == mes and dia_actual < dia):
        edad -= 1  # Aún no cumple años este año
        cumplio = "AÚN NO HA CUMPLIDO AÑOS ESTE AÑO"
    else:
        cumplio = "YA CUMPLIÓ AÑOS ESTE AÑO"
    
    # Mostrar resultado
    print("\n" + "="*60)
    print("     RESULTADO DE LA COTIZACIÓN")
    print("="*60)
    print(f"Fecha de nacimiento: {dia:02d}-{mes:02d}-{anio}")
    print(f"Fecha actual: {dia_actual:02d}-{mes_actual:02d}-{anio_actual}")
    print(f"Edad calculada: {edad} años")
    print(f"Estado: {cumplio}")
    
    # Clasificación por edad para seguros
    print("\n--- CLASIFICACIÓN PARA SEGUROS ---")
    if edad < 18:
        print("Categoría: Menor de edad (requiere tutor)")
        print("Tipo de póliza: Seguro infantil")
    elif edad < 30:
        print("Categoría: Adulto joven")
        print("Tipo de póliza: Seguro básico")
    elif edad < 50:
        print("Categoría: Adulto")
        print("Tipo de póliza: Seguro estándar")
    elif edad < 65:
        print("Categoría: Adulto mayor")
        print("Tipo de póliza: Seguro preferente")
    else:
        print("Categoría: Tercera edad")
        print("Tipo de póliza: Seguro de retiro")
    
    return edad

# Ejecutar la función
if __name__ == "__main__":
    calculadora_edad()