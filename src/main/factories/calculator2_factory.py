from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyNumber



def calculator2_factory():
    numpy_handler = NumpyNumber()
    calc = Calculator2(numpy_handler)
    return calc