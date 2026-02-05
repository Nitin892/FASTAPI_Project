from fastapi import APIRouter
from app.modules.accounts.routes import router as accounts_router

api_router = APIRouter()

api_router.include_router(accounts_router)
