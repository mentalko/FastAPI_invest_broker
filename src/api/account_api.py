import json
from typing import List, Optional
from fastapi import APIRouter, Body, HTTPException
from fastapi import Depends, Response, status
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File
from fastapi_pagination import Page, add_pagination, paginate
from fastapi.encoders import jsonable_encoder
from odmantic.bson import ObjectId

# from ..database import get_session
from ..models.account import Account, AccountInfo #, AccountShares, AccountBalance
from ..services.accounts_service import AccountsService
from ..core.db import engine, db

router = APIRouter(
    prefix='/accounts'
)


@router.get("/all", tags=["Account"], response_model=List)
async def root(    service: AccountsService = Depends()
):
    """
        Get news
    :return: List of all accounts
    """
    response = await service.fetch_accounts_list()
    # print (response)
    return response #paginate(response)

@router.get('/{id}',tags=["Account"], response_model=AccountInfo)
async def list_accounts(
    id: ObjectId,
    service: AccountsService = Depends()
):
    response = await service.fetch_account_by_id(id)
    print(response)
    return response


# @router.post(
#     "/create",
#     tags=["Account"],
#     summary="Creates a Account",
#     status_code=201,
# )
# async def create(
#     AccountCreate: Account = Body(None, description="The Person to be created"),
# ) -> AccountSerializer:
#     """This operation creates a Person entity."""

#     try:
#         return await engine.save(AccountCreate)
#     except (HTTPException, Exception) as e:
#         # TODO handel 400 401 403 405 409
#         raise e








#service = AccountsService()

# @router.get('/me', response_model=AccountSerializer, 
# #response_model_exclude=('email', 'hashed_password', 'shares',)
# )
# async def get_me(
#     # kind: Optional[TariffKind] = None,
#     service: AccountsService = Depends()
# ):
#     response = await service.get_my_account()
#     return response






# @router.get('/all_info', response_model=List[AccountSerializer])
# async def get_accounts(
#     # kind: Optional[TariffKind] = None,
#     # service: AccountsService = Depends()
# ):
#     response = await service.fetch_all()
#     return response

# @router.get('/info_by_id/{account_id}', response_model=AccountSerializer)
# async def get_accounts(
#     account_id: int,
# ):
#     response = await service.fetch_one(account_id)
#     return response



# @router.get('/balance/{account_id}', response_model=List[AccountBalance])
# async def get_account_balace(
#     account_id: int, 
# ):
#     profit = await service.compute_shares_profit(account_id)
#     return profit

# @router.post('/', response_model=Account)
# def create_account(
#     account_data: AccountCreate,
#     service: AccountsService = Depends()
# ):
#     return service.create(account_data)

# @router.get('/{id}', response_model=Account)
# def get_account(
#     account_id: int, 
#     service: AccountsService = Depends()
# ):
#     return service.get(account_id)

# @router.put('/{id}', response_model=Account)
# def update_account(
#     account_id: int,
#     account_data: AccountUpdate,
#     service: AccountsService = Depends()
# ):
#     return service.update(
#         account_id,
#         account_data,
#     )

# @router.delete('/{id}')
# def delete_account(
#     account_id: int,
#     service: AccountsService = Depends()
# ):
#     service.delete(account_id)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

