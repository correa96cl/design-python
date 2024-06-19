from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.drivers.numpy_handler import NumpyNumber
from .calculator_2 import Calculator2
from typing import Dict
from pytest import raises

class MockRequest:
   def __init__(self, body: Dict) -> None:
      self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
         return 3

def test_calculate_integration():
    mock_request = MockRequest({'numbers': [1, 2, 3]})
    driver = NumpyNumber()
    calculator2 = Calculator2(driver)
    formated_response = calculator2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.14}}

def test_calculate():
    mock_request = MockRequest({'numbers': [1, 2, 3]})
    driver = NumpyNumber()
    calculator2 = Calculator2(driver)
    formated_response = calculator2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.14}}