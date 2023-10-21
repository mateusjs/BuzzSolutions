from fastapi import APIRouter

from app.api.endpoints.suggestion_endpoint import router

api_router = APIRouter()
api_router.include_router(router, prefix="/suggestions", tags=["buzz"])
