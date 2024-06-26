class HttpUnprocessableEntity(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422

try:
    print('Estou no bloco')
    raise Exception('Deu ruim')
except Exception as exception:
    print('Estou no except')
    print(exception.name)
    print(exception.message)
    print(exception.status_code)