from datetime import datetime
from typing import Optional

from bson.objectid import ObjectId
from odmantic import Field, Model, EmbeddedModel

from src.core.config import SECRET_KEY, PWD_CONTEXT, ALGORITHM
# from src.core.db import instance, db




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

