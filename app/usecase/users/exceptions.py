from fastapi import HTTPException

class UserNotAuthorization(HTTPException):
    def __init__(self, detail: str, status_code: int = None):
        super().__init__(status_code=status_code, detail=detail)
