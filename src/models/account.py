from datetime import date, datetime
from typing import List, Optional
from bson.objectid import ObjectId

from typing import Optional

from src.core.config import SECRET_KEY, PWD_CONTEXT, ALGORITHM
# from src.core.db import instance, db

# from src.models.share import Share

from odmantic import Field, Model, EmbeddedModel
from pydantic import EmailStr

class Transaction(Model):
    # _id: int
    account_id: str 
    share_id: int  
    deal_price: str 
    deal_date: str

    class Config:
        collection = 'transaction'
        json_encoders = {ObjectId: str}

class Share(Model):
    # _id: int
    name: str 
    ticker: str  
    currency: str 
    close_price: float 
    description: Optional[str] 

    class Config:
        collection = 'shares'
        json_encoders = {ObjectId: str}

    

class Account(Model):
    # _id: int
    full_name: str
    email: str #EmailStr
    registration_date: str # datetime = datetime.utcnow()
    tariff: str
    deposited_usd: float 
    hashed_password: str
    share_list: List = []
    
    class Config:
        collection = 'accounts'
        json_encoders = {ObjectId: str}


# class AccountCreate(Account):
#     shares: List[Share] = []
    
    # location: Optional[str] = None







# @instance.register
# class Account(Document):
#     id = fields.IntField() #fields.ObjectIdField()
#     full_name = fields.StrField()
#     email = fields.StrField()
#     registration_date = fields.DateTimeField(default=datetime.now)
#     tariff = fields.StrField(default='investor')
#     deposited_usd = fields.FloatField(default=0.0)
#     hashed_password = fields.StrField()

#     shares = fields.ListField(fields.EmbeddedField(Share))

#     class Meta:
#         collection_name = 'accounts'
#         #collection = db.accounts

    
#     @classmethod
#     async def get_my_account(cls) -> Optional['Account']:
#         account = await cls.collection.find_one({'_id': 2})
#         return account

#     @classmethod
#     async def get(cls, id: str) -> Optional['Account']:
#         if not ObjectId.is_valid(id):
#             return None
#         account = await cls.find_one({'_id': ObjectId(id)})
#         return account

#     @classmethod
#     async def get_by_email(cls, email: str):
#         return await cls.find_one({'email': email})

#     def add_share(self, share: Share):
#         self.shares = self.shares + [share]

#     def set_password(self, password: str):
#         self.hashed_password = PWD_CONTEXT.hash(password)

#     @classmethod
#     async def register_new_user(cls, email: str, full_name: str, password: str):
#         account = cls(email=email, full_name=full_name)
#         account.set_password(password)
#         await account.commit()
#         return account