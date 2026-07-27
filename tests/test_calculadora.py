from src.calculadora import (
    somar, subtrair, multiplicar, dividir, potencia, resto
)
import pytest


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(5, 3) == 2


def test_multiplicar():
    assert multiplicar(4, 3) == 12


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_potencia():
    assert potencia(2, 3) == 8


def test_resto():
    assert resto(10, 3) == 1


def test_resto_por_zero():
    with pytest.raises(ValueError):
        resto(10, 0)
