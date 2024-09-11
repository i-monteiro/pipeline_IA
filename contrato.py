from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto_1 = "Zapflow com Gemini"
    produto_2 = "Zapflow com ChatGPT"
    produto_3 = "Zapflow com Llama3.0"

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
