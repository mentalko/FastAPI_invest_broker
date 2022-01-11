from pydantic import BaseModel, Field
from odmantic import Field, Model
from decimal import Decimal
from bson.objectid import ObjectId
from typing import Optional
from datetime import date


class Transaction(Model):
    account_id: ObjectId 
    share_id: ObjectId  
    deal_price: Decimal = Field(...)
    deal_date: date = Field(...)

    class Config:
        collection = 'transaction'
        json_encoders = {ObjectId: str}



class TransactionCreate(Transaction):
    pass












# class TransactionBase(BaseModel):
#     #account_id: str
#     #share_id: str 
#     deal_price: Decimal = Field(...)
#     deal_date: date = Field(...)



# class TransactionUpdate(TransactionBase):
#     pass

# class Transaction(TransactionBase):
#     _id: int = Field(...)
    
#     class Config:
#         orm_mode = True