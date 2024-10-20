import doctest

def tipo_triangulo(lado1, lado2, lado3):
    """
    Determina el tipo de triángulo dado tres lados.

    Parámetros:
    lado1 (float): longitud del primer lado
    lado2 (float): longitud del segundo lado
    lado3 (float): longitud del tercer lado

    Retorna:
    str: Tipo de triángulo o mensaje de error

    Casos de Prueba:
    >>> tipo_triangulo(3, 3, 3)
    'Equilátero'
    >>> tipo_triangulo(3, 4, 4)
    'Isósceles'
    >>> tipo_triangulo(3, 4, 5)
    'Escaleno'
    >>> tipo_triangulo(1, 1, 2)
    'No es un triángulo'
    >>> tipo_triangulo(0, 0, 0)
    'No es un triángulo'
    >>> tipo_triangulo(-1, 2, 3)
    'Entrada inválida'
    >>> tipo_triangulo(5, 10, 5)
    'No es un triángulo'
    >>> tipo_triangulo(2, 2, 3)
    'Isósceles'
    >>> tipo_triangulo(10, 10, 1)
    'Isósceles'
    >>> tipo_triangulo(2147483647, 2147483647, 2147483647)
    'Equilátero'
    >>> tipo_triangulo(1, 2, 10)
    'No es un triángulo'
    >>> tipo_triangulo(3, 4, -5)
    'Entrada inválida'
    >>> tipo_triangulo(1000000, 1000000, 1000000)
    'Equilátero'
    >>> tipo_triangulo(999999, 999999, 500000)
    'Isósceles'
    >>> tipo_triangulo(0, 2, 2)
    'No es un triángulo'
    """

    # Verificar si los lados son válidos (mayores que 0)
    if lado1 < 0 or lado2 < 0 or lado3 < 0:
        return 'Entrada inválida'

    # Verificar la desigualdad del triángulo
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return 'No es un triángulo'

    # Si todos los lados son iguales
    if lado1 == lado2 == lado3:
        return 'Equilátero'

    # Si dos lados son iguales
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'Isósceles'

    # Si todos los lados son diferentes
    return 'Escaleno'


if __name__ == "__main__":
    doctest.testmod(verbose=True)
