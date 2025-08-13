from fastapi import HTTPException


class DatabaseError(HTTPException):
    def __init__(self, detail: str, status_code: int = None):
        super().__init__(status_code=status_code, detail=detail)

class RecordAlreadyExist(HTTPException):
    def __init__(self, detail: str, status_code: int = None):
        super().__init__(status_code=status_code, detail=detail)