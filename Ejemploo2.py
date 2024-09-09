def multiplicacion(factor1, factor2):
    """Multiplica dos números y devuelve el resultado."""
    producto = factor1 * factor2
    return producto

def suma(a, b):
    """Suma dos números y devuelve el resultado."""
    resultado = a + b
    return resultado

def principal():
    # Solicitar al usuario que ingrese los valores
    multiplicando = float(input("Ingrese el valor del multiplicando: "))
    multiplicador = float(input("Ingrese el valor del multiplicador: "))
    valor_a_sumar = float(input("Ingrese el valor a sumar: "))

    # Realizar la multiplicación
    resultado_multiplicacion = multiplicacion(multiplicando, multiplicador)

    # Realizar la suma del resultado de la multiplicación con el valor a sumar
    resultado_final = suma(resultado_multiplicacion, valor_a_sumar)

    # Mostrar los resultados
    print(f"{multiplicando} * {multiplicador} = {resultado_multiplicacion}")
    print(f"Resultado final es ({resultado_multiplicacion} + {valor_a_sumar}) = {resultado_final}")

principal()
