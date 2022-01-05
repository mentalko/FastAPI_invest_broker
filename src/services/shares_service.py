import json
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, query

from .. import tables
from src.models.account import Share
# from src.models.share import Share
from src.core.db import db, engine

#from ..database import col_shares, col_shares, col_transactions
from src.settings import settings

import logging


class SharesService:
    def __init__(self):
        pass

    async def fetch_all_shares(self):
        shares = []

        cursor = await engine.find(Share)
        print(cursor)

        for doc in cursor:
            print(doc)
            share_ids = doc.share_list
            # doc.id = str(doc.id)
            shares.append(doc)
        return shares



    async def get_list_shares(self):
        shares = await engine.find(Share) 
        print(shares)
        return shares
     
