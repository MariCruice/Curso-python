# Ejercicio 2: Sistema de Evaluación Escolar
# Aplicando funciones y estructuras de datos (listas, diccionarios, tuplas)
# Marisa Cruz González

def sistema_evaluacion():
    """
    Función principal que gestiona la evaluación de alumnos
    Utiliza listas, diccionarios y tuplas para almacenar la información
    """
    
    print("\n" + "="*70)
    print("     SISTEMA DE EVALUACIÓN ESCOLAR - SECRETARÍA ACADÉMICA")
    print("="*70)
    
    # Solicitar número de alumnos
    while True:
        try:
            num_alumnos = int(input("\nNúmero de alumnos a evaluar: "))
            if num_alumnos <= 0:
                print("ERROR: Debe ingresar un número positivo")
                continue
            break
        except ValueError:
            print("ERROR: Ingrese un número entero válido")
    
    # Solicitar número de materias
    while True:
        try:
            num_materias = int(input("Número de materias por alumno: "))
            if num_materias <= 0:
                print("ERROR: Debe ingresar un número positivo")
                continue
            break
        except ValueError:
            print("ERROR: Ingrese un número entero válido")
    
    # Lista principal para almacenar todos los alumnos (lista de diccionarios)
    alumnos = []
    
    # Captura de datos por alumno
    for i in range(1, num_alumnos + 1):
        print(f"\n--- ALUMNO {i} de {num_alumnos} ---")
        
        # Solicitar nombre del alumno (validar vacío)
        while True:
            nombre = input("Nombre completo: ").strip()
            if nombre == "":
                print("ERROR: El nombre no puede estar vacío")
            else:
                break
        
        # Solicitar matrícula (validar vacío)
        while True:
            matricula = input("Matrícula: ").strip()
            if matricula == "":
                print("ERROR: La matrícula no puede estar vacía")
            else:
                break
        
        # Lista para almacenar las materias del alumno (lista de tuplas)
        materias = []
        
        # Captura de materias y calificaciones
        print("\n--- Captura de calificaciones ---")
        for j in range(1, num_materias + 1):
            print(f"Materia {j}:")
            
            # Solicitar nombre de la materia
            while True:
                materia_nombre = input("  Nombre de la materia: ").strip()
                if materia_nombre == "":
                    print("  ERROR: El nombre de la materia no puede estar vacío")
                else:
                    break
            
            # Solicitar calificación
            while True:
                try:
                    calificacion = float(input("  Calificación (0-10): "))
                    if calificacion < 0 or calificacion > 10:
                        print("  ERROR: La calificación debe estar entre 0 y 10")
                    else:
                        break
                except ValueError:
                    print("  ERROR: Ingrese un número válido")
            
            # Determinar si está aprobado o reprobado
            if calificacion > 6:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"
            
            # Almacenar como tupla (nombre_materia, calificacion, estado)
            materias.append((materia_nombre, calificacion, estado))
        
        # Calcular promedio del alumno
        suma = 0
        for materia in materias:
            suma += materia[1]  # materia[1] es la calificación
        promedio = suma / num_materias
        
        # Determinar estado general del alumno
        if promedio > 6:
            estado_general = "APROBADO"
        else:
            estado_general = "REPROBADO"
        
        # Crear diccionario del alumno
        alumno = {
            "nombre": nombre,
            "matricula": matricula,
            "materias": materias,
            "promedio": promedio,
            "estado": estado_general
        }
        
        # Agregar a la lista de alumnos
        alumnos.append(alumno)
        
        print(f"\n✓ Alumno {nombre} registrado exitosamente")
    
    # Mostrar reporte final
    print("\n" + "="*70)
    print("     REPORTE FINAL DE EVALUACIONES")
    print("="*70)
    
    # Estadísticas generales
    aprobados = 0
    reprobados = 0
    
    for alumno in alumnos:
        if alumno["estado"] == "APROBADO":
            aprobados += 1
        else:
            reprobados += 1
    
    print(f"\nRESUMEN GENERAL:")
    print(f"  Total de alumnos: {len(alumnos)}")
    print(f"  Aprobados: {aprobados}")
    print(f"  Reprobados: {reprobados}")
    
    # Detalle por alumno
    print("\n" + "-"*70)
    print("DETALLE POR ALUMNO:")
    print("-"*70)
    
    for idx, alumno in enumerate(alumnos, 1):
        print(f"\nALUMNO {idx}: {alumno['nombre']}")
        print(f"Matrícula: {alumno['matricula']}")
        print("Calificaciones:")
        
        for materia in alumno["materias"]:
            # materia es una tupla: (nombre, calificacion, estado)
            print(f"  - {materia[0]}: {materia[1]} ({materia[2]})")
        
        print(f"Promedio: {alumno['promedio']:.2f}")
        print(f"ESTADO FINAL: {alumno['estado']}")
    
    print("\n" + "="*70)
    print("     FIN DEL REPORTE")
    print("="*70)
    
    return alumnos

# Ejecutar la función
if __name__ == "__main__":
    sistema_evaluacion()