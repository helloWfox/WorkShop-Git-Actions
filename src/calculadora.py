def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


def potencia(a, b):
    return a ** b


def resto(a, b):
    if b == 0:
        raise ValueError("Não é possível calcular o resto da divisão por zero")
    return a % b
