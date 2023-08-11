from fastapi import APIRouter

from routers import health_check, measurements

api_router = APIRouter()

api_router.include_router(health_check.router)
api_router.include_router(measurements.router)
