import math
import doctest

def suma(a, b):
    """
    Suma dos números.
    
    >>> suma(1, 2)
    3
    >>> suma(-1, 1)
    0
    >>> suma(0, 0)
    0
    >>> suma(1.5, 2.5)
    4.0
    >>> suma(-1.5, -2.5)
    -4.0
    """
    return a + b

def resta(a, b):
    """
    Resta dos números.
    
    >>> resta(5, 3)
    2
    >>> resta(3, 5)
    -2
    >>> resta(0, 0)
    0
    >>> resta(1.5, 0.5)
    1.0
    >>> resta(-1.5, -0.5)
    -1.0
    """
    return a - b

def multiplicacion(a, b):
    """
    Multiplica dos números.
    
    >>> multiplicacion(2, 3)
    6
    >>> multiplicacion(-2, 3)
    -6
    >>> multiplicacion(0, 3)
    0
    >>> multiplicacion(1.5, 2)
    3.0
    >>> multiplicacion(-1.5, -2)
    3.0
    """
    return a * b

def division(a, b):
    """
    Divide dos números.
    
    >>> division(6, 3)
    2.0
    >>> division(3, 2)
    1.5
    >>> division(1, 3)
    0.3333333333333333
    >>> division(1.5, 0.5)
    3.0
    >>> division(-1.5, -0.5)
    3.0
    >>> division(1, 0)
    Traceback (most recent call last):
        ...
    ValueError: No se puede dividir por cero
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def modulo(a, b):
    """
    Calcula el módulo de dos números.
    
    >>> modulo(5, 3)
    2
    >>> modulo(5, 5)
    0
    >>> modulo(5, 2)
    1
    >>> modulo(5.5, 2)
    1.5
    >>> modulo(-5, 3)
    1
    """
    return a % b

def sen(x):
    """
    Calcula el seno de un ángulo en radianes.
    
    >>> round(sen(0), 10)
    0.0
    >>> round(sen(math.pi/2), 10)
    1.0
    >>> round(sen(math.pi), 10)
    0.0
    >>> round(sen(3*math.pi/2), 10)
    -1.0
    >>> round(sen(2*math.pi), 10)
    0.0
    """
    result = math.sin(x)
    return 0.0 if abs(result) < 1e-10 else result

def cos(x):
    """
    Calcula el coseno de un ángulo en radianes.
    
    >>> round(cos(0), 10)
    1.0
    >>> round(cos(math.pi/2), 10)
    0.0
    >>> round(cos(math.pi), 10)
    -1.0
    >>> round(cos(3*math.pi/2), 10)
    0.0
    >>> round(cos(2*math.pi), 10)
    1.0
    """
    result = math.cos(x)
    return 0.0 if abs(result) < 1e-10 else result

def tan(x):
    """
    Calcula la tangente de un ángulo en radianes.
    
    >>> round(tan(0), 10)
    0.0
    >>> round(tan(math.pi/4), 10)
    1.0
    >>> round(tan(math.pi), 10)
    0.0
    >>> round(tan(3*math.pi/4), 10)
    -1.0
    >>> round(tan(2*math.pi), 10)
    0.0
    """
    result = math.tan(x)
    return 0.0 if abs(result) < 1e-10 else result

def sumatorio(n):
    """
    Calcula el sumatorio de 1 a n.
    
    >>> sumatorio(1)
    1
    >>> sumatorio(2)
    3
    >>> sumatorio(3)
    6
    >>> sumatorio(4)
    10
    >>> sumatorio(5)
    15
    """
    return sum(range(1, n+1))

def factorial(n):
    """
    Calcula el factorial de un número.
    
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    if n == 0:
        return 1
    return n * factorial(n-1)

def mcd(a, b):
    """
    Calcula el máximo común divisor de dos números.
    
    >>> mcd(48, 18)
    6
    >>> mcd(48, 48)
    48
    >>> mcd(48, 0)
    48
    >>> mcd(0, 18)
    18
    >>> mcd(7, 3)
    1
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    doctest.testmod(verbose=True)
