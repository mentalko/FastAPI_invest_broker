from fastapi import APIRouter
from . import (
    account_api,
    share_api
)

router = APIRouter()
router.include_router(account_api.router)
router.include_router(share_api.router)
