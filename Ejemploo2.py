def multiplicacion(factor1, factor2):
    """Multiplica dos números y devuelve el resultado."""
    producto = factor1 * factor2
    return producto


def suma(a, b):
    """Suma dos números y devuelve el resultado."""
    resultado = a + b
    return resultado


def principal():
    x = 5.0
    y = 3.0
    z = 7.0

    # Realizamos la multiplicación
    resultado_multiplicacion = multiplicacion(x, y)

    # Realizamos la suma de la multiplicación con z
    resultado_final = suma(resultado_multiplicacion, z)

    print(f"{x} * {y} = {resultado_multiplicacion}")
    print(f"Resultado final ({resultado_multiplicacion} + {z}) = {resultado_final}")


principal()
