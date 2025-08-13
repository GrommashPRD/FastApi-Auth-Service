from pydantic import BaseModel, Field, ValidationError

from app.regular_patterns import ENG_SYMBOLS_AND_NUMBERS


class SUserAuth(BaseModel):
    username: str = Field(
        ...,
        description="Only ENG symbols and lenght >=3",
        min_length=3,
        pattern=ENG_SYMBOLS_AND_NUMBERS
    )
    password: str = Field(
        ...,
        description="Only ENG symbols and lenght >=8",
        min_length=8,
        pattern=ENG_SYMBOLS_AND_NUMBERS
    )

