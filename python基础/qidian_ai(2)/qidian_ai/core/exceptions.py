from core.status_code import StatusCodes


class QiDianAiException(Exception):
    """
    七点ai异常
    """
    def __init__(self, status_code: StatusCodes, message: str = None):
        self.status_code = status_code
        self.message = message or status_code.message
        super().__init__()

    def get_code(self):
        return self.status_code.code

    def get_status_code(self):
        return self.status_code