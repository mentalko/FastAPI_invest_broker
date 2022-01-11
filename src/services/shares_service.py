import json
from typing import List, Optional
from bson import json_util
from fastapi import Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from odmantic.bson import ObjectId

from src.models.share import Share
from src.models.account import Account
from src.core.db import db, engine


def parse_json(data):
    return json.loads(json_util.dumps(data))


pipeline = []
pipeline.append(
    {
        "$match": {'_id': ObjectId('61d89b312d6834eb6c1a1653')}
    })

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


class SharesService:
    def __init__(self):
        pass

    async def fetch_all_shares(self):
        shares = await engine.find(Share) 
        print(shares)
        return jsonable_encoder(shares)
    
    async def fetch_shares_by_id(self, id):
        # share = await engine.find_one(Share, Share.id == id)
        # account = await engine.find_one(Account, 
        #                 Account.id == id)
        
        account = await engine.get_collection(Account).aggregate(pipeline).to_list(length=None)
        print(account)
        # share = []
        # if share is None:
        #     raise HTTPException(404)
        return parse_json(account)
     
