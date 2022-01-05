import json
from typing import List, Optional
from fastapi import APIRouter, Body, HTTPException
from fastapi import Depends, Response, status
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File
from fastapi_pagination import Page, add_pagination, paginate

from .. import tables 
# from ..database import get_session
from ..models.account import Share #, AccountShares, AccountBalance
from ..services.shares_service import SharesService
from ..core.db import engine, db

router = APIRouter(
    prefix='/shares'
)

@router.get("/all", tags=["Shares"], response_model=Page)
async def root(    service: SharesService = Depends()
):
    response = await service.fetch_all_shares()
    return paginate(response)

@router.get('/search',tags=["Shares"], response_model=Page)
async def list_shares(
    service: SharesService = Depends()
):
    response = await service.get_list_shares()
    return paginate(response)
