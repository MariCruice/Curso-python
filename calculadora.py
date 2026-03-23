class calculadora:  
    def __init__(self, numero1=0, numero2=0):
        self._numero1 = numero1
        self._numero2 = numero2
        self._historial = []
    
    # Propiedades
    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1(self, nuevo_numero1):
        if type(nuevo_numero1) in (int, float):
            self._numero1 = nuevo_numero1
        else:
            raise ValueError("Debe ser un número")
    
    @property
    def numero2(self):
        return self._numero2
    
    @numero2.setter
    def numero2(self, nuevo_numero2):
        if type(nuevo_numero2) in (int, float):
            self._numero2 = nuevo_numero2
        else:
            raise ValueError("Debe ser un número")
    
    # Métodos de operaciones 
    def suma(self):  
        resultado = self._numero1 + self._numero2
        self._registrar_operacion('+', resultado)
        return resultado
    
    def resta(self):  
        resultado = self._numero1 - self._numero2
        self._registrar_operacion('-', resultado)
        return resultado
    
    def multiplicacion(self):  
        resultado = self._numero1 * self._numero2
        self._registrar_operacion('*', resultado)
        return resultado
    
    def division(self): 
        if self._numero2 == 0:
            raise ValueError("Error: División entre cero no permitida")
        resultado = self._numero1 / self._numero2
        self._registrar_operacion('/', resultado)
        return resultado
    
    def _registrar_operacion(self, operador, resultado):
        self._historial.append({
            'operacion': f"{self._numero1} {operador} {self._numero2}",
            'resultado': resultado
        })
    
    def ver_historial(self): 
        if not self._historial:
            print("No hay operaciones en el historial.")
            return
        print("\n--- Historial de Operaciones ---")
        contador = 1
        for operacion in self._historial:
            print(f"{contador}. {operacion['operacion']} = {operacion['resultado']}")
            contador += 1
        print()


def interpretar_expresion(expresion):
    for operador in ['+', '-', '*', '/']:
        if operador in expresion:
            partes = expresion.split(operador)
            if len(partes) == 2:
                try:
                    num1 = float(partes[0].strip())
                    num2 = float(partes[1].strip())
                    return num1, num2, operador
                except ValueError:
                    return None
    return None


def main():
    calc = calculadora() 
    print("Calculadora Básica. Escribe 'salir' para terminar o 'historial' para ver operaciones.\n")
    
    while True:
        entrada = input("Ingresa la operación (ejemplo: 5 + 5): ")
        
        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break
        
        if entrada.strip().lower() == "historial":
            calc.ver_historial() 
            continue
        
        resultado = interpretar_expresion(entrada)
        if not resultado:
            print("Expresión no válida. Usa el formato: número operador número (ej. 5 + 5)\n")
            continue
        
        num1, num2, operador = resultado
        
        try:
            calc.numero1 = num1
            calc.numero2 = num2
        except ValueError as e:
            print(e)
            continue
        
        try:
            if operador == '+':
                print("Resultado:", calc.suma()) 
            elif operador == '-':
                print("Resultado:", calc.resta()) 
            elif operador == '*':
                print("Resultado:", calc.multiplicacion())
            elif operador == '/':
                print("Resultado:", calc.division()) 
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()