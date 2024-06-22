from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import Dict

class Calculator3:
    def __init__(self, driver_hander: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_hander

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)
        formated_response = self.__format_response(multiplication)
        return formated_response

    
    def __validate_body(self, body: Dict) -> list[float]:
        if "numbers" not in body:
            raise Exception("numbers is required")
        
        input_date = body["numbers"]
        return input_date
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication + 1
        for num in numbers:
            multiplication *= num
        return multiplication
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception("variance is less than multiplication")
    
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "result": variance,
                "Success": True
            }
        }