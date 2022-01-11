from datetime import datetime
from typing import Optional
from enum import Enum
from bson.objectid import ObjectId
from odmantic import Field, Model, EmbeddedModel

# from src.core.db import instance, db


class CurrencyKind(str, Enum):
    USD = 'USD'
    EUR = 'EUR'
    RUB = 'RUB'


class Share(Model):
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

# class Share(EmbeddedModel):
#     _id: int
#     name: str 
#     ticker: str  
#     currency: CurrencyKind 
#     close_price: float 
#     description: Optional[str] 


# @instance.register
# class Share(Document):
#     id = fields.IntField() # fields.ObjectIdField()
#     name = fields.StrField()
#     ticker = fields.StrField()
#     currency = fields.IntField()
#     close_price = fields.FloatField(default=0.0)
#     description = fields.StrField(allow_none=True, default='')

#     class Meta:
#         collection_name = 'share'
#         collection = db.share

#     @classmethod
#     async def get(cls, id: str) -> Optional['Share']:
#         # if not ObjectId.is_valid(id):
#         #     return None

#         return await cls.find_one({'_id': id})
#         # return await cls.find_one({'_id': ObjectId(id)})

