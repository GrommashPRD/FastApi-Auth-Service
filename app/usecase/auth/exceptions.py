from fastapi import HTTPException

class UsernameRequired(HTTPException):
    def __init__(self, detail: str, status_code: int = None):
        super().__init__(status_code=status_code, detail=detail)

class UserAlreadyExist(HTTPException):
    def __init__(self, detail: str, status_code: int = None):
        super().__init__(status_code=status_code, detail=detail)

class IncorrectTypeData(HTTPException):
    def __init__(self, detail: str, status_code: int = None):
        super().__init__(status_code=status_code, detail=detail)

class DataValidationError(HTTPException):
    def __init__(self, detail: str, status_code: int = None):
        super().__init__(status_code=status_code, detail=detail)

class UserNotFound(HTTPException):
    def __init__(self, detail: str, status_code: int = None):
        super().__init__(status_code=status_code, detail=detail)

class WrongPassword(HTTPException):
    def __init__(self, detail: str, status_code: int = None):
        super().__init__(status_code=status_code, detail=detail)