from pydantic import (
    BaseModel,
    field_validator,
)


class Drug(BaseModel):
    atccode: str
    drug: str

    # @field_validator('atccode')
    # @classmethod
    # def atccode_must_start_with_a_letter(cls, v: str) -> str:
    #     if v[0].isalpha():
    #         return v
    #     raise ValueError('Atccode must start with a letter')


class PubMed(BaseModel):
    id: int
    title: str
    date: str
    journal: str


class Clinical_Trials(BaseModel):
    id: str
    scientific_title: str
    date: str
    journal: str
