from typing import Dict, List
from pytest import raises
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers: list[float]) -> float:
        return 3

class MockDriverHandler:
    def variance(self, numbers: list[float]) -> float:
        return 1000000

def test_calcularte_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)
    
    assert str(excinfo.value) == 'variance is less than multiplication'

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())
    formated_response = calculator_3.calculate(mock_request)

    assert formated_response == {'data': {'Calculator': 3, 'result': 1000000, 'Success': True}}

