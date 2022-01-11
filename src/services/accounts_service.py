import json
from bson import json_util
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder

from src.models.account import Account
# from src.models.share import Share
from src.core.db import db, engine
    
def parse_json(data):
    return json.loads(json_util.dumps(data))


pipeline = []
pipeline.append(
    {
        "$addFields": {
            "balance": {
                "$sum": [++Account.deposited_usd, ++1000000000 ]
            }  # Compute the area remotely
        }
    }
)
pipeline.append(
    {
        "$lookup": {
            'from': 'shares',
            'localField': 'share_list',
            'foreignField': 'ticker',
            'as': 'share_list'
        }
    }
)
    
class AccountsService:
    def __init__(self):
        pass

    async def fetch_accounts_list(self):
        accounts = await engine.find(Account) 
        
        collection = engine.get_collection(Account)
        
        documents = await collection.aggregate(pipeline).to_list(length=None)
        print(jsonable_encoder(accounts))
        print(parse_json(documents))
        return  parse_json(documents) #jsonable_encoder(documents)

    async def fetch_account_by_id(self, id):
        account = await engine.find_one(Account, Account.id == id)
        if account is None:
            raise HTTPException(404)
        # account['profitability'] = "{:.2f}%".format((deposit - balance)/deposit*100)
        # transactions = await _shares_list_by_account(id)
        
        return account
    
    
    














# async def _shares_by_id_or_ticker( share_ids: List):
#     shares = []
#     for id in share_ids:
#         share = await db.shares.find_one({"_id": id})
#         shares.append(Share(**share))
#     # print(shares)
#     return shares

# async def _shares_sum_price(share_ids: List):
#     pass


# async def _balance(deposited_usd, share_ids: List):
#     shares = await _shares_by_id_or_ticker( share_ids)
#     sum_share_prices = sum([s.close_price for s in shares])
#     return deposited_usd - sum_share_prices


# async def _shares_list_by_account(account_id):
#     transactions = db.transactions.find({"account_id": account_id})
#     for doc in await transactions.to_list(10):
#         print (doc)

#     return transactions
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     

    # async def fetch_one(self, account_id: int):
    #     account = await Account.find_one({"_id": account_id})
    #     return account
    
    # async def fetch_all(self):
    #     accounts = []
    #     cursor = Account.find({})
    #     async for doc in cursor:
    #         accounts.append(tables.Account(**doc))
    #     return accounts

    # async def fetch_account_shares(self, account_id: int):
    #     total = []
    #     transactions = self.transactions.find({"account_id": account_id}, 
    #     {"_id": 0,"share_id": 1,"deal_price": 1} )
    #     shares = []
        
    #     for doc in await transactions.to_list(length=100): 
    #         print(doc)
    #         s = await Share.find_one({"_id": doc["share_id"]}, 
    #         {"_id": 0, "name": 1,"ticker": 1} )
    #         #s.update( doc )
    #         shares.append({**s, **doc})

    #     #total = transactions
    #     # async for doc in cursor:
    #     #     transactions.append(tables.Transaction(**doc))

    #     print(shares)
    #     return shares

    # async def compute_shares_profit(self, account_id: int):
    #     deal_prices = self.transactions.find({"account_id": account_id}, 
    #     {"_id": 0, "deal_price": 1} )
    #     deal_sums = 0
    #     for price in await deal_prices.to_list(length=100):
    #         values = sum(list(price.values()))
    #         print (values)
    #         deal_sums+= values

    #     print(deal_sums)
    #     return deal_sums
        

    # async def compute_shares_balance(self, account_id: int):

    #     # deposited = await Account.find_one({"_id": account_id}, 
    #     # {"_id": 0, "deposited_usd": 1})
    #     # profit = await compute_shares_profit(self, account_id)

    #     return

    # def _get(self, account_id: int) -> tables.Account:
    #     account = (
    #         self.session
    #         .query(tables.Account)
    #         .filter_by(id=account_id)
    #         .first()
    #     )
    #     if not account:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    #     return account

    # def get_list(self, kind: TariffKind=None) -> List[tables.Account]:
    #     query = self.session.query(tables.Account)
    #     if kind:
    #         query = query.filter_by(kind=kind)
    #     accounts = query.all()
    #     return accounts

    # def get(self, account_id: int) -> tables.Account:
    #     return self._get(account_id)
       

    # def create(self, account_data: AccountCreate) -> tables.Account:
    #     account = tables.Account(**account_data.dict())
    #     self.session.add(account)
    #     self.session.commit()
    #     return account

    # def create_many(self, account_data: List[AccountCreate]) -> List[tables.Account]:
    #     accounts = [
    #         tables.Account(
    #             **account_data.dict(),
    #             #user_id=user_id,
    #             )
    #         for account_data in account_data
    #     ]
    #     self.session.add_all(accounts)
    #     self.session.commit()
    #     return accounts

    # def update(self, account_id: int, account_data: AccountUpdate) -> tables.Account:
    #     account = self._get(account_id)
    #     for field, value in account_data:
    #         setattr(account, field, value)
    #     self.session.commit()
    #     return account
    
    # def delete(self, account_id: int):
    #     account = self._get(account_id)
    #     self.session.delete(account)
    #     self.session.commit()




################################################################
# пример на обычном движке
    # async def fetch_all_accounts(self):
    #     accounts = []
    #     cursor =  db.accounts.find({})
    #     for doc in await cursor.to_list(10):
    #         print(doc)
    #         share_ids = doc["share_list"]
    #         doc["_id"] = str(doc["_id"])
    #         doc["share_list"] = await _get_shares_by_account(share_ids)
    #         accounts.append(doc)
    #     return accounts