from datetime import date
from enum import Enum
from typing import List, Optional

from odmantic import Field, Model, EmbeddedModel

from bson.objectid import ObjectId
from pydantic.main import BaseModel
from umongo import Document, fields

from src.core.config import SECRET_KEY, PWD_CONTEXT, ALGORITHM
from src.models.account import Share
# from src.core.db import instance, db

class CurrencyKind(str, Enum):
    USD = 'USD'
    EUR = 'EUR'
    RUB = 'RUB'

class ShareEmbedded(BaseModel):
    id: str
    name: str 
    ticker: str  
    currency: CurrencyKind 
    close_price: float 
    description: Optional[str] 

    class Config:
            collection = 'shares'
            json_encoders = {ObjectId: str}



class AccountShares(Model):
    name: str 
    ticker: str  
    currency: CurrencyKind 
    close_price: float 

class TariffKind(str, Enum):
    INVESTOR = 'investor'
    TRADER = 'trader'

class AccountSerializer(BaseModel):
    id: ObjectId
    full_name: str 
    email: str  
    registration_date: date
    tariff: TariffKind 
    deposited_usd: float 
    hashed_password: str 
    
    shares: List

    class Config:
        collection = 'accounts'
        json_encoders = {ObjectId: str}





# class TransactionBase(BaseModel):
#     #account_id: str
#     #share_id: str 
#     deal_price: Decimal = Field(...)
#     deal_date: date = Field(...)




















# class AccountShares(BaseModel):
#     name: str 
#     ticker: str  
#     #count: int 
#     share_id: int 
#     deal_price: Decimal 
#     #deal_date: date

# class AccountBalance(BaseModel):
#     #deposited_usd: Decimal
#     profit: Decimal 
#     balance: Decimal 


#    class Config:
#        allow_population_by_field_name = True
#        schema_extra = {
#            "example": {
#                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
#                "name": "My important task",
#                "completed": False,
#            }
#        }