from src.drivers.numpy_handler import NumpyNumber
from src.calculators.calculator_3 import Calculator3

def calculator3_factory():
    numpy_number = NumpyNumber()
    calc = Calculator3(numpy_number)
    return calc