from fastapi import APIRouter

from src.init import cmc_client

router = APIRouter(
    prefix="/currencies"
)

@router.get("/cryptocurrencies")
async def get_cryptocyrrencies():
    return await cmc_client.get_listings()

@router.get("/cryptocurrencies/{currency_id}")
async def get_cryptocyrrency(currency_id: int):
    return await cmc_client.get_currency(currency_id)