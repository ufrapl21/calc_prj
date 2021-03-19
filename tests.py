from calculadora import somar
from calculadora import subtrair
from calculadora import multiplicar
from calculadora import dividir

def test_somar():
    assert somar(2,4) == 6

def test_subtrair():
    assert subtrair(4,2) == 2

def test_multiplicar():
    assert multiplicar(4,2) == 8

def test_dividir():
    assert dividir(4,2) == 2
