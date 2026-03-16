# Ejercicio 2: Inicio de Sesión
# Aplicando estructuras de control y operadores lógicos
# Marisa Cruz González

# 1. Credenciales válidas (variables de tipo string)
usuario_correcto = "admin"
clave_correcta = "1234"

# 2. Variables para control de intentos
intentos_maximos = 3
intentos_realizados = 0
acceso_concedido = False  # Variable booleana para controlar el acceso

# Mensaje de inicio del sistema
print("\n--- Sistema de Inicio de Sesión ---")
print("Por favor, identifíquese (máximo 3 intentos)")

# 3. Ciclo principal para control de intentos (estructura while)
while intentos_realizados < intentos_maximos and not acceso_concedido:
    # Cálculo de intentos restantes
    intentos_restantes = intentos_maximos - intentos_realizados
    print(f"\n--- Intentos restantes: {intentos_restantes} ---")
    
    # 4. Solicitud de credenciales
    print("Usuario: ")
    usuario = input()
    
    print("Contraseña: ")
    clave = input()
    
    # 5. Validación de campos vacíos usando operadores lógicos
    if usuario == "" or clave == "":
        print("Error de autenticación: Los campos no pueden estar vacíos")
        intentos_realizados += 1
        
        # Verificar si se agotaron los intentos
        if intentos_realizados == intentos_maximos:
            print("\n--- ACCESO BLOQUEADO ---")
            print("Ha excedido el número máximo de intentos permitidos")
        continue  # continue para saltar al siguiente intento
    
    # 6. Validación de credenciales (comparación de strings)
    if usuario == usuario_correcto and clave == clave_correcta:
        # Acceso concedido
        print("\n--- ACCESO CONCEDIDO ---")
        print(f"Bienvenido al sistema, {usuario}")
        acceso_concedido = True
        break  # break para salir del ciclo
    else:
        # Credenciales incorrectas
        print("Error: Usuario o contraseña incorrectos")
        intentos_realizados += 1
        
        # Verificar si se agotaron los intentos
        if intentos_realizados == intentos_maximos:
            print("\n--- ACCESO BLOQUEADO ---")
            print("Ha excedido el número máximo de intentos permitidos")

# 7. Mensaje final si no se concedió el acceso
if not acceso_concedido and intentos_realizados == intentos_maximos:
    print("\nEl sistema ha sido bloqueado por seguridad.")
    print("Contacte al administrador para restablecer su acceso.")