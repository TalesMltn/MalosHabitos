# Función para calcular el área de un rectángulo
def f(a, b):
    result = a * b
    return result

# Función para calcular el área de un triángulo
def g(b, h):
    r = 0.5 * b * h
    return r

# Función principal
def main():
    # Entrada de valores para el rectángulo
    x = float(input("Ingrese el ancho del rectángulo: "))
    y = float(input("Ingrese la altura del rectángulo: "))
    rect_area = f(x, y)
    print("Área del rectángulo:", rect_area)

    # Entrada de valores para el triángulo
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    tri_area = g(base, altura)
    print("Área del triángulo:", tri_area)

main()

